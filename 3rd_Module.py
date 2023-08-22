from bmi import person3

import sys, time, os
from termcolor import colored, cprint

text = colored('''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                   ๏⁌ BMI OF PERSON THREE ⁍๏                                                                                ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'green', attrs=['reverse', 'blink']) 
print(text)

def p3():
    if person3.formula() >= 29.5:
        print('''
             [______' YOU ARE OBESE' ______]''')
    elif person3.formula() >= 24.5:
        print('''
           [______' YOU ARE OVERWEIGHT' ______]''')
    elif person3.formula() < 18:
        print('''
           [______' YOU ARE UNDERWEIGHT' ______]''')
        
    else:
        print('''
           [______' YOU ARE NORMAL' ______]''') 

text = colored(f'''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                                                                                                                                                                                                                                                                                     [___Hello {person3.get_name()}, your BMI is {person3.formula()}.___]                                                                                                                                                                                        ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'white', attrs=['reverse', 'blink']) 
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)
print("____________________________________________________________")       
p3()
print("____________________________________________________________")     
text = colored('''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                                ____________________________________________________________\n''', 'green', attrs=['reverse', 'blink'])
print(text)    