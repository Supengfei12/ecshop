import unittest
from parameterized import parameterized

import page
from page.page_login import Page_login
from util.tool import Tool

data = Tool().get_data('./data/login_data.csv')


class test_login(unittest.TestCase):
    def setUp(self):
        self.login = Page_login()

    def tearDown(self):
        self.login.driver.quit()

    @parameterized.expand(data)
    def test_login(self, username, password):
        self.login.page_login(username, password)
        try:
            result = self.login.base_exist_element(page.login_ok)
            self.assertTrue(result,msg='未登录')
        except AssertionError as e:
            self.login.base_get_img()
            raise e



if __name__ == '__main__':
    s = unittest.main()