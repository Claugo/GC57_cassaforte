import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os
from tkinter import messagebox
import customtkinter as tkc
from tkinter import messagebox

# from datetime import datetime
import time
import locale
from tkinter import simpledialog
from math import gcd
from sympy import nextprime
import hashlib
from random import randint, seed

T = int(time.time())
seed(T)

locale.setlocale(locale.LC_TIME, "it_IT")

# ****************************************************
# * Controlla se ci sono le cartelle di cui ha bisogno
# ****************************************************
cartella1 = "f:\\DCP"
cartella2 = "f:\\DCP/DCP_drop"
if os.path.exists(cartella1):
    pass
else:
    os.makedirs(cartella1)

if os.path.exists(cartella2):
    pass
else:
    os.makedirs(cartella2)

# ****************************************************
# **            Password
# ****************************************************


def hash_password(password):
    # Genera un salt casuale per aggiungere casualità all'hashing
    salt = os.urandom(32)

    # Combina la password con il salt e calcola l'hash
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )

    # Combina il salt e l'hash in un unico valore da memorizzare nel database
    hashed_password_hex = salt.hex() + hashed_password.hex()

    return hashed_password_hex


def verify_password(input_password, stored_password):
    # Estrae il salt dal valore memorizzato
    salt = bytes.fromhex(stored_password[:64])

    # Calcola l'hash della password di input con lo stesso salt
    hashed_input_password = hashlib.pbkdf2_hmac(
        "sha256", input_password.encode("utf-8"), salt, 100000
    )

    # Confronta il salt e l'hash con il valore memorizzato
    return stored_password[64:] == hashed_input_password.hex()


def get_password_from_user():
    password = simpledialog.askstring("Password", "Inserisci la password:", show="*")
    return password


# Esempio di utilizzo
password = "Dicembre2023"
hashed_password = hash_password(password)

# Verifica della password
input_password = get_password_from_user()

if verify_password(input_password, hashed_password):
    pass
else:
    messagebox.showerror("Errore", "La password inserita è errata.")
    quit()

apri_dati = simpledialog.askstring("USB", "Inserisci la porta USB se diversa da D")
if not apri_dati:
    apri_dati = "d"

# ****************************************************
# **  Cerca nella USB i dati di criptazione GC57
# ****************************************************

file_path = os.path.join(apri_dati + ":", "dati_cassaforte_crp.txt")

try:
    with open(file_path, "r") as leggif:
        leggi1 = leggif.readline().strip()
        leggi2 = leggif.readline().strip()
        leggi3 = leggif.readline().strip()
        leggi4 = leggif.readline().strip()
        leggi5 = leggif.readline().strip()
        leggi6 = leggif.readline().strip()
        leggi7 = leggif.readline().strip()
        m1 = int(leggif.readline())
        m2 = int(leggif.readline())
        m3 = int(leggif.readline())
        m4 = int(leggif.readline())
        m5 = int(leggif.readline())
except FileNotFoundError:
    messagebox.showerror("Errore", "Dati su USB non trovati")
    quit()

# ****************************************************
# ** Vede se c'è il file criptato delle chiavi per decriptarlo
# ****************************************************

path = cartella2 + "/database_chiavi.cr"
if os.path.exists(path):
    leggi = open(path, "r")
    n_semiprimo = leggi.readline()
    testo_criptato = leggi.readline()
    leggi.close()
    n_semiprimo = n_semiprimo.strip()

    testo_criptato = testo_criptato.strip()
    chiave = int(leggi1) ** int(leggi2)
    n_semiprimo = int(n_semiprimo)
    a = n_semiprimo % chiave
    b = n_semiprimo - a
    for i in range(10):
        r = gcd(b, a)
        if r != 1:
            break
        a = a + chiave
        b = b - chiave
    if r == 1:
        messagebox.showerror("Attenzione", "Chiave GC57 errata")
        quit()
    start1 = str(r)
    start2 = len(start1)
    start = int(start1[start2 - 5] + start1[start2 - 4])
    ln = list(str(r))
    if len(ln) % 2 == 0:
        pass
    else:
        ln.append("0")

    divln = []
    for i in range(0, len(ln), 2):
        c1 = int(ln[i])
        c2 = int(ln[i + 1])
        c3 = c1 * 10 + c2
        divln.append(c3)

    te = []
    d0 = list(testo_criptato)
    for i in range(0, len(d0), 3):
        d1 = d0[i]
        d2 = d0[i + 1]
        d3 = d0[i + 2]
        te.append(d1 + d2 + d3)
    cont = start
    tdecript = ""
    for i in range(len(te)):
        if cont >= len(divln):
            cont = 0
        x = int(divln[cont])
        if x >= 0 and x < 25:
            y = int(te[i])
            tdecript = tdecript + (chr(y - x - m1))
        if x >= 25 and x < 40:
            y = int(te[i])
            tdecript = tdecript + (chr(y - x - m2))
        if x >= 40 and x < 50:
            y = int(te[i])
            tdecript = tdecript + (chr(y - x - m3))
        if x >= 50 and x < 75:
            y = int(te[i])
            tdecript = tdecript + (chr(y - x - m4))
        if x >= 75 and x < 100:
            y = int(te[i])
            tdecript = tdecript + (chr(y - x - m5))
        cont = cont + 1
    path = cartella1 + "/database_chiavi.txt"
    scrivi = open(path, "w")
    scrivi.write(str(tdecript) + "\n")
    scrivi.close()
else:
    risposta = messagebox.askquestion(
        "Attenzione",
        "Il database_chiavi è stato rimosso\no non ancora creato\nsi vuole proseguire",
    )
    if risposta == "yes":
        pass
    else:
        quit()

# ****************************************************
# ** Esce dal programma e cripta il database delle chiavi fernet
# ****************************************************


def esci():
    if lmodifica.cget("text") == "O":
        scegli = messagebox.askquestion(
            "Uscita Programma",
            "Il database chiavi non è stato modificato\nVuoi Cancellare tutti i file decriptati?",
        )
        if scegli == "yes":
            cartella = cartella1
            for elemento in os.listdir(cartella):
                percorso_elemento = os.path.join(cartella, elemento)

                if os.path.isfile(percorso_elemento):
                    os.remove(percorso_elemento)
            window.destroy()
            quit()
        else:
            cancella = cartella1 + "/database_chiavi.txt"
            if os.path.exists(cancella):
                os.remove(cancella)
            window.destroy()
            quit()

    messagebox.showinfo(
        "Uscita Programma",
        "Lasciare che il programma esegua la criptazione delle chiavi",
    )
    path = cartella1 + "/database_chiavi.txt"
    testo = ""
    apri = open(path, "r")
    for i in range(10000):
        te = apri.readline()
        if te == "\n" or te == "":
            apri.close()
            break
        testo = testo + te
    testo = testo.strip()
    p = int(leggi1) ** int(leggi3)
    q = int(leggi1) ** int(leggi4)
    nd = nextprime(p + randint(1, int(leggi5) * 2 ** int(leggi6)))
    nd2 = nextprime(q + randint(1, int(leggi5) * 2 ** int(leggi6)))
    n = nd * nd2
    # ******************* controllo di fattorizzazione
    chiave = int(leggi1) ** int(leggi2)
    a = n % chiave
    b = n - a
    for i in range(10):
        r = gcd(a, b)
        if r != 1:
            break
        else:
            a = a + chiave
            b = b - chiave
    if r == 1:
        messagebox.showerror("Attenzione", "Test non superato: Riprovare")
        return
    # ******************* fine controllo
    start1 = str(nd)
    start2 = len(start1)
    start = int(start1[start2 - 5] + start1[start2 - 4])
    ln = list(str(nd))
    if len(ln) % 2 == 0:
        pass
    else:
        ln.append("0")
    divln = []
    for i in range(0, len(ln), 2):
        c1 = int(ln[i])
        c2 = int(ln[i + 1])
        c3 = c1 * 10 + c2
        divln.append(c3)

    text = testo
    te = list(text)
    cont = start
    tcript = ""

    for i in range(len(text)):
        if cont >= len(divln):
            cont = 0
        if ord(te[i]) > 700:
            pass
        else:
            x = int(divln[cont])
            if x >= 0 and x < 25:
                x = x + m1 + ord(te[i])
            if x >= 25 and x < 40:
                x = x + m2 + ord(te[i])
            if x >= 40 and x < 50:
                x = x + m3 + ord(te[i])
            if x >= 50 and x < 75:
                x = x + m4 + ord(te[i])
            if x >= 75 and x < 100:
                x = x + m5 + ord(te[i])
            tcript = tcript + str(x)
            cont = cont + 1

    path = cartella2 + "/database_chiavi.cr"
    scrivi = open(path, "w")
    scrivi.write(str(n) + "\n")
    scrivi.write(tcript + "\n")
    scrivi.close()
    messagebox.showinfo("OK", "Database memorizzato con GC57 correttamente")
    path = cartella2 + "/database_chiavi.cr"
    cancella = cartella1 + "/database_chiavi.txt"
    if os.path.exists(path):
        os.remove(cancella)
    else:
        pass

    cartella = cartella1

    elementi_cartella = os.listdir(cartella)

    file_nella_cartella = any(
        os.path.isfile(os.path.join(cartella, elemento))
        for elemento in elementi_cartella
    )

    if file_nella_cartella:
        risposta = messagebox.askquestion(
            "Cartella DCP", "Ci sono dei dati decodificati\nVuoi Eliminarli?"
        )
        if risposta == "yes":
            for elemento in os.listdir(cartella):
                percorso_elemento = os.path.join(cartella, elemento)
                if os.path.isfile(percorso_elemento):
                    os.remove(percorso_elemento)

    window.destroy()


# ****************************************************
# **        Cancella file criptati
# ****************************************************
def cancella_cr():
    initial_dir = cartella2
    filename = filedialog.askopenfilename(
        initialdir=initial_dir,
        filetypes=(("File Criptato", "*.crp"), ("File Criptato", "*.crp")),
    )
    nome_file = os.path.split(filename)
    risposta = messagebox.askquestion("Vuoi cancellare questo file??", nome_file)
    if risposta == "yes":
        pass
    else:
        return
    nome_database = nome_file[1].replace(".crp", "")
    database = []
    trovato = 0
    apri = open(cartella1 + "/database_chiavi.txt", "r")
    for i in range(10000):
        leggi_database = apri.readline()
        if leggi_database == "\n" or leggi_database == "":
            apri.close()
            break
        if nome_database in leggi_database:
            trovato = 1
            pass
        else:
            leggi_database = leggi_database.strip()
            database.append(leggi_database)
    database.append("fine")
    if trovato == 0:
        messagebox.showerror("Cancella file criptato", "Nessun dato trovato")
        return
    lmodifica.configure(text="M")

    apri = open(cartella1 + "/database_chiavi.txt", "w")
    for i in range(10000):
        if database[i] == "fine":
            apri.close()
            break
        apri.write(database[i] + "\n")
    cancella = cartella2 + "/" + nome_file[1]
    os.remove(cancella)
    messagebox.showinfo("Cancella file criptao:", "File cancellato con successo")


# ****************************************************
# **             Generazione codice fernet
# ****************************************************
def generate_key_if_not_exists(key_filename):
    if not os.path.exists(key_filename):
        key = generate_key()
        save_key(key, key_filename)
    else:
        key = load_key(key_filename)
    return key


def generate_key():
    return Fernet.generate_key()


def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)


def load_key(filename):
    return open(filename, "rb").read()


def encrypt_file(key, input_file, output_file):
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(key, input_file, output_file):
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)


def choose_file(entry_widget):
    initial_dir = cartella1
    filename = filedialog.askopenfilename(
        initialdir=initial_dir,
        filetypes=(
            ("Tutti i File", "*.*"),
            ("File di testo", "*.txt"),
            ("File eseguibile", "*.exe"),
            ("File Video", "*.mpeg *.mpg *.mkw *.mp4"),
            ("File Audio", "*.mp3 *.wav *.flac "),
            ("File Immagini", "*.jpg *.jpeg *.jpe *.webp *.ico *.png *.xcf *.bmp"),
            ("File Libreoffice", "*.odt *.ods *.odg *.odf"),
        ),
    )
    nome_file = os.path.split(filename)
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, nome_file[1])


def choose_file2(entry_widget):
    initial_dir = cartella2
    filename = filedialog.askopenfilename(
        initialdir=initial_dir,
        filetypes=(("File Criptato", "*.crp"), ("File Criptato", "*.crp")),
    )
    nome_file = os.path.split(filename)
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, nome_file[1])


# ****************************************************
# **  crea i dati per criptare il file
# ****************************************************


def on_encrypt():
    file_to_encrypt = e1.get()
    if file_to_encrypt == "":
        messagebox.showerror("Errore:", "Nessun file selezionato")
        return
    if file_to_encrypt == "database_chiavi.txt":
        messagebox.showinfo("File criptato come: ", "questo file non si può criptare")
        e1.delete(0, "end")
        return
    output_filename = cartella2 + "/" + file_to_encrypt + ".crp"

    if os.path.exists(output_filename):
        messagebox.showerror(
            "Cripta File:",
            "questo file esiste già e non può essere sostituito\ncancellare prima il file se lo si vuole sostituire",
        )
        return
    lmodifica.configure(text="M")

    nome_file = file_to_encrypt
    file_to_encrypt = cartella1 + "/" + file_to_encrypt
    key = generate_key()

    encrypt_file(key, file_to_encrypt, output_filename)
    # os.remove(file_to_encrypt)
    data = time.strftime("%A:%B:%Y")
    memorizza_key = key.decode("utf-8") + "," + nome_file + "," + str(data)
    apri_file_key = open(cartella1 + "/database_chiavi.txt", "a")
    apri_file_key.write(memorizza_key + "\n")
    apri_file_key.close()
    messagebox.showinfo("File criptato come: ", output_filename)
    e1.delete(0, "end")
    path = output_filename
    cancella = file_to_encrypt
    if os.path.exists(path):
        os.remove(cancella)
    else:
        pass


# ****************************************************
# **  crea i dati per decriptare il file
# ****************************************************


def on_decrypt():
    file_to_decrypt = e2.get()
    if file_to_decrypt == "":
        messagebox.showerror("Errore:", "Nessun file selezionato")
        return
    nome_originale = e2.get().replace(".crp", "")
    apri = open(cartella1 + "/database_chiavi.txt", "r")
    for i in range(1000):
        stringa = apri.readline()
        stringa = stringa.strip()
        if stringa == "\n" or stringa == "":
            messagebox.showinfo("Ricerca Codice:", "Nessun codice Trovato")
            apri.close()
            return
        trovata = nome_originale in stringa
        if trovata == True:
            sp = stringa.split(",")
            chiave = sp[0].encode("utf-8")
            apri.close()
            break

    original_filename = cartella1 + "/" + file_to_decrypt.replace(".crp", "")
    file_to_decrypt = cartella2 + "/" + file_to_decrypt

    decrypt_file(chiave, file_to_decrypt, original_filename)
    e2.delete(0, "end")
    messagebox.showinfo("File decriptato come:", original_filename)


# ****************************************************
# **  Interfaccia principale customtkinter
# ****************************************************

# Modes: system (default), light, dark
tkc.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
tkc.set_default_color_theme("blue")
window = tkc.CTk()  # create CTk window like you do with the Tk window
window.geometry("460x250")
window.title("Cripta/Decripta Metodo Fermat 128bit")
# Creazione degli elementi nella finestra
px = 50
e1 = tkc.CTkEntry(window, width=300, font=("Helvetica", 12), justify=tkc.CENTER)
e1.place(x=px, y=10)
b1 = tkc.CTkButton(
    master=window,
    width=50,
    text="Apri file",
    fg_color="blue",
    hover_color="green",
    command=lambda: choose_file(e1),
)
b1.place(x=px + 320, y=10)
b2 = tkc.CTkButton(
    master=window,
    width=300,
    text="Cripta File",
    fg_color="blue",
    hover_color="green",
    command=on_encrypt,
)
b2.place(x=px, y=40)

py = 100
e2 = tkc.CTkEntry(window, width=300, font=("Helvetica", 12), justify=tkc.CENTER)
e2.place(x=px, y=py)
b3 = tkc.CTkButton(
    master=window,
    width=300,
    text="Decripta file",
    fg_color="blue",
    hover_color="green",
    command=on_decrypt,
)
b3.place(x=px, y=py + 30)
b4 = tkc.CTkButton(
    master=window,
    width=50,
    text="Apri file",
    fg_color="blue",
    hover_color="green",
    command=lambda: choose_file2(e2),
)
b4.place(x=px + 320, y=py)
lmodifica = tkc.CTkLabel(
    master=window, text="O", fg_color="transparent", font=("arial", 12, "bold")
)
lmodifica.place(x=10, y=py + 70)
b5 = tkc.CTkButton(
    master=window,
    width=300,
    text="Elimina un file criptato e aggiorna il Database",
    fg_color="blue",
    hover_color="red",
    command=cancella_cr,
)
b5.place(x=px, y=py + 100)


window.protocol("WM_DELETE_WINDOW", esci)

window.mainloop()
