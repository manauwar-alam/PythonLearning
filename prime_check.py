def check_prime(n) :
    """Program to check prime number """
    if n > 1 :
        for i in range(2,int(n/2)) :
            if (n % i) == 0:
                print(str(n)," is not a prime number")
                break
        else :
            print(n,"is a prime number")
    else :
        print(n,"is not a prime number")

if __name__ == "__main__" :
     import sys
     check_prime(int(sys.argv[1]))
                
                    