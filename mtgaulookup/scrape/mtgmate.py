from bs4 import BeautifulSoup as BS
import requests, re

def lookup(card):
    '''
    This operation is used to look up the cheapest price of a MTG card at GUF -  https://www.mtgmate.com.au/.
    
    Input & requirements:
    - A valid MTG card that is in existence
    - Name has to be exact and full

    Output:
    - Cheapest price
    or
    - None

    It involves:
    - Use the search URL to look for a card using its name then parse the HTML into a soup
    - Using regex:
        - Find available cards by looking for its price wrapper.
            e.g: <td class="price text-right">
                    1x $91.00ea
                 </td>
        (Unavailable cards are normally "out of stock".)
    - Get cheapest price
    '''

    html_src = requests.get(url= f'https://www.mtgmate.com.au/cards/search?utf8=✓&q={card}').text
    soup = BS(html_src, 'html.parser')

    prices = soup.find_all('td', {'class': 'price text-right'})

    results = []
    avl_regex = re.compile(r'([\s]+[\d]+x \$)([\d]+\.[\d]+)')
    for price in prices:
        price = price.text
        money = avl_regex.match(price)
        if money:
            results.append(float(money.group(2)))
    
    try:
        return min(results)
    except:
        return None
