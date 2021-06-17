from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True

driver = Edge(options = options)
driver.get('https://www.python.org/')

event_times = driver.find_elements_by_css_selector('.event-widget time')
event_names = driver.find_elements_by_css_selector('.event-widget li a')
events = {n:{"time": event_times[n].text, "event": event_names[n].text} for n in range(0,len(event_times)) }


driver.quit()