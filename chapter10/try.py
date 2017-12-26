#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


while True:
    reply = input("Enter text:")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print("Bad"*8)
    else:
        num = int(reply)
        if num < 20:
            print("low")
        else:
            print(num**2)
print("Bye")
