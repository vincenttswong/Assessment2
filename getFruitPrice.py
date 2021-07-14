FruitList = ['Apple', 'Orange','Pear','Grape','Kiwi']  #List of fruits
PriceList = [1.30,1.00,0.80,2.20,1.70]  #Price list; index matches FruitList


def getFruitPrice():
        
    while (True):
        #Get user to enter a fruit 
        abort, fruit = getInput('fruit')
        if abort:
            break
        else:   
            if (fruit in FruitList):  #Validate fruit keyed in
                abort, qty = getInput('qty')
                if abort:
                    break
                else:
                    price = PriceList[FruitList.index(fruit)]*float(qty)    #Calculate price
                    print('Fruit : %s\nQuantity : %s\nPrice x Quantity : %0.2f\n'%(fruit,qty,price))
            else:   #Get user to enter price
                print('[%s] is invalid\nFruit List : %s \n '%(fruit,FruitList))
            
    

def getInput(dataType): # returns abort, user input
        
    while (True):
        # Get user input
        inp = input("Please key in a %s(leave field empty to exit) and hit enter : "%dataType)
        if (inp == ""):
            if (abortConfirmation() == True): #user wants to abort
                return True, 'User abort'
        else:
            if (dataType == 'fruit'):
                return False, inp
            elif(dataType == 'qty'):
                if isInt(inp):
                    return False, inp
                else:
                    print('Invalid input, please key in a numeric value' )
            else:
                return True, 'Invalid dataType\n'
    

def abortConfirmation():
    
    while (True):
        inp = input('Are you sure to exit?\ny if YES, n if NO : ')
        if (inp in ['y','Y']):
            return True
        elif (inp in ['n','N']):
            return False
        else:
            print('Invalid input\n')
    
    
def isFloat(s):
	try:
		float(s)
		return True
	except:
		return False
        
def isInt(s):
	try:
		float(s)
		return True
	except:
		return False
    
if __name__ == "__main__":
    getFruitPrice() 