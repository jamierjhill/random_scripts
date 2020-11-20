## Code to autmoatically play the latest Ben Foster GK cycling video

from selenium import webdriver
 
url = 'https://www.youtube.com/channel/UCi33DX7KG3M3bI0ipjOP2Eg'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
