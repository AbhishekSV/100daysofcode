from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time

FORM_URL = 'https://forms.gle/nvpKizkXFj3TYKG79'


class FormFillerBot:
    
    
    def __init__(self):
        options = EdgeOptions()
        options.use_chromium = True
        self.driver = Edge(options = options)
    
    def fillform(self, address, rent, url):
        self.driver.get(FORM_URL)
        time.sleep(3)        
        address_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)
        rent_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        rent_input.send_keys(rent)
        url_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_input.send_keys(url)
        submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
        submit.click()
    
    def endprogram(self):
        self.driver.quit()
