from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://github.com/vitorramosdasilva/dashboard-genghiscode")

driver.find_element(By.XPATH, '/html/body/div[4]/div/main/div[2]/div/div[2]/div[2]/div/div[5]/div/ul/li[1]/a/span[1]')
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.close()


