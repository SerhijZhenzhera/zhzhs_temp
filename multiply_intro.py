'''
Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers
'''


def mult_two(a: int, b: int) -> int:
    if type(a) is int and type(b) is int:
        return a*b
    else:
        ValueError


'''
[https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions]
-----[MaxiMouse]
In the following code:

def f(x) -> int:
    return int(x)

the -> int just tells that f() returns an integer (but it doesn't force the function to return an integer).
It is called a return annotation, and can be accessed as f.__annotations__['return'].
Python also supports parameter annotations:

def f(x: float) -> int:
    return int(x)

: float tells people who read the program (and some third-party libraries/programs, e. g. pylint) that x should be a float.
It is accessed as f.__annotations__['x'], and doesn't have any meaning by itself...


-----[Dimitris Fasarakis Hilliard]
...the -> symbol is used as part of function annotations.
In more recent versions of Python >= 3.5, though, it has a defined meaning... 
'''
