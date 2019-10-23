from selenium import webdriver

path = "../Drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)

driver.get("https://google.com")

print(driver.title)

driver.close()
driver.quit()
