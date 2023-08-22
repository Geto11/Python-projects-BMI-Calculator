from bmi import person1

import sys, time, os
from termcolor import colored, cprint
text = colored('''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                    ๏⁌ BMI OF PERSON ONE ⁍๏                                                                                 ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'green', attrs=['reverse', 'blink']) 
print(text)

def p1():
    if person1.formula() >= 29.5:
        print('''
             [______' YOU ARE OBESE' ______]''')
    elif person1.formula() >= 24.5:
        print('''
           [______' YOU ARE OVERWEIGHT' ______]''')
    elif person1.formula() < 18:
        print('''
           [______' YOU ARE UNDERWEIGHT' ______]''')
        
    else:
        print('''
            [______' YOU ARE NORMAL' ______]''')  

text = colored(f'''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                                                                                                                                                                                                                                                                                    [___Hello {person1.get_name()}, your BMI is {person1.formula()}.___]                                                                                                                                                                                       ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'white', attrs=['reverse', 'blink']) 
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)
print("____________________________________________________________") 
p1()    
print("____________________________________________________________")                   
text = colored(f'''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                               _____________________________________________________________\n''', 'green', attrs=['reverse', 'blink'])
print(text) 