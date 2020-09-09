import time

from selenium import webdriver


def minecraftServerEu(browser):
    # https://minecraft-server.eu/vote/index/7FF3
    # print(browser)
    browser.get('https://minecraft-server.eu/vote/index/7FF3')
    time.sleep(18)
    text_Field = browser.find_element_by_id('playername')
    text_Field.send_keys('Spielername')
    time.sleep(1)
    acceptButton = browser.find_element_by_id('captcha')
    acceptButton.click()
    pass

if __name__ == '__main__':
    browser = webdriver.Chrome('D:\selenium\chromedriver.exe')
    minecraftServerEu(browser)