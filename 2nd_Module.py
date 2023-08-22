from bmi import person2

import sys, time, os
from termcolor import colored, cprint
text = colored('''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                     ๏⁌ BMI OF PERSON TWO ⁍๏                                                                                ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'green', attrs=['reverse', 'blink']) 
print(text)
def p2():
    if person2.formula() >= 29.5:
        print('''
             [______' YOU ARE OBESE' ______]''')
    elif person2.formula() >= 24.5:
        print('''
           [______' YOU ARE OVERWEIGHT' ______]''')
    elif person2.formula() < 18:
        print('''
           [______' YOU ARE UNDERWEIGHT' ______]''')
        
    else:
        print('''
            [______' YOU ARE NORMAL' ______]''') 

text = colored(f'''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                                                                                                                                                                                                                                                                                      [___Hello {person2.get_name()}, your BMI is {person2.formula()}.___]                                                                                                                                                                                       ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'white', attrs=['reverse', 'blink']) 
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)
print("____________________________________________________________") 
p2() 

print("____________________________________________________________")  
    
text = colored('''\n䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉                                                                                ____________________________________________________________\n''', 'green', attrs=['reverse', 'blink'])
print(text)      