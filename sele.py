from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='C:\\Users\dell\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://smartours.com/new-tours/')
driver.find_element_by_xpath('//*[@id="menu-item-26864"]/a/span[1]').click()
user_ele=driver.find_element_by_xpath('//*[@id="sma_gatekeeper_login"]/div/label[1]/input')
print(user_ele.is_displayed())

pwd_ele=driver.find_element_by_xpath('//*[@id="sma_gatekeeper_login"]/div/label[2]/input')
print(pwd_ele.is_displayed())

user_ele.send_keys('sachinbagoriya2@gmail.com')
pwd_ele.send_keys('your password')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="sma_gatekeeper_login"]/input[2]').click()
driver.implicitly_wait(10)#in seconds
driver.find_element_by_xpath('//*[@id="page-banner"]/div/div/div/div[1]/h4/a[2]').click()#Edit your profile

fName=driver.find_element_by_xpath('//*[@id="sma_profile_info"]/div[1]/label[2]/input')
fName.send_keys('Premchand')
time.sleep(5)

#here im getting the location for updating the password
curr_pass=driver.find_element_by_xpath('//*[@id="sma_update_password"]/div[1]/label[1]/input')
new_pass=driver.find_element_by_xpath('//*[@id="sma_update_password"]/div[1]/label[2]/input')
conf_new_pass=driver.find_element_by_xpath('//*[@id="sma_update_password"]/div[1]/label[3]/input')


time.sleep(5)
curr_pass.send_keys('CurrPassword')
new_pass.send_keys('update password')
conf_new_pass.send_keys('updated Password')
time.sleep(20)
driver.find_element_by_xpath('//*[@id="sma_update_password"]/div[2]/input').click()
driver.close()