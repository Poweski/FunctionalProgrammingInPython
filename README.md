### Introduction
The project was created as part of studying the idea of ​​scripting languages ​​in college and aims to familiarize oneself with basic functional programming techniques and advanced mechanisms in Python. The project implemented various functions that used such approaches as higher-order functions, generators, decorators, and memoization. The goal was to understand and practically apply functional programming elements such as manipulating iterable objects, creating iterators, handling recursive functions, and managing logging, which was a key element in exploring the possibilities of scripting languages.

### Python Functions
The task implements functions using functional programming that solve various problems, such as generating acronyms from a list of words, calculating the median of numbers without using external modules, calculating the square root using Newton's method, creating a dictionary with letters and their corresponding words, and flattening nested lists. All functions are developed in a way that follows the principles of functional programming, avoiding the use of imperative statements such as for, while, or if.

### Higher-order functions
Higher-order functions have also been implemented, which take a predicate and an iterable object, checking various conditions. These functions allow for flexible manipulation of data, verifying conditions such as: whether all elements satisfy the predicate, whether at least one element satisfies the predicate, whether at least n elements satisfy the predicate, and whether at most n elements satisfy the predicate. Thanks to these functions, it is possible to create more complex operations on data sets.

### PasswordGenerator - Iterator Class
The next task was to create a PasswordGenerator class, which acts as an iterator generating random passwords. This class has __init__, __iter__ and __next__ methods, allowing you to configure the password length, the set of characters for generating passwords and the maximum number of generated passwords. The iterator allows you to conveniently generate passwords on demand, while strictly controlling the number of generated passwords.

### Generator with closures
Additionally, a make_generator function was created that takes a function as an argument and returns a generator. This generator lazily calculates the function values ​​for subsequent arguments, which allows for efficient memory management and computing large data sets. The function was tested on various numerical sequences, such as the Fibonacci sequence, the Catalan sequence, arithmetic, geometric and power sequences.

### Generator memoization
The make_generator_mem function has also been implemented, which works similarly to make_generator, but additionally uses memoization, which prevents multiple calculations of results for the same arguments. Memoization significantly improves computation efficiency, especially in cases of recursive computations, by storing previously calculated results and reusing them.

### Log Decorator
Finally, we created a log decorator that logs the details of a function call or class instantiation. This decorator logs data such as the call time, duration, function name, arguments, and the returned value. It also allows you to set the logging level using the logging module, which allows you to more closely track the application's activity and monitor its performance.
