from tkinter import * 
import time
root =Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand =1)
x=40
y=450
r=20
jumper=canv.create_oval(x-r,y-r,x+r,y+r)# krug
for i in range(5):
	x+=10
	canv.coords(jumper,x-r,y-r,x+r,y+r)
	canv.update()
	time.sleep(0.3)




mainloop()

