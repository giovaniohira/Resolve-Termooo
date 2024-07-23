import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_days_since_start():
    return (datetime.date.today() - datetime.date(2022, 1, 1)).days

def get_daily_word():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        if get_days_since_start() <= len(lines):
            return lines[get_days_since_start() - 1].strip()
    return None

def complete_termooo(word):
    driver = webdriver.Chrome()
    driver.get("https://www.term.ooo")

    #Click on the screen to skip the tutorial
    driver.execute_script("document.elementFromPoint(100, 100).click()")

    #Get the element to type the word in.
    body = driver.find_element(by="tag name", value="body")
    main = body.find_element(by="tag name", value="main")
    wcboard = main.find_element(by="tag name", value="wc-board")
    shadowroot1 = wcboard.shadow_root
    hold = shadowroot1.find_element(by="id", value="hold")
    wcrow = hold.find_element(by="css selector", value="wc-row[termo-row='0']")
    shadowroot2 = wcrow.shadow_root
    letter = shadowroot2.find_element(by="css selector", value="div[lid='0']")


    #Type the day's word
    letter.send_keys("{}".format(word) + Keys.ENTER)
    time.sleep(4)
    driver.close()

if __name__ == "__main__":
    word = get_daily_word()
    if word:
        complete_termooo(word)
    else:
        print("No word for today.")