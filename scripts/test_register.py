import unittest
from page.page_register import Page_register
from util.ECSHOPDB import ECSHOPDB
from util.tool import Tool
from parameterized import parameterized

data = Tool().get_data('./data/register_data.csv')


class Test_register(unittest.TestCase):

    def setUp(self):
        self.register = Page_register()

    def tearDown(self):
        ECSHOPDB().delete_data('users', 'user_name', self.username)
        self.register.driver.quit()

    @parameterized.expand(data)
    def test_register(self, username, email, password, tel):
        self.username = username
        self.register.page_register(username, email, password, tel)
