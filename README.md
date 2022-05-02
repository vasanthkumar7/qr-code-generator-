# Introduction

## What is QR code?

QR codes are machine readable two dimensional pixelated barcodes which can be used to store a variety of information. QR in QR code stands for Quick Response.
QR code was invented by a Japanese engineer Masahiro Hara from automobile manufacturer Denso Wave in the year 1994 to track the movement of car parts.
QR Code has increased in popularity in the later 2010s with improvement in optical capabilities of mobile phones and their wide adoption.
Nowadays, QR codes are being used for wide variety of applications like, make online payments, check hotel menu, share wifi password, obtain price and other details of products etc. QR Codes have become so popular that now every new smartphone comes with in built QR code reader.
In this blog we will learn how to create a customizable QR Code generator using python.

# Requirements

Install pil, qrcode modules

```
pip install pillow qrcode
``` 
Pillow module is used for images
Qrcode module is used for generating Qr code


# Code

## Headers


```
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import ImageTk,Image
import qrcode

``` 

Tkinter is used for Graphical user interface 
Pil is used for getting image information
Qrcode is used for generating qrcode

## Setting up tittle of the application


```
root=Tk()
root.title("Customisable QR code generator")

``` 

![Screenshot (215).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1651502990254/leamxAi1c.png )

In This root is gonna act as main window of this application

## Getting Text from user


```
top=Frame(root)
content=Entry(top, font=('calibre',15,'normal'),width=25)
content.grid(row=0,column=0,pady=10,padx=10)
generate=Button(top, text ="generate",font=( 'calibre',15, "bold"),command=generate_qrcode)
generate.grid(row=0,column=1,pady=10)
top.grid(row=0,column=0)
``` 

![Screenshot (216).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1651503097262/I2CsCe9Lo.png)

top is gonna be first frame in this application .
content is where user gonna type the input which is in the top frame.
generate is a button when it gets clicked it will invoke the generate_qrcode function

## Displaying the QR code

```
bottom=Frame(root)
img=Image.open("code.png")
resized=img.resize((400,400),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(resized)
qrcodes=Label(bottom,image=img1)
qrcodes.grid(row=0,column=0,columnspan=3)
bg=Button(bottom,text="Background Color",command=lambda:color_change("bg") )
bg.grid(row=1,column=0,pady=20)
fg=Button(bottom,text="Foreground Color",command=lambda:color_change("fg"))
fg.grid(row=1,column=1,pady=20)
save_=Button(bottom,text="Save",command=save_qrcode)
save_.grid(row=1,column=2,pady=20)
``` 

![Screenshot (217).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1651503323673/TW1NurLHQ.png )

bottom is gonna be second frame in this application 
img gonna open a sample qr code we have 
then img is resized to 400*400 pixles to display it in the application
qrcodes is a image label where qrcode will be displayed

bg is a button which wll invoke color_change("bg") function 
fg is a button which wll invoke color_change("fg") function
save_ is button which will invoke save_qrcode function 

## Functions

```
def generate_qrcode():
    global content,glb_bg,glb_fg,qrcodes,img1
    
    if content.get()=="":
        messagebox.showerror("Customisable QR code generator", "Give some text")
    else:
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
        qr.add_data(content.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color=glb_fg, back_color=glb_bg)
        img.save("code.png")
        
        img=Image.open("code.png")
        resized=img.resize((400,400),Image.ANTIALIAS)
        img1=ImageTk.PhotoImage(resized)
        qrcodes=Label(bottom,image=img1)
        qrcodes.grid(row=0,column=0,columnspan=3)
        

def color_change(what):
    global content,glb_bg,glb_fg,qrcodes,img1
    colors = askcolor(title="Tkinter Color Chooser")
    if what=="bg":
        glb_bg=colors[1]
    else:
        glb_fg=colors[1]
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(content.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color=glb_fg, back_color=glb_bg)
    img.save("code.png")
    img=Image.open("code.png")
    resized=img.resize((400,400),Image.ANTIALIAS)
    img1=ImageTk.PhotoImage(resized)
    qrcodes=Label(bottom,image=img1)
    qrcodes.grid(row=0,column=0,columnspan=3)

def save_qrcode():
    global img
    name=filedialog.asksaveasfile(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),),defaultextension=".png")
    if(name!=None):
        img.save(name.name,quality=200)
        messagebox.showinfo("Customisable QR code generator", "qrcode saved successfully")

``` 

### generate_qrcode function

It will first check whether user as given any input . if content.get() is empty 
it will show a error . Then based on the input given it will generate qr code
and save it as "code.png" and then it will display it in the application

### color_change(what) function

It will change the foreground and background color of the qrcode . ""what""
parameter is used to check whether to change foreground color or background color
"fg" means foreground "bg" means background and then it will display the modified qr code in the application

### save_qrcode function

It will open filedialog box to ask filename to be saved as , then it will show the succesfully saved message

![Screenshot (217).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1651504427791/H3BF5H9Vv.png )


# Final code


```
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageTk,Image
import qrcode

root=Tk()
root.title("Customisable QR code generator")

##global variables
glb_bg="white"
glb_fg="black"

def generate_qrcode():
    global content,glb_bg,glb_fg,qrcodes,img1
    
    if content.get()=="":
        messagebox.showerror("Customisable QR code generator", "Give some text")
    else:
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
        qr.add_data(content.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color=glb_fg, back_color=glb_bg)
        img.save("code.png")
        
        img=Image.open("code.png")
        resized=img.resize((400,400),Image.ANTIALIAS)
        img1=ImageTk.PhotoImage(resized)
        qrcodes=Label(bottom,image=img1)
        qrcodes.grid(row=0,column=0,columnspan=3)
        

def color_change(what):
    global content,glb_bg,glb_fg,qrcodes,img1
    colors = askcolor(title="Tkinter Color Chooser")
    if what=="bg":
        glb_bg=colors[1]
    else:
        glb_fg=colors[1]
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(content.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color=glb_fg, back_color=glb_bg)
    img.save("code.png")
    img=Image.open("code.png")
    resized=img.resize((400,400),Image.ANTIALIAS)
    img1=ImageTk.PhotoImage(resized)
    qrcodes=Label(bottom,image=img1)
    qrcodes.grid(row=0,column=0,columnspan=3)

def save_qrcode():
    global img
    name=filedialog.asksaveasfile(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),),defaultextension=".png")
    if(name!=None):
        img.save(name.name,quality=200)
        messagebox.showinfo("Customisable QR code generator", "qrcode saved successfully")



top=Frame(root)
content=Entry(top, font=('calibre',15,'normal'),width=25)
content.grid(row=0,column=0,pady=10,padx=10)
generate=Button(top, text ="generate",font=( 'calibre',15, "bold"),command=generate_qrcode)
generate.grid(row=0,column=1,pady=10)
top.grid(row=0,column=0)



bottom=Frame(root)
img=Image.open("code.png")
resized=img.resize((400,400),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(resized)
qrcodes=Label(bottom,image=img1)
qrcodes.grid(row=0,column=0,columnspan=3)

bg=Button(bottom,text="Background Color",command=lambda:color_change("bg") )
bg.grid(row=1,column=0,pady=20)

fg=Button(bottom,text="Foreground Color",command=lambda:color_change("fg"))
fg.grid(row=1,column=1,pady=20)

save_=Button(bottom,text="Save",command=save_qrcode)
save_.grid(row=1,column=2,pady=20)

bottom.grid(row=1,column=0)
root.mainloop()


``` 


![image](https://cdn.hashnode.com/res/hashnode/image/upload/v1651504668297/4KmwsdW2Q.png )

