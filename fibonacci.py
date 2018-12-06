def fibo(n) :
    """ Print fibonacce series of number """
    a,b = 0,1
    print("Function with argv[1] : ",str(n))
    while a < n :
        print(a, end =' ')
        a,b = b,a + b
    print() 

if __name__ == "__main__" :
     import sys
     fibo(int(sys.argv[1]))
       
  