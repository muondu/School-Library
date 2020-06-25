asking = input("Are you regestered. Yes(y) or No(n):  ")
if asking == "y":
    complete = False
    user = {"username1" : "12345", "username2" : "67890" }
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
            a = input("Enter yourname to check if you are verified:   ")
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
else:
    print("We are going to make you get regestered")
  

    elif asking1 == "No":
        print("Hello. We are going to get you regestered")
        username = input("Please enter your username:  ")
        password = input("Please enter your password:  ")
        c = user[username] = password
        d = user.update(c)
   
      


