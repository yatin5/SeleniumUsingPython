from selenium import webdriver
import selenium

d = webdriver.Chrome("../Drivers/chromedriver.exe")

d.get("http://google.com")

d.close()
d.quit()
print("Test passed")