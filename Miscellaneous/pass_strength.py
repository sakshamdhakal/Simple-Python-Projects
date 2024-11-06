#CHECKS THE STRENGTH OF A PASSWORD

""" **REQUIREMENTS** 
# length >= 8
# number atleast 1
# uppercase at least 1 """

while True :
    password = input("Enter your password:")
    result = {}


    if len(password) >= 8 :
        result["length"] = True

    else :
        result["length"] = False
    
    upper_case = False

    for i in password :
        if i.isupper() :
            upper_case = True
    result["upper_case"] = upper_case

    digits = False

    for i in password :
        if i.isdigit() :
            digits = True
    result["digits"] = digits

    if all(result.values()):
        print("Strong Password")
    else :
        print("Weak Password")

    for key, value in result.items() :
        print(f"{key}={value}")
