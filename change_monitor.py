import pywhatkit
import time
import pytz
import datetime
import hashlib
from urllib.request import urlopen, Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import string
import json
import random
import re
import time
from PIL import Image
from datetime import datetime
from threading import Timer
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
from getpass import getpass
from discord import Webhook, RequestsWebhookAdapter, Embed, errors
driver: webdriver.Chrome = None
tim1=datetime.now()
rand=tim1.hour*10000+tim1.minute*100+1
config = None
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--use-fake-ui-for-media-stream')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile.default_content_setting_values.media_stream_mic': 1,
    'profile.default_content_setting_values.media_stream_camera': 1,
    'profile.default_content_setting_values.geolocation': 1,
    'profile.default_content_setting_values.notifications': 1,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# make the window a minimum width to show the meetings menu
window_size = driver.get_window_size()
if window_size['width'] < 1200:
    print("Resized window width")
    driver.set_window_size(1200, window_size['height'])

if window_size['height'] < 850:
    print("Resized window height")
    driver.set_window_size(window_size['width'], 850)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://erp.iitkgp.ac.in")
user_id="19MA20040"
pswd="thunderstar"
time.sleep(3)
id_element=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[1]/input")
id_element.send_keys(user_id)
print("User id entered")
pswd_element=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[2]/input")
pswd_element.send_keys(pswd)
print("Password Entered")
time.sleep(3)
nn_element=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[3]/input")
nn_element.send_keys(pswd)
print("Nick name entered")
button=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/form/fieldset/div[4]/div/input[3]")
button.click()
print("Logged in")
time.sleep(3)
driver.get("https://erp.iitkgp.ac.in/IIT_ERP3/menulist.htm?module_id=26")
time.sleep(2)
random1=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]")
random1.click()
time.sleep(2)
random2=driver.find_element_by_xpath('//*[@id="collapse2610"]/div/div[1]/a[1]')
random2.click()
time.sleep(2)
size = len(driver.find_elements_by_tag_name("iframe"))
driver.switch_to.frame("myframe")
random3=driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[5]/div/table/tbody/tr/td[3]/div').text
st=str(random3)
prev_len=st[15:17]
rand2=str(rand)+".png"
random4=driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[3]/div[2]/div/table/thead/tr[3]/th[10]")
time.sleep(1)
random4.click()
time.sleep(2)
random4.click()
driver.save_screenshot(rand2)
rand=rand+1
tim = datetime.now()
h=tim.hour
m=tim.minute
pywhatkit.sendwhats_image("CfQv1lFwoOgKsaDQimMG2V",rand2,"New Companies' applications open in ERP!",20)
while True:
    time.sleep(300)
    random3=driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[5]/div/table/tbody/tr/td[3]/div").text
    curr_len=str(random3)
    curr_len=curr_len[15:17]
    if curr_len != prev_len :
        rand2=str(rand)+".png"
        random4=driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[3]/div[2]/div/table/thead/tr[3]/th[10]")
        time.sleep(1)
        random4.click()
        time.sleep(2)
        random4.click()
        driver.save_screenshot(rand2)
        rand=rand+1
        tim = datetime.now()
        h=tim.hour
        m=tim.minute
        pywhatkit.sendwhats_image("CfQv1lFwoOgKsaDQimMG2V",rand2,"New Companies' applications open in ERP!",20)
    else :
        print("no change")