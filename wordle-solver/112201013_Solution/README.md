# Solution for the Popular Wordle Solver
This program in the ```112201013_Solution``` folder is one version of a solution for solving the wordle game.

# Running the program
To run the program, navigate to the folder ```112201013_Solution``` and type the following command in the 
terminal
```$ python3 main.py```

# Basic Idea and working
1. The program prompts a word to the user.
2. The user will have to type that input in a wordle game page
    (prefarably <a href="https://wordly.org/">this</a> page)

3. Once the user is done and the website prompts the user for different colored letters and/or indices
    The user will have to enter the 
    a. ```Space seperated indices (0 based)``` for green colored letters and
    b. ```Space seperated letters``` for yellow colored letters

4. Once the user is done entering, the program outputs another word to the user and steps 1, 2 and 3 will
    be repeated until a stopping condition is met

# Stopping condition
1. If the user has won the game:
    The program will be asking ```Is your game done?``` to the user before step 3 in the above algorithm
2. If the program has no more words to check for:
    The program will quit saying ```Sorry, I don't know such a word exists``` and quits
3. If the number of chances exceed the ```MAX_CHANCES``` value (it is set to 6 in the program)