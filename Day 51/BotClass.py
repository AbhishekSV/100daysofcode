from msedge.selenium_tools import Edge, EdgeOptions
import os

class InternetSpeedTwitterBot:
    
    
    def __init__(self):
        self.up = 0
        self.down = 0
        options = EdgeOptions()
        options.use_chromium = True
        self.driver = Edge(options = options)
        self.driver.get("https://www.speedtest.net/")
    
    def get_internet_speed():
        pass
    
    def tweet_at_provider():
        pass
