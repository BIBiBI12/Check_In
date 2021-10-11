import time, ddddocr, requests, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
from muacloud import *

username = "wmathor@163.com" # 登录账号
password = "w739616037" # 登录密码
img_path = os.getcwd() + "/1.png"

def ocr(img_path):
    ocr = ddddocr.DdddOcr()
    with open(img_path, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res

def save_img(src):
    img = requests.get(src)
    with open(img_path, "wb") as f:
        f.write(img.content)
        f.close()

def gamekegs(driver):
    try:
        
        driver.get("https://gamekegs.com/login")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        driver.find_element_by_xpath("//*[@class='captcha-clk2']").click() # 点击验证码
        time.sleep(1)

        propertery = driver.find_element_by_xpath("//*[@class='captcha-clk2']")
        driver.save_screenshot(img_path)

    finally:
        driver.quit()
        # muacloud(driver)