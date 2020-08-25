from selenium import webdriver                                  #import libraries
import urllib.request

driver = webdriver.Chrome("path to web driver")                 #give path to webdriiver

url = "https://www.instagram.com/"                              
url_user = input("enter the handle:")
url_p = url + url_user                                          #url of instagram user

driver.get(url_p)                                               #go to that webpage

try:
	image=driver.find_element_by_xpath('//img[@class="_6q-tv"]')  #finds the profile pic src
except:
	image=driver.find_element_by_xpath('//img[@class="be6sR"]')
  
img_link=image.get_attribute('src')                             #gets the source

path="download path"                                            #path where you want to download

urllib.request.urlretrieve(img_link,path)                       #retrieves the image

print("The profile pic has been downloaded at: "+path)          #prints the confirmation message
