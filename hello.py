import os
from pathlib import Path

import digikey
from digikey.v3.productinformation import KeywordSearchRequest
from digikey.v3.batchproductdetails import BatchProductDetailsRequest
from config import DIGIKEY_CONFIG, CACHE_DIR

# 设置 DigiKey API 环境变量
os.environ['DIGIKEY_CLIENT_ID'] = DIGIKEY_CONFIG['CLIENT_ID']
os.environ['DIGIKEY_CLIENT_SECRET'] = DIGIKEY_CONFIG['CLIENT_SECRET']
os.environ['DIGIKEY_CLIENT_SANDBOX'] = DIGIKEY_CONFIG['SANDBOX']
os.environ['DIGIKEY_STORAGE_PATH'] = DIGIKEY_CONFIG['STORAGE_PATH']

# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)

# Search for parts
search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
result = digikey.keyword_search(body=search_request)

# Only if BatchProductDetails endpoint is explicitly enabled
# Search for Batch of Parts/Product
mpn_list = ["0ZCK0050FF2E", "LR1F1K0"] #Length upto 50
batch_request = BatchProductDetailsRequest(products=mpn_list)
part_results = digikey.batch_product_details(body=batch_request)