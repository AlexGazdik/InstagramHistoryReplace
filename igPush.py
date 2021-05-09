from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import os 
import json

chrome_driver = "C:\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
actions = ActionChains(driver)

f = open('media.json', encoding='utf-8')
data = json.load(f)
photoList = []

#cursor position assignment
postButton= (428, -86)
entryButton = (261, -755)
nextButton = (641, -1112)
captionLocation = (274, -1045)

for post in data['photos'][::-1]:
    pyautogui.moveTo(postButton)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(post['path'][14:])
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(nextButton)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(captionLocation)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(post['caption'])
    pyautogui.moveTo(nextButton)
    pyautogui.click()
    time.sleep(10)
