from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import requests

def get_driver():
    # chrome options settings
    chrome_options = webdriver.ChromeOptions()
    settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId":"Save as PDF", "version": 2}
    prefs = {"printing.print_preview_sticky_settings.appState": json.dumps(settings)}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--kiosk-printing")

    # Launch browser with predefined settings
    browser = webdriver.Chrome(executable_path = ChromeDriverManager().install(), options=chrome_options)
    return browser

def download_article(URL):
    browser = get_driver()
    browser.get(URL)

    # Launch print and save as pdf
    browser.execute_script("windows.print();")
    browser.close()

if __name__ == "__main__":
    URL = input("provide article URL:")
    # Check if the url is valid/reachable
    if requests.get(URL).status_code==200:
        try:
            download_article(URL)
            print("Your article is successfully downloaded!")
        except Exception as e:
            print(e)
    else:
        print("Enter a valid working URL")