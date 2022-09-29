from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import argparse
import os
import psutil
import webbrowser
import wmi


URLS = [
    "https://studio.youtube.com/",
    "https://www.facebook.com/",
    "https://www.twitch.tv/"
    ]


def open_tools():
    """Opens programs like OBS Studio and nginx"""
    # os.startfile("\\Users\\Ken\\Desktop\\church-example\\nginx-sample.txt")
    # os.startfile("\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")
    os.startfile("\\Users\\Public\\Desktop\\OBS Studio")


def check_processes(process):
    """Looks for nginx process and prints the results"""
    process_count = 0
    for p in psutil.process_iter():
        if process in p.name():
            process_count += 1
    if process_count >= 3:
        print(f"Processes {process} ({process_count}) are running normal.")
    else:
        print(f"Check process {process}. ")


def get_date():
    """Returns today's date in the format of MM/DD/YYY"""
    today = datetime.today()
    formatted_date = today.strftime("%m/%d/%Y")
    # print(f"INFO: Today's result: {formatted_date}")
    return formatted_date


def open_sites(chrome=True):
    """Opens browsers depending on if Chrome is True or not"""
    # Gets proper driver for browser
    if chrome:
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.get(URLS[1])
        # create = driver.find_element(By.ID, "create-icon")
        # create.click()
        # path = "C:\\python\\church\\chromedriver.exe"
        # url = "https://yahoo.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(URLS[0])
        driver.close()
    else:
        driver = webdriver.Firefox()
        driver.get(URLS[0])
        # email = driver.find_element(by=By.NAME, value="identifier")
        # email.send_keys("sauk42@gmail.com")
        # submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        # submit_button.click()
        # password = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        # password_input = input("Password: ")
        # password.send_keys(password_input)
        # submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        # submit_button.click()
        driver.quit()

# Main function to run program
def main():
    # Initiates the program and parser
    parser = argparse.ArgumentParser(
        prog="Streaming setup",
        description="Set up streaming",
    )
    # Argument for time of service
    parser.add_argument(
        "-t", "--time",
        default="9:00",
        choices=["9:00", "11:00", "10:00"],
        required=True,
    )
    # Argument for sermon
    parser.add_argument(
        "-s", "--sermon",
        required=True,
    )
    args = parser.parse_args()


    # Open browser to URLs, OBS, and nginx (Atom for now)
    # open_tools()

    # Check certain processes
    check_processes("atom")

    date = get_date()

    stream_title = f'{date} - "{args.sermon}" - ({args.time} Service)'
    print(f"INFO: The stream title will be {stream_title}")

    with open("/python/church/chat-links/links.txt", mode="r") as links:
        for l in links.readlines():
            print(l)

    # Opens sites and manipulates sites
    # open_sites(chrome=False)


if __name__ == "__main__":
    main()
