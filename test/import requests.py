# This script tests the SSL connection to the DigiKey API.
# It is used for debugging SSL certificate issues.
# 
import requests

url = "https://api.digikey.com/v1/oauth2/token"
try:
    response = requests.get(url, timeout=10)
    print("SSL connection successful:", response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL error:", e)
except Exception as e:
    print("Other error:", e)