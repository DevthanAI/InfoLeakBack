from crawling_function import crawl_driver


def get_results(inital_list=[]):

    final_list = []

    for i in range(len(inital_list)):
        initial_result = crawl_driver(keyword=inital_list[i])
        final_list.extend(initial_result)
        
    print(final_list)
    return final_list

# Test example
# get_results(inital_list=["soolee0701", "soojlee0106",
#             "ofdetectivesandcats", "010-8839-2919"])
