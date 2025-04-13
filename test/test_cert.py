# This script is used to debug SSL-related issues and inspect the environment configuration.
# It prints environment variables, Python version, and SSL certificate settings.
import os
import sys
import ssl

print("Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

print("\nPython Version:", sys.version)
print("SSL Certificate File:", ssl.get_default_verify_paths().cafile)
print("SSL Environment Variable:", os.environ.get('REQUESTS_CA_BUNDLE'))