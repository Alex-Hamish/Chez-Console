import re

#Here The Functions Lie
def FindBracketedText(text):
    x = re.search("(?<=\().+?(?=\))", text)
    return x.group()
def FindBracketedString(text):
    x = re.search("(?<=\(\").+?(?=\"\))", text)
    return x
def hasechogood(text):
    x = re.findall("echo\(\"[^\"]*\"\)", text)
    if (x):
        return True
    else:
        return False
def hasechobad(text):
    x = re.findall("echo\([^\)]*\)", text)
    if (x):
        return True
    else:
        return False
    
print("Welcome To Chez Console")
while True:
    Input = input("")
    CurrentCommand = Input.lower()
    if CurrentCommand == "help":
        print("Do Help() For All Commands")
    elif CurrentCommand == "help()":
        print("""Help() Shows All Commands
End() Ends The Program
Error() Shows What Errors Are
Echo() Responds With The Input""")
    elif CurrentCommand == "end()":
        print("Bye Bye!!")
        break
    elif CurrentCommand == "error()":
        print("Put The Command With The First Letters To Learn About It")
    elif CurrentCommand == "error(nce)":
        print("NCE Means There Is No Current Command For That")
    elif CurrentCommand == "error(nie)":
        print("NIE Means There Is A Blank Space In An Input")
    elif CurrentCommand == "error(se)":
        print("SE Means There Is A Syntax Error")
    elif CurrentCommand == "echo()":
        print("NIE")
    elif hasechobad(CurrentCommand):
        if hasechogood(CurrentCommand):
            print(FindBracketedString(Input).group())
        else:   
            print("SE")
    else:
        print("NCE")
