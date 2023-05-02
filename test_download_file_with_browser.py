import time
import os.path

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_file_with_browser():
    options = webdriver.ChromeOptions()
    prefs = {
    "download.default_directory": '/Users/kot/GitHubProjects/qa-guru/qa_guru_python_5_7_files',
    "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    browser.config.driver = driver
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(10)

    download_file = os.path.join(RESOURCES_PATH, 'pytest-main.zip')
    assert os.path.exists(download_file)




