from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://202.117.80.137:8080/portal/templatePage/20170417191642175/login_custom.jsp")

elem_user = driver.find_element_by_id("id_userName")
elem_user.send_keys("学号")
elem_pwd = driver.find_element_by_id("id_userPwd")
elem_pwd.send_keys("密码")
elem_pwd.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
driver.quit()