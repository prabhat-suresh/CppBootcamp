# Roadmap

If you are already well-versed with the basics of programming you can skip to the [Wordle Solver Challenge](./wordle-solver/README.md) section.

## Why C++ ?

C++ is a very powerful language and has a lot of features that make it a good choice for many applications:

- It is fast and efficient.
- It is a compiled language.
- Object-oriented programming is very popular in C++.
- It is a very good language for scientific computing and game development.
- It teaches a lot of low-level concepts that are very useful for programming.
- The STL (Standard Template Library) is a very important part of the language and it is very easy to use, making it ideal for competitive programming and implementing Data Structures and Algorithms which are crucial for internship and placement preparation. Most companies expect you to know C++ and STL.
- Overall it's a great place to start learning programming.

## Basics of C++

### Input and Output

Printing to the console is done using the `cout` object. The `endl` object is used to insert a new line after printing. Similarly, the `cin` object is used to read input from the user.

```cpp
cout << "Hello World!" << endl;

string name;
cout << "Enter your name:\n";
cin >> name;
cout << "Hello " << name << endl;
```

### Comments

Comments are used to add notes to the code to help the programmer understand the code. These are not executed by the computer and are ignored by the compiler.

```cpp
// This is a single line comment

/* This is a multi-line comment
   It can span multiple lines
*/
```

### Variables and Data Types

Variables are used to store data in the computer. They can be of different data types. The data type of a variable is specified when it is declared.

| Type   | Description           |
| ------ | --------------------- |
| int    | Integer               |
| float  | Floating point number |
| char   | Character             |
| bool   | Boolean               |
| string | String                |

```cpp
int x;  // declare an integer variable x
float f = 0.01; // declare a float variable f and initialize it to 0.01
char c = 'c';
bool b;
b = true; // assign the value true to the boolean variable b
string s = "Don't stop at C++. Once you get familiar with low level concepts learn Rust and functional programming languages like Ocaml and Haskell";
```

There are many more data types in C++ such as `long`, `double`, `short`, `unsigned int` etc.

### Operators

| Operator | Description                   |
| -------- | ----------------------------- |
| +        | Addition                      |
| -        | Subtraction                   |
| \*       | Multiplication                |
| /        | Division                      |
| %        | Modulo                        |
| ++       | Increment                     |
| --       | Decrement                     |
| +=       | Addition and assignment       |
| -=       | Subtraction and assignment    |
| \*=      | Multiplication and assignment |
| /=       | Division and assignment       |
| %=       | Modulo and assignment         |
| ==       | Equal to                      |
| !=       | Not equal to                  |
| <        | Less than                     |
| >        | Greater than                  |
| <=       | Less than or equal to         |
| >=       | Greater than or equal to      |
| &&       | Logical AND                   |
| \|\|     | Logical OR                    |
| !        | Logical NOT                   |
| >>       | Right shift                   |
| <<       | Left shift                    |
| &        | Bitwise AND                   |
| \|       | Bitwise OR                    |
| ^        | Bitwise XOR                   |

### Control Structures

#### If, Else, Else If Statements

```cpp
if (condition) {
    // code to execute if condition is true
}
// the following code is optional
else if (condition) {
    // code to execute if condition is true
}
else if (condition) {
    // code to execute if condition is true
}
// ... and so on, we can have as many else if statements as we want
else {  // optional
    // code to execute if all conditions are false
}
```

#### Switch Statement

```cpp
switch (expression) {
    case value1:
        // code to execute if expression is equal to value1
        break;
    case value2:
        // code to execute if expression is equal to value2
        break;
    case value3:
        // code to execute if expression is equal to value3
        break;
    // ... and so on, we can have as many case statements as we want
    default:
        // code to execute if expression is not equal to any of the values
        break;
}
```

#### For Loop

```cpp
for (int i = 0; i < 5; i++) {
    // code to execute 5 times where i takes the values 0, 1, 2, 3, 4 in each iteration
}

// in general the syntax is
for (initialization; condition; increment) {
    // code to execute
}
```

> [!NOTE]
> The initialization and increment are optional and the condition is mandatory.
> The initialization executes only once (at the start of the loop) and the increment executes at the end of each iteration.
> The condition is checked at the start of each iteration and if it is true the loop continues, if it is false the loop stops.

#### While Loop

```cpp
while (condition) {
    // code to execute while condition is true
}
```

> [!IMPORTANT]
> The only way you get better at programming is by practicing.
> **Practise - Loops and Conditionals**
>
> **Odd-Even sum**
> Write a program which does the following:
> Accepts an integer n asks the user to input n numbers and output the sum of even numbers, odd numbers and the total sum
>
> > **Sample input:**
> > 4 (value of n)
> > 1 6 3 5 (4 numbers inputted by the user)
>
> > **Sample output:**
> > Sum of even numbers is: 6
> > Sum of odd numbers is : 9
> > Total sum = 15
>
> **Fibonacci numbers**
> Fibonacci numbers. The fibonacci sequence is as follows: 1 1 2 3 5 8 13 ...
> The first two numbers are '1' each and every number that follows it is the sum of the preceeding two numbers (the two numbers before it).
> Eg: (2 = 1+1, 3 = 1+2, 5 = 2+3)
> Write a program to print the first 'n' fibonacci numbers.
>
> > **Sample input:**
> > n = 6
>
> > **Sample output:**
> > 1 1 2 3 5 8
>
> **Prime Numbers**
>
> Prime Numbers. A prime number is a number (>=2) which has its factors as 1 and the number itself ONLY.
> Write a program that takes as input 'n' (an integer) and prints all the prime numbers in the range [2,n].
>
> > **Sample input : 11**
>
> > **Sample output : 2 3 5 7 11**

### Arrays

Arrays are used to store multiple values of the same data type in a single variable.

```cpp
int arr[5] = {1, 2, 3, 4, 5}; // arr is an array of 5 integers
arr[0] = 10;
// now arr is {10, 2, 3, 4, 5}
```

#### Strings

In C strings are represented as an array of characters.

```cpp
string s = "hello world!";
s[0] = 'H';
s[6] = 'W';
// s is now "Hello world!"
```

### Header Files

```cpp
#include <iostream>    // for input and output
#include <string>      // for string
#include <vector>      // for vector
#include <algorithm>   // for sorting, searching, etc.
#include <cmath>       // for mathematical functions
```

```cpp
#include <bits/stdc++.h>    // for all the STL libraries which includes all the above and much more
using namespace std;        // to use std namespace so that we don't have to write std:: before every function
```

> [!TIP]
> Practice the above concepts with the following questions:
>
> **Palindrome Checker**
> A palindrome is a WORD which reads the same backwards and forwards.
>
> > For example - "racecar" is a palindrome whereas "prabhat" is not a palindrome
> > "prabhat" read backwards is "tahbarp" which is clearly not the same as "prabhat".
> > s is a single word with no spaces and is entirely in lowercase
>
> ```cpp
> using namespace std;
>
> int main(){
> 	string s;
> 	cin>>s; //input the string
> 	//write code to check if its a palindrome
> 	cout<<s<<" is/is not a palindrome\n";
> }
> ```
>
> **Find dulicates in a sorted array**
> You are given n followed by an array of n integers sorted in increasing order. Print out all the duplicated elements in the array.
>
> > Example:
> > Input: n = 5, arr[] = {1, 2, 2, 2, 3, 4, 5, 5}
> > Output: 2 5
>
> ```cpp
> #include <bits/stdc++.h>
> using namespace std;
>
> int main(){
> 	int n;
> 	cin>>n;
> 	int arr[n];
> 	for(int i=0;i<n;i++){
> 		cin>>arr[i];
> 	}
> 	// arr is in sorted order
>     // now find the duplicates and print them
> }
> ```

### Functions

```cpp
int add(int a, int b) {   // function declaration
    return a + b; // the return statement is optional and returns control back to the caller.
}

int main() {
    int x = add(5, 3);    // function call
    cout << x << endl;
}

// The general syntax of a function is as follows:

return_type function_name(parameter_list) {
    // function body
}
```

### Recursion

```cpp
int factorial(int n) {
    if (n == 0) {   // base case
        return 1;
    }
    else {
        return n * factorial(n - 1);    // recursive call
    }
}
```

### Scope of Variables

```cpp
int x = 5;
{
    int x = 10;   // x is in the local scope of the block (The space within the curly braces)
    cout << x << endl;  // prints 10
}   // The scope of the local x ends here
cout << x << endl;  // prints 5 as the x here refers to the global x
```

### Pointers

```cpp
// call by reference
void increment(int *x) {
    // a new integer pointer variable x is created in the function scope and the value of the parameter passed is copied to it
    (*x)++;
}

// call by value
void increment(int x) {
    // a new integer variable x is created in the function scope and the value of the parameterpassed is copied to it

    x++;
}

int main() {
    int x = 5;
    increment(x);
    cout << x << endl;

    int *p = &x;
    increment(p);
    // or equivalently increment(&x);
    cout << x << endl;
}
```

## STL (Standard Template Library)

The STL is a collection of template classes and functions that are defined in various header files. You can use **"bits/stdc++.h"** to include all of them (not a good practice. Ideally one must include only those header files that are required for the program. But this can be ignored for now). Following are some of the commonly used ones:

### Vector

Vector is a dynamic array that can grow or shrink in size. It is a template class and it can be used to store elements of any data type. The elements are stored in contiguous memory locations. The size of the vector is fixed at the time of declaration and can be changed at any time.

```cpp
vector<int> v;  // declare an empty vector of integers
v.push_back(10);  // add an element to the end of the vector
v.push_back(20);  // add another element to the end of the vector
v.push_back(30);  // add another element to the end of the vector
v.pop_back();  // remove the last element from the vector
cout << v.size() << endl;  // print the size of the vector
```

### String

String is a class that represents a sequence of characters. Like vectors, strings are also a template class, can be used to store elements of any data type and are dynamic in size. However unlike vectors, strings can take input directly from the user.

```cpp
string s;  // declare an empty string
cout << "Enter a string: ";
cin >> s;  // take input from the user
s.push_back('!');  // add an element to the end of the string
cout << s << endl;  // print the string
s.pop_back();  // remove the last element from the string
```

### Sorting

```cpp
vector<int> v = {5, 2, 3, 1, 4};
sort(v.begin(), v.end());  // sort the vector in ascending order
reverse(v.begin(), v.end());  // sort the vector in descending order
```

> [!IMPORTANT]
> Now that you have learnt all about functions, pointers, vectors and much more, you can start preparing for technical interviews by solving some [Easy level questions on Leetcode](https://leetcode.com/problemset/?difficulty=EASY&page=1).
> These are a [list of beginner questions](BeginnerLeetcodeQuestions.md) which can be solved if you have clearly understood whatever we have learned so far.

## Programming Challenge - Wordle Solver

### Problem Statement

Wordle is a popular word game in which the player has to guess a five-letter word.

- Check out the rules and play today's [Wordle](https://www.nytimes.com/games/wordle/index.html). You can play multiple games at [Wordly](https://wordly.org/) to get a hang of the game.
- The challenge is to build a wordle solver that can assist you in solving the game.

> [!TIP]
> Check out the [wordle bot](https://ybenhayun.github.io/wordlebot/) to get an idea of what's expected from your wordle solver.

##### Guidelines

- This is the [list](WordleAnswersList.txt) of all possible wordle answers and this is [set](FiveLetterWords.txt) of all possible valid guesses.
- Your wordle solver can be written in any language of your choice.
- Your solution can be a CLI (Command Line Interface) application. However a GUI or TUI will garner more brownie points.
- Your solution will be scored based on the following criteria:
  1. Correctness
  2. Optimality
  3. Good software practices such as modularity, readability, code quality, documentation (adding a README.md file), etc.
  4. Memory and Run-time efficiency
  5. Elegance
- To submit your solution you can use any of the following methods (they are in the increasing order of brownie points):

  - As a zip file
  - Submit a link to your github repository
  - Fork this repository and create a pull request.

- Fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLScouBuDeG-ncgLcF9OkEt4HLFaC-nhHMfNjlH5fBBphAkvWVQ/viewform?usp=sf_link)
  to submit your solution as per your choice on or before **27th October 2024**.

> [!TIP]
> You can refer to this [quick tutorial](https://www.youtube.com/watch?v=HkdAHXoRtos&t=43s) to get started with git and look into other detailed tutorials available online as per need.

- You can refer to articles or videos on various algorithms and approaches to solve the problem. However we strongly discourage any form of plagiarism.
  > [!TIP]
  > Watch this [video by 3B1B](https://www.youtube.com/watch?v=v68zYyaEmEA)
- It would be great if you could design your own solution and explain the logic behind it.
- Achieving feature parity with the [wordle bot](https://ybenhayun.github.io/wordlebot/) would be commendable.

> [!CAUTION]
> If you feel this is a piece of cake for you, develop a solution wherein the bot automatically solves the wordle game for you (Absolutely no human intervention is required).
