print("welcome to humid summer")
ans=0
print('please enter the number and press enter')
while input('take input[y]')=='y':
    ans += int(input('enter a number:'))
print('the sum is',ans)    

uname="admin"
pwd="hahah"
while True:
    username=int(input("enter the usernme"))
    password=int(input("enter the password"))
    if username!=uname:
        print("invalid username")
    if password!=pwd:
        print("invalid password")
    if username==uname and password==pwd:
        print("welcome")
        break45
                




