#def logic():
#    a = input("Enter your favorite video game:  ")
#    for c in a:
#        if a != str():
#            print("Inputed the wrong thing")
#            logic()
#logic()
def votes():
    while True:
        try:
            global age
            age = int(input("Enter your age:  "))
        except ValueError:
            print("Sorry, I did'nt understand that")
            votes()
        finally:
            if age >= 18:
                print("You can vote")
                break
            else:
                print("Sorry, You can't vote")
                break
votes()


#def name():
#    while True:
#        try:
#            global name
#            name = input("Enter your name:  ")
#        except ValueError:
#            print("Sorry, I did'nt understand that")
#            name()
#        finally:
#            if len(name) >= 2:
#                print("Hello " + name)
#                break
#            else:
#                print("Sorry, Too short to be a name")
#                break
#name()
def name():
    while True:
        name = input("Enter your name:  ")
        try:
            len(name)< 2
            break         
        except ValueError:
            print("Greater than 3 characters")
        
        
            
        
name()