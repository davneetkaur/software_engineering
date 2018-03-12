from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = None

def setup_module(module):
    global browser
    browser = webdriver.Chrome()
    browser.get("http://www.amazon.com")

def teardown_module(module):
    time.sleep(10)
    if browser:
        browser.close()

def test_did_we_get_to_amazon():
    assert "Amazon" in browser.title
    print (browser.title)

def test_on_displayed_blenders():
    id = "twotabsearchtextbox"
    searchbox = browser.find_element_by_id(id)
    searchbox.clear()
    searchbox.send_keys("blender")
    searchbox.submit() 
    time.sleep(10)
    id="s-results-list-atf"
    result_text = browser.find_element_by_id(id).text
    assert "Oster" in result_text
    assert "Hamilton Beach" in result_text