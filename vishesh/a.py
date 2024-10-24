from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice

with open("WordleAnswersList.txt", "r") as fh:
    wordlst = list(map(lambda st: st.strip().lower(), fh.readlines()))  

absentlst = set()
correctdic = {}
otherposdic = {}

def updatelst(tiles, words):
    global absentlst, correctdic, otherposdic
    filtered_words = []
    
    for tile in tiles:
        aria_label = tile.get_attribute("aria-label")
        data_state = tile.get_attribute("data-state")
        condition = aria_label.split()
        pos = int(condition[0][0]) - 1  
        letter = condition[2][:-1].lower()  

        if data_state == 'correct':
            correctdic[pos] = letter
        elif pos not in correctdic:  
            if data_state == 'absent':
                absentlst.add(letter)
            elif data_state == 'present':
                otherposdic[pos] = letter

    if len(correctdic) == 5:
        sleep(2)
        print(correctdic)
        driver.quit()
        exit(1)

    for word in words:
        if any(letter in word for letter in absentlst):
            continue
        if any(word[pos] != letter for pos, letter in correctdic.items()):
            continue
        if any(word[pos] == letter or letter not in word for pos, letter in otherposdic.items()):
            continue
        filtered_words.append(word)

    return filtered_words

driverpath = r"C:\Users\Vishesh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driverpath)
driver = webdriver.Chrome(service=service)
driver.get("https://www.nytimes.com/games/wordle/index.html")
sleep(2)

buttons = driver.find_elements(By.CLASS_NAME, "Welcome-module_button__ZG0Zh")
if len(buttons) >= 3:
    buttons[2].click()
    sleep(3)  
crossbtn = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
crossbtn.click()
sleep(2)  

body = driver.find_element(By.TAG_NAME, 'body')

word = "ADIOS"
body.send_keys(word + Keys.RETURN)
sleep(3)

tiles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tile"]')
wordlst = updatelst(tiles, wordlst)
def make_guess():
    global wordlst
    if not wordlst:
        driver.quit()
        exit(1)
    word = choice(wordlst)
    body.send_keys(word + Keys.RETURN)
    sleep(4)
    tiles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tile"]')
    wordlst = updatelst(tiles, wordlst)

for i in range(5):
    make_guess()

driver.quit()
