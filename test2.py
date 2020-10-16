from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:\\Users\\pk111\\AppData\\Local\\Google\\Chrome\\")

driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(driver, chrome_options=chrome_options)
chrome_browser.maximize_window()
