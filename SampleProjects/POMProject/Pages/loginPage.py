class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_click_id = "btnLogin"
        self.invalid_password_message_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_click_id).click()

    def not_login(self):
        msg = self.driver.find_element_by_xpath(self.invalid_password_message_xpath).text
        return msg
