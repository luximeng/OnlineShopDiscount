'''
Luxi Meng
Date:10/21/2020
Description Project:
Write a program to calculate different discount rate for different group of
 people during Black Friday sales on a shopping Website. For example,
 senior(65+) discount 20%, student discount 15%, military discount 10%.
 student ID always between 20000-29999. Military ID is between 30000-39999
 '''
from Person import *
from Product import *

# global variables
eligible_birth_year = 1955
product_list = []

def load_product_input_file():
    '''
    this function will read the data input text file in the same folder
    '''
    data_source = "product_input_file.txt"
    file = open(data_source, "r")#open txt,read only
    line_read = file.readline().rstrip()#remove the EOL space
    while line_read != '':
        # split the next line and get to a list
        current_product_info = line_read.split(" ")
        # put instances of the Product class into the product_list
        product = Product(current_product_info[0], current_product_info[1])
        product_list.append(product)
        line_read = file.readline().rstrip()#read next line
    file.close()

def identity_classify(id_input):
    '''
    classify what kind of shopper identity according to their ID or birth year
     input
    '''
    id_input= int(id_input)
    identity = ""
    #military ID is pre-determined to be between 30000 and 39999
    if isinstance(id_input, int) and 30000 <= id_input <= 39999:
        identity = "military"
    elif (isinstance(id_input, int) and 20000 <= id_input <= 29999):
        identity = "student"
    #eligible birth year is a global variable defined to be 1955
    elif (isinstance(id_input, int) and id_input <= eligible_birth_year):
        identity = "senior"
    return identity

def generate_catalog(product_list):
    '''
    created a function that will convert the product list into a set of tuples
    '''
    #make a set of tuple of product and its price
    catalog_set = set()
    for item in product_list:
        product_tuple = (item.product_name, item.price)
        catalog_set.add(product_tuple)
    return catalog_set



if __name__ == "__main__":
    #Print welcome message for shoppers
    print("Shop right now on our BLACK FRIDAY SALES! "
          "you might qualify for more discount!\n")

    #while loop will prevent the user input something out of range,
    #program will ask again until input is correct
    while True:
        # prompt user for either student/military ID/date of birth
        id_input = input('If you are a student, please enter your '
                         'student ID number between 20000-29999 without comma. \n'
                         'If you are a service member, please enter your military '
                         'ID between 30000-39999 without comma.\n'
                         f'If you are a senior (born on or '
                         f'before {eligible_birth_year}), '
                         f'please enter your birth year in the format of YYYY:\n')
        #try block will make sure user inputed number only
        try:
            id_input = int(id_input)
        except ValueError as e:
            print("Input  Error. Please enter number only.")
            continue
        if 20000 <= id_input < 40000 or 0 < id_input <= eligible_birth_year:
            break
        else:
            print('Please follow the instruction: ')

    #classify what kind of shopper identity according to their ID
    # or birth year input
    identity = identity_classify(id_input)

    #prompt shopper to enter their name
    shopper_name=input("Please login with your name:\n")

    #creat instance of various person based on their identity
    if identity == "military":
        person1 = Military(shopper_name,id_input)
    elif identity == "student":
        person1 = Student(shopper_name,id_input)
    elif identity == "senior":
        person1 = Senior(shopper_name,id_input)

    #call the txt file loading function
    load_product_input_file()
    #created a product catalog based on product list, this is a set of tuple
    catalog = generate_catalog(product_list)

    print("We have following products:")
    # iterate through the product list and print each product and price for
    # the shopper
    for i in range(len(product_list)):
        print(i+1, product_list[i])
    # ask user to enter item number
    choose_item_index = input(f'Which product would you like to order, '
                      f'please enter item number between 1~{len(product_list)}:')
    # associate item number with the item from the product list
    choose_item = product_list[int(choose_item_index) - 1]

    quantity = input("How many would you like to purchase,enter between 1-10:")
    total_payment = person1.get_total_payment(choose_item, int(quantity))
    # final shopping cart tells shopper their total price after discount and
    # how much they saved
    print("-------------------------Shopping Cart----------------------------")
    print(f'For you are a {identity}, we provide a '
          f'{person1.discount*100:.2f}% off discount')
    print(choose_item)
    print(f'With {identity} discount, the price is '
          f'${person1.apply_discount(choose_item):.2f}')
    print(f'You order {quantity} {choose_item.product_name}')
    print(f'The total payment of your order is: ${total_payment:.2f}')
    print(f'You saved ${total_payment/(1-person1.discount)*person1.discount:.2f}')


