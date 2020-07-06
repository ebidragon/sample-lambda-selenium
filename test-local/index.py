import json
import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

env_key = os.environ.get("ENV_KEY")

sys_platform = platform.system()
executable = os.path.join(os.getcwd(), "chromedriver")
if sys_platform == "Windows":
    executable += ".exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=executable, options=options)

driver.get("https://httpbin.org/ip")
ip = json.loads(driver.find_element_by_css_selector("body").text)["origin"]
driver.close()
driver.quit()

response_body = {"ip": ip}
if env_key:
    response_body["envKey"] = env_key
response = {"body": response_body}

print(response)
