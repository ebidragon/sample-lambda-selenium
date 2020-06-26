import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

env_key = os.environ.get('ENV_KEY')

def crawler(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/opt/chromedriver', options=options)

    driver.get('https://httpbin.org/ip')
    ip = json.loads(driver.find_element_by_css_selector('body').text)['origin']

    driver.close()
    driver.quit()

    response_body = {
        'ip': ip
    }
    if env_key:
        response_body['envKey'] = env_key

    response = {
        'body': json.dumps(response_body)
    }

    return response
