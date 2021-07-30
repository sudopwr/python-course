# Built-in Math Functions

Python provides built-in `math` module for mathematical operations.

You can use it like below:

```
import math

number = math.pow(2, 3)
```

## math.pow()

Returns the value of x to the power of y. It is same as like Arithmetic operator exponentiation `**`.

```
import math

number = math.pow(2, 3)
print(number)

Output:
8
```

It is same as
```
2*2*2 = 8
2 ** 3 = 8
```

## round()

Rounds a numbers

```
round(2.55) # 3 
round(2.45) # 2
round(2.75) # 3
```

## math.floor()

Rounds a number **down** to the nearest integer

```
import math

math.floor(2.55) # 2
math.floor(2.45) # 2
math.floor(2.75) # 2
```

## math.ceil()

Rounds a number **up** to the nearest integer

```
import math

math.ceil(2.55) # 3
math.ceil(2.45) # 3
math.ceil(2.75) # 3
```

## More functions and List

https://www.w3schools.com/python/module_math.asp