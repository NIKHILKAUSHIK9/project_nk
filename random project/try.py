import os 


def od(x):
    if (x & 1)==0:  #it is using the bitwise $ operator so if last digit of number is 0 it is false condition
        print('even')
    else:
        print('odd')
        
od(3)


