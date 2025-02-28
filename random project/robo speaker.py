# creating a robot speaker
#works in mac linux
import os

#oop using in this for working
if __name__== '__main__':
    print('welcome to the robot speaker 1.1 created by nikhil kaushik')
    while True:
        x=input('what do you want me to speak : ')
        if x=='q':
            os.system(f"say 'bye bye friend'")
            break
        command= f"say {x}"
        os.system(command)

# import win32com.client

# def speak(text):
#     speak = win32com.client.Dispatch("SAPI.SpVoice")
#     speak.Speak(text)

# speak("Hello, world!")

