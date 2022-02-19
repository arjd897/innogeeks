import time
import pandas
import numpy as np
from matplotlib import pyplot as plt
from termcolor import colored
from playsound import playsound 


playsound('music.mp3', False)
print(colored('WELOCOME TO THE QUIZ','red'))
time.sleep(2)
input(colored('ENTER YOUR NAME','green'))
time.sleep(2)
print(colored('\nFASTEN UP YOUR SEAT BELT,YOUR QUIZ IS ABOUT TO START\n','blue'))
time.sleep(6)
print('YOUR PYTHON QUIZ STARTS NOW')
time.sleep(3)


python_file= open("Python.txt","r")
python =python_file.readlines()

dict = {}

for i in range(len(python)):
    if i%2==0:
        a = python[i]
        a = a[0:len(a)-1]
        b = python[i+1]
        if i!=(len(python)-2):
            b = b[0:len(b)-1]
        dict.update({a:b})
    

marks_python=0
count1=0



for i in dict:
    count1=count1+1
    print (i)
    answer1=input()
    answer1=answer1.title()
    
    if answer1==dict[i]:
        marks_python=marks_python+1
    
    print("\n", end="")
    
    if count1!=len(dict):
        print(colored('Gear up for your next question', 'red'))
        time.sleep(1)
    
    print("\n",end="")

print('PYTHON QUIZ IS ENDED...NOW YOUR MATHS QUIZ STARTS \n')
time.sleep(1.5)

maths_file= open("Maths.txt","r")
maths =maths_file.readlines()

dict1 = {}

for j in range(len(maths)):
    if j%2==0:
        c= maths[j]
        c = c[0:len(c)-1]
        d = maths[j+1]
        if j!=(len(maths)-2):
            d= d[0:len(d)-1]
        dict1.update({c:d})
    


marks_maths=0
count2=0

for j in dict1:
    count2=count2+1
    print (j)
    answer2=input()
    answer2=answer2.title()
    if answer2==dict1[j]:
       
        marks_maths=marks_maths+1
 
    
    print("\n",end="")

    if count2!=len(dict1):
        print(colored('Gear up for your next question','red'))
        time.sleep(1)
    
    print("\n",end="")

print('YOUR MATHS QUIZ ENDED....NOW YOUR PHYSICS QUIZ STARTS')
time.sleep(1.5)

physics_file= open("Physics.txt","r")
physics =physics_file.readlines()

dict2 = {}

for k in range(len(physics)):
    if k%2==0:
        e = physics[k]
        e = e[0:len(e)-1]
        f = physics[k+1]
        if k!=(len(physics)-2):
            f = f[0:len(f)-1]
        dict2.update({e:f})
    


marks_physics=0
count3=0

for k in dict2:
    count3=count3+1
    print (k)
    answer3=input()
    answer3=answer3.title()
    if answer3==dict2[k]:
        
        marks_physics=marks_physics+1
    

    print("\n",end="")

    if count3!=len(dict2):
        print(colored('Gear up for your next question','red'))
        time.sleep(1)

    print("\n",end="")


print ('PHYSICS QUIZ HAS ENDED... \n Now get ready for your score')

time.sleep(1.5)

TOTAL_MARKS=marks_python+marks_maths+marks_physics
print("Total Marks = ",TOTAL_MARKS,"/15")

if TOTAL_MARKS<8:
    print('CONGRATULATIONS,YOU ARE PASSED IN THE QUIZ')
else:
    print('SORRY,YOU WERE NOT ABLE TO QUALIFY')

M=pandas.DataFrame({"Subjects":["Python","Maths","Physics"],"Marks":[marks_python,marks_maths,marks_physics],"Max_Marks":[5,5,5]})
print (M)

X=np.array(["Python","Maths","Physics"])
Y=np.array([marks_python,marks_maths,marks_physics])
Z=np.array(['red','blue','green'])
plt.bar(X,Y)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Distribution")
plt.show()

plt.pie(Y,labels=X,colors=Z)
plt.show()