
#a = 10
#b = 10
# if a>b:
#     print("a is greater")
# elif(b>a):
#     print("b is greater")
# else:
#     print("both are equal")
# i = 1
# for i in range(6):
#     print(i)

# i = 10
# while i<=20:
#     print(i)
#     i += 1
# a = 20
# txt = f"the value is {a}"
# print(txt)

# def myFuntion(name,age):
#     print("Hello wolrd " + name , age)

# myFuntion("welcome",18)

# def myFunction(food):
#     for i in food:
#         print(i , end=" ")

# fruites = ["Apple","Banana","Orange"]
# myFunction(fruites)

#def myNumber(num):
 #   return num * 5

#a = myNumber(5)
#print(a)

# class Main:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        

# p = Main("Mouli",24)
# # print(f"The name is {p.name} and the age is {p.age}")
# print(f"the name is {p.name} and the age is {p.age}")

# class MyInfo:
#     def __init__(self,name,age,work):
#         self.name = name
#         self.age = age
#         self.work = work

#     def __str__(self):
#         return f"My name is {self.name} \n My age is {self.age} \n My work is {self.work}"

# p = MyInfo("Mouli",23,"Trainer")
# print(p)
# print(p.name)

# class Basic:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def myMethod(self):
#         print("My name is " + self.name)
#     def myAge(self):
#         print(f"My age is  {self.age}")
# p = Basic("Mouli",23)
# p.myMethod()
# p.myAge()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!"

# # Create an object of class Dog
# dog = Dog("Buddy")
# print(dog.speak())  # Output: Buddy says woof!


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow!"

# animals = [Dog("Buddy"), Cat("Whiskers")]

# for animal in animals:
#     print(animal.speak())
# Output:
# Buddy says woof!
# Whiskers says meow!


# a = 5
# b = 5

# if a > b or a == b:
#     print(" a is greater or equal")
# elif b > a or b == a:
#     print("b is greater or equal")

# else:
#     print("the numbers are negative")

# i = 1
# while i<=10:
#     print(i)
#     i += 1

# i = 1
# for i in range(11):
#     print(i)

# fruites = ["apple","orange","banana"]
# for i in fruites:
#     print(i)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def study(self):
#         print(f"my name is {self.name} and age is {self.age}")
    
# myData = Student("ibrahim",29)
# myData.study()
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana" and "cherry":
#     break
#   print(x) 

# parties = ["dmk","admk","bjp"]
# for i in parties:
#     print(i)
#     if i == "tvk":
#         break
#     print(i)

# class Bank:
#     def __init__(self,account_numnber,balance):
#         self.account_number = account_numnber
#         self.balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount

# myCurr = Bank(63375,1000)

# print(f"My Account Number {myCurr.account_number} \n my balance is {myCurr.balance}")

# myCurr.deposit(500)
# print(f"Balance is {myCurr.balance}")

# myCurr.withdraw(600)
# print(f"balanace is {myCurr.balance}")

# class MyAccount:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount

# myCurr = MyAccount(1150063375,10000)

# print(f"Account_Number : {myCurr.account_number} \nBalanace : {myCurr.balance}")

# myCurr.deposit(1500)

# print(f"After deposit : {myCurr.balance}")

# myCurr.withdraw(1000)
# print(f"After the successfull withdrawel , balance is {myCurr.balance}")

# class MyAccount:
#     def __init__(self,acc_no,balance):
#         self.acc_no = acc_no
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self,balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             print("balance cannot be negative")


# myCurr = MyAccount(1150063375,5000)
# print(myCurr.acc_no)
# print(myCurr.get_balance())
# myCurr.deposit(5000)
# print(myCurr.get_balance())
# myCurr.withdraw(2000)
# print(myCurr.get_balance())
# myCurr.set_balance(-500)
#print(myCurr.get_balance())


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name : {self.name} Age : {self.age}")

# class Student(Person):
#     def __init__(self, name, age,id):
#         super().__init__(name, age)
#         self.id = id

#     def display(self):
#         super().display()
#         print(f"Id : {self.id}")

# a = Student("Mouli",23,284323)
# a.display()

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def display(self):
#         pass

# class Student(Person):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = 20

#     def display(self):
#         return f"Name : {self.name} , Age : {self.age}"

# b = Student("Mouli",24)
# print(b.display())

# my_list = [1, 2, 3]
# my_list.append(4)  # Output: [1, 2, 3, 4]
# my_list.insert(1, 5)  # Output: [1, 5, 2, 3, 4]
# print(my_list)
# my_list[1] = 6
# print(my_list)
# my_list.remove(6)
# print(my_list)
# my_list.pop()
# print(my_list)
# print(len(my_list))

# a = "Kasi pathi!"
# b = "EEE"
# age  = 20
# info = "I am currently wokring as one organization, and as well as student"
# #printing a string
# print("String is " + a)

# # string length
# print(len(a))

# # index value
# print("index value of string is " + a[2])

# #slice
# print("slice value of string is " + a[0:4])

# #Modify
# print("Modify string is " + a.replace("i" , "y"))

# #Concatenate
# print("Concatenated string is " + (a+" "+b))

# #format
# print(f"{a} is {b} student and the age is {age}")

# #Escape characters
# print(f"{a} is \"{b}\" student")

# #split
# print(info.split(","))

# class MyAccout:
#     def __init__(self,balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self,amount):
#         self.__balance += amount

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount

#     def set_balance(self,balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             print("balance cannot be negative")

# myCurrent = MyAccout(1000)
# print(myCurrent.get_balance())
# myCurrent.deposit(5000)
# print(myCurrent.get_balance())
# myCurrent.withdraw(1000)
# print(myCurrent.get_balance())
# myCurrent.set_balance(600)
# print(myCurrent.get_balance())

# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def display(self):
#         return self.name

# class Dog():
#     def __init__(self, breed):
#         self.breed = breed
        
#     def display(self):
#         return self.breed

# class Puppy(Dog,Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         Animal.__init__(self,breed)
        
#     def display(self):
#         return f"{self.name} is a {self.breed} breed "

# pup = Puppy("Buddy", "Lab")
# print(pup.display())

# my_module.py




