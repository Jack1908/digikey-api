import os
from pathlib import Path

# DigiKey API 配置
DIGIKEY_CONFIG = {
    'CLIENT_ID': os.getenv('DIGIKEY_CLIENT_ID', ''),
    'CLIENT_SECRET': os.getenv('DIGIKEY_CLIENT_SECRET', ''),
    'SANDBOX': os.getenv('DIGIKEY_CLIENT_SANDBOX', 'False'),
    'STORAGE_PATH': os.getenv('DIGIKEY_STORAGE_PATH', str(Path('./path')))
}

# 缓存目录配置
CACHE_DIR = Path('./path') 