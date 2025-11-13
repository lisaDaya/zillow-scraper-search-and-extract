thonfrom bs4 import BeautifulSoup

def extract_property_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    properties = []

    listings = soup.find_all('div', class_='property-listing')
    for listing in listings:
        property_data = {
            'rawHomeStatusCd': listing.find('span', class_='status').text,
            'detailUrl': listing.find('a', class_='property-link')['href'],
            'statusType': listing.find('span', class_='status-type').text,
            'statusText': listing.find('span', class_='status-text').text,
            'price': listing.find('span', class_='price').text,
            'address': listing.find('div', class_='address').text.strip(),
            'latLong': {
                'latitude': listing['data-latitude'],
                'longitude': listing['data-longitude']
            },
            'beds': listing.find('span', class_='beds').text,
            'baths': listing.find('span', class_='baths').text,
            'area': listing.find('span', class_='area').text
        }
        properties.append(property_data)

    return properties