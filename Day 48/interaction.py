from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options = options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# user_count = driver.find_element_by_css_selector('#articlecount a')
# print(user_count.text)
# user_count.click()

driver.get('http://secure-retreat-92358.herokuapp.com/')
firstName = driver.find_element_by_name('fName')
firstName.send_keys('Abhishek')
lastName = driver.find_element_by_name('lName')
lastName.send_keys('Sabnivis')
email_input = driver.find_element_by_name('email')
email_input.send_keys('abhisabnives@gmail.com')
submit_button = driver.find_element_by_css_selector('form button')
submit_button.click()

driver.quit()