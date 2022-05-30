import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from alive_progress import alive_bar


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
df_in = pd.read_csv('../data/rna_seq_samples_details.csv')
#implicit wait
driver.implicitly_wait(10)
#maximize browser
driver.maximize_window()

counter = 0
with alive_bar(280, title="downloading dataset", length=100, spinner="arrow") as bar:
    for index,row in df_in.iterrows():
        p_or_r = row[4]
        link = row[14]
        img_file_save = p_or_r + str(counter) + '.jpg'
        # launch URL
        driver.get(link)
        ############
        if counter == 0:
            cookie_accept = driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']")
            cookie_accept.click()


        change_img_type = driver.find_element_by_xpath( "/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/select")
        change_img_type.click()

        select_correct_type = Select(driver.find_element_by_xpath("/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/select"))
        select_correct_type.select_by_index("0")


        first_download = driver.find_element_by_xpath("/html/body/div[1]/span/table/tbody/tr/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td[2]/div")
        first_download.click()


        img_id = driver.find_element_by_xpath("/html/body/div[12]/div[2]/table/tbody/tr[3]/td[2]/input")
        img_id.send_keys(Keys.CONTROL + "a")
        img_id.send_keys(Keys.DELETE)
        img_id.send_keys(img_file_save)


        final_download = driver.find_element_by_xpath("/html/body/div[12]/div[2]/div[2]/input")
        final_download.click()
        bar()
        counter = counter + 1