from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def updating_ad():
    option = webdriver.ChromeOptions()
    option.add_argument(" - incognito")
    browser = webdriver.Chrome('C:\Develpment\PycharmProjects\chromedriver.exe', chrome_options=option)
    browser.get('https://www.shufersal.co.il/online/')

    # Wait 20 seconds for page to load
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='corporateHeader']/div[1]/div/div[2]/a/img")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    # find_elements_by_xpath returns an array of selenium objects.
    # browser.find_element_by_class_name("icon.icon-search").click()
    browser.find_element_by_class_name("btnToggleSearch.collapsed.hidden-md.hidden-lg").click()
    browser.find_element_by_id("js-site-search-input").send_keys("קמח לבן")
    titles_element = browser.find_elements_by_xpath('//strong[@id="formSearchSubmit"]')
    # titles_element = browser.find_elements_by_xpath('//h3[@class="corporateTitle"]')
    # language_element = browser.find_elements_by_xpath('//span[@class="productName"]')
    # use list comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]
    # languages = [x.text for x in language_element]

    # for title, language in zip(titles, languages):
    #     # print("title: items")
    #     print(f"{title}:->->->->  {language}")

    print('titles: ')
    print(titles, '\n')
    print("languages:")
    # print(languages, '\n')
    # browser.quit()

updating_ad()

    #    """ Login to the website """
#    user_name = 'avihay30@gmail.com'
#    password = 'avihay3052'
#    driver.find_element_by_id('userName').send_keys(user_name)
#    driver.find_element_by_id('password').send_keys(password)
#    driver.find_element_by_id('submitLogonForm').click()


#     """ Search The Shop """
#     # driver.get("http://my.yad2.co.il/newOrder/index.php?action=edit&CatID=2&SubCatID=2&OrderID=40084379")
#     # """ Finish Button """
#     driver.find_element_by_class_name("icon.icon-search").click()
#     driver.find_element_by_id('js-site-search-input').send_keys(search[0])
#     driver.find_element_by_class_name('tile.row.miglog-prod.miglog-sellingmethod-by_unit.tt-suggestion.tt-selectable'[0])
#     # driver.close()
#
# # קמח לבן
# # קמח לבן שופרסל
# def testing():
#     print("this is test!")
#
#
# if __name__ == '__main__':
#     def iteration_loop(start, counter, timer, difference):
#         while (start + difference) > time():
#             pass
#         else:
#             counter += 1
#             difference = timer * counter
#             updating_ad()
#             print(colored(f"*****An update as been done to Your Ad***** \n ", 'green'),
#                   colored(f"->->->->-> {strftime('%Y-%m-%d %H:%M:%S')} <-<-<-<-<-\n", 'white'))
#             return iteration_loop(start, counter, timer, difference)
#             # real_time = time()
#
#
#     class Yad2Automation:
#         start_time = time()
#         counter = 1
#         timer = 30  # seconds between every action
#         difference_time = timer * counter
#         iteration_loop(start_time, counter, timer, difference_time)
