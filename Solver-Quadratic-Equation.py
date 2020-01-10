import math
import time
def equation_solve(a,b,c): #Find Equation's Roots
    D = (b**2) - (4*a*c)
    if D < 0:
        X_1 = "Αδύνατη"
        X_2 = "Aδύνατη"
        return X_1, X_2;
    X_1 = (-(b) + math.sqrt(D))/(2*a)
    X_2 = (-(b) - math.sqrt(D))/(2*a)
    return X_1 , X_2 ;

def equation_maker(a,b,c,unknown_letter):
    equation_msg = f"{str(a)}{unknown_letter}²{str(b)}{unknown_letter}{str(c)}"
    return equation_msg

def inputs():
    print("Welcome to Quadratic Equation Solver")
    a = input("Value for a(add + or -) ?: ")
    b = input("Value for b(add + or -) ?: ")
    c = input("Value for c(add + or -) ?: ")
    unknown = input("Letter for unknown variable ?: ")
    return a,b,c,unknown ;

def printmsg(equation_msg,unknown,X_1,X_2):
    msg = f"Οι λύσεις της εξίσωσης {equation_msg} ειναι οι {unknown}₁ = {str(X_1)} και {unknown}₂ = {str(X_2)}"
    print(msg)


a , b , c , unknown = inputs()
X_1 , X_2 = equation_solve(float(a),float(b),float(c))
equation_msg = equation_maker(a,b,c,unknown)

check = True
while check:
    equation_check_user = input(f"Άρα η εξίσωση είναι η: {equation_msg} (Yes/No)?")
    if equation_check_user == "Yes":
        printmsg(equation_msg ,unknown , X_1 , X_2)
        break
    elif equation_check_user == "No":
        print("Restarting......")
        time.sleep(5)
        a, b, c, unknown = inputs()
        X_1, X_2 = equation_solve(float(a), float(b), float(c))
        equation_msg = equation_maker(a, b, c, unknown)
    else:
        print("ΜΗ ΑΠΟΔΕΚΤΗ ΑΠΑΝΤΗΣΗ")
        break
