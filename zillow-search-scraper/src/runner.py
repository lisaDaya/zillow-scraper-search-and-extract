thonimport json
import os
import requests
from zillow_parser import extract_property_data
from exporters import export_to_json
from config.settings import load_config

def run_scraper():
    config = load_config()
    search_url = config['search_url']
    proxies = config.get('proxies', None)

    # Fetch Zillow data
    response = requests.get(search_url, proxies=proxies)
    if response.status_code == 200:
        properties = extract_property_data(response.text)
        export_to_json(properties)
    else:
        print(f"Error: Unable to fetch data from Zillow (status code {response.status_code})")

if __name__ == '__main__':
    run_scraper()