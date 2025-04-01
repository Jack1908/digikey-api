# DigiKey Component Search Tool

This tool allows you to search for electronic components using the DigiKey API.

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Set up your `config.yaml` file with your DigiKey API credentials.

## Usage

### Basic Commands

1. Search by keyword:
```bash
python3 search_components.py -k "Arduino Uno"
```

2. Search by part number:
```bash
python3 search_components.py -p "1050-1024-ND"
```

3. Search from CSV file:
```bash
python3 search_components.py -i input.csv
```

### Options

- `-k`, `--keyword`: Search by keyword
- `-p`, `--part-number`: Search by specific part number
- `-i`, `--input-csv`: Input CSV file containing part numbers
- `-c`, `--count`: Number of results to return (default: 10)
- `--csv`: Save results to CSV file
- `-o`, `--output`: Output CSV filename (default: search_results.csv)

### CSV File Format

For input CSV files:
- Must contain a 'Part Number' column
- Example:
```csv
Part Number
1050-1024-ND
1050-1041-ND
```

For output CSV files:
- Contains the following columns:
  - Part Number
  - Manufacturer
  - Description
  - Category
  - Detailed Description
  - Primary Photo
  - Unit Price

## Configuration

Create a `config.yaml` file with your DigiKey API credentials:
```yaml
digikey:
  client_id: "your-client-id"
  client_secret: "your-client-secret"
  redirect_uri: "http://localhost:8080/callback"
  sandbox: true  # Set to false for production environment
```

## Windows 11 Setup

This project can run on Windows 11. Follow these steps:

1. **Python Installation**:
   - Download and install Python 3.9 or later from [python.org](https://www.python.org/downloads/windows/)
   - During installation, make sure to check "Add Python to PATH"

2. **Environment Setup**:
   - Open Command Prompt or PowerShell
   - Create a virtual environment:
     ```cmd
     python -m venv digikey-env
     ```
   - Activate the virtual environment:
     ```cmd
     digikey-env\Scripts\activate
     ```

3. **Install Dependencies**:
   - Install required packages:
     ```cmd
     pip install -r requirements.txt
     ```

4. **Configuration**:
   - Create the `config.yaml` file in the project directory
   - Create the `.digikey_storage` directory manually

5. **Running the Tool**:
   - Use the same commands as on macOS:
     ```cmd
     python search_components.py -k "Arduino Uno"
     ```

### Windows-Specific Considerations

1. **File Paths**:
   - Use backslashes (`\`) instead of forward slashes (`/`) in file paths
   - Example: `C:\Users\YourName\Projects\digikey-api`

2. **Environment Variables**:
   - To set environment variables permanently:
     1. Right-click on "This PC" and select "Properties"
     2. Click "Advanced system settings"
     3. Click "Environment Variables"
     4. Add new variables under "User variables"

3. **CSV Files**:
   - Make sure CSV files are saved with UTF-8 encoding
   - Use Excel or Notepad++ to create/edit CSV files

4. **Common Issues**:
   - If you get permission errors, run Command Prompt as Administrator
   - If you get SSL errors, try updating your Windows certificates
   - If the script doesn't run, check Python is in your PATH:
     ```cmd
     python --version
     ```

### Setup Script for Windows

You can use this `setup.bat` file to automate the setup process:

```batch
@echo off
echo Setting up DigiKey API tool...

:: Check Python version
python --version
if errorlevel 1 (
    echo Python not found. Please install Python 3.9+ first.
    pause
    exit /b 1
)

:: Create virtual environment
python -m venv digikey-env
if errorlevel 1 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)

:: Activate environment and install dependencies
call digikey-env\Scripts\activate
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

:: Create storage directory
mkdir .digikey_storage

echo Setup complete!
echo To use the tool, run:
echo   digikey-env\Scripts\activate
echo   python search_components.py -k "Arduino Uno"
pause
```

To use the setup script:
1. Download the project files
2. Run `setup.bat`
3. Create `config.yaml` with your API credentials
4. Use the tool as normal