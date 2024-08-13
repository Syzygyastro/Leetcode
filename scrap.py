import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def browser_function():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    path  = "C:\\Users\\kkapo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    # Use ChromeDriverManager to automatically download and manage the correct ChromeDriver version
    chr_driver = webdriver.Chrome(path)
    url = "https://www.youtube.com/@NeetCodeIO/videos"
    chr_driver.get(url=url)
    time.sleep(50000)

browser_function()
