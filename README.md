
Author: Luxi Meng   
Date: 10/24/2021
------------------

# Description
The program mimics a shopping website for Black Friday Sales. The website provides 
further discount for three classes of people,(military, senior, and student).
The program will offer 20% off for seniors 65+, 15% off for students with valid student ID 
and 10% for military service member with valid military ID. 

The website offers three products, Gerber, book or vitamin. Shoppers can purchase any one item for up to 
10 quantity per order. 

This program is helpful because it not only validates the user's identity according to their ID or birth year,
the shopping cart page in the end will also automatically recognize their discount category and calculates their total 
price after the discount of their category. The program further entices the shopper by showing htem how much they've 
saved on this order. 

The program not only automatically classify the shopper's discount rate, but also applies their discount in their 
shopping cart. It's closely relevant to our daily life since the pandemic, many people have been shopping online, and 
November is right around the corner, this could be used in the upcoming Black Friday sales. 

#instruction
There are a total of 4 files in this program. They are as follows:
-	OnlineShopDiscount.py (main program)
-	Person.py (imported class)
-	Product.py (imported class)
-	Product_input_file.text (input data)

To run the program, one should open the OnlineShopDiscount.py and run it. First the program will prompt the user to 
input their 5 digit student/military ID or birth year, the program if you entered incorrectly, it will keep asking until 
you enter it correctly. Note that this program only works for the people who is part of the three special category 
(valid student ID, military ID or senior who is born on or before 1955). 

Next the program will ask you to “login” with your name, and then provide you with a list of products for sale, 
each product is labeled with a number 1~3. Please pick a product to buy by entering the product number between 1 to 3. 
Then it will ask you to choose the quantity you want between 1-10. 

After entering all the user and product info, the website will show you your shopping cart, which will automatically 
recognize which discount category you will have and applied the discount to the products you put in the cart, 
and it will show you the final price after discount. 




#UML
![img.png](img.png)
"# OnlineShopDiscount" 
