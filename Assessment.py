import gui_lib as G
import Analysis as anl
import getFruitPrice as gFP

def swapClicked():
	a_before = a.get()
	b_before = b.get()
	a_after,b_after = anl.swap_func(a_before, b_before)
	swapMessage['text'] = "Before : a = %s and b = %s\nAfter : a = %s and b = %s" %(a_before,b_before,a_after,b_after)

def fruitChanged(event):
	#totalPriceMessage['text'] = qty.get()
	totalPriceMessage['text'] = 'Total Price = $%0.2f'%(anl.lookup_func(selFruit.get(),float(qty.get())))
    
def quantityChanged():
    totalPriceMessage['text'] = 'Total Price = $%0.2f'%(anl.lookup_func(selFruit.get(),float(qty.get())))


if __name__ == "__main__":
    gui = G.GUI()
    a = gui.user_input("Key in a value for a: ", 0,0)
    b = gui.user_input("Key in a value for b: ", 1,0)
    swap = gui.button("Swap", 2,0)

    qty= gui.quantity("Quantity", 1,2,1,100)
    selFruit = gui.drop_down("Select fruit:",gFP.FruitList,0,2,36)
    swapMessage=gui.message("Before: \nAfter:",2,1)
    totalPriceMessage=gui.message("Total Price = ",2,3)
    swap['command'] = swapClicked
    selFruit.bind("<<ComboboxSelected>>", fruitChanged)
    qty['command'] =quantityChanged
    swapMessage.configure({"aspect":300})
    totalPriceMessage.configure({"aspect":300})

    gui.mainloop()