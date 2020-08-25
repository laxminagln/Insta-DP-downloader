from selenium import webdriver

driver = webdriver.Chrome("path to web driver")

url = "https://www.instagram.com/"
url_user = input("enter the handle:")
url_p = url + url_user

driver.get(url_p)

driver.find_element_by_xpath("//*img[@class='']")
