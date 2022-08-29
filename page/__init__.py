# ecshop商城页面配置文件
from selenium.webdriver.common.by import By

ecshop_url = "http://192.168.88.102/ecshop/index.php"

# 登录页面
login_link = By.LINK_TEXT, '请登录'
login_username = By.NAME, 'username'
login_password = By.NAME, 'password'
login_btn = By.NAME, 'submit'
login_ok = By.CSS_SELECTOR, '.f4_b'

# 注册页面
register_link = By.LINK_TEXT, '免费注册'
register_username = By.NAME, 'username'
register_email = By.NAME, 'email'
register_password = By.NAME, 'password'
register_confirm_password = By.NAME, 'confirm_password'
register_tel = By.NAME, 'extend_field5'
register_btn = By.CSS_SELECTOR, '.us_Submit_reg'

# 添加地址
address_link = By.LINK_TEXT, '用户中心'
address_link_ = By.LINK_TEXT, '收货地址'
address_province = By.CSS_SELECTOR, '[name="province"] [value="20"]'
address_city = By.CSS_SELECTOR, '[name="city"] [value="233"]'
address_district = By.CSS_SELECTOR, '[name="district"] [value="2415"]'
address_username = By.CSS_SELECTOR, '[name="consignee"]'
address_address = By.CSS_SELECTOR, '[name="address"]'
address_tel = By.CSS_SELECTOR, '[name="tel"]'
address_btn = By.CSS_SELECTOR, '.bnt_blue_2'
