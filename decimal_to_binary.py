def decimalToBinary(n) :
    """Program to convert decimal to binary"""
    if n > 1 :
        decimalToBinary(n//2)
    print(n%2, end =' ')
    
    
if __name__ == "__main__" :
     import sys
     decimalToBinary(int(sys.argv[1]))