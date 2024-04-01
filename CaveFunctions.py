                        # After giving values ​​to the first function, press enter to display outputs (one by one) !!
import random
def calculate_magic_numbers(start,end):
    magic_nums = []
    for i in range(l):
        if i >= 0 and i <= end-start:
            m=random.randint(start,end)
            magic_nums.append(m)
    return magic_nums
start = int(input("Start with:"))
end = int(input("End with:"))
l = int(input("My range:"))
opx = calculate_magic_numbers(start,end)
print(opx)
print("tap to see all defs resultd:D")
import time 
def exam_numbers():
    valid_answer = 0 #number of correct and incorrect answers by user
    unvalid_answer = 0
    start_time = time.time() #start(operation)
    while time.time() - start_time < 20:
        binary_numbers = []
        for _ in range(4): #if we use(i,j,...) instead of (_) it would be useless cuz it wasnt used in command below.
         binary_numbers.append(random.choice("10"))
                                     #this function randomly displays 1,0 in 10 bits.
        decimal_numbers = list((int,input().split())) #map(function,iterable)
        for i in binary_numbers:
            for j in decimal_numbers:
                if j==int(i,2):               #two fors (binary =>> decimal)
                    valid_answer +=1
                else:
                    unvalid_answer +=1
        print(f"valid ans:{valid_answer}")
        print(f"unvalid ans:{unvalid_answer}")
        break
exam_numbers()
import string
def check_pass(users):
    for username,password in users:
        if len(password) >= 8 and any(ch.islower() for ch in password) and any(ch in string.punctuation for ch in password):
           print(f"{username} has this password:{password}!<3")
users = [("user1","DkPm@1234"),("user2","12345678"),("user3","34aJ@5678903"),("user4","98QQ7654378"),("user5","3866266DDnx@"),("user6","Q765pu4378")]
check_pass(users)