import datetime as time
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 17:
    print("Good afternoon")
elif hour > 17 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
def askings():
    global asking
    asking = input("Are you regestered. Yes(y) or No(n):  ")
askings()
if asking == "y" or asking == "Y":
    complete = False
    user = {"Nesh" : "12", "Dad" : "5" }
    while not complete:
        username = input("Username: ")
        password = input("Password: ")
        if username == user and password == password:
            continue        
        elif username not in user:
            print("This is not a valid username, input username again!")
            continue
        elif password != user[username]:
            print(f"Password is not valid for {username}. ")
            continue
        elif password == user[username]:
            print(f"Welcome {username} ")
            print(f"Thank you for logging on. ")
            complete = True
            print("Welcome.")
            def input_a():
                global a
                a = input("Enter yourname to check if you are verified:   ")
            input_a()
            if a == "Nesh" or a == "Malli":
                print("Welcome back")
                def awsome():
                    print("these are the categories that we have")
                    print(
                    '''
                      a Math
                      b.English
                      Chose the caetegories you want:
                    ''')
                    def inputs():
                        b = input("Which categorie to you want: ")
                        if b == "a":
                            print("these are the books we have:  ")
                            print('''
                            1.Primary Math
                            2.Quiz Math
                            ''')
                            b = input("chose the book you want:  ")
                            print("Make sure you return the books in two weeks time.")
                        elif b == "b":
                            print("these are the books we have:  ")
                            print('''
                            1. Primary English
                            2.Quiz English
                            ''')
                        else:
                            print("There is no such category. Please try again")
                            inputs()

                    inputs()
                awsome()
#            elif a == int():
#                print("No numbers are allowed")
#                input_a()
#            elif a == float():
#                print("Decimals are not allowed")
#                input_a()
    
            else:
                print("Go to the school office")
elif asking == "n" or asking == "N":
    print("We are going to make you get regestered")
    print("Hello. We are going to get you regestered")
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    c = user[username] = password
    d = user.update(c)
else:
    print("Please input Yes(y) or No(n)")
    askings()
    
