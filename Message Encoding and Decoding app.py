from tkinter import *
import base64
from tkinter import messagebox
root = Tk()

root.geometry("600x300")

root.title(" Message Encryption and Decryption")


Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

label = Label(root, text='Enter Message', font=('Helvetica',10))
label.place(x=10,y=0)

mes = Entry(root,textvariable=Msg, font=('calibre',10,'normal'))
mes.place(x=200,y=0)

label1 = Label(root, text='e for encrypt and d for decrypt', font=('Helvetica',10))
label1.place(x=10,y=50)

l_mode = Entry(root, textvariable=mode, font=('calibre',10,'normal'))
l_mode.place(x=200,y=50)

label2 = Label(root, text='Enter key', font=('Helvetica',10))
label2.place(x=10,y=100)

l_key = Entry(root, textvariable=key, font=('calibre',10,'normal'))
l_key.place(x=200,y=100)

label3 = Label(root, text='Result', font=('Helvetica',10))
label3.place(x=10,y=150)

res = Entry(root,textvariable=Result, font=('calibre',10,'normal'))
res.place(x=200,y=150)


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()
    m.lower()
    if (m == 'e'):
        Result.set(encode(k, msg))
    elif(m== 'd'):
        Result.set(decode(k, msg))
    else:
        messagebox.showinfo('Shantanu', 'Wrong mode entered. Try again.')



def qExit():
    root.destroy()



def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


btnshow = Button(root, text='Show Message', foreground='green', command=Results)
btnshow.place(x=10,y=200)

btnreset = Button(root, text='Reset', foreground='red', command=Reset)
btnshow.place(x=150,y=200)

btnexit = Button(root, text='Exit', foreground='black', command=qExit)
btnshow.place(x=300,y=200)


root.mainloop()
