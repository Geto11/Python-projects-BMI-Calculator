package store;
import java.util.Scanner;
import java.util.*;
import java.util.Arrays;


public class cafe {

	public void showfood() {
		String food[][] = {
				{"Burger", "$5"}, {"Hotdog", "$5"}, {"Taco", "$8"}, {"Pizza", "$15"}	
		};
		
		System.out.println(Arrays.deepToString(food));
	}
	
	public void showdrink() {
		String drink[][] = {
				{"Cola", "$5"}, {"ChocoMilk Shake", "$5"}, {"Blueberry Shake", "$5"}
		};
		
		System.out.println(Arrays.deepToString(drink));
	}
	
	public void mode() {
		String Md_payment [] = {"G-cash", "Paypal"};
		System.out.println(Arrays.toString(Md_payment));
	}

	public static void main(String[] args) {
		cafe menu = new cafe();
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter Start! : ");
		String a = input.nextLine();

		
		switch(a.toLowerCase()) {
		case "start":
			System.out.println("Welcome to (__Keith's Cafe__)\n");
			System.out.println("Hi!, What's your Name? \n");
			
			String Name = input.nextLine();
			String name = Name.substring(0,1).toUpperCase() + Name.substring(1);
			
			System.out.println("\nWelcome to our Cafe "+name+ ", would you like to order? (yes/no):\n");
			String select = input.nextLine();
			
			switch (select.toLowerCase()) {
			case "yes":
				System.out.println("\nHere's our Menu: \n");
				System.out.println("\n       (__________Food Menu__________)\n");
				menu.showfood();
				System.out.println("\n       (__________Drink Menu__________)\n");
				menu.showdrink();
				
				System.out.println("\n Enter your Order: \n");
				List<String> list = new ArrayList<String>();
				List<Integer> price = new ArrayList<Integer>();
				
				int sum =0;
				
				int i = 1;
				while(i < 100) {
					
					String order = input.nextLine().toLowerCase();
					
					switch (order) {
		
					case "burger":
						list.add("Burger");
						System.out.println("\n_____Burger is added to your Order List, cost of $5._____\n");
						price.add(5);
						System.out.println("\nEnter another Order: (enter quit to stop ordering!)\n");
						break;
					case "hotdog":
						list.add("Hotdog");
						System.out.println("\n_____Hotdog is added to your Order List, cost of $5._____\n");
						price.add(5);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "taco":
						list.add("Taco");
						System.out.println("\n_____Taco is added to your Order List, cost of $8._____\n");
						price.add(8);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "pizza":
						list.add("Pizza");
						System.out.println("\n_____Pizza is added to your Order List, cost of $15._____\n");
						price.add(15);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "cola":
						list.add("Cola");
						System.out.println("\n_____Cola is added to your Order List, cost of $5._____\n");
						price.add(5);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "chocomilk shake":
						list.add("ChocoMilk Shake");
						System.out.println("\n_____ChocoMilk Shake is added to your Order List cost of $5._____\n");
						price.add(5);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "blueberry shake" :
						list.add("Blueberry Shake");
						System.out.println("\n_____Blueberry Shake is added to your Order List, cost of $5._____\n");
						price.add(5);
						System.out.println("\n Enter another Order: (enter quit to stop ordering!)\n");
						break;
					case "quit":
						System.out.println("\n    Here is your Order List: " + list + "\n");
						System.out.println("\n    Price respectively in $:  " + price + "\n");
						for (int j = 0; j<price.size(); j++) {
							sum += price.get(j);
						}
						System.out.println("\n \n _____Total Cost of: $" + sum +"_____");
						System.out.println("\n \n _____Modes of Payment: _____\n");
						
						menu.mode();
						
						System.out.print("\nEnter Mode: ");
						String payment_mode = input.next().toLowerCase();
						
						switch (payment_mode) {
						case "g-cash":
							double peso = sum*56.14;
							System.out.println("\n ______Usd currency to Philippine peso is ₱56.14 ______\n");
							System.out.println("(___Your bill amount in Philippine peso: ₱" + peso+"___)");
							System.out.print("\n G-cash #: (+63-)");
							double number = input.nextDouble();
							
							if (number == number) {
								
								System.out.print("\nEnter 4-pin: ");
								int Pin = input.nextInt();
								if (Pin == Pin) {
									System.out.println("\nYou'll be redirected to your payment.........\n");
									System.out.print("Enter Amount of Cash: ");
									int cash = input.nextInt();
									
									if(cash >= peso) {
										double change = cash - peso;
										System.out.println("\n");
										System.out.println("\n __Here's your receipt "+name+ ":__ \n");
										System.out.println(
												"______Amount of Cash: ₱"+ cash +
												" _______Subtotal ₱" +peso+
												"______Change: ₱" + change );
										System.out.print("\n \n \n               (____Keith's Cafe____)");
										System.out.println("\n \n         ____Thank You for Checking Out!!____");
										System.out.println("\n             ____' Have a Good Day!! '____");
										break;
									}
								}
								else {
									System.out.println("Wrong Number!!");
									break;
								}
							}
							else {
								System.out.println("Wrong Number!!");
								break;
							}
							
							break;
						case "paypal":
							System.out.println("\nYou'll be redirected to your payment.........\n");
							System.out.print("Enter Amount of Cash: ");
							int cash1 = input.nextInt();
							
							if(cash1 >= sum) {
								int change = cash1 - sum;
								System.out.println("\n");
								System.out.println("\n __Here's your receipt "+name+ ":__ \n");
								System.out.println(
										"______Amount of Cash: $"+ cash1 +
										" _______Subtotal $" +sum+
										"______Change: $" + change );
								System.out.print("\n \n \n               (____Keith's Cafe____)");
								System.out.println("\n \n         ____Thank You for Checking Out!!____");
								System.out.println("\n             ____' Have a Good Day!! '____");
							break;
							
						}
						
						System.out.println("Enter Amount of Cash for Payment: ");
						break;
						
						default:
							System.out.println("\n _____Invalid Input!_____\n");
						}
						
					}
						
						
					
					i++;
				
				}				
				
				break;
			case "no":
				System.out.println("Thank You for checking our Cafe, feel free to come again!!");
				break;
			default:
				System.out.println("Invalid Input!!");
			}
			
			
			break;
		default:
			System.out.println("Invalid Input!!");
		}
			

	}
}
