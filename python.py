name = input("enter your name\n")
print("your name-",name)

list

l1=[1,53,465,6,54]
print(type(l1))
print(l1)
l1.sort()
l1.append(45)
l1.pop()
l1.extend([23,6,6,45,15,4])
print(l1)

  #sets

a1={3,5,23,5,5,5}
a2={3,5,23,65,26,5,6}
print(a1.pop())
print(a1.intersection(a2))
print(a1)


  #dictionary

dict1={"good":"something pleasent","fetch":"to bring"}
marks={"snayan":99,"harry":55,"ambika":77}

print(dict1["good"])
print(marks["snayan"])
marks["raju"]=11
print(marks)
 
  #ifelse

age=int(input("enter your age\n"))
if(age>=18):
    print("yess,you can drive")
elif(age==1):
    print("you are kid")
else:
    print("no,you cant drive")
print("end of program")

 #matchcase

a=int(input("enter number\n "))
match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case 4:
        print("case is 4")
    case 5:
        print("case is 5")
    case 6:
        print("case is 6")
    case _:
        print("mo match found")

a= int(input("enter numkber between 1 to 10\n"))
match a:
    case 1:
        print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 2:
        print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 3:
       print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 4:
       print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 5:
       print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 6:
       print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 7:
       print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 8:
        print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 9:
        print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)
    case 10:
        print(a*1,a*2,a*3,a*4,a*5,a*6,a*7,a*8,a*9,a*10)

 #for loop
for i in range(5):
    print(i+1)

a = [1,34,456,35,262]
s =[3,5,5,8,2,8,65,32,5]
for i in a,s:
    print(i)

 #while loop

i = 0
for i in range(5):
    if(i == 3):
       continue
    print(i+1)
    
while(True):
    num = int(input("enter number: "))
    print(num)
    if(num==0):
        break

 #funtions

def greethello(name,ending):
    print("hello " + name)
    print("hello")
    print("hello")
    print(ending)

def letter(name,date):
    i=f" hello ,good morning {name} today is a {date}" #f string consists f""
    print(i)

def average(a,b):
    return(a+b)/2

print("excecuting funtion")
greethello("snayan","thank you")
print("done")  
name = (input("enter name \n"))
date = int(input("enter date\n"))
letter(name,date)
print(average(2,4))

 #.......try except
try:
    a = int(input("enter your number:\n"))
    print(a +3)
except Exception as e:
    print("some error occur",e) 