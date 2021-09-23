from Product import *


class Person:
    def __init__(self, name):
        """
        Constructor for base class Person's name
        """
        # Person class has an attribute called name
        self.name = name

    def apply_discount(self, product):
        """
         user-defined method will be overriden later, leave as-is
        :param product:Product object
        """
        pass

    def get_total_payment(self, product, amount):
        """
        user-defined method will be overriden later
        """
        pass

    def __uppercase_name(self, name):
        '''
        user-defined Private Method
        :param name: user input name
        :return: Capitalize all letters in the name
        '''
        return name.upper()


class Military(Person):
    '''
    Military is a subclass of Person class
    '''
    # static variable defines military discount as 10% off
    discount = 0.1

    def __init__(self, name, military_id):
        '''
        constructor for Military class
        :param name:
        :param military_id:
        '''
        # instance variables will define military id and name
        self.military_id = military_id
        self.name = name

    def __str__(self):
        return f'I am a military service member. My name is {self.name}, my military ID is {self.military_id}'

    def apply_discount(self, product):
        '''
        user-defined method overrode parent class method
        :param product:
        :return:
        '''
        # to calculate price after discount
        price_after_discount = float(product.price) * (1 - self.discount)
        return price_after_discount

    def get_total_payment(self, product, amount):
        total_payment = self.apply_discount(product) * int(amount)
        return total_payment


class Senior(Person):
    # static attribute defines that senior gets 20% off
    discount = 0.2

    def __init__(self, name, birth_year):
        '''
        constructed a constructor for senior class
        :param name: this is the name of the senior shopper
        :param birth_year: this will be the date of birth of a senior shopper
        '''
        # one can't legally change their birth year, so making this a private attribute
        self.__birth_year = birth_year
        self.name = name
        self.age = 2020 - self.__birth_year

    def __repr__(self):
        '''
        method overriding the father class's built-in __repr__ method
        '''
        #make a user friendly
        return f'I am a senior. My name is {self.name}, my date of birth is {self.__birth_year}'

    def apply_discount(self, product):
        price_after_discount = float(product.price) * (1 - self.discount)
        return price_after_discount

    def get_total_payment(self, product, amount):
        total_payment = self.apply_discount(product) * int(amount)
        return total_payment

    def __ge__(self, other):
        '''
        implement a magic method
        :param other:
        :return:
        '''
        return True if self.age >= other.age else False


class Student(Person):
    discount = 0.15

    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f'I am a student. My name is {self.name}, my student ID is {self.student_id}'

    def apply_discount(self, product):
        price_after_discount = float(product.price) * (1 - self.discount)
        return price_after_discount

    def get_total_payment(self, product, amount):
        total_payment = self.apply_discount(product) * int(amount)
        return total_payment


# unit test
if __name__ == '__main__':
    person1 = Person("peter")
    assert (person1.name == "peter"), "Person.name test fail"
    print("Person class test pass")

    military1 = Military("john", 31234)
    assert (military1.name == "john"), "Military.name test fail"
    assert (military1.military_id == 31234), "Military.military_id test fail"
    print("Military class test pass")

    # test magic method __ge__
    senior1 = Senior("Bob", 1954)
    senior2 = Senior("Roy", 1949)
    assert (senior2.__ge__(senior1)), "Senior age comparison test fail"
    print("Senior age comparison test pass")

    # test discount application method
    student1 = Student("Lilian", 24367)
    book = Product("book", 3.5)
    assert student1.apply_discount(book) == 2.975, "Student discount application test fail"
    print("Student discount applied test pass")

    # test the get_total_payment method
    total_payment = military1.get_total_payment(book, 10)
    assert total_payment == 31.5, "Military total payment test fail"
    print("Military total payment test pass")
