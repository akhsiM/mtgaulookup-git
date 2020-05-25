from bs4 import BeautifulSoup as BS
import requests, re


def lookup(card):
    '''
    This operation is used to look up the cheapest price of a card at GUF -  https://guf.com.au/.
    
    Input & requirements:
    - A valid MTG card that is in existence.
    - Name has to be full & casing should be correct.

    Output:
    - Cheapest price
    or
    - None

    It involves:
    - Use the search URL to look for a card using its name then parse the HTML into a soup
    - Using regex:
        - Find all available cards. These are wrapped around "<div ... onclick="addToCart('12561609130078','{Card Name}...>"
            e.g: <div class="addNow single" onclick="addToCart('12562056282206','Mana Vault [Fourth Edition] - Ballarat' , '2' ,1)">
        - Find price
    - Get cheapest price
    '''

    html_src = requests.get(url= f'https://guf.com.au/search?q={card}').text
    soup = BS(html_src, 'html.parser')

    soup_regex_str = r"addToCart\(\'[\d]+\',\'" + card + ".*"
    soup_regex = re.compile(soup_regex_str)
    cards = soup.find_all('div', {'onclick': soup_regex})

    if len(cards) == 0:
        return None
    else:
        results = []
        price_regex = re.compile('\$[\d]+\.[\d]+')
        for card in cards:
            price = price_regex.search(card.text).group()[1:]
            price = float(price)
            results.append(price)
    
    return min(results)
