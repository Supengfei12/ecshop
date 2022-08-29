import page
from base.base import Base


class Page_login(Base):

    def page_login(self, username, password):
        self.base_click_element(page.login_link)
        self.base_input_element(page.login_username, username)
        self.base_input_element(page.login_password, password)
        self.base_click_element(page.login_btn)

    def page_login_ok(self):
        self.page_login('sususu', '123456')


if __name__ == '__main__':
    s = Page_login()
    s.page_login_ok()