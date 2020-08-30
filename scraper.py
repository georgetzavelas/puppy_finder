from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait

# configure Chrome Webdriver
def configure_chrome_driver():
    # Add additional Options to the webdriver
    chrome_options = ChromeOptions()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # if driver is in PATH, no need to provide executable_path
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chrome_options)
    return driver


def get(url):
    driver = configure_chrome_driver()
    driver.get(url)
    return driver


def get_and_wait(url, div):
    driver = configure_chrome_driver()
    driver.get(url)
    WebDriverWait(driver, 6).until(
        lambda s: s.find_element_by_id(div).is_displayed()
    )
    return driver
