# Built-in String Functions

## len()

Return length of string

```
name = "sudo"
nameLength = len(name)
print(nameLength)


Output:
4
```

## substring

There is no function in python for substring. You can easily use it as below:

```
string[start:end:step]
```

```
name = "sudo power youtube"
print(name[0:4])

Output:
sudo
```

## find()

Return the position of string which you want to find.

```
name = "sudo power youtube"

print(name.find("p"))
print(name.find("power"))
print(name.find("u"))
print(name.find("a"))

Output:
5
5
1
-1
```


## index()

Return the position of string which you want to find. `find()` and `index()` both are same but difference is `index()` function returns exception/error when element is not found and `find()` returns `-1`

```
name = "sudo power youtube"

print(name.find("p"))
print(name.find("power"))
print(name.find("u"))

Output:
5
5
1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

## replace

replace given string with another given string

```
replace(old, new, count)
```

```
mySelf = "I love cricket. I play cricket everyday."
print(mySelf.replace("cricket", "football"))

Output:
I love football. I play football everyday.
```

## Reverse String

There is not really a direct function for reverse string but there are many other ways. You can use substring logic like below:

```
name = "sudo"
print(name[::-1])

Output:
odus
```

## Casing

```
name = "Sudo Power"

print(name.upper()) # SUDO POWER, convert into upper case
print(name.casefold()) # sudo power, convert into lower case
print(name.swapcase()) # sUDO pOWER, convert upper to lower and lower to upper case
```

## More string functions and list

https://www.w3schools.com/python/python_ref_string.asp

