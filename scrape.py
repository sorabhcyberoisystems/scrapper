import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    #driver.quit()
    return r

goog_search = 'https://app.workfolio.io/login'

r = render_page(goog_search)

soup = BeautifulSoup(r, "html.parser")

loginFeild = soup.select('#root > div.login-root > div.text-center.col-md-6.offset-md-3 > div > form > input')
password = soup.select('#root > div.login-root > div.text-center.col-md-6.offset-md-3 > div > form > div.login-password-field-form-group.form-group > input')

print(loginFeild)
print(password)