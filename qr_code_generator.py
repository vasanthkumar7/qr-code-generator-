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




