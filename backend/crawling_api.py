from crawling_function import crawl_driver


def get_results(id="initial_id", name="initial_name", phone_number="initial_phone_number", email="initial_email"):
    crawl_driver(keyword=id)
    crawl_driver(keyword=name)
    crawl_driver(keyword=phone_number)
    crawl_driver(keyword=email)


get_results(id="soolee0701", name="soojeong lee",
            phone_number="010-8839-2919", email="soojlee0106@naver.com")
