import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox

def togli_sfondo(img):
    img = img.convert("RGBA")
    larghezza, altezza = img.size
    for punto in [(0, 0), (larghezza - 1, 0), (0, altezza - 1), (larghezza - 1, altezza - 1)]:
        ImageDraw.floodfill(img, punto, (0, 0, 0, 0), thresh=40)
    return img

root = tk.Tk()
root.title("GothParadise Shop")
root.geometry("600x950")
root.configure(bg="#280137")
root.state("zoomed")

root.state("zoomed")
root.update()
larghezza = root.winfo_width()
altezza = root.winfo_height()

img = Image.open("images/bt.png").convert("RGBA").resize((larghezza, altezza), Image.NEAREST)
foto_cornice = ImageTk.PhotoImage(img)
sfondo = tk.Label(root, image=foto_cornice, bg="#280137")
sfondo.place(x=0, y=0)
sfondo.lower()

products = [
{"name" : "Raven", "desc" : "Black lace corset, ruffled skirt and cross necklace", "price" : 89.99, "image" : "images/raven.jpg"},
{"name" : "Nyx", "desc" : "Leather skirt, fishnet tights, platform boots and studs", "price" : 95.99, "image" : "images/nyx.jpg"},
{"name" : "Lenore", "desc" : "Black Victorian jacket, jabot shirt and ankle boots", "price" : 110.00, "image" : "images/lenore.jpg"}
]

tk.Label(root, text=f"WELCOME TO GOTHPARADISE ONLINE SHOP!", wraplength=300, font=("Arial", 12, "bold"), fg="#280137" ,bg="#A095BF").pack(pady=10)


totale = 0
etichetta_totale = tk.Label(root, text="Your total is $0.00", font=("Arial", 12, "bold"), bg="#280137", fg="#A095BF")
etichetta_totale.pack(pady=10)

def aggiungi(prezzo):
    global totale
    totale += prezzo
    etichetta_totale.config(text=f"Your total is: ${totale: .2f}")

for p in products:
    card = tk.Frame(root, bg="#A095BF")
    card.pack(pady=10)

    img = Image.open(p["image"]).resize((120, 160))
    img = togli_sfondo(img)
    foto = ImageTk.PhotoImage(img)
    etichetta_foto = tk.Label(card, image=foto, bg="#A095BF")
    etichetta_foto.image = foto
    etichetta_foto.pack(side="left", padx=10)

    tk.Label(card, text=p["name"], wraplength=300, font=("Arial", 12, "bold"), bg="#A095BF").pack()
    tk.Label(card, text=p["desc"], wraplength=300, font=("Arial", 12, "bold"), bg="#A095BF").pack()
    tk.Label(card, text=f"${p['price']:.2f}", font=("Arial", 12, "bold"), bg="#A095BF").pack()
    tk.Button(card, text="Add to cart", wraplength=300, font=("Arial", 12, "bold"), bg="black", fg="#A095BF",
              command=lambda prezzo=p["price"]: aggiungi(prezzo)).pack(pady=5)

def apri_checkout():
    finestra = tk.Toplevel(root)
    finestra.state("zoomed")
    finestra.title("Checkout")
    finestra.geometry("600x950")
    finestra.configure(bg="#280137")
    finestra.update()
    centro = tk.Frame(finestra, bg="#280137")
    centro.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(centro, text="Enter your email address:", font=("Arial", 20, "bold"), fg="#280137" ,bg="#A095BF").pack(pady=10)
    entry_email = tk.Entry(centro, width=30, font=("Arial", 30, "bold"))
    entry_email.pack(pady=20)
    tk.Label(finestra,text="© 2026 GothParadise. All rights reserved.\n" "This is a fictional shop created for educational purposes.\n" "No real products are sold and no payments are processed.\n" "Characters and artwork belong to their respective creators.", font=("Arial", 8), fg="#A095BF",bg="#280137", justify="center").pack(side="bottom", pady=10)

    larg = finestra.winfo_width()
    alt = finestra.winfo_height()
    larg = finestra.winfo_width()
    alt = finestra.winfo_height()
    img = Image.open("images/bt.png").convert("RGBA").resize((larg, alt), Image.NEAREST)
    foto_cornice = ImageTk.PhotoImage(img)
    sfondo = tk.Label(finestra, image=foto_cornice, bg="#280137")
    sfondo.image = foto_cornice
    sfondo.place(x=0, y=0)
    sfondo.lower()

    def conferma():
        email = entry_email.get()
        if email == "":
            messagebox.showwarning("Attention", "Please enter your email")
            return

        messagebox.showinfo("Thank you for buying on GothParadise", "Your order has been confirmed ^^")
        root.destroy()

    tk.Button(centro, text="Confirm order", font=("Arial", 20, "italic"), command=conferma).pack(pady=10)
tk.Button(root, text="Checkout", wraplength=300, font=("Arial", 10, "italic"), bg="#A095BF", command=apri_checkout).pack(pady=10)

tk.Label(root, text="© 2026 GothParadise. All rights reserved.\n" "This is a fictional shop created for educational purposes.\n" "No real products are sold and no payments are processed.\n"
"Characters and artwork belong to their respective creators.", font=("Arial", 8), fg="#A095BF", bg="#280137", justify="center").pack(side="bottom", pady=10)

root.mainloop()
