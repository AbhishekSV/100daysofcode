from bs4 import BeautifulSoup
import requests

class RentScraperBot:
    
    def __init__(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8'
            }
        response = requests.get(url="https://www.zillow.com/phoenix-az/apartments/1-_beds/paymenta_sort/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Phoenix%2C%20AZ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-112.59883590039063%2C%22east%22%3A-111.65126509960938%2C%22south%22%3A33.2127881856902%2C%22north%22%3A33.99740672869016%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A40326%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        self.all_links = []
        self.all_addresses = []
        self.all_prices = []
        
    def find_rentals(self):
        all_link_elements = self.soup.select(".list-card-top a")
        for link in all_link_elements:
            href = link["href"]
            if "http" not in href:
                self.all_links.append(f"https://www.zillow.com{href}")
            else:
                self.all_links.append(href)

        all_address_elements = self.soup.select(".list-card-info address")
        self.all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

        all_price_elements = self.soup.select(".list-card-heading")
        for element in all_price_elements:
            # Get the prices. Single and multiple listings have different tag & class structures
            try:
                # Price with only one listing
                price = element.select(".list-card-price")[0].contents[0]
            except IndexError:
                print('Multiple listings for the card')
                # Price with multiple listings
                price = element.select(".list-card-details li")[0].contents[0]
            finally:
                self.all_prices.append(price)
    