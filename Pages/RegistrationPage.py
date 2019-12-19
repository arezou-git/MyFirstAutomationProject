from selenium.webdriver.support.select import Select


class RegisterClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_name("fld_username").send_keys(username)

    def enter_email(self, email):
        driver.find_element_by_name("fld_email").send_keys(email)

    def enter_password(self, password):
        driver.find_element_by_name("fld_password").send_keys(password)

    def enter_ConfirmPassword(self, password):
        driver.find_element_by_name("fld_cpassword").send_keys(password)

    def enter_date(self,date):
        driver.find_element_by_name("dob").send_keys(date)

    def enter_phone(self, phone):
        driver.find_element_by_name("phone").send_keys(phone)

    def enter_address(self, address):
        driver.find_element_by_name("address").send_keys(address)

    def enter_addressType(self, addressType):
        driver.find_element_by_xpath("//input[@value='home']").click()


    def enter_gender(self, gender):
        obj = Select(driver.find_element_by_name("sex"))
        obj.select_by_visible_text(gender)

    def enter_country(self, country):
        obj = Select(driver.find_element_by_name("country"))
        obj.select_by_visible_text(country)

    def enter_state(self, state):
        obj = Select(driver.find_element_by_name("state"))
        obj.select_by_visible_text(state)

    def enter_city(self,city):
        obj = Select(driver.find_element_by_name("city"))
        obj.select_by_visible_text(city)

    def enter_zipCode(self,zipCode):
        driver.find_element_by_name("zip").send_keys(zipCode)

    def enter_agree(self):
        driver.find_element_by_name("terms").click()

    def enter_signUp(self):
        driver.find_element_by_xpath("//input[@type = submit").click()