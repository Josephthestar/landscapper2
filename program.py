# this will not be executed
# print("hello!")

# a = "hello"
# print(a) ##print the value of the variable 'a'

# a = str(1)
# print(a)
# b = int("5")
# print (b)
# c = float(4)
# print(c)
# d = int(5.7)
# print(d)

# a = 1
# b = a+1
# print(b)
# c = b * 3
# print(c)
# d = c - 1
# print(d)
# e = d / 2
# print(e)
# f = d ** 2
# print(f)
# a = "first string"
# b = "second string"
# c = a + " " + b
# print(c)

# a = [1, 5, "some string", True, 5.6]
# print(a[1])

# a = [
#     [1, 2, 3], #first row 
#     [4, 5, 6], #second row
#     [7, 8, 9], #third row
#     [10] #fourth row
# ]


# a = [
#     {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
#     },
#     [4, 5, 6],
#     [7, 8, 9],
#     [10]
# ]
# print(a)
 
# b = {
#   "firstGrade": ["Bobby", "Kyle", "Suzy"],
#   "secondGrade": ["Jennifer", "Jasmine", "Javier"],
#   "thirdGrade": "Nobody, they all failed last year!"
# }
# print(b)

# a = 9
# if a < 10:
#     print("a is less than 10")
# elif a == 10:
#     print("a is 10")
# else:
#     print("a is greater than 10")

# a = 'oh hai!'
# if a == 'oh hai!':
#     print('this works')

# a = 1
# b = 2
# if a == 1 and b == 2:
#   print('y') # will print only when both a==1 AND b==2
# else:
#   print('n') # will print if either condition is false

# if a == 0 and b == 2:
#   print('y') # will print only when both a==1 AND b==2
# else:
#   print('n') # will print if either condition is false

# a = 2
# b = 2
# if a == 1 or b == 2:
#   print('y') # will print when either a==1 OR b==2
# else:
#   print('n') # will print if both conditions are false

# if a == 1 or b == 1:
#   print('y') # will print when either a==1 OR b==2
# else:
#   print('n') # will print if both conditions are false




# user_input = input("Please enter your name: ")
# print("Hello, " + user_input + "!")

# Repeatedly perform a set of commands
# we have to be very specific,if we have something not a string we have to manually convert it . 

# a = 10
# while a < 20:
#     print("The value of a is currently: " + str(a))
# a += 1 
# print('end of loop joe')
# a += 1 like this it will make an infinite loop 
# print('end of loop joe')

# foods = ['hot dogs', 'beer', 'bald eagles']
# for food in foods:
#     print(food)

# for loop
# for x in range(0, 3):
#   print(x)

# def greet(name):
#   print('hi, ' + name)

# greet('joe')

# def add(value1, value2):
#   return value1 + value2

# print(add(1,3))

# Create a class for an object
# You can use a class or blueprint for objects that you’ll use

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name + ". My age is " + str(self.age))

# me = Person("yugi muto", 200)
# me.greet()
# sally = Person("seito kaiba", 25)
# sally.greet()



# Have a class inherit from another
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is " + self.name + ". My age is " + str(self.age))

#     def work(self):
#         print("Boring...")

# class SuperHero(Person): # tell it to inherit from Person
#     def __init__(self, name, age, powers):
#         super().__init__(name,age) # call Person's __init__()
#         self.powers = powers

#     def greet(self):
#         super().greet() # call Person's greet()
#         self.listPowers()

#     def listPowers(self):
#         for power in self.powers:
#             print(power)

#     def work(self): # override Person's work()
#         print("To action!")

# superman = SuperHero('Clark Kent', 200, ['flight', 'strength', 'invulnerability'])

# superman.greet()
# superman.work()

# Create a factory for objects
# class Car:
#     def __init__(self, maker, model, serial):
#         self.maker = maker
#         self.model = model
#         self.serial = serial

# class CarFactory:
#     def __init__(self, name):
#         self.name = name
#         self.cars = []

#     def makeCar(self, model):
#         self.cars.append(Car(self.name, model, len(self.cars)))

#     def listCars(self):
#         for car in self.cars:
#             print(car.maker + " " + car.model + " serial#: " + str(car.serial))

#     def findCar(self, serial):
#         for car in self.cars:
#             if(car.serial == serial):
#                 return car

# toyota = CarFactory('Toyota')
# toyota.makeCar('Prius')
# toyota.makeCar('Rav 4')
# toyota.listCars()
# print(toyota.findCar(1).model)



# the function converting from java into python
# get name 

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# now converting into python 
# def is a define a function ! remember
# invoke a function,remember 

# def get_name():
#     name = input("What is your name? ")
#     return name

# # Call the get_name() function
# result = get_name()

# # Print the result
# print("Your name is:", result)




# import random

# def play_hangman():
#     words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grapefruit", "honeydew", "imbe", "jackfruit"]
#     word = random.choice(words)
#     guessed_letters = []
#     attempts = 6

#     print("Welcome to Hangman!")
#     print("Guess the letters to reveal the word.")
#     print("You have", attempts, "attempts.")

#     while True:
#         print("\n")
#         display_word(word, guessed_letters)
#         print("\n")

#         if is_word_guessed(word, guessed_letters):
#             print("Congratulations! You guessed the word correctly.")
#             if play_again():
#                 play_hangman()
#             else:
#                 break

#         if attempts == 0:
#             print("Game over! You ran out of attempts.")
#             print("The word was:", word)
#             if play_again():
#                 play_hangman()
#             else:
#                 break

#         guess = input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess not in word:
#             attempts -= 1
#             print("Incorrect guess! Attempts remaining:", attempts)

# def display_word(word, guessed_letters):
#     for letter in word:
#         if letter in guessed_letters:
#             print(letter, end=" ")
#         else:
#             print("_", end=" ")

# def is_word_guessed(word, guessed_letters):
#     for letter in word:
#         if letter not in guessed_letters:
#             return False
#     return True

# def play_again():
#     choice = input("Would you like to play again? (yes/no): ").lower()
#     return choice == "yes"

# # Start the game
# play_hangman()




