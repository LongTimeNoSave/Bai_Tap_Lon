import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import cv2
import numpy as np
import base64
import easyocr

def check_vi_pham():
    # Khởi tạo EasyOCR
    reader = easyocr.Reader(['en'])  

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()

    # Truy cập trang web
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    time.sleep(3)

    
    captcha_img = driver.find_element(By.ID, "imgCaptcha")
    captcha_base64 = captcha_img.screenshot_as_base64

  
    captcha_bytes = base64.b64decode(captcha_base64)
    img_array = np.frombuffer(captcha_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.convertScaleAbs(gray, alpha=2.0, beta=0)

    # Đọc text từ captcha bằng EasyOCR
    results = reader.readtext(gray)
    textcaptcha = results[0][-2].replace(" ", "") if results else ""

    driver.find_element(By.NAME, "txt_captcha").send_keys(textcaptcha)
    driver.find_element(By.NAME, "BienKiemSoat").send_keys("73H1-123456")
    Select(driver.find_element(By.NAME, "LoaiXe")).select_by_index(1)

    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "btnTraCuu").click()
    time.sleep(3)

    # Kiểm tra kết quả
    element_result = driver.find_element(By.ID, "bodyPrint123")
    text_result = element_result.text

    if 'Không tìm thấy kết quả !' in text_result:
        print("Không tìm thấy vi phạm phạt nguội")
    else:
        print("Tìm thấy vi phạm phạt nguội")

    driver.quit()

# Lên lịch chạy
schedule.every().day.at("06:00").do(check_vi_pham)
schedule.every().day.at("12:00").do(check_vi_pham)
check_vi_pham()
while True:
    schedule.run_pending()
    time.sleep(30)
