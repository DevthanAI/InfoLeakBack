from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("lang=en-GB")
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")
# options.add_argument('--headless')

driver = get_driver()
driver.get("https://www.google.com/")

wait = WebDriverWait(driver, 10)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def crawling(id="", name="", phone_number="", email_address=""):
    if id != "":
        search = find(
            wait, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
        search.send_keys(id+"\n")

        for i in range(3, 10):
            i = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#rso > div:nth-child("+str(i)+") > div > div > div:nth-child(2) > div > span")))
            print(i.text)

        driver.close()

    return


crawling(id="hi")
