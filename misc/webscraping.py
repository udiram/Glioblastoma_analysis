from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#implicit wait
driver.implicitly_wait(10)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("http://glioblastoma.alleninstitute.org/ish/specimen/show/298324043")
#identify element
cookie_accept =driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']")
#perform click
cookie_accept.click()

change_img_type = driver.find_element_by_xpath("/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/select")
change_img_type.click()

select_correct_type = Select(driver.find_element_by_xpath("/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/select"))
select_correct_type.select_by_index("0")

#
first_download = driver.find_element_by_xpath("/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[2]/div")
first_download.click()

img_id = driver.find_element_by_xpath("/html/body/div[12]/div[2]/table/tbody/tr[3]/td[2]/input")
img_id.send_keys(Keys.CONTROL + "a")
img_id.send_keys(Keys.DELETE)
img_id.send_keys("something.jpg")

final_download = driver.find_element_by_xpath("/html/body/div[12]/div[2]/div[2]/input")
final_download.click()

print("Page title is: ")
print(driver.title)
# #close browser
# driver.quit()

# /input[starts-with(@id, ‘submit_’)]