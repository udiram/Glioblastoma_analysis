from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://glioblastoma.alleninstitute.org/ish/specimen/show/298324043")

wait = WebDriverWait(driver=driver, timeout=5)
action = ActionChains(driver)


# try:
#     menu = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=view_control5036select_image_type]")))
#     print("found")
#     action.move_to_element(menu).click().perform()
# except:
#     print("not found")
# change_img_type = driver.find_element_by_id("view_control5036select_image_type").click()
# print(driver.page_source)
# driver.quit()

