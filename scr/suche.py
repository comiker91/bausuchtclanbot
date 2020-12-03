import time
import platform
import random
from datetime import datetime, timedelta
from pathlib import Path
import pyautogui

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdrivermanager import GeckoDriverManager
from fake_useragent import UserAgent

from util import get_lines, out

preis = ""


# TODO Replace time.sleep() with proper Selenium waiting functions

class Votebot():

    def __init__(self):
        self.project_dir = Path.absolute(Path(__file__).parent)
        self.host_os = platform.system()


    def install_driver(self):
        gdd = GeckoDriverManager()
        gdd.download_and_install()

    def set_viewport_size(self, driver, width, height):
        window_size = driver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
            window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        driver.set_window_size(*window_size)

    def init_driver(self):
        # Initialize a Firefox webdriver
        while True:
            try:
                options = Options()
                profile = webdriver.FirefoxProfile()
                profile.set_preference('dom.webdriver.enabled', False)




                driver_filename_extension = ""
                if (self.host_os == "Linux" or self.host_os == "Darwin"):  # Linux or MacOS
                    driver_folder = "macos" if self.host_os == "Darwin" else "linux"
                elif self.host_os == "Windows":
                    driver_folder = "windows"
                    driver_filename_extension = ".exe"
                driver_path = str(Path.joinpath(self.project_dir, f"browser/driver/{driver_folder}/geckodriver{driver_filename_extension}"))

                driver = webdriver.Firefox(profile, options=options, executable_path=driver_path)
                break
            except WebDriverException:
                self.install_driver()
                continue  # Retry
        return driver

    def install_ext(self, driver):
        extension_dir = Path.joinpath(self.project_dir, "browser/extensions/")

        extensions = [
            "{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi",
            "uBlock0@raymondhill.net.xpi"
        ]

        for ext in extensions:
            # Path has to be converted to a string because a path object won't work here
            driver.install_addon(str(Path.joinpath(extension_dir, ext)))

    def vote(self, driver, url, item):
        global preis
        preis = ""
        # TODO set viewport depending on whether a mobile or desktop useragent is used
        self.set_viewport_size(driver, 1920, 1080)
        driver.get(url)
        try:
            text_input = driver.find_element_by_id("search-item")              

            text_input.click()

            text_input.send_keys(item)
            
            text_input.send_keys(Keys.ENTER)
            time.sleep(2)
            submit_button = driver.find_element_by_xpath("/html/body/section/div/div/div/div[2]/div/div/a/div/h5")
            submit_button.click()

            preis = driver.find_element_by_xpath("/html/body/section/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/h5/b").get_attribute("innerText").replace("$","").replace("\n","")
        except NoSuchElementException:
            pass


        



        driver.close()
    def run(self, url,item):
        for url in url:
            driver = self.init_driver()
            self.install_ext(driver)
            while True:
                try:
                    self.vote(driver, url,item)
                    break
                except UnexpectedAlertPresentException:
                    out("Seite war nicht erreichbar wir versuchen es erneut!")
                    break

    def start(item):
        global preis
        bot = Votebot()

        url = get_lines("urls.txt")  # URL to the vote page of a server on minecraft-server.eu

        bot.run(url,item)
        return preis

