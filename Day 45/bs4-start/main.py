from bs4 import BeautifulSoup
import requests

# # Basic Exercise

# with open("/Users/abhisheksabnivis/Desktop/100daysofcode/Day 45/bs4-start/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.p)

# all_links = soup.find_all(name="a")

# for link in all_links:
#     print(link.getText())
#     print(link.get("href"))

# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)

# # Navigate using CSS Selectors
# company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# headings = soup.select(selector=".heading")


# Working with live website
response = requests.get(url='https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find(name="a", class_="storylink").getText())
