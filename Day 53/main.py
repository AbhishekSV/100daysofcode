from Resources.rentscraper import RentScraperBot
from Resources.formfiller import FormFillerBot

soupbot = RentScraperBot()
seleniumbot = FormFillerBot()

soupbot.find_rentals()
for n in range(len(soupbot.all_links)):
    seleniumbot.fillform(soupbot.all_addresses[n], soupbot.all_prices[n], soupbot.all_links[n])
seleniumbot.endprogram()