keep_going= True
while keep_going:
    print("1. DIisplay Hello message")
    print("2.calculate a+b")
    print("9.Exit")


    choice=input("select 1,2,3,4, or9:")


    if choice=="1":
        print("heloo all")
    elif choice=="2":
        print("We will calculate a+b, but first enter a and b.")
        a= int(input("a= ")) 
        b= int(input("b="))
        sum = a+b
        print(f"{a}+{b} = {sum}\n")  
    elif choice == '9' 
       keep_going = False