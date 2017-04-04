# pure [![PyPI version](https://badge.fury.io/py/pure.svg)](https://badge.fury.io/py/pure) 
_Optimizing decorator for pure functions_

| Branch  | Build  | Coverage |
| ------- | ------ | -------- |
| master  | [![Build Status master]](https://travis-ci.org/Enteee/pure) | [![Coverage Status master]](https://coveralls.io/github/Enteee/pure?branch=master) |
| develop  | [![Build Status develop]](https://travis-ci.org/Enteee/pure) | [![Coverage Status develop]](https://coveralls.io/github/Enteee/pure?branch=develop) |

From wikipedia:
> In computer programming, a function may be considered a pure function if both of the following statements about the function hold:
> 1. The function always evaluates the same result value given the same argument value(s). The function result value cannot depend on any hidden information or state that may change while program execution proceeds or between different executions of the program, nor can it depend on any external input from I/O devices (usually—see below).
> 2. Evaluation of the result does not cause any semantically observable side effect or output, such as mutation of mutable objects or output to I/O devices (usually—see below).

<details>

<summary>## Prerequisites</summary>

* [python]:
  - 3.4
  - 3.5
  - 3.5-dev
  - nightly
* [pip](https://pypi.python.org/pypi/pip)
</details>

## Installation
```shell
    $ sudo pip install pure
```

## Usage

### Simple Usage
```python
In [1]: from pure import *

In [2]: @pure
   ...: def f(x):
   ...:     print('x: {}, x+1: {}'.format(x, x+1))
   ...:     return x+1
   ...: 

In [3]: f(1)
x: 1, x+1: 2
Out[3]: 2

In [4]: f(1)
Out[4]: 2
```

### Fibonacci Example

without @pure:



[python]: https://www.python.org/
[Build Status master]: https://travis-ci.org/Enteee/pure.svg?branch=master
[Coverage Status master]: https://coveralls.io/repos/github/Enteee/pure/badge.svg?branch=master
[Build Status develop]: https://travis-ci.org/Enteee/pure.svg?branch=develop
[Coverage Status develop]: https://coveralls.io/repos/github/Enteee/pure/badge.svg?branch=develop
