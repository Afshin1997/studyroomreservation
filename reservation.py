
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:58:31 2021

@author: afshin

"""
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telegram_send
import calendar
from selenium.webdriver.chrome.options import Options
global slots
def studyroom(username, password):
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=option)
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    
    driver.get("https://idp.polito.it/idp/x509mixed-login")
    
    driver.find_element(By.ID, 'j_username').send_keys("{username}".format(username = username))
    driver.find_element(By.ID, 'j_password').send_keys("{password}".format(password = password))
    driver.find_element_by_xpath("//*[@id='usernamepassword']").click()
    time.sleep(0.5)

    driver.find_element_by_xpath("/html/body/div/div/div[6]/div[3]/div/section/div[3]/div[2]/div/a").click()
    time.sleep(0.05)
    
    Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[3]/div/div[5]/a")))
    Element.click()
    time.sleep(0.05)

    Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[4]/div[2]/table/tbody/tr[6]/td/h4/span[2]")))
    Element.click()
    time.sleep(0.05)
    Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[5]/div/table/tbody/tr[15]/td/h4/span[2]")))
    Element.click()
    time.sleep(0.05)

    weekday_r = datetime.datetime.today().weekday()
    current_time = datetime.datetime.now()
    current_time = current_time.hour
    if ( 1<= current_time <= 10):
        slots = [1,2]
    elif ( 12<= current_time <= 16):
        slots = [3,4]
    
    
    weekday = weekday_r
    
    if weekday in range(0,3):
        
        weekday = weekday_r + 4
        for s in slots:
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[6]/div[3]/div/div[3]/table/tbody/tr[2]/td[{weekday}]/div/div[{slot}]/div[1]".format(weekday = weekday , slot = s))))).click()
            time.sleep(0.5)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/input")))).click()
            time.sleep(0.5)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/button[1]")))).click()
            time.sleep(0.75)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[3]/button")))).click()
            # time.sleep(0.75)
            telegram_send.send(messages=["Reserved Fucking Studyroom {weekday} slot {slot} for {username} ".format(weekday = calendar.day_name[weekday_r], slot = s, username = username)])
            time.sleep(0.5)
        driver.close()
        
    elif weekday in range(5,7):
        
        time.sleep(2)
        weekday = weekday_r - 3
        (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[6]/div[3]/div/div[1]/div[2]/button[3]/span[1]")))).click()
        time.sleep(0.5)
        for s in slots:  
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[6]/div[3]/div/div[3]/table/tbody/tr[2]/td[{weekday}]/div/div[{slot}]/div[1]".format(weekday = weekday , slot = s))))).click()
            time.sleep(0.5)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/input")))).click()
            time.sleep(0.5)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/button[1]")))).click()
            time.sleep(0.5)
            (WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div/div[3]/button")))).click()
            time.sleep(0.5)
            telegram_send.send(messages=["Reserved Fucking Studyroom {weekday} slot {slot} for {username}".format(weekday = calendar.day_name[weekday_r], slot = s, username = username)])
            time.sleep(0.25)
        
        driver.close()
            
            
    
