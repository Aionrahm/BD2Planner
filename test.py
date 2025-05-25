from tkinter import *

root = Tk()

buttonA0 = Button(root, width = 50, text = 'Hi')
buttonB0 = Button(root, text = 'Bye')
buttonC0 = Button(root, text = 'Option 0')
buttonC1 = Button(root, text = 'Option 1')
buttonC2 = Button(root, text = 'Option 2')
buttonC3 = Button(root, text = 'Option 3')
buttonC4 = Button(root, text = 'Option 4')

buttonA0.grid(column = 0, row = 0, rowspan = 5, sticky = NE+SW)
buttonB0.grid(column = 0, row = 5, columnspan = 2, sticky = E+W)
buttonC0.grid(column = 1, row = 0)
buttonC1.grid(column = 1, row = 1)
buttonC2.grid(column = 1, row = 2)
buttonC3.grid(column = 1, row = 3)
buttonC4.grid(column = 1, row = 4)

root.mainloop()