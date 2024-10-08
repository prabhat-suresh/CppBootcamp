# Roadmap

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

```cpp
cout << "Hello World!" << endl;

string name;
cout << "Enter your name:\n";
cin >> name;
cout << "Hello " << name << endl;
```

### Comments

```cpp
// This is a single line comment

/* This is a multi-line comment
   It can span multiple lines
*/
```

### Variables and Data Types

| Type | Description |
| --- | --- |
| int | Integer |
| float | Floating point number |
| char | Character |
| bool | Boolean |
| string | String |

```cpp
int x = 5;
float f = 0.01;
char c = 'c';
bool b = true;
string s = "Don't stop at C++. Once you get familiar with low level concepts learn Rustand functional programming languages like Ocaml";
```

### Operators

| Operator | Description |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulo |
| ++ | Increment |
| -- | Decrement |
| += | Addition and assignment |
| -= | Subtraction and assignment |
| *= | Multiplication and assignment |
| /= | Division and assignment |
| %= | Modulo and assignment |

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

### Functions

```cpp
int add(int a, int b) {
    return a + b;
}
```

### Arrays

```cpp
int arr[5] = {1, 2, 3, 4, 5};
```

### Pointers

```cpp
int *ptr;
ptr = &arr[0];
```
