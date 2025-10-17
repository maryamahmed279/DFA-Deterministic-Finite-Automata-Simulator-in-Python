# the code to make DFA system 
import numpy as np #lib
import functions as fun #package
import math
#the states
x=input("Enter the number of states : ")
x=x.split()
x=x[0]
while not x or not x.split() or not x.isdigit() or int(x)==0 :
    print("Try again can't be empty or not a digit value")
    x=input("Enter the number of states : ")
states_number=int(x)
states =[]
i=0
print()
while(i!=states_number):
    x=input(f"Enter {i+1} state : ")
    if x and x.split() and x not in states:
         states.append(x)
         i=i+1
    elif x in states:
        print("the value already exist ? try again ")
    else:
        print("Try again can't be empty value")
print(f"The states : {states}")
#the initial state 
intial_state=input("what is the initial state? ")
intial_state=intial_state.split()
intial_state=intial_state[0]
while not intial_state or not intial_state.split() or intial_state not in states:
    print("it can't be empty or not exist , try again")
    intial_state=input("what is the initial state? ")
intial_state=intial_state
#The final state
num_final=input("number of final state : ")
while not num_final or not num_final.split() or not num_final.isdigit() or int(num_final)==0 or len(states) < int(num_final) :
    print("Try again can't be empty or not a digit value or out of range ")
    num_final=input("number of final state : ")
num_final=int(num_final)
final_states=[]
i=0
while(i!=num_final):
    x=input(f"Enter {i+1} final state : ")
    if x and x.split() and x in states and x not in final_states:
         final_states.append(x)
         i=i+1
    elif x not in states:
        print("the value not exist ? try again ")
    elif x in final_states:
        print("the value already exist ? try again ")
    else:
        print("Try again can't be empty value")
# the inputs 
x=input("Enter the number of inputs : ")
while not x or not x.split() or not x.isdigit() or int(x)==0:
    print("Try again can't be empty or not a digit value")
    x=input("Enter the number of inputs : ")
inputs_number=int(x)
inputs_values=[]
i=0
while(i!=inputs_number):
    x=input(f"Enter {i+1} input : ")
    if x and x.split() and x not in inputs_values:
         inputs_values.append(x)
         i=i+1
    elif x in inputs_values:
        print("the value already exist ? try again ")
    else:
        print("Try again can't be empty value")
print(f"The inputs :{inputs_values}")
#the transition table
table=np.empty((states_number+1,inputs_number+1),dtype=object)
table[0][0]=""
for i in range(states_number):
    table[i+1][0]=states[i]
for j in range(inputs_number):
    table[0][j+1]=inputs_values[j]
for i in range(1,states_number+1):
    for j in range(1,inputs_number+1):
        x=input(f"enter value if state is {table[i][0]} and input is {table[0][j]} ") 
        if x.replace('.', '', 1).isdigit():
            x=str(int(math.floor(float(x))))
            print(x)
        while not x or not x.split() or x not in states :
            print("Try again can't be empty or not found")
            x=input(f"enter value if state is {table[i][0]} and input is {table[0][j]} ")
        table[i][j]=x
# print the transition table 
print("------------------------------------------------------------------------")
for i in range(states_number+1):
    for j in range(inputs_number+1):
        print(table[i][j], end="\t") 
    print()
print("------------------------------------------------------------------------")
print ("THE FORMAL DIFINITION")
print("------------------------------------------------------------------------")
print(f"{ states , inputs_values, table, intial_state, final_states}")
print("------------------------------------------------------------------------")
print("PRESS Q OR q IN CASE YOU WANT TO QUIT THE PROGRAM")
x=input("Enter your String : ")
while x.lower() != "q" :
    fun.check(x,intial_state,final_states,inputs_values,table,states)
    x=input("Enter your String : ")
print("YOU EXIT THE PROGRAM <BYE> ")
