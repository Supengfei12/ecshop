import page
from page.page_login import Page_login


class Page_cart(Page_login):

    def page_cart(self):
        open('../data/su.txt',mode='w',encoding='utf-8').write(
            'spf,'
            'spf,'
            'spf,'
            'spf'
        )

if __name__ == '__main__':
    s = Page_cart()
    s.page_cart()