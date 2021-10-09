import tkinter as tk

def onclick(args):
    if args == 1:
          print("Choice 1")
    if args == 2:
          print("Choice 2")
    if args == 3:
          print("Choise 3")

root = tk.Tk()
root.title("GUI Button")

btn1 = tk.Button(root, text ="choice 1",pady=25,padx=50,command=lambda:onclick(1))
btn2 = tk.Button(root, text ="choice 2",pady=25,padx=50,command=lambda:onclick(2))
btn3 = tk.Button(root, text ="choice 3",pady=25,padx=50,command=lambda:onclick(3))


btn1.pack()
btn2.pack()
btn3.pack()

root.mainloop()