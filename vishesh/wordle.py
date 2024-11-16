from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice

with open("WordleAnswersList.txt", "r") as fh:
    wordlst = list(map(lambda st: st.strip().lower(), fh.readlines()))  
#text file was converted to a list strip removed the /n on every element using map  

absentlst = set()
correctdic = {}
otherposdic = {}

def updatelst(ele, words):
    global absentlst, correctdic, otherposdic
    restst = []
    
    for tile in ele:
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

    if len(correctdic) == 5:  #exit if game won as correct dictionary will have length 5 now
        sleep(2)
        print(correctdic)
        driver.quit()
        exit(1)

    for i in words:
        if any(letter in i for letter in absentlst):
            #checks that any letter is not in absent list (letter in i return a list of true or falses)
            continue
        if any(i[pos] != letter for pos, letter in correctdic.items()):
            # tells if any of the correct words are not in the position they have to be in the word, if this is the case then skip else continue
            continue
        if any(i[pos] == letter or letter not in i for pos, letter in otherposdic.items()):
            #checks if the letter is present in the position or not at all in the word, if this is te case then skip the word
            continue
        restst.append(i)
        # if the above three don't match add the word to our restst and return it

    return restst

# driverpath = r".\chromedriver-win64\chromedriver.exe"
# uncomment the above driver for windows, the lower driver is for linux
driverpath = r"./chromedriver-linux64/chromedriver"

service = Service(executable_path=driverpath)
driver = webdriver.Chrome(service=service)
driver.get("https://www.nytimes.com/games/wordle/index.html")
sleep(2)

buttons = driver.find_elements(By.CLASS_NAME, "Welcome-module_button__ZG0Zh")
if len(buttons) >= 3:
    buttons[2].click()
    sleep(3)  

#had to do this because the three bittons had the same class and if not used the subsribe button was being clicked, so i had to acces button[2]

crossbtn = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
crossbtn.click()
sleep(2)  

#when run using selenuim, the website gave a tutorial window which had to be crossed, this will not come while normally playing it because it doesn't show up after one itme

body = driver.find_element(By.TAG_NAME, 'body')

word = "ADIOS" #an initial word
body.send_keys(word + Keys.RETURN)
sleep(3)

ele = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tile"]')
wordlst = updatelst(ele, wordlst)
def make_guess():
    global wordlst
    if not wordlst:
        #sometimes was giving errors where wordlst was returning empty maybe because it was not given enough time to process
        driver.quit()
        exit(1)
    word = choice(wordlst)
    body.send_keys(word + Keys.RETURN)
    sleep(4)
    ele = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tile"]')
    wordlst = updatelst(ele, wordlst)

for i in range(5):
    make_guess()

driver.quit()
