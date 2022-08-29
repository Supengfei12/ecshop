from time import strftime

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import page


class Base:
    def __init__(self, url=page.ecshop_url):
        # self.driver = webdriver.Chrome(r'C:\Users\THINK\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.driver = webdriver.Firefox()
        # options = webdriver.ChromeOptions()
        # options.binary_location = r'C:\Users\THINK\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(url=url)

    def base_find_element(self, loc, timeout=30):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.5).until(
            lambda x: x.find_element(*loc)
        )

    def base_input_element(self, loc, value):
        ele = self.base_find_element(loc)
        ele.clear()
        ele.send_keys(value)

    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    def base_exist_element(self, loc):
        try:
            self.base_find_element(loc,timeout=5)
            return True
        except:
            return False
    def base_get_img(self):
        filename = './images/' + strftime('%Y%m%d%H%M%S') + '.png'
        self.driver.get_screenshot_as_file(filename)