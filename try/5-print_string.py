#!/usr/bin/python3
str = "Holberton School"
print(f"{str}"*3, f"\n{str[:10]}")
# but also possible to use like:
# print(("%s " * 3) % (str, str, str), "\n%s" % str[:10])
