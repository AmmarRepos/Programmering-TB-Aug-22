#! python 3.10.4

from colorama import Fore, init
from datetime import datetime
import random


global console_color
console_color = None


def capture_user_input(user_message):
   try:
      user_input = input(user_message)
      return user_input
   except Exception as ex:
      print(ex)
      return capture_user_input(user_message)


def capture_user_input_int(user_message):
   try:
      user_input = input(user_message)
      return int(user_input)
   except Exception as ex:
      print(ex)
      print('Please enter value of type integer')
      return capture_user_input_int(user_message)


def capture_user_input_float(user_message):
   try:
      user_input = input(user_message)
      return float(user_input)
   except Exception as ex:
      print(ex)
      print('Please enter value of type float')
      return capture_user_input_float(user_message)


def fun_0():
   print("Thank you for using the program")
   quit()

   
def fun_1():
   print("Hello World")
   
      
def fun_2():
   mesgs = ('first name', 'last name', 'Age')
   user_info = [capture_user_input('Please enter your ' + mesg + ': ') for mesg in mesgs]
   print(' '.join(user_info))

   
# I did not find from where to read the console font color from the system environment
# so I declare it as a global vairable for the script.
def fun_3():
   init()
   global console_color
   if console_color == 'RED':
      print(Fore.RESET + 'console color has changed to default')
      console_color = 'RESET'
   else:
      print(Fore.RED + 'console color has changed to red')
      console_color = 'RED'

      
def fun_4():
   print(datetime.now())

   
def fun_5():
   num_1=  capture_user_input_float('Please Enter first number: ')
   num_2=  capture_user_input_float('Please Enter second number: ')
   desc = 'The largest number is: '
   print(desc, num_1) if num_1 > num_2 else print(desc, num_2)

def fun_6():
   guess_num = 0
   secret = random.randrange(1, 100, 1)
   try_again = 'y'
   while try_again == 'y':
      guess_num += 1
      ans = capture_user_input_int('Please enter a guess between [1, 100]: ')
      diff = secret - ans
      if diff == 0:
         print('Correct')
         break
      elif diff > 0:
         print('Your guess is smaller than the sercet by about: ', random.randrange(1,diff+1,1))
      else:
         print('Your guess is larger than the sercet by about: ', random.randrange(1,abs(diff)+1,1))
      try_again = input('Do you want to try again? (y/n) ')
   print('The secret was:', secret, 'you have tried: ', guess_num, ' Times')



def fun_7():
   with  open('content.txt', 'w') as file:
      content = input('Please Enter you text here: ')
      file.write(content)
      file.close()

      
def fun_8():
   with open('content.txt', 'r') as file:
      content = file.read()
      print(content)
      file.close()


def fun_9():
   float_num = capture_user_input_float('Please Enter any number: ')
   print('square root: ', float_num ** 0.5, '\nsquare: ', float_num ** 2, '\nto power 10: ', float_num ** 10)


def fun_10():
   data = list(range(1,11))
   format_row = '{:<4}' * (len(data) + 1)
   [print(format_row.format('', *[m*n for n in data])) for m in data]

# bubble sort
def fun_11():
   array = [random.randrange(0, 1000) for i in range(1,100)]
   n = len(array)
   for i in range(n):
      already_sorted = True
      for j in range(n - i - 1):
         if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            already_sorted = False
      if already_sorted:
            break
   print(array)
   return(array)


def fun_12():
   user_str =  capture_user_input('Please Enter a text to check if Palindrome or not: ')
   for i in range(0, int(len(user_str)/2)):
      if user_str[i] != user_str[len(user_str)-i-1]:
         print('Not Palindrome')
         return None
   print('Palindrome')

def fun_13():
   num_1 = capture_user_input_int('Please enter first number: ')
   num_2 = capture_user_input_int('Please enter second number: ')
   if num_1 == num_2:
      print('No numbers between {} and {}'.format(num_1, num_2))
   elif num_1 > num_2:
      [print(i) for i in range(num_1, num_2-1, -1)]
   else:
      [print(i) for i in range(num_1, num_2+1, 1)]

      
def fun_14():
   user_str = capture_user_input('Please enter a list of number seperated by ,: ')
   user_str = user_str.split(',')
   user_int_even = []
   user_int_odd = []
   for x in user_str:
      y = int(x)
      if y%2 == 0:
         print(y)
         user_int_even.append(y)
      else:
         user_int_odd.append(y)
   print('even numbers: ', sorted(user_int_even))
   print('odd numbers: ', sorted(user_int_odd))


def fun_15():
   user_str = capture_user_input('Please enter a list of digits seperated by ,: ')
   user_str = user_str.split(',')
   digit_list = []
   [digit_list.append(int(d)) for d in user_str]
   print('The sum of the digits is: ', sum(digit_list))


class Player:
   def __init__(self, name):
      self.name = name
      self.health = random.randrange(1,10,1)
      self.strength = random.randrange(1,100,5)
      self.luck = random.randrange(1,1000,10)
   def info(self):
      print('Player {} info: health ({}), stength ({}), luck: ({})'.format(self.name, self.health, self.strength, self.luck))

def fun_16():
   player_name = capture_user_input('Please enter your name: ')
   player = Player(player_name)
   player.info()
   opponent_name = capture_user_input('Please enter opponent name: ')
   opponent = Player(opponent_name)
   opponent.info()
   

      

funcs = {'0':(fun_0, 'Exit'),
         '1':(fun_1, 'Hellow World'),
         '2':(fun_2, 'Name And Age'),
         '3':(fun_3, ''),
         '4':(fun_4, ''),
         '5':(fun_5, ''),
         '6':(fun_6, ''),
         '7':(fun_7, ''),
         '8':(fun_8, ''),
         '9':(fun_9, ''),
         '10':(fun_10, ''),
         '11':(fun_11, ''),
         '12':(fun_12, ''),
         '13':(fun_13, ''),
         '14':(fun_14, ''),
         '15':(fun_15, ''),
         '16':(fun_16, '')}


def run_fun():
   [print('{}:{}, '.format(key, value[1]), end = '') for key, value in funcs.items()]
   print()
   user_message = 'Please select an option number between [1,16]: '
   user_input = capture_user_input(user_message)
   try:
      funcs[user_input][0]()
   except Exception as ex:
      print('Please select o vaild option', ex)
   run_fun()

run_fun()
