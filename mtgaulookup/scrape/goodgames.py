from bs4 import BeautifulSoup as BS
import requests, re

def lookup(card):
    '''
    This operation is used to look up the cheapest price of a card at GUF -  https://guf.com.au/.
    
    Input & requirements:
    - A valid MTG card that is in existence.
    - Name has to be full.

    Output:
    - Cheapest price
    or
    - None

    It involves:
    - Use the search URL to look for a card using its name then parse the HTML into a soup
        Note: Product listing limit is set to max (256)
    - Using regex:
        - From list of items, find the ones that matches exact card name
            - If item is available (action includes 'Add to Cart'), add price to list of results
    - Get cheapest price
    '''

    html_src = requests.get(url= f'https://tcg.goodgames.com.au/catalogsearch/result/?q={card}&product_list_limit=256').text
    soup = BS(html_src, 'html.parser')

    items = soup.find_all('div', {'class': 'product details product-item-details'})
    regex_str = r'(^[\s]+)' + f'({card})'

    results = []
    for item in items:       
        card_name = item.find('a', {'class': 'product-item-link'}).text      

        # Check if card's name matches.
        match = re.compile(regex_str).match(card_name)
        if match:
            # Check if item is available.
            # There should be 'Add to Cart'.
            actions = item.find('div', {'class': 'product-item-inner'}).text
            if 'Add to Cart' in actions:            
                price = item.find('span', {'class': 'price-container price-final_price tax weee'}).text
                price = re.sub(r'[^\d\.]', '', price)
                results.append(float(price))
    
    try:
        return min(results)
    except:
        return None

