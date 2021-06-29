import time
from selenium import webdriver
from pywinauto import application
from selenium.webdriver.chrome.options import Options



#Go to the screen of whom you want to send images: (Note : I'm using this according my req. you can use another approach to go there.
ph = '+628882660532'
strs = 'https://api.whatsapp.com/send?phone=' + ph
search_xpath = '//*[@id="input-chatlist-search"]'
driver.driver.find_element_by_xpath(search_xpath).send_keys(phone + Keys.ENTER)

#Click on attachment on whatsapp using :
driver.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span').click()

#Search the upload button like..(Note: Please change XPATH accordingly)
element = driver.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input')

#Use the function to send images (Note : file_path -> '/home/Desktop/image.jpg')
element.send_keys(file_path)
time.sleep(1)
