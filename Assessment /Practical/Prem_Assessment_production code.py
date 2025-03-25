d={}
while True:
    menu = """
    press 1 for Manager Mode
    press 2 for Cudtomer Mode 
    press 3 for Exit
    """
    print(menu)
 
    choice = int(input("Enter The Choice !!: "))
    if choice==1:
        print("######### Wlcome to manger mode #########")
        number = int(input("Enter Index Number : "))
        if number in d:
            print("index already in use overriting !!")
        fname = input("Enter Fruit name : ")
        qty = int(input("ENter The Quintity : "))
        price = int(input("Enter The Price Per Pice :"))

        
        d[number] = {"name":fname , "qty":qty, "price":price,}
        print("######### Data Added Succesfully #########")
        print(d)
        # choice = ("enter your choice : ")


    elif choice == 2:
        print("######### Welcome To Customer Mode ########")
        print(d)
        number2 = int(input("Enter Index Number :"))
        if number2 in d:
            print(d[number2])
            print("how many piece do you want !! ")
            quantity = int(input("Enter The Quantity : "))
        else:
            print("Index Not Found !!")
            break
        
        if quantity <= qty :
            print("available !!")
            price2 = quantity * price
            print("net value of your qty is ", price2)
        else:
            print("the net qty is not available !!")
        

    elif choice == 3:
        print("######### THANK YOU ##########")
        break        

