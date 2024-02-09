from insensitive_strenum import InsensitiveStrEnum
print("Welcome To Chez Console")
while True:
    CP = input("")
    if CP == "Help":
        print("Do help() For All Commands")
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
    else:
        print("NCE")
        

