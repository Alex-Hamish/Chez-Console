print("Welcome To Chez Console")
while True:
    CP = input("")
    if CP == "Help":
        print("Do Help() For All Commands")
    elif CP == "Help()":
        print("""Help() Shows All Commands
End() Ends The Program
Error() Shows What Errors Are""")
    elif CP == "End()":
        print("Bye Bye!!")
        break
    elif CP == "Error()":
        print("Put The Command With The First Letters To Learn About It")
    elif CP == "Error(NCE)":
        print("NCE Means There Is No Current Command For That")
    elif CP == "Error(NIE)":
        print("NIE Means There Is A Blank Space In An Input")
    elif CP == "Echo()":
        Echo = input("""What Would You Like To Echo?
""")
        if Echo == "":
            print("NIE")
        else:
            print(Echo)
    elif CP == "":
        print("NIE")
    else:
        print("NCE")
        

