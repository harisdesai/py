# num1=int(input("Enter 1st number"))
# num2=int(input("Enter 2st number"))
# num3=int(input("Enter 3st number"))
# if(num1>num2):
#     if(num1>num3):
#         print(f"{num1} is greatest")
#     else:
#         print(f"{num3} is greatest")
# elif(num2>num3):
#     print(f"{num2} is greatest")   
# else:
#     print(f"{num3} is greatest")



# n=int(input("Enter number"))
# sum=0
# while(n>0):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print("the sum of digit is ",sum)    



# n=int(input("Enter number of rows"))
# for i in range(0,n):
#  for j in range(0,n-i-1):
#     print(end="")   
#  for j in range(0,i+1):
#     print("*",end=" ")
#  print()


# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end="")
#     print()




# n = int(input("Enter the rows:"))
# for i in range(1, n+1):
#   for j in range(0, n-i+1):
#    print('', end='')
#   C = 1
#   for j in range(1, i+1):
#     print(' ', C, sep='', end='')
#     C = C * (i - j) // j
#   print()





# l=[]
# ch='y'
# while(ch=='y'):
#     print("1.add book\n2.display book")
#     choice=int(input("Enter choice:"))
#     if(choice==1):
#         book=input("Enter name of book:")
#         l.append(book)
#     elif(choice==2):
#         print(l)
#     else:
#         print("invalid choice")    
#     ch=input("Do u want to continue?")
# print("bye")





# components=['RADIATOR','AC COMPRESSOR','BATTERY','ALTERNATOR','AXLE','BRAKES','SHOCK ABSORBERS','TRANSMISSION','FUEL TANK']
# components1=['CATALYTIC CONVERTER','MUFFLER','TAILPIPE']
# ch='y'
# while(ch=='y'):
#  print('''
#  1. Display Main Components
#  2. Display All Components
#  3. Total Components
#  4. Components in Alphabetical Order
#  ''')
#  choice=int(input("Enter choice: "))
#  if(choice==1):
#   print("The Main components are:")
#   print(components)
#  elif(choice==2):
#   print("The components are:")
#   print(components+components1)
#  elif(choice==3):
#   print("The components are:")
#   print("Main Components:",len(components))
#   print("Other Components:",len(components1))
#  elif(choice==4):
#   print("The components in alphabetical order are:")
#   components.sort()
#   print("Main Components:",components)
#   print("Sorted order")
#  else:
#   print("Invalid choice!")
#  ch=input("Do you want to continue...?")
# print("Bye!")







# components={}
# print(type(components))
# components=set()
# print(type(components))
# components={"Clutch","Gear Box ","Front dead axle","Engine","Rear drive axle","Differential"}
# print(components)
# b=input("Enter the components to be added" )
# components.add(b)
# print("Components of automobile after adding an element in set")
# print(components)
# print("Removing the one Component")
# components.pop()
# print("Updated Components after removing an element is set")
# print(components)





# dict={1:"haris",2:"sahil",3:"sarthak"}
# print(type(dict))
# print(dict)
# print(dict.pop(2))
# dict[4]="digya"
# print(dict)






# n = int(input("Please enter number of students:"))
# all_students = []
# for i in range(0, n):
#     stud_name = input('Enter the name of student: ')
#     print (stud_name)
#     stud_rollno = int(input('Enter the roll number of student: '))
#     print (stud_rollno)
#     mark1 = int(input('Enter the marks in subject 1: '))
#     print (mark1)
#     mark2 = int(input('Enter the marks in subject 2: '))
#     print (mark2)
#     mark3 = int(input('Enter the marks in subject 3: '))
#     print (mark3)
#     total = (mark1 + mark2 + mark3)
#     print("Total is: ", total)
#     average = total / 3
#     print ("Average is :", average)
#     all_students.append({
#     'Name': stud_name,
#     'Rollno': stud_rollno,
#     'Mark1': mark1,
#     'Mark2': mark2,
#     'Mark3': mark3,
#     'Total': total,
#     'Average': average
#     })
#     for student in all_students:
#        print ('\n')
#     for key, value in student.items():
#        print (key, value)





# def func(n):
#     if n==1 or n==0:
#        return 1
#     else:
#        return n*func(n-1)
# num=int(input("enter the no.:"))
# print(func(num))




# def find_max(li):
#     max=li[0]
#     for a in li:
#         if a>max:
#             max=a
#     return max
# lis=[]
# num=int(input("numbers"))
# for n in range(num):
#     number=int(input("enter the number:"))
#     lis.append(number)
# print(find_max(lis))    




# def cir():
#  r=int(input("Enter the radious"))
#  area=3.14*r*r
#  return area
# def tria():
#  b=int(input("Enter the base"))
#  h=int(input("Enter the height"))
#  area=1/2*b*h
#  return area
# def square():
#  a=int(input("Enter the side"))
#  area=a*a
#  return area
# def rect():
#  l=int(input("Enter the length"))
#  w=int(input("Enter the width"))
#  area=l*w
#  return area
# print(cir())
# print(tria())
# print(square())
# print(rect())





# def sum_list(l):
#  sum=0
#  for i in range(len(l)):
#   sum=sum+l[i]
#  return sum
# l=[]
# n=int(input("Enter the number of elements"))
# for i in range(n):
#  x=int(input("Enter the element"))
#  l.append(x)
#  result=sum_list(l)
#  print(result)





# def add(x, y):
#   return x + y
# def subtract(x, y):
#   return x - y
# def multiply(x, y):
#   return x * y
# def divide(x, y):
#   return x / y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# while True:
#   choice = input("Enter choice(1/2/3/4): ")
#   if choice in ('1', '2', '3', '4'):
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#   if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
#   elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
#   elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
#   elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
#   next_calculation = input("Let's do next calculation? (yes/no): ")
#   if next_calculation == "no":
#     break
#   else:
#     print("Invalid Input")





# def reverse(s):
#  str = ""
#  for i in s:
#   str = i + str
#  return str
# s =input("Enter the string to reverse:")
# print ("The original string is : ",end="")
# print (s)
# print ("The reversed string is : ",end="")
# print (reverse(s))

# string=input(("Enter a letter:"))
# print(string[::-1])





# string=input(("Enter a letter:"))
# if(string==string[::-1]):
#  print("The letter is a palindrome")
# else:
#  print("The letter is not a palindrome")






# test_str = input("Enter the String:")
# character=input("Enter the Character:")
# count = 0
# for i in test_str:
#  if i == character:
#   count = count + 1
# print ("Count is : "+ str(count))






# string = " HI! HI! HI! WELCOME TO PYTHON PROGRAMMING"
# print ("Original String:",string)
# replace1=string.replace("HI", "HELLO")
# print ("Replaced String 1:",replace1)
# replace2=replace1.replace("HELLO", "Hello")
# print ("Replaced String 2:",replace2)








# print("Enter the Name of Source File: ")
# sourcefile = input()
# print("Enter the Name of Target File: ")
# targetfile = input()
# fileHandle = open(sourcefile, "r")
# texts = fileHandle.readlines()
# fileHandle.close()
# fileHandle = open(targetfile, "w")
# for s in texts:
#  fileHandle.write(s)
#  fileHandle.close()
# print("File Copied Successfully!")





# fin = open("book.txt","r")
# str = fin.read()
# l = str.split()
# count_words = 0
# for i in l:
#  count_words = count_words + 1
# print(count_words)
# fin.close()






# fin = open("name.txt","r")
# str = fin.read()
# words = str.split()
# max_len = len(max(words, key=len))
# for word in words:
#  if len(word)==max_len:
#   longest_word =word
# print(longest_word)