
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\geckodriver.exe")
driver.get("https://www.amazon.com/")
driver.close()