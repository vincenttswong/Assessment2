FruitList = ['Apple', 'Orange','Pear','Grape','Kiwi']  #List of fruits
PriceList = [1.30,1.00,0.80,2.20,1.70]  #Price list; index matches FruitList

def swap_func(a,b):  #returns new a and b
    
    a = int(a) + int(b)
    b = a-int(b)
    a=a-b
    
    return str(a),str(b)

def lookup_func(fruit,qty):  #returns total price
    return PriceList[FruitList.index(fruit)]*float(qty)