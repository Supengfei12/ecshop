import page
from base.base import Base


class Page_register(Base):

    def page_register(self,username,email,password,tel):
        self.base_click_element(page.register_link)
        self.base_input_element(page.register_username,username)
        self.base_input_element(page.register_email,email)
        self.base_input_element(page.register_password,password)
        self.base_input_element(page.register_confirm_password,password)
        self.base_input_element(page.register_tel,tel)
        self.base_click_element(page.register_btn)

if __name__ == '__main__':
    s = Page_register()
    s.page_register("susu1","susu1@qq.com","123456","12313212312")