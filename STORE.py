import sys,time,os
app_name = ("🆂🅷🅰🅿🅴🆂 🅰🆁🅴🅰 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁 ")
import sys,time,os
import sys
from termcolor import colored, cprint
text = colored('''\n                                       ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉ _WELCOME TO_ ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉
                         ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉๏⁌  "• ꤥ꤭ KEITH'S CAFE ꤥ꤭ •"  ⁍๏䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉\n''', 'yellow', attrs=['reverse', 'blink'])
print(text)


welcome2 = ("\n|•___________________|• WELCOME USER •|___________________•|\n")
for char in welcome2:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
Enter = input("ENTER |• START •|: ").upper()
print("\n|• ______________________________________________________ •|")
if Enter == "START":

    my_cafe = ("• ꤥ꤭ KEITH'ꤔ Cafꤕ꤬ ꤥ꤭ •")

    print(f'''                      •|  WELCOME  |•
                            _to_
   •ꤥꤥ꤭ꤥ________|• {my_cafe} •| ________ꤥꤥ꤭ꤥ•
 |•ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ_ꤥ•|
|•_______________________________________________________•|''')
    Name = input("\nEnter your Name: ").title()

    welcome4 = (f'''____________________________________________________________\n
      WELCOME TO {my_cafe}, {Name}. 
      
      |•  __MAY YOUR WANTS WILL BE SATISFIED.__√ •|
|•________________________________________________________•|''')
    for char in welcome4:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(0.01)

    print("\n     |•________ DO YOU WANT TO ORDER ?________•| ")
    print("\n     |•Enter | MENU | if you want to order.")
    print("     |•Enter | QUIT | if you don't want to.")

    my_selection = input("\nEnter your Choice: ").upper()
    if my_selection == "MENU":
        print("\n")

        order_basket = []
        price = []

        sum = 0

        print("\n")
        print("\n ꤥ꤭|•________________________________________________•|ꤥ꤭")
        print(''' |• HERE ARE THE AVAILABLE FOODS & DRINKS IN OUR MENU •|
        ____________________________________''')

        print('''\n  |• PLACE YOUR ORDER ACCORDING TO THE SELECTION BELOW. •|''')

        welcomeZ = ('''\n ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉__GUIDE FOR SELECTION!!__䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉
|•_________________|•_MENU SELECTION_•|_________________•|

             ꤥ꤭______|•ꤥ FOOD-ꤠꤕꤡꤝ √______ꤥ꤭
               
          ꤥ꤭ |• A. Chocolate Cake_____Php 140.00•| √
          ꤥ꤭ |• B. Vanilla Cake_______Php 140.00•| √
          ꤥ꤭ |• C. Strawberry Muffins_Php 120.00•| √
          ꤥ꤭ |• D. Blueberry Muffins___Php 120.00•| √
            
            ꤥ꤭______|•ꤥ Drink-ꤠꤕꤡꤝ √______ꤥ꤭
              
          ꤥ꤭ |• X. Chocofudge_____Php 50.00•| √
          ꤥ꤭ |• Y. Black Coffee_____Php 30.00•| √
          ꤥ꤭ |• Z. Brown Coffee____Php 30.00•| √
|•______________________________________________________•|''')
        for char in welcomeZ:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

        welcome3 = (f'''\n\n
________________________________________________________________________________________________________________________
|• NOTE: Enter the letter that correspond to the Food or Drink of your choice!!

|• NOTE: IF YOUR ORDER IS NOT INCLUDED IN THE MENU-SELECTION ABOVE, THAT WON'T BE PROCESSED. (INVALID INPUT !).
________________________________________________________________________________________________________________________\n\n''')
        for char in welcome3:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)


        while True:
            Order = input("\nPLEASE ENTER YOUR ORDER. ENTER |• QUIT •| TO STOP ORDERING.  : \n").upper()
            if Order == "A":
                bhb = ("\nChocolate Cake (Php 140.00)  is added to your Order List.\n")
                for char in bhb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                order_basket.append("Chocolate Cake")
                price.append(140)


            elif Order == "B":
             brb = ("\nVanilla Cake (Php 140.00) is added to your Order List.\n")
             for char in brb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Vanilla Cake")
             price.append(140)


            elif Order == "C":
             bnb = ("\nStrawberry Muffins (Php 120.00) is added to your Order List.\n")
             for char in bnb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Strawberry Muffins")
             price.append(120)


            elif Order == "D":
             bmb = ("\nBlueberry Muffins (Php 120.00) is added to your Order List.\n")
             for char in bmb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Blueberry Muffins")
             price.append(120)


            elif Order == "X":
             bkb = ("\nChocofudge (Php 50.00) is added to your Order List.\n")
             for char in bkb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Chocofudge")
             price.append(50)


            elif Order == "Y":
             bqb = ("\nBlack Coffee (Php 30.00) is added to your Order List.\n")
             for char in bqb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Black Coffee")
             price.append(30)


            elif Order == "Z":
             bxb = ("\nBrown Coffee (Php 30.00) is added to your Order List.\n")
             for char in bxb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

             order_basket.append("Brown Coffee")
             price.append(30)


            elif Order == "QUIT":
                break

            else:
             bb = ("\n______SORRY, INVALID INPUT !!______\n\n")
             for char in bb:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)


        print("\n|•HERE ARE THE FOODS YOU'VE ENTERED: ")
        for i in order_basket:
            print(i)

        print(f"HERE ARE THE PRICES:  {price} RESPECTIVELY. ")

        print("\n IS THERE ANY ITEM YOU WISH TO REMOVE?")
        Remove_choice = input("\nYES OR NO: ").upper()
        if Remove_choice == "YES":
            print('''             ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉__GUIDE FOR SELECTION!!__䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉
                         ꤥ꤭______|•ꤥ FOOD-ꤠꤕꤡꤝ √______ꤥ꤭
               
          ꤥ꤭ |• Enter A to remove Chocolate Cake in your Order List !     | √
          ꤥ꤭ |• Enter B to remove Vanilla Cake in your Order List !       | √
          ꤥ꤭ |• Enter C to remove Strawberry Muffins in your Order List ! | √
          ꤥ꤭ |• Enter D to remove Blueberry Muffins in your Order List !  | √
            
            ꤥ꤭______|•ꤥ Drink-ꤠꤕꤡꤝ √______ꤥ꤭
              
          ꤥ꤭ |• Enter X to remove Chocofudge in your Order List !   | √
          ꤥ꤭ |• Enter Y to remove Black Coffee in your Order List ! | √
          ꤥ꤭ |• Enter Z to remove Brown Coffee in your Order List ! | √''')

            while True:
                remove_choice = input("\nPLEASE ENTER YOUR CHOICE. (Enter |• QUIT •| To Stop.): ").upper()
                if remove_choice == "A":
                    order_basket.remove("Chocolate Cake")
                    price.remove(140)
                    print("\nChocolate Cake has been removed.\n")

                elif remove_choice == "B":
                    order_basket.remove("Vanilla Cake")
                    price.remove(140)
                    print("\nVanilla Cake has been removed.\n")

                elif remove_choice == "C":
                    order_basket.remove("Strawberry Muffins")
                    price.remove(120)
                    print("\nStrawberry Muffins has been removed.\n")

                elif remove_choice == "D":
                    order_basket.remove("Blueberry Muffins")
                    price.remove(120)
                    print("\nBlueberry Muffins has been removed.\n")

                elif remove_choice == "X":
                    order_basket.remove("Chocofudge")
                    price.remove(50)
                    print("\nChocofudge has been removed.\n")

                elif remove_choice == "Y":
                    order_basket.remove("Black Coffee")
                    price.remove(30)
                    print("\nBlack Coffee has been removed.\n")

                elif remove_choice == "Z":
                        order_basket.remove("Brown Coffee")
                        price.remove(30)
                        print("\nBrown Coffee has been removed.\n")
                elif remove_choice == "QUIT":
                    print("\n")
                    break
                else:
                        bRb = ('''\t|•CANNOT PROCESS YOUR REQUEST.•|
   • lT MUST BE THAT YOUR ORDER DOESN'T EXIST.\n''')
                        for char in bRb:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)

        for value in price:
            sum = sum + value
        print(f"\nHERE'S YOUR UPDATED ORDER LIST: {order_basket}")
        print(f"COST OF: {price} RESPECTIVELY.      SUBTOTAL: |• {sum} •|")

        Amount = int(input("Please Enter Amount of Cash: "))
        if Amount < sum:
            print("NOT ENOUGH CASH !!")
        else:
            Change = Amount - sum
            jhj = ("\nꤥ꤭ |• CHECKING OUT YOUR PURCHASE, PLEASE STAND BY ! •|ꤥ꤭")
            for char in jhj:
                 sys.stdout.write(char)
                 sys.stdout.flush()
                 time.sleep(0.01)
            hkh = ("\n.................................\n")
            for char in hkh:
                 sys.stdout.write(char)
                 sys.stdout.flush()
                 time.sleep(0.2)

            welcomeB = (f'''\nOKAY  HERE'S YOUR RECEIPT {Name}:
                     |• CASH: Php {Amount}.00
                     |• SUBTOTAL: Php {sum}.00
                     |• CHANGE: Php {Change}.00
                     
   ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉ Thank You for Ordering ䷉䷉䷉䷉䷉䷉䷉䷉䷉䷉
   
   |• ꤥ꤭ "Dꤥꤡτ Hꤌ꤂ꤕ ꤌ G꤀꤀d Dꤌꤟ, Hꤌ꤂ꤕ ꤌ Grꤕꤌτ Dꤌꤟ!!" ꤥ꤭ •|''')
            for char in welcomeB:
             sys.stdout.write(char)
             sys.stdout.flush()
             time.sleep(0.01)


    elif my_selection == "QUIT":
        welcomeA = (f'''\nTHANK YOU FOR CHECKING {my_cafe}. 
FEEL FREE TO COME AGAIN {Name}. 
 

 |• ꤥ꤭ " Dꤥꤡτ Hꤌ꤂ꤕ ꤌ G꤀꤀d Dꤌꤟ, Hꤌ꤂ꤕ ꤌ Grꤕꤌτ Dꤌꤟ! " ꤥ꤭ •|''')
        for char in welcomeA:
             sys.stdout.write(char)
             sys.stdout.flush()
             time.sleep(0.01)
    else:
        welcomeK = ("CANNOT PROCESS YOUR REQUEST. |• INVALID INPUT !! •|")
        for char in welcomeK:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.01)
        #break
else:
    welcome43 = ("|• SORRY, INVALID INPUT !!! •|")
    for char in welcome43:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(0.01)

       