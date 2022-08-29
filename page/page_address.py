import page
from page.page_login import Page_login


class Page_address(Page_login):
    def page_address(self,address_username,address_address,address_tel):
        self.page_login_ok()
        self.base_click_element(page.address_link)
        self.base_click_element(page.address_link_)
        self.base_click_element(page.address_province)
        self.base_click_element(page.address_city)
        self.base_click_element(page.address_district)
        self.base_input_element(page.address_username,address_username)
        self.base_input_element(page.address_address,address_address)
        self.base_input_element(page.address_tel,address_tel)
        self.base_click_element(page.address_btn)

if __name__ == '__main__':
    s = Page_address()
    s.page_address('苏鹏飞','新安街道','12312341234')
