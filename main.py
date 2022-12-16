import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = os.getenv('EMAIL')
password = os.getenv('PASS')

chrome_driver_path = '/Users/racool/Desktop/chromedriver'


class InternetSpeedTwitterBot:
    def __init__(self, up='--', down='--'):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.up = up
        self.down = down

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)
        self.up = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.down = self.driver.find_element(By.CLASS_NAME, 'upload-speed')

        return f'download: {self.up.text} mbps \nupload: {self.down.text} mbps'

    def tweet_at_provider(self):
        pass


speed = InternetSpeedTwitterBot()
data = speed.get_internet_speed()
print(data)
time.sleep(5)
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://twitter.com/')
time.sleep(5)
driver.find_element(By.XPATH,
                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'r-30o5oe').send_keys(email)

driver.find_elements(By.CLASS_NAME, 'r-1phboty')[2].click()
time.sleep(5)
passWord = driver.find_element(By.NAME, 'password')
passWord.send_keys(password)
passWord.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block').send_keys(f'Just Testing My Python Code :\n My '
                                                                               f'Internet speed is :\n{data}')
time.sleep(3)
driver.find_elements(By.CLASS_NAME, 'r-sdzlij')[35].click()


