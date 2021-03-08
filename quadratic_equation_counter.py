"""
Simple but complex calculator for quadratic equations with Tkinter
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Quadratic equation')
root.geometry('300x145')
root.attributes('-topmost', True)
root.resizable(False, False)


aLabel = ttk.Label(root, text='a:')
bLabel = ttk.Label(root, text='b:')
cLabel = ttk.Label(root, text='c:')

aLabel.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))
bLabel.grid(row=1, column=0, padx=(10, 5), pady=5)
cLabel.grid(row=2, column=0, padx=(10, 5), pady=5)


aEntry = ttk.Entry(root, width=10)
bEntry = ttk.Entry(root, width=10)
cEntry = ttk.Entry(root, width=10)

aEntry.grid(row=0, column=1, padx=5, pady=(10, 5))
bEntry.grid(row=1, column=1, padx=5, pady=5)
cEntry.grid(row=2, column=1, padx=5, pady=5)

resultLabel = tk.Label(root, text='Result:', justify='center', font=('TkDeafultFont', 10))
resultLabel.place(x=110, y=10, width=180)

def count():
    
	try:
		a = int(aEntry.get())
		b = int(bEntry.get())
		c = int(cEntry.get())

		x1 = round(((-b)+((b**2-4*a*c))**0.5)/(2*a), 10)
		x2 = round(((-b)-((b**2-4*a*c))**0.5)/(2*a), 10)

		resultLabel.config(text=f'Result:\n\n x1  =  {x1} \n\n x2  =  {x2}')

	except ValueError:

		resultLabel.config(text='Error:\n\nValueError')

	except TypeError:

		resultLabel.config(text='Error:\n\nTypeError')

resultButton = ttk.Button(root, text='Count!', command=count)
resultButton.place(x=10, y=110, width=280)


root.mainloop()
