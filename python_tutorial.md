# Basics of Python

Bored of repeating the same tasks again and again? Let the computer do the work, make your life easier and free up time for more interesting tasks.

Python is widely applicable to a variety of tasks, from web-development to data science to file I/O operations.

We will use Python to automate tasks needed to be performed frequently in computational chemistry.

> This tutorial is valid for Python 3.6 or later.

# How to use Python?

Many machines will have Python2 and Python3 installed. To check this, type
`python` into a command prompt.

On MacOS:

```bash
$ python
Python 2.7.16 (default, Apr 12 2019, 15:32:40)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

As you can see, python2 is loaded. To access Python3, `python3` must be written.

```bash
$ python3
Python 3.7.3 (default, Mar 27 2019, 09:23:15)
[Clang 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If Python3 is not installed, it can be downloaded from the Python online site or
by using Homebrew, `brew install python3`.

When typing `python` or `python3`, a prompt appears waiting for user input. This
is the Python command line interpreter, allowing you to write Python code
directly from the terminal. To re-use code, Python scripts can be saved to a
file, usually with the `py` extension and run like so: `python3 file.py`

# Python specifics

Python relies on indentation to group lines of code together. Most languages use curly brackets, but by using white space, Python code is generally easier to read and write. Just try not to mix tabs with spaces as Python will not run if both are used. 

An important concept in Python is that everything is an object, with a type. To find out what kind of object you are dealing with, use the function `type()`.

Comments can be written in Python using the `#` symbol, and multi-line comments
are wrapped in triple quotes.

# Fundamental data types

## Variables

To be able to pass information around in Python, that data needs to be stored in
a variable, using the `=` sign:

```python
>>> var = 'Here is a sentence.'
>>> var
'Here is a sentence.'
```

## Strings

Text is entered as a `string` using quotation marks:

```python
>>> text = 'This is a string'
>>> type(text)
<class 'str'>
```

Strings can be joined together, or concatenated with the `+` operator:
```python
>>> more_text = 'of more text'
>>> text + more_text
'This is a stringof more text'
```
Notice that no spaces are added when strings are concatenated. To fix this, simply add a space that is placed in between quotation marks:

```python
>>> text + ' ' +  more_text
'This is a string of more text'
```
Or print the text in a formatted string, known as an f-string, with variables
printed using curly braces:

```python
>>> print(f'{text} {more_text}')
This is a string of more text
```

It is useful to look for certain phrases in a string. In Python, there are many
methods that have been implemented to make this easy.

| Place | command |
| :---: | :---:   |
Start of string | `string.startswith(phrase)` |
End of string  | `string.endswith(phrase)` |
Anywhere | `if 'phrase' in string` or `string.contains(phrase)` |


## Numerical values

Whole numbers are known as integers, with decimals called floats, as
they contain floating point values. As you would expect, basic mathematical operations are supported 'out of the box', and integers and floats can be combined in the same expression:

```python
>>> integer1 = 1
>>> integer2 = 4
>>> float1 = 0.2
>>> float2 = 2.0
>>> integer1 + integer2
5
>>> float1 + float2
2.2
>>> integer2 * float2
8.0
>>> integer2 / float2
2.0
>>> integer2 - integer1
3
```

## Boolean values

Boolean values can take the value of `True` or `False`. For example, when
looking for a certain phrase, a boolean variable named `found` can be defined,
set to `False`. When the phrase is found, it can be set to `True`:

```python

found = False

if 'phrase' in line:
    found = True
```

# Data structures

## Lists
Variables are useful, but let's say you wanted to store multiple items together. Lists can be used to achieve this, written using square brackets:

```python
>>> lst = [1, 2, 3, 4, 5]
>>> type(lst)
<class 'list'>
```
Properties of lists can be found using functions that were written to be applied to them. For example, to find how many items are stored in a list, use the function `len()`:

```python
>>> len(lst)
3
```

To access items, or elements, of each list, square bracket notation is used.
Note that 'zero-indexing' is used in Python, with the first element in the list
located at the 0th position:

```python
>>> lst[0]
1
>>> lst[2]
3
```

Lists can be sliced to select a subset of the array. The syntax is as follows: `lst[start : end]`, selecting items from `start` up to but not including the `end`:
```python
>>> lst[:3] # first three items
[1, 2, 3]
>>> lst[2:4]
[3, 4] 
```

Lists can be added together with the `+` sign:
```python
>>> [1, 2, 3] + [7, 8, 9]
[1, 2, 3, 7, 8, 9]
```

To add things to the end of a list, use the `append` method, modifying the original list in place:
```python
>>> first = [1, 2, 3]
>>> second = 4
>>> first.append(second)
>>> first
[1, 2, 3, 4]
```

Watch out for unexpected behaviour. If you want to take the list `items = [1, 2, 3]` and multiply every item by 3, you might tempted to do this:

```python
>>> items = [1, 2, 3] 
>>> items * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

However this just takes the contents of the list and repeats it three times...

To do this, we have to move through the list and multiply each item as we go.

Use a loop! See the loops section [here](#loops)

Sometimes it useful to get the index of each item of a list. This can be done using the
length of the list, or the `enumerate` method:
```python
>>> lst = ['One', 'Two', 'Three']
>>> for index in range(len(lst)):
...     print(index, lst[index])
...
0 One
1 Two
2 Three
```

or

```python
>>> for index, item in enumerate(lst):
...     print(f"Index {index} = {item}")
...
Index 0 = One
Index 1 = Two
Index 2 = Three
```

The enumerate function actually returns a generator object (see later), with each index and item contained in a tuple:

```python
>>> enumerate(lst)
<enumerate object at 0x106feaaf8>
>>> list(enumerate(lst))
[(0, 'One'), (1, 'Two'), (2, 'Three')]
```

## Tuples

Lists are mutable data types, where items in the list can be modified after being added to the list. Tuples are similar, but immutable- once a tuple is created, it cannot be changed. This can be useful when dealing with large amounts of data, and python runs faster when using tuples over lists. Tuples are assigned with parentheses:

```python
>>> tup = (1, 2, 3)
```

Tuples are also iterable:

```python
>>> for num in tup:
...     print(num)
...
1
2
3
```

## Dictionaries

You may want to store data and refer to it later using another variable. For example, the names and ages of people. This can be done using a list of lists:

```python
>>> people = [['John', 35], ['Gemma', 50], ['David', 25]]
```

To get the names of each person:

```python
>>> for person in people:
...     print(person[0])
...
John
Gemma
David
```

This works but there is no indication of the kind of value that `person[0]` refers to.

A better way is to use a dictionary. A dictionary uses key-value pairs, where the key can be used to refer to values at a later time. Create a dictionary using curly braces and separate keys from their values with a colon:

```python
>>> people = {'John': 35, 'Gemma': 50, 'David': 25}
>>> for name in people:
...     print(name)
...
John
Gemma
David
```

Much clearer! Ages can be accessed with the `values` method:

```python
>>> for age in people.values():
...     print(age)
...
35
50
25
```

To find the age of John:

```python
>>> people['John']
35
```

But wouldn't it be good to access both names and ages? This can be done with the `items` method:

```python
>>> for name, age in people.items():
...     print(name, age)
...
John 35
Gemma 50
David 25
```

Lists and dictionaries can also be combined. Using a list of dictionaries, the names of each person will be stored as values with the key `name`, same with their ages:

```python

>>> people = [{'name': 'John' , 'age': 35}, 
              {'name': 'Gemma', 'age': 50},
              {'name': 'David', 'age': 25}]

>>> for person in people:
...     print(f"{person['name']} is {person['age']} years old")
...
John is 35 years old
Gemma is 50 years old
David is 25 years old
```

## Conditional statements

Conditional statements let us dictate what we would like to happen in a situation where two results can occur. If you want to see if one number is less than another:

```python
>>> num1 = 10
>>> num2 = 5
>>> if num2 < num1:
...     print('True')
...
True
```

Multiple conditions can be placed together in the same block:

```python
>>> if num1 < num2:
...     print('num1 is less than num2')
... elif num1 == num2: # else if
...     print('num1 is equal to num2')
... else:
...     print('num1 is greater than num2')
...
num1 is greater than num2
```

To negate a comparison, use the `not` keyword:

```python

>>> name = 'Tom'
>>> if name is not 'Jerry':
...    print('Not Jerry')
...
Not Jerry
```

# Loops

## For loops

Every data structure in Python that contains multiple items can be 'iterated'
over using a `for` loop, with the following syntax:

```python
for item in iterable:
  do_something_with_the_item()
```

Now, to multiple every item of the `items` list by 3:

```python
>>> items = [1, 2, 3]
>>> for item in items:
...     multiple = item * 3
...     print(multiple)
...
3
6
9
```

But the original list still contains the original values! The multiples need to be added to a new list:

```python
>>> items
[1, 2, 3] # The loop didn't change the original values

>>> multiples = []
>>> for item in items:
...     multiple = item * 3
...     multiples.append(multiple)
...
>>> multiples
[3, 6, 9]
```

List comprehensions are a nice way to achieve the same thing with less typing:

```python
>>> multiples = [x * 3 for x in items]
>>> multiples
[3, 6, 9]
>>>
```

Useful keywords include `break` and `continue`. The `break` command forces
Python to exit the loop immediately, and the `continue` keyword tells Python to
skip this iteration and move to the next item in the list.


## While loops

The `while` loop can be used together with conditional statements like so:

```python
>>> while num2 < num1:
...     print('num2 = ', num2)
...     num2 += 1 # add one to num2
...
num2 =  5
num2 =  6
num2 =  7
num2 =  8
num2 =  9
```

When `num2` was set to 10, Python broke out of the loop.


# File operations

Lots of menial tasks involve reading text files, modifying them, then writing the data to a new file.
These tasks are simple using Python. To open a file, just use the `open` function. This takes two arguments, the file name and how you'd like to open it: in read mode, `'r'`, write mode, `'w'`, or append mode, `'a'`. There are other options available for binary, such as `'rb'` and `'wb'`.
Remember to close the file after you have finished processing it!

```python
f = open('file1.txt', 'r')
# process file...
f.close()
```

To avoid having to write `f.close()`, use the `with` keyword that automatically closes the file when Python is finished executing code using the file:

```python
with open('file1.txt', 'r') as f:
    # process file...
```

To read the contents of a file, the `file.read()` command can be used. 

With the file called `file1.txt`:
```text
# file1.txt
one
two
three
```

```python
>>> with open('file1.txt', 'r') as f:
...     contents = f.read() # store file in the variable 'contents'
...
>>> contents
'one\ntwo\nthree\n'
```

`f.read()` returns one string containing the contents of the entire file. For
small files, this is not a problem, but for larger files, it is more efficient
to store the data in a list, using `f.readlines()`.

```python
>>> with open('file1.txt', 'r') as f:
...     contents = f.readlines() 
...
>>> contents
['one\n', 'two\n', 'three\n']
```

Again, for larger files storing the entire contents in a list is inefficient. If
you wish to process the file line-by-line, it is possible to do so without
storing the data in a container. Just iterate over the file itself:

```python
>>> with open('file1.txt', 'r') as f:
...     for line in f:
...         print(line)
...
one

two

three

```
Notice that the newline characters at the end of each line are printed, and can be dropped with the
`strip` method, applicable to any string:
```python

>>> with open('file1.txt', 'r') as f:
...     for line in f:
...         print(line.strip())
...
one
two
three
```

This method of reading files is the fastest way of reading in plain text files-
reading binary files is faster, but requires decoding to process the data.

To write to a file, use the `'w'` argument with a file name:

```python
with open('new_file', 'w') as f:
    f.write(content)
```

To write a list to a file:

```python
with open('new_file', 'w') as f:
    for item in list:
        f.write(item + '\n')
```

Don't forget the newline character otherwise all the items will be placed on the
same line!

# Functions

Writing 'procedural' code, line by line, can quickly get very confusing. A clearer way to layout code involves writing functions, pieces of code that can be re-used multiple times.

For example, to add atomic numbers to a list of coordinates in an xyz format,
you could write something like this:

```text
# coords.xyz
5

C  13.456 12.321 13.054
H  11.222 12.542 10.342
H  10.321  9.896  5.341
O   3.451  5.759  4.531
N   8.421  9.582 10.888
```

```python
atnums = {}
atnums['C'] = 6.0
atnums['H'] = 1.0
atnums['N'] = 7.0
atnums['O'] = 8.0

new_coords = []
with open('coords.xyz', 'r') as f:
    for line in f.readlines()[2:]: # list slicing to only select the coordinates
        sym, x, y, z = line.split()
        atnum = atnums[sym] 
        new_coords.append(f"{sym:<2} {atnum:<4} {x:<6} {y:<6} {z:<6}\n") #string formatting

print(str(len(new_coords)) + '\n\n')
for line in new_coords:
    print(line)

# Output:
# 5
# 
# 
# C  6.0  13.456 12.321 13.054
# 
# H  1.0  11.222 12.542 10.342
# 
# H  1.0  10.321 9.896  5.341
# 
# O  8.0  3.451  5.759  4.531
# 
# N  7.0  8.421  9.582  10.888
# 
```

This block defines a dictionary of atomic numbers for carbon, hydrogen, nitrogen
and oxygen, reads in the coordinates, finds the corresponding atomic number,
then adds the number into
the line and appends the new line to the `new_coords` list.

The code can be re-written using functions, defining a function using the `def`
keyword. Comments can be added to each function definition using triple quotes,
called a docstring:

```python

def read_file(file): 
    """
    Reads a file into Python, overlooking the first two lines. Returns a list
    of the file contents
    """
    
    with open(file, 'r') as f:
        contents = f.readlines()[2:]
    return contents

def get_atomic_number(symbol):
    """
    Returns the atomic number of a given chemical element
    """

    atnums = {}
    atnums['C'] = 6.0
    atnums['H'] = 1.0
    atnums['N'] = 7.0
    atnums['O'] = 8.0

    return atnums[symbol]    

def add_atomic_number(line):
    """
    Finds the atomic number of the atom passed as an argument and returns a
    formatted string including that atomic number
    """
    
    sym, x, y, z = line.split()
    atnum = get_atomic_number(sym) 
    return f"{sym:<2} {atnum:<4} {x:<6} {y:<6} {z:<6}\n"

def modify_coords(coords):
    """
    Modifies coordinates and returns a new list
    """

    new_coords = []
    for line in coords:
        line = add_atomic_number(line)
        new_coords.append(line)
    return new_coords

def print_coordinates(coordinates):
    """
    Prints out the coordinates in an xyz format
    """

    print(str(len(coords)) + '\n\n') 
    # the length of list is an integer that needs converting to a string before adding newlines
    for coord in coordinates:
        print(coord)

def main():

    coords = read_file('coords.xyz')
    new_coords = modify_coords(coords)
    print_file(new_coords)

main()

# Output:
# 5
# 
# C  6.0  13.456 12.321 13.054
# H  1.0  11.222 12.542 10.342
# H  1.0  10.321 9.896  5.341 
# O  8.0  3.451  5.759  4.531 
# N  7.0  8.421  9.582  10.888
```

In this example, the code using functions is longer than the procedural
version, but now we can re-use the code! The function `modify_coords` can be
used to modify 1000 xyz files in one go if we wanted to:

```python

lst = [file1, file2, file3...]

for file in lst:
    coords = read_file(lst)
    new_coords = modify_coords(coords)
    write_file(new_coords)
```

It's that easy!

# Python modules- using external code

In Python, the `import` keyword gives you access to code that sits outside of
the file that is being written. To include the math module that comes
pre-installed with Python, type `import math`:

```python
>>> import math
>>> math.pi
3.141592653589793
```

Atrributes of the math module are accessed through `math.attribute`. As shown
above, the value of $\pi$ can be obtained with `math.pi`. 

To give an alias to an imported package, use `import ... as ...`

```python
import matplotlib.pyplot as plt
```

This saves you from having to type out `matplotlib.pyplot` every time you use code
from that module.

Many useful modules and packages have been written by others, and can be
installed using the `pip` command from a shell prompt:

To install the NumPy package:
```bash
pip install numpy
```

This command will download the NumPy package from the Python Package Index,
PyPi, and install it in a location that Python can access by default. This
location can be found by typing

```python
>>> import site
>>> site.getsitepackages()
['/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
```

Using the pointers given above, you can definitely start writing some useful
programs! 
