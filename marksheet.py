while(1):
    print("Press 1 for area of circle")
    print("Press 2 for area of triangle")
    print("Press 3 for area of square")
    print("Press 4 for area of rectangle")
    print("Press 5 for exit")
    ch=int(input("Enter your choice="))

    if(ch==1):
        r=float(input("Enter radius= "))
        area=3.14*r*r
        print("Area of circle= ",area)

    elif(ch==2):
        l=float(input("Enter length= "))
        b=float(input("Enter breadth= "))
        area=l*b
        print("Area of trinagle= ",area)

    elif(ch==3):
        l=float(input("Enter length= "))
        area=l*l
        print("Area of square= ",area)

    elif(ch==4):
        l=float(input("Enter length= "))
        h=float(input("Enter height= "))
        area=l*h
        print("Area of rectangle= ",area)
    elif(ch==5):
        break
    else:
        print("Invalid option")
