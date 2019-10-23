from selenium import webdriver
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")

from webdriver_manager.chrome import ChromeDriverManager
d = webdriver.Chrome(ChromeDriverManager().install())

#d = webdriver.Chrome(chrome_options=chrome_options, executable_path="../Drivers/chromedriver.exe")

d.get("https://google.com")
d.find_element_by_name("q").send_keys("ABCD")
d.find_element_by_name("btnK").click()

print(d.title)
d.close()
d.quit()
