# pure [![PyPI version](https://badge.fury.io/py/pure.svg)](https://badge.fury.io/py/pure) 
_Decorator for pure functions_

| Branch  | Build  | Coverage |
| ------- | ------ | -------- |
| master  | [![Build Status master]](https://travis-ci.org/Enteee/pure) | [![Coverage Status master]](https://coveralls.io/github/Enteee/pure?branch=master) |
| develop  | [![Build Status develop]](https://travis-ci.org/Enteee/pure) | [![Coverage Status develop]](https://coveralls.io/github/Enteee/pure?branch=develop) |

## Prerequisites
* [python]:
  - 3.4
  - 3.5
  - 3.5-dev
  - nightly
* [pip](https://pypi.python.org/pypi/pip)

## Installation
```shell
    $ sudo pip install pure
```

## Usage
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

[python]: https://www.python.org/

[Build Status master]: https://travis-ci.org/Enteee/pure.svg?branch=master
[Coverage Status master]: https://coveralls.io/repos/github/Enteee/pure/badge.svg?branch=master
[Build Status develop]: https://travis-ci.org/Enteee/pure.svg?branch=develop
[Coverage Status develop]: https://coveralls.io/repos/github/Enteee/pure/badge.svg?branch=develop
