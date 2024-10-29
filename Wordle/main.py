import os
import time
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import tkinter as tk
import Testing
from selenium.webdriver.support import expected_conditions as EC
from Testing import allGuesses
import customtkinter as ctk

os.environ['PATH'] += os.pathsep + os.path.dirname(__file__)

def quitGame():
    driver.quit()


def trackWordAndColor(iterationNo):
    wordColorsScraped = ""
    rows = driver.find_elements(By.CLASS_NAME, "Row")
    row_n = rows[iterationNo-1]
    letterElements = row_n.find_elements(By.CLASS_NAME, "Row-letter")
    for letterElement in letterElements:
        if letterElement.value_of_css_property("background-color") == 'rgba(164, 174, 196, 1)':
            wordColorsScraped += "B"
        elif letterElement.value_of_css_property("background-color") == 'rgba(243, 194, 55, 1)':
            wordColorsScraped += "Y"
        else:
            wordColorsScraped += "G"
    return wordColorsScraped


def find_possible_words(word, colorList, initialPossibilities):
    possibleWords = initialPossibilities
    for i in range(len(colorList)):
        if colorList[i] == "G":
            possibleWords = [oneWord for oneWord in possibleWords if oneWord[i] == word[i]]
        elif colorList[i] == "B":
            possibleWords = [oneWord for oneWord in possibleWords if word[i] not in oneWord]
        else:
            possibleWords = [oneWord for oneWord in possibleWords if word[i] in oneWord and oneWord[i] != word[i]]
    return possibleWords


def openwordle():
    driver.get("https://wordly.org/")
    close_button = driver.find_element(By.TAG_NAME, "body")
    close_button.click()


def main(iterationNo, initialPossibilities):
    while iterationNo <= 6:
        bestAns = "raise" if iterationNo == 1 else Testing.chooseGuessWithBestEntropyPlusFreq(initialPossibilities)
        driver.find_element(By.TAG_NAME, "body").send_keys(bestAns)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
        time.sleep(2)
        colorScrapedList = trackWordAndColor(iterationNo)
        if colorScrapedList == "GGGGG":
                return
        initialPossibilities = find_possible_words(bestAns.lower(), colorScrapedList, initialPossibilities)
        iterationNo += 1


root = ctk.CTk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title('Wordle')
root.maxsize(853,600)

ctk.set_appearance_mode("dark")

driver = webdriver.Chrome()

frame = ctk.CTkFrame(root)
frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S), padx=10, pady=10,columnspan=2)

background = Image.open("words.jpg")
background.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
backgroundImg = ImageTk.PhotoImage(background)
backgroundImgLabel = ctk.CTkLabel(master=frame, text="", image=backgroundImg)
backgroundImgLabel.place(x=0,y=0)

playGUI = ctk.CTkButton(master=frame, text='Play', command=lambda : openwordle(), anchor="center")
playGUI.pack(padx=15, pady=15)

newGameGuessGUI = ctk.CTkButton(master=frame, text='New Game', command=lambda : main(1, allGuesses))
newGameGuessGUI.pack(padx=15, pady=15)

quitGUI = ctk.CTkButton(master=frame, text='Quit', command=lambda : quitGame())
quitGUI.pack(padx=15, pady=15)


root.mainloop()


