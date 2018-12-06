def facto(n) :
    """Factorial of a number"""
    fact = 1
    if n < 0 :
        print("Sorry factorial of neagative number does not exist")
    elif n == 0:
        print("Factorial of 0 is 1")
    else :
        for i in range(1,n+1):
            fact = fact * i 
        print("Factorial of ",str(n)," is ",str(fact))      

if __name__ == "__main__" :
     import sys
     facto(int(sys.argv[1]))  
           