import random as r
import numpy as np

lower='abcdefghijklmnopqrstuvwxyz'
upper=lower.upper()
n="0123456789"
special="*-+/!@#$%^&*()_=?<>,.[`~;:]{}"

#choosing the length of the password
length=int(input('length of the password: '))
h=int(input('how many passwords: '))
all=lower+upper+n+special
password=''
#using the loop for generating the password
for i in range(h):
    for j in range(length):
        password+=r.choice(all)
    print(i+1,':',password)
    password=''
    
