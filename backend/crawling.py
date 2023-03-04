from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=10000,10000")
options.add_argument("lang=en-GB")
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")
options.add_argument('--headless')


def crawl_driver(keyword="intial keyword"):
    driver = get_driver()
    driver.get('https://www.google.com/')
    search_box = driver.find_element('name', 'q')
    search_box.send_keys(keyword)
    search_box.submit()
    driver.implicitly_wait(10)
    span_elements = driver.find_elements(By.XPATH, '//*[@id="rso"]')
    for element in span_elements:
        print(element.text)
    driver.quit()
