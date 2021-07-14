def swap():
    a = input("Key in value for a : ")
    b = input("Key in value for b : ")
    #print("Before : a = %s and b = %s\nAfter : a = %s and b = %s" %(a,b,b,a))
    print("Before : a = %s and b = %s"%(a,b))

    a = int(a) + int(b)
    b = a-int(b)
    a=a-b
    print("After : a = %d and b = %d" %(a,b))

if __name__ == "__main__":
    swap()