from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

drivers = 2
refresh = 5
url =  'https://www.youtube.com/watch?v=I0ESYlp85Rk'
drivers_list = []

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

for i in range(drivers):
    drivers_list.append(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options))
    drivers_list[i].get(url)

    while True:
        time.sleep(refresh)
        drivers_list[i].refresh()
        for i in range(drivers):
            drivers_list[i].refresh()