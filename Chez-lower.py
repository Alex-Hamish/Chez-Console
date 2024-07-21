print("Welcome To Chez Console")
# Put Functions Here!
while True:
    Input = input("")
    CP = Input.lower()
    if CP == "help":
        print("Do Help() For All Commands")
    elif CP == "help()":
        print("""Help() Shows All Commands
End() Ends The Program
Error() Shows What Errors Are
Echo() Responds With The Input""")
    elif CP == "end()":
        print("Bye Bye!!")
        break
    elif CP == "error()":
        print("Put The Command With The First Letters To Learn About It")
    elif CP == "error(nce)":
        print("NCE Means There Is No Current Command For That")
    elif CP == "error(nie)":
        print("NIE Means There Is A Blank Space In An Input")
    elif CP == "echo()":
        print("ECHO IS BEING TESTED")
    else
        print("NCE")
         

