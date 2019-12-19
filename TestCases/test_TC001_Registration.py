import pytest
from Library import IntiateDriver
from Pages import RegistrationPage
from Data import DataGenerator


@pytest.mark.parametrize('data', DataGenerator.DataGenerator())
def test_validateRegistration(data):
    driver = IntiateDriver.startBrowser()
    register = RegistrationPage.RegisterClass(driver)

    register.enter_username(data[0])
    register.enter_password(data[1])
    register.enter_ConfirmPassword(data[2])
    register.enter_email(data[3])

