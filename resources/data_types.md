# Data Types

Python characterized variables in its code by data types. They can be any of the following:

## Types

| type | name | code | example |
| - | - | - | - |
| text | [String](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#string) | ```str()``` | ```x = "Hello World"``` |
| numeric | [Integer](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#integer) | ```int()``` | ```x = 20``` |
| - | [Float](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#float) | ```float()``` | ```x = 20.5``` |
| - | [Complex](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#complex) | ```complex()``` | ```x = 1j``` |
| sequence | [List](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#list) | ```list()``` | ```x = ["apple", "banana", "cherry"]``` |
| - | [Tuple](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#tuple) | ```tuple()``` | ```x = ("apple", "banana", "cherry")``` |
| - | [Range](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#range) | ```range()``` | ```x = range(6)``` |
| mapping | [Dictionary](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#dictionary) | ```dict()``` | ```x = {"name" : "John", "age" : 36}``` |
| set | [Set](https://github.com/mvecchione145/python-quickstart/blob/main/resources/data_types.md#set) | ```set()``` | ```x = {"apple", "banana", "cherry"}``` |
| - | [Frozen Set]() | ```frozenset()``` | ```x = frozenset({"apple", "banana", "cherry"})``` |
| boolean | [Boolean]() | ```bool()``` | ```x = True``` |
| binary | [Bytes]() | ```bytes()``` | ```x = b"Hello"``` |
| - | [Byte Array]() | ```bytearray()``` | ```x = bytearray(5)``` |
| - | [Memory View]() | ```memoryview()``` | ```x = memoryview(bytes(5))``` |
| **custom** | [object]() | ```object()``` | ```x = object()``` |

### String

Strings are text that can be manipulated in the following ways:

```
x = "Hello World"

x + " from python!"
# "Hello World from python!"

x * 2
# "Hello WorldHello World"

x[0]
# "H"

x[0:4]
# "Hello"

x.split(" ")
# ["Hello", "World"]

len(x)
# 11

x.upper()
# "HELLO WORLD"

x.lower()
# "hello world"
```

### Integer

Integers are numbers that can be manipulated in the following ways:

```
x = 20

x + 10
# 30

x - 10
# 10

x * 2
# 40

x / 10
# 2

x ** 2
# 400

x > 10
# True

x <= 15
# False
```

### Float

### Complex

### List

### Tuple

### Range

### Dictionary

### Set

### Frozen Set