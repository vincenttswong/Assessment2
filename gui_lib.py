from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os


widget_font = 'Helvetica'
widget_text_size = 14
widget_background = 'white'
widget_foreground = 'blue'

	
class GUI(tk.Tk):
	def __init__(self):
		"""super() lets you avoid referring to the base class explicitly, 
		which can be nice. But the main advantage comes with multiple inheritance, 
		where all sorts of fun stuff can happen. See the standard docs on super if you haven't already."""
		super().__init__()

		self.geometry('750x140')
		self.resizable(0, 0)
		self.title('Assessment 2')
		
	def user_input(self,caption,rw,cl):
		label = tk.Label(self, text=caption)
		label.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font,widget_text_size)})
		label.grid(column=cl, row=rw)
		entry = tk.Entry(self)
		entry.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font, widget_text_size)}
						)
		entry.grid(column=(cl+1), row=rw)
		return entry
		
	def button(self,caption,rw,cl):
		btn = tk.Button(self, text=caption)
		btn.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font,widget_text_size)})
		btn.grid(column=cl, row=rw)
		return btn

	def quantity(self,caption,rw,cl,min,max):
		label = tk.Label(self, text=caption)
		label.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font,widget_text_size)})
		label.grid(column=cl, row=rw)
		spbx = tk.Spinbox(self,
							from_=min,
							to=max)
		spbx.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font, widget_text_size)}
						)
		spbx.grid(column=(cl+1), row=rw)
		return spbx
		
	def drop_down(self,caption,items,rw,cl,width_):
			# n = tk.StringVar()
			# monthchoosen = ttk.Combobox(self, width = 27, 
								# textvariable = n)
		label = tk.Label(self, text=caption)
		label.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font,widget_text_size)})
		label.grid(column=cl, row=rw)
		combo = ttk.Combobox(self, width = width_)
		combo.grid(column=(cl+1), row=rw)
		combo['values'] = items
		#combo.set(items[0])
		return combo

	def message(self,txt,rw,cl):
		msg = tk.Message(self, text=txt)
		msg.configure({"background": widget_background,
						"foreground": widget_foreground,
						"font":(widget_font,widget_text_size)})
		msg.grid(column=cl, row=rw)
		return msg

