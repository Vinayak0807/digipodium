
uname="admin"
pwd="hahah"
attempt=0
while True:
    attempt+=1
    print(f'attempt{attempt}of 3')
    username=(input("enter the usernme"))
    password=(input("enter the password"))
    if attempt==3:
        print("too many attempt")
        break
    if username!=uname:
        print("invalid username")
    if password!=pwd:
        print("invalid password")
    if username==uname and password==pwd:
        print("welcome")
        break
