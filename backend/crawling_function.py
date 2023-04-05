from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import TimeoutException


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=50,100")
options.add_argument("lang=en-GB")
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")


def crawl_driver(keywords=[]):
    with get_driver() as driver:
        driver.get('https://www.google.com/')
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
        info_list = []

        for keyword in keywords:
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.submit()
            try:
                WebDriverWait(driver, 2).until(
                    visibility_of_element_located((By.ID, 'rso')))
            except TimeoutException:
                info_list.append('no results found')
                driver.back()
                continue
            span_elements = driver.find_elements(By.ID, 'rso')
            info_list += [element.text for element in span_elements]
            driver.back()

    print(info_list)
    return info_list
