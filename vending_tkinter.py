# Sebelum menjalankan program, harap ketik line berikut di terminal Anda:
# pip install -r requirements.txt

from tkinter import *
from playsound import playsound
from PIL import ImageTk,Image

root=Tk()
root.title("7 Vending Machine")
root.geometry("900x900")
root["bg"] = "white"
root.iconbitmap('DrinksPic')

# Membuat widget display label utama
label =Label(root, text = "Welcome to 7\'s Vending Machine!\n Masukkan Kode Minuman yang Ingin Anda beli!", font = "garamond", fg="white", bg = "Black", borderwidth = 2)

label.pack()
#  Membuat widget display label mengambil barang
take_label = Label(root, text = "↓↓ Ambil Minuman Anda di Bawah ↓↓", font= "cambria, 10", bg="gray", fg="white")
take_label.place(x = 660, y= 570)

# Membuat Fungsi memainkan suara
def playbeep():
    playsound('beep3.wav')

# Membuat widget utama, sebagai wadah input
e = Entry(root, width = 20, fg ="white", bg = "black", font= ("cambria","10"),borderwidth = 2)
e.place(x=700, y=250)

# Membuat fungsi klik
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    box["image"] = ""
    border_color["background"] = ""
    box.pack(padx=0, pady= 0)

# Membuat fungsi menghapus/mengosongkan entry input
def button_clear():
    e.delete(0, END)

border_color = Frame(root )
border_color.place(x= 700, y = 600)

box = Label(border_color, bd=0, bg="white")
box.pack(padx= 1, pady= 1)       

# Membuat fungsi Konfirmasi 

def button_confirm():
    answer = e.get()
    global barang
    if answer in ("1"):
        label["text"] = "Baik, Aqua akan Mengenakan Anda Biaya Sebesar Rp10.000"
        barang = "Aqua"
        label1["bg"] = "green"
        label1["fg"] = "white"
        e.delete(0,END)
    elif answer in ("2"):
        label["text"] = "Baik, Pocari akan Mengenakan Anda Biaya Sebesar Rp15.000"
        barang = "Pocari"
        label2["bg"] = "green"
        label2["fg"] = "white"
        e.delete(0,END)
    elif answer in ("3"):
        label["text"] = "Baik, Teh Pucuk akan Mengenakan Anda Biaya Sebesar Rp10.000"
        barang = "Teh"
        label3["bg"] = "green"
        label3["fg"] = "white"
        e.delete(0,END)
    elif answer in ("4"):
        label["text"] = "Baik, Yogurt akan Mengenakan Anda Biaya Sebesar Rp15.000"
        barang = "Yogurt"
        label4["bg"] = "green"
        label4["fg"] = "white"
        e.delete(0,END)
    elif answer in ("5"):
        label["text"] = "Baik, Sprite akan Mengenakan Anda Biaya Sebesar Rp10.000"
        barang = "Sprite"
        label5["bg"] = "green"
        label5["fg"] = "white"
        e.delete(0,END)
    elif answer in ("6") :
        label["text"] = "Baik, Fanta akan Mengenakan Anda Biaya Sebesar Rp10.000"
        barang = "Fanta"
        label6["bg"] = "green"
        label6["fg"] = "white"
        e.delete(0,END)
    elif answer in ("7"):
        label["text"] = "Baik, Coca-cola akan Mengenakan Anda Biaya Sebesar Rp10.000"
        barang = "Coca"
        label7["bg"] = "green"
        label7["fg"] = "white"
        e.delete(0,END)
    elif answer in ("8"):
        label["text"] = "Baik, Milo akan Mengenakan Anda Biaya Sebesar Rp20.000"
        barang = "Milo"
        label8["bg"] = "green"
        label8["fg"] = "white"
        e.delete(0,END)
    elif answer in ("9"):
        label["text"] = "Baik, Starbucks akan Mengenakan Anda Biaya Sebesar Rp30.000"
        barang = "Starbucks"
        label9["bg"] = "green"
        label9["fg"] = "white"
        e.delete(0,END)
    else:
        label["text"] = "ERROR : Harap Masukkan Nomor Kode yang Valid"
        e.delete(0,END)
        
# Proses display image ke tkinter    
aqua_img = Image.open('aqua.png')
coca_img = Image.open('coca.png')
fanta_img = Image.open('fanta.png')
milo_img = Image.open('milo.png')
pocari_img = Image.open('pocari.png')
pucuk_img = Image.open('pucuk.png')
sprite_img = Image.open('sprite.png')
starbucks_img = Image.open('starbucks.png')
yogurt_img = Image.open('yoghurt.png')

resized_aqua = aqua_img.resize((150,160), Image.ANTIALIAS) 
new_aqua = ImageTk.PhotoImage(resized_aqua)
resized_coca = coca_img.resize((150,160), Image.ANTIALIAS)
new_coca = ImageTk.PhotoImage(resized_coca)
resized_fanta = fanta_img.resize((85,140), Image.ANTIALIAS)
new_fanta = ImageTk.PhotoImage(resized_fanta)
resized_milo = milo_img.resize((90,160), Image.ANTIALIAS)
new_milo = ImageTk.PhotoImage(resized_milo)
resized_pocari = pocari_img.resize((150,160), Image.ANTIALIAS)
new_pocari = ImageTk.PhotoImage(resized_pocari)
resized_pucuk = pucuk_img.resize((140,160), Image.ANTIALIAS)
new_pucuk = ImageTk.PhotoImage(resized_pucuk)
resized_sprite = sprite_img.resize((150,160), Image.ANTIALIAS)
new_sprite = ImageTk.PhotoImage(resized_sprite)
resized_starbucks = starbucks_img.resize((150,160), Image.ANTIALIAS)
new_starbucks = ImageTk.PhotoImage(resized_starbucks)
resized_yogurt = yogurt_img.resize((180,160), Image.ANTIALIAS)
new_yogurt = ImageTk.PhotoImage(resized_yogurt)


aqua_label = Label(image=new_aqua)
coca_label = Label(image=new_coca)
fanta_label = Label(image=new_fanta)
milo_label = Label(image=new_milo)
pocari_label = Label(image=new_pocari)
pucuk_label = Label(image=new_pucuk)
sprite_label = Label(image=new_sprite)
starbucks_label = Label(image=new_starbucks)
yogurt_label = Label(image=new_yogurt)


aqua_label.place(x = 100, y = 125)
pocari_label.place(x = 302, y = 125)
pucuk_label.place(x = 503, y = 125)

yogurt_label.place(x = 83, y = 375)
sprite_label.place(x = 299,y = 375)
fanta_label.place(x = 529, y = 385)

coca_label.place(x = 100, y = 625)
milo_label.place(x = 329, y = 625)
starbucks_label.place(x=498, y = 623)


# Membuat Fungsi Pembayaran 
        
def button_payment():
    price = e.get() 
    if price in "10000" and barang == "Aqua":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Aqua Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli "
        playsound('vending2.wav')
        label1["bg"] = "white"
        label1["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 695, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_aqua
               
    elif price in "15000" and barang == "Pocari" :
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Pocari Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label2["bg"] = "white"
        label2["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 695, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_pocari
    elif price in "10000" and barang == "Teh":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Teh Pucuk Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label3["bg"] = "white"
        label3["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 705, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_pucuk
    elif price in "15000" and barang == "Yogurt":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Yogurt Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label4["bg"] = "white"
        label4["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 689, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_yogurt
    elif price in "10000" and barang == "Sprite":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Sprite Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label5["bg"] = "white"
        label5["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 700, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_sprite
    elif price in "10000" and barang == "Fanta":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Fanta Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label6["bg"] = "white"
        label6["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 730, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_fanta
    elif price in "10000" and barang == "Coca":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Coca-cola Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label7["bg"] = "white"
        label7["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 700, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_coca
    elif price in "20000" and barang == "Milo":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Milo Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label8["bg"] = "white"
        label8["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 720, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_milo
    elif price in "30000" and barang == "Starbucks":
        label["text"] = "Terima Kasih atas Pembeliannya, berikut Starbucks Anda\nJika Ingin Melakukan Pembayaran yang Lain, Tekan Kode Minuman yang Anda ingin Beli"
        playsound('vending2.wav')
        label9["bg"] = "white"
        label9["fg"] = "black"
        e.delete(0,END)
        border_color["background"] = "gray"
        border_color.place(x= 690, y = 675)
        box.pack(padx= 1, pady= 1)   
        box["image"] = new_starbucks


# Defining Kode
label1 = Label(root, text = "1", bg ="white", font = "cambria")
label1.place(x = 170, y = 100)
label2 = Label(root, text = "2", bg ="white", font = "cambria")
label2.place(x = 373, y = 100)
label3 = Label(root, text = "3", bg ="white", font = "cambria")
label3.place(x = 570, y = 100)

label4 = Label(root, text = "4", bg ="white", font = "cambria")
label4.place(x = 170, y = 335)
label5 = Label(root, text = "5", bg ="white", font = "cambria")
label5.place(x = 373, y = 335)
label6 = Label(root, text = "6", bg ="white", font = "cambria")
label6.place(x = 570, y = 335)

label7 = Label(root, text = "7", bg ="white", font = "cambria")
label7.place(x = 170, y = 580)
label8 = Label(root, text = "8", bg ="white", font = "cambria")
label8.place(x = 373, y = 580)
label9 = Label(root, text = "9", bg ="white", font = "cambria")
label9.place(x = 570, y = 580)


# Defining Buttons
button1=Button(root, text="1", width=5, bg = "dark blue" , fg= "white" ,command= lambda: [button_click(1), playbeep()])
button1.place(x=700, y=300)

button2=Button(root, text="2", width=5, bg = "dark blue" , fg= "white" ,command= lambda: [button_click(2), playbeep()])
button2.place(x=750, y =300)

button3=Button(root, text="3", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(3), playbeep()])
button3.place(x=800, y=300)

button4=Button(root, text="4", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(4), playbeep()])
button4.place(x=700, y=350)

button5=Button(root, text="5", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(5), playbeep()])
button5.place(x=750, y=350)

button6=Button(root, text="6", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(6), playbeep()])
button6.place(x=800, y=350)

button7=Button(root, text="7", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(7), playbeep()])
button7.place(x=700, y=400)

button8=Button(root, text="8", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(8), playbeep()])
button8.place(x=750, y=400)

button9=Button(root, text="9", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(9), playbeep()])
button9.place(x=800, y=400)

button0=Button(root, text="0", width=5,bg = "dark blue" , fg= "white" ,command= lambda: [button_click(0), playbeep()])
button0.place(x=700, y=450)

buttonE=Button(root, text="E", width=5, bg= "red", fg="black", command= button_clear)
buttonE.place(x=750, y=450)

buttonC=Button(root, text="✓", bg= "cyan", fg="black", width=5, command = button_confirm)
buttonC.place(x=800, y=450)

buttonP=Button(root, text="Pay", font = "cambria", bg= "green", fg = "black", width =15, borderwidth =2, command = button_payment )
buttonP.place(x = 700, y =500)



root.mainloop()