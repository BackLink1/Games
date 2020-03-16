from tkinter import * 
import time
root =Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root,bg='blue')
canv.pack(fill=BOTH,expand =1)

def click(event):
	global ay 
	ay = -10
	ax = 0
canv.bind('<Left>',click) 
x =40 
y =45
r =20  #radius
jumper=canv.create_oval(x-r,y-r,x+r,y+r)# krug
ax =6#Speed
ay= 0
while 1:
	ay += 0.5
	y += ay
	x += ax
	ax *= 0.99
	if y > 550:
		ay *= -0.7
		ax *= 0.8
		y=550 
	canv.coords(jumper,x-r,y-r,x+r,y+r)
	canv.update()
	time.sleep(0.03)
	




#mainloop()

