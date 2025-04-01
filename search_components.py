#!/usr/bin/env python3
import argparse
import os
import yaml
from digikey.v3.productinformation import KeywordSearchRequest
import digikey.v3.api as digikey_api

def load_config():
    """Load configuration from config.yaml file."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config['digikey']
    except Exception as e:
        raise ValueError(f"Error loading config file: {e}")

def setup_environment():
    """Set up environment variables from config file."""
    config = load_config()
    
    if not config['client_id'] or not config['client_secret']:
        raise ValueError("Please set your client_id and client_secret in config.yaml")

    # Create storage directory if it doesn't exist
    storage_path = os.path.join(os.path.dirname(__file__), '.digikey_storage')
    os.makedirs(storage_path, exist_ok=True)

    # Set environment variables
    os.environ['DIGIKEY_CLIENT_ID'] = config['client_id']
    os.environ['DIGIKEY_CLIENT_SECRET'] = config['client_secret']
    os.environ['DIGIKEY_CLIENT_SANDBOX'] = str(config.get('sandbox', 'true')).lower()
    os.environ['DIGIKEY_STORAGE_PATH'] = storage_path

def search_by_keyword(keyword, record_count=10):
    """Search for parts using a keyword."""
    try:
        # Create search request
        search_request = KeywordSearchRequest(
            keywords=keyword,
            record_count=record_count
        )
        
        # Execute the search
        api_response = digikey_api.keyword_search(body=search_request)
        return api_response
    except Exception as e:
        print(f"Error searching for parts: {e}")
        return None

def search_by_part_number(part_number):
    """Search for a specific part by part number."""
    try:
        # Execute the search
        api_response = digikey_api.product_details(part_number)
        return api_response
    except Exception as e:
        print(f"Error searching for part: {e}")
        return None

def display_results(results, is_keyword_search=True):
    """Display the search results in a formatted way."""
    if not results:
        print("No results found.")
        return

    if is_keyword_search:
        products = results.products
    else:
        products = [results]  # Single product for part number search

    # Prepare data for CSV
    csv_data = []
    
    for product in products:
        print("\n" + "="*50)
        print(f"Part Number: {product.digi_key_part_number}")
        print(f"Manufacturer: {product.manufacturer.value}")
        print(f"Description: {product.product_description}")
        if hasattr(product, 'category'):
            print(f"Category: {product.category.value}")
        if hasattr(product, 'detailed_description'):
            print(f"Detailed Description: {product.detailed_description}")
        if hasattr(product, 'primary_photo'):
            print(f"Primary Photo: {product.primary_photo}")
        if hasattr(product, 'unit_price'):
            print(f"Unit Price: {product.unit_price}")
        print("="*50)
        
        # Add product data to CSV list
        csv_data.append({
            'Part Number': product.digi_key_part_number,
            'Manufacturer': product.manufacturer.value,
            'Description': product.product_description,
            'Category': product.category.value if hasattr(product, 'category') else '',
            'Detailed Description': product.detailed_description if hasattr(product, 'detailed_description') else '',
            'Primary Photo': product.primary_photo if hasattr(product, 'primary_photo') else '',
            'Unit Price': product.unit_price if hasattr(product, 'unit_price') else ''
        })
    
    return csv_data

def save_to_csv(data, filename="search_results.csv"):
    """Save search results to a CSV file."""
    import csv
    if not data:
        return
        
    fieldnames = ['Part Number', 'Manufacturer', 'Description', 'Category', 
                 'Detailed Description', 'Primary Photo', 'Unit Price']
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"\nSearch results saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def search_from_csv(input_file):
    """Search for components from a CSV file containing part numbers."""
    import csv
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'Part Number' not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'Part Number' column")
            
            part_numbers = [row['Part Number'] for row in reader]
            return part_numbers
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Search for electronic components on DigiKey')
    parser.add_argument('--keyword', '-k', help='Search by keyword')
    parser.add_argument('--part-number', '-p', help='Search by part number')
    parser.add_argument('--input-csv', '-i', help='Input CSV file containing part numbers')
    parser.add_argument('--count', '-c', type=int, default=10, help='Number of results to return (default: 10)')
    parser.add_argument('--csv', action='store_true', help='Save results to CSV file')
    parser.add_argument('--output', '-o', default='search_results.csv', help='Output CSV filename')
    
    args = parser.parse_args()
    
    if not args.keyword and not args.part_number and not args.input_csv:
        parser.error("Either --keyword, --part-number, or --input-csv must be provided")
    
    try:
        setup_environment()
        
        if args.input_csv:
            part_numbers = search_from_csv(args.input_csv)
            if part_numbers:
                all_results = []
                for part_number in part_numbers:
                    results = search_by_part_number(part_number)
                    if results:
                        csv_data = display_results(results, is_keyword_search=False)
                        if csv_data:
                            all_results.extend(csv_data)
                if args.csv and all_results:
                    save_to_csv(all_results, args.output)
        elif args.keyword:
            results = search_by_keyword(args.keyword, args.count)
            csv_data = display_results(results, is_keyword_search=True)
            if args.csv and csv_data:
                save_to_csv(csv_data, args.output)
        else:
            results = search_by_part_number(args.part_number)
            csv_data = display_results(results, is_keyword_search=False)
            if args.csv and csv_data:
                save_to_csv(csv_data, args.output)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 