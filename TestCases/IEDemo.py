from selenium import webdriver

#path = "../Drivers/IEDriverServer.exe"
#driver = webdriver.Ie(executable_path = path)
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(IEDriverManager().install())

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("ABCD")
driver.find_element_by_name("btnK").click()

print(driver.title)

driver.close()
driver.quit()
