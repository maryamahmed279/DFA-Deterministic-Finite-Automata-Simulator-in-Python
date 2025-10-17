#the function to check if the string is accepted or not 
#the function take the string that will be checked 
# the states and the inputs and decleared which is the final 
# and which is the intial state to trace the input
def check(s, inital, final, inputs, tabel, states):
    if not s or not s.split() :
        print("It's empty input , Try again")
        return
    else:
       c=check_string(s,inputs) 
       if not c:
           print("There is unknown data , try again?")
           return
       else:
           check_last(s,final,tabel,inital,states,inputs)

#check if the string is all from the existed inputs 
def check_string(s,inputs):
    for i in s:
        if i not in inputs:
            return False
    return True

#check it the last string in the accepted statge 
def check_last(s,final,tabel,intial,states,inputs):
    current = intial
    print(f"Trace: {current}", end=" ")
    for i in s:
        next_state = check_next(i, tabel, states, inputs, current)
        print(f"--{i}--> {next_state}", end=" ")
        current = next_state  # move to the next state
    print()  # newline
    if current in final:
        print(f"The string is ACCEPTED ✅ (ended in {current})")
    else:
        print(f"The string is REJECTED ❌ (ended in {current})")

#function take the input and want to know the next state from tabel 
def check_next(symbol, table, states, inputs, current_state):
    row = states.index(current_state) + 1
    col = inputs.index(symbol) + 1
    next_state = table[row][col]
    return next_state
