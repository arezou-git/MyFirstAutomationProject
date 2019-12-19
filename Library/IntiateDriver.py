from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from . import ConfigReader


def startBrowser():
    global driver
    config = ConfigReader.Config()

    if config.readConfigData('Details', 'Browser') == Chrome:
        #path = "../Driver/chromedriver.exe"
        driver = Chrome()
    elif config.readConfigData('Details', 'Browser') == Firefox:
        path = "../Driver/geckodriver.exe"
        driver = Firefox(path)
    else:
        path = "../Driver/chromedriver.exe"
        driver = Chrome(path)

    driver.get(config.readConfigData('Details','ApplicationUrl'))
    driver.maximize_window()

    return driver


def closeBrowser():
    driver.close()