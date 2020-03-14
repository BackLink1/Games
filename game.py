from tkinter import * 

root =Tk()
root.geometry('800x600')
canv = Canvas(root,bg='green')
canv.pack(fill=BOTH,expand =1)
x=40
y=450
r=20
jumper=canv.create_oval(x-r,y-r,x+r,y+r)# krug
mainloop()