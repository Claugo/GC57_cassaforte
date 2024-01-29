# chat criptata Dicembre 2023
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.widgets import Button
from ttkbootstrap.constants import *
from tkinter import messagebox
import socket
import threading
from sympy import nextprime
from math import gcd, log
from random import randint, seed
import time

# ******************************************************
# Invia i dati criptati a un computer in rete
# ******************************************************


def manda_tw1():
    message = tw3.get("1.0", tk.END)
    codice = e1.get()
    tw3.delete("1.0", END)
    if message == "" or codice == "":
        messagebox.showerror("Attenzione", "Nessun testo")
        return
    messaggio1 = str(message)
    messaggio2 = str(codice)
    # porta_destinatario = porta_ue

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((indirizzo_ip, porta_ue))

        # Invia la lunghezza del primo messaggio seguita dal messaggio stesso
        s.sendall(len(messaggio1).to_bytes(4, "big"))
        s.sendall(messaggio1.encode())

        # Invia la lunghezza del secondo messaggio seguita dal messaggio stesso
        s.sendall(len(messaggio2).to_bytes(4, "big"))
        s.sendall(messaggio2.encode())


# ******************************************************
# Riceve i dati criptati da un computer in rete
# ******************************************************


def ricevi():
    indirizzo_locale = "0.0.0.0"  # Accetta connessioni da qualsiasi interfaccia di rete
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((indirizzo_locale, porta_ue))
        s.listen()

        while True:
            conn, addr = s.accept()
            with conn:
                # Ricevi il primo messaggio
                lunghezza_messaggio1 = int.from_bytes(conn.recv(4), "big")
                messaggio1_criptato = conn.recv(lunghezza_messaggio1)
                #    print("Primo messaggio:", messaggio1_criptato.decode())

                # Ricevi il secondo messaggio
                lunghezza_messaggio2 = int.from_bytes(conn.recv(4), "big")
                messaggio2_criptato = conn.recv(lunghezza_messaggio2)
                #    print('Secondo messaggio:', messaggio2_criptato.decode())

                # Ora puoi fare qualcosa con il messaggio, ad esempio aggiungerlo a tw2
                tw2.insert("1.0", messaggio1_criptato)
                e1.delete(0, END)
                e1.insert(0, messaggio2_criptato)


def start_ricevi():
    ricevi_thread = threading.Thread(target=ricevi)
    ricevi_thread.daemon = True
    ricevi_thread.start()


# ******************************************************
# Decodifica i dati ricevuti
# ******************************************************


def decodifica():
    f = tw2.get("1.0", END)
    f1 = f.strip()
    if f1 == "":
        messagebox.showerror("Attenzione", "Testo assente\no codice non creato")
        return
    tw2.delete("1.0", END)
    chiave = base_codice**chiave_codice
    nn = e1.get()
    n = int(nn)
    a = n % chiave
    b = n - a
    for i in range(1000):
        r = gcd(a, b)
        if r != 1:
            codice_creato = r
            break
        a = a + chiave
        b = b - chiave
    if r == 1:
        messagebox.showerror("Attenzione", "Codice non trovato: Abortire")
        return

    start1 = str(codice_creato)
    start2 = len(start1)
    start = int(start1[start2 - 5] + start1[start2 - 4])

    ln = list(str(codice_creato))
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

    # **********************************************
    m1 = 101
    m2 = 213
    m3 = 157
    m4 = 255
    m5 = 341
    # **********************************************
    te = []
    d0 = list(f1)
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
    tw4.delete("1.0", END)
    tw4.insert("1.0", str(tdecript))


# ******************************************************
# Codifica i dati scritti
# ******************************************************


def codifica():
    f1 = tw1.get("1.0", tk.END)
    message = f1.strip()
    if message == "":
        messagebox.showerror("Attenzione", "Nessun testo")
        return
    T = int(time.time())
    seed(T)
    p = base_codice**es1_codice
    q = base_codice**es2_codice
    nd = nextprime(p + randint(1, 2**campo_codice))
    nd2 = nextprime(q + randint(1, 2**campo_codice))
    n = nd * nd2
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

    # **********************************************
    m1 = 101
    m2 = 213
    m3 = 157
    m4 = 255
    m5 = 341
    # **********************************************

    text = message
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
    tw3.delete("1.0", END)
    tw3.insert("1.0", str(tcript))
    e1.delete(0, END)
    e1.insert(0, str(n))


# ******************************************************
# Pulizia delle quattro finestre di dialogo
# ******************************************************


def puliscitw1():
    tw1.delete("1.0", END)


def puliscitw4():
    tw4.delete("1.0", END)


# ******************************************************
# Trasforma numero in un primo
# ******************************************************


def trasforma_primo(entry):
    var2 = entry.get()
    if var2 == "":
        messagebox.showerror("Attenzione", "Nessun numero trovato")
        return
    if var2.isnumeric() == False:
        messagebox.showerror("Attenzione", "Non possono esserci lettere")
        return
    var2 = int(var2)
    var = nextprime(var2)
    entry.delete(0, END)
    entry.insert(0, str(var))


# ******************************************************
# Crea un nuovo codice
# ******************************************************


def crea_codice_nuovo(
    entry1,
    entry2,
    entry3,
    entry4,
    entry5,
    entry6,
    entry7,
    entry8,
    entry9,
    entry10,
    entry11,
):
    var2 = entry1.get()
    var3 = entry2.get()
    if var2 == "" or var3 == "":
        messagebox.showerror("Attenzione", "Nessun numero trovato")
        return
    if var3.isnumeric() == False or var2.isnumeric() == False:
        messagebox.showerror("Attenzione", "Non possono esserci lettere")
        return
    var3 = int(var3)
    var2 = int(var2)
    bit = 2**var3
    esponente = int(log(bit, var2)) + 1
    entry9.delete(0, END)
    entry9.insert(0, str(esponente))
    var = var2**esponente
    bit = int(log(var, 2)) + 1
    entry8.delete(0, END)
    entry8.insert(0, str(bit))

    var4 = entry3.get()
    var5 = entry4.get()
    var6 = entry5.get()
    var7 = entry6.get()
    var8 = entry7.get()
    if var4 == "" or var8 == "":
        messagebox.showerror("Attenzione", "Manca IP e Porta")
        return
    es = esponente // 2
    ee1 = es - 5
    ee2 = es + 5
    if ee1 + ee2 == esponente:
        pass
    else:
        ee2 = ee2 + 1
    chiave = var2**es
    analizzo = 450
    trovato = 0
    for i in range(25):
        p = nextprime(var2**ee1 + randint(1, 2**analizzo))
        q = nextprime(var2**ee2 + randint(1, 2**analizzo))
        n = p * q
        a = n % chiave
        b = n - a
        for ii in range(10):
            r = gcd(a, b)
            if r != 1:
                trovato = 1
                break
            a = a + chiave
            b = b - chiave
        if trovato == 1:
            risultato_analisi = "OK: " + str(analizzo)
            entry10.delete(0, END)
            entry10.insert(0, risultato_analisi)
            break
        analizzo -= 25
        if analizzo == 0:
            break
    if r == 1:
        messagebox.showerror("Attenzione", "Test Fallito")
        return
    usb = entry11.get()
    try:
        # Tentativo di aprire il file in modalità lettura ('r')
        with open(str(usb) + ":/datichat.txt", "r") as file:
            file.close()
            # Il file esiste, puoi eseguire le azioni necessarie
            messagebox.askyesno("File esistente", "Sovrascrivere?")
            risposta = messagebox.askyesno("File esistente", "Sovrascrivere?")
            if risposta == False:
                return
            else:
                scrivi = open(str(usb) + ":/datichat.txt", "w")
                scrivi.write(str(var2) + "\n")
                scrivi.write(str(es) + "\n")
                scrivi.write(str(ee1) + "\n")
                scrivi.write(str(ee2) + "\n")
                scrivi.write(str(var4) + "\n")
                scrivi.write(str(var5) + "\n")
                scrivi.write(str(var6) + "\n")
                scrivi.write(str(var7) + "\n")
                scrivi.write(str(var8) + "\n")
                scrivi.write(str(analizzo) + "\n")
                scrivi.close()
                messagebox.showinfo("OK", "File memorizzato correttamente")
                return

    except FileNotFoundError:
        scrivi = open(str(usb) + ":/datichat.txt", "w")
        scrivi.write(str(var2) + "\n")
        scrivi.write(str(es) + "\n")
        scrivi.write(str(ee1) + "\n")
        scrivi.write(str(ee2) + "\n")
        scrivi.write(str(var4) + "\n")
        scrivi.write(str(var5) + "\n")
        scrivi.write(str(var6) + "\n")
        scrivi.write(str(var7) + "\n")
        scrivi.write(str(var8) + "\n")
        scrivi.write(str(analizzo) + "\n")
        scrivi.close()
        messagebox.showinfo("OK", "File memorizzato correttamente")
        return


def carica_dati(
    entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10
):
    global base_codice
    global chiave_codice
    global indirizzo_ip
    global porta_ue
    global campo_codice
    global es1_codice
    global es2_codice
    usb = entry10.get()
    try:
        # Tentativo di aprire il file in modalità lettura ('r')
        with open(str(usb) + ":/datichat.txt", "r") as leggi:
            le0 = leggi.readline()
            le1 = leggi.readline()
            le2 = leggi.readline()
            le3 = leggi.readline()
            le4 = leggi.readline()
            le5 = leggi.readline()
            le6 = leggi.readline()
            le7 = leggi.readline()
            le8 = leggi.readline()
            le9 = leggi.readline()
            leggi.close()

            entry1.delete(0, END)
            entry1.insert(0, le0)

            entry2.delete(0, END)
            entry2.insert(0, le1)

            entry3.delete(0, END)
            entry3.insert(0, le2)

            entry4.delete(0, END)
            entry4.insert(0, le3)

            entry5.delete(0, END)
            entry5.insert(0, le4)
            entry6.delete(0, END)
            entry6.insert(0, le5)
            entry7.delete(0, END)
            entry7.insert(0, le6)
            entry8.delete(0, END)
            entry8.insert(0, le7)

            entry9.delete(0, END)
            entry9.insert(0, le8)

            base_codice = int(le0)
            chiave_codice = int(le1)
            es1_codice = int(le2)
            es2_codice = int(le3)
            porta_ue = int(le8)
            campo_codice = int(le9)
            indirizzo_ip = (
                str(int(le4))
                + "."
                + str(int(le5))
                + "."
                + str(int(le6))
                + "."
                + str(int(le7))
            )

            return

    except FileNotFoundError:
        # Il file non esiste
        messagebox.showerror("Attenzione", "Nome file inesistente")
        return


# ******************************************************
# Finestra principale
# ******************************************************


class Finestra1(tk.Tk):
    def __init__(self):
        super().__init__()

        style = tb.Style("superhero")
        self.title("Finestra Principale")
        self.geometry("550x650")

        # *** variabili dizionario
        self.var_e = {
            "e2": 0,
            "e3": 0,
            "e4": 0,
            "e5": 0,
            "e6": 0,
            "e7": 0,
            "e8": 0,
            "e9": 0,
            "e10": 0,
            "e11": 0,
            "ce2": 0,
            "ce4": 0,
            "ce5": 0,
            "ce6": 0,
            "ce7": 0,
            "ce8": 0,
            "ce9": 0,
            "ce10": 0,
            "ce11": 0,
            "ce12": "D",
        }

        # ****   crea nuovo codice
        b10 = tb.Button(
            self,
            text="Apri Chat",
            style="success.Outline.TButton",
            command=self.apri_chat,
        )
        b10.place(x=450, y=600)
        l1 = tb.Label(self, text="Inserisci un numero", font="arial 12")
        l1.place(x=10, y=20)
        e2 = tb.Entry(self, width=50, justify="center")
        e2.place(x=10, y=40)
        b11 = tb.Button(
            self,
            text="Trasforma in Primo",
            style="success.Outline.TButton",
            command=lambda: trasforma_primo(e2),
        )
        b11.place(x=10, y=70)
        b12 = tb.Button(
            self,
            text="Crea Nuovo Codice",
            style="success.Outline.TButton",
            command=lambda: crea_codice_nuovo(
                e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12
            ),
        )
        b12.place(x=150, y=70)
        l2 = tb.Label(self, text="Inserisci i Bit", font="arial 12")
        l2.place(x=400, y=20)
        e3 = tb.Entry(self, width=10, justify="center")
        e3.place(x=410, y=40)
        l3 = tb.Label(self, text="Indirizzo IP del ricevente", font="arial 12")
        l3.place(x=10, y=150)
        e4 = tb.Entry(self, width=5, justify="center")
        e4.place(x=10, y=170)
        e5 = tb.Entry(self, width=5, justify="center")
        e5.place(x=60, y=170)
        e6 = tb.Entry(self, width=5, justify="center")
        e6.place(x=110, y=170)
        e7 = tb.Entry(self, width=5, justify="center")
        e7.place(x=160, y=170)
        l4 = tb.Label(self, text="Apri Porta", font="arial 12")
        l4.place(x=250, y=150)
        e8 = tb.Entry(self, width=6, justify="center")
        e8.place(x=260, y=170)
        l5 = tb.Label(self, text="Codice Creato Bit", font="arial 12")
        l5.place(x=10, y=230)
        e9 = tb.Entry(self, width=10, justify="center")
        e9.place(x=30, y=250)
        l6 = tb.Label(self, text="Esponente", font="arial 12")
        l6.place(x=180, y=230)
        e10 = tb.Entry(self, width=10, justify="center")
        e10.place(x=180, y=250)
        l7 = tb.Label(self, text="Test di campo", font="arial 12")
        l7.place(x=300, y=230)
        e11 = tb.Entry(self, width=10, justify="center")
        e11.place(x=310, y=250)

        l8 = tb.Label(
            self,
            text="Att.: compilare il campo (IP e Porta) prima di creare nuovo codice",
            font="arial 12",
        )
        l8.place(x=20, y=300)
        l8 = tb.Label(
            self,
            text="NB:assegnare la porta USB sempre se quella non corrispone",
            font="arial 12",
        )
        l8.place(x=20, y=320)
        e12 = tb.Entry(self, width=3, justify="center")
        e12.insert(0, "D")
        e12.place(x=450, y=320)
        l9 = tb.Label(
            self,
            text="****************************************************************************",
            font="arial 12",
        )
        l9.place(x=20, y=350)

        # *** caricamento codice

        cl1 = tb.Label(self, text="Codice di Criptaggio", font="arial 12")
        cl1.place(x=10, y=380)
        ce2 = tb.Entry(self, width=50, justify="center")
        ce2.place(x=10, y=400)
        b13 = tb.Button(
            self,
            text="Carica Dati",
            style="success.Outline.TButton",
            command=lambda: carica_dati(
                ce2, ce9, ce10, ce11, ce4, ce5, ce6, ce7, ce8, e12
            ),
        )
        b13.place(x=10, y=600)
        cl3 = tb.Label(self, text="Indirizzo IP del ricevente", font="arial 12")
        cl3.place(x=10, y=450)
        ce4 = tb.Entry(self, width=5, justify="center")
        ce4.place(x=10, y=470)
        ce5 = tb.Entry(self, width=5, justify="center")
        ce5.place(x=60, y=470)
        ce6 = tb.Entry(self, width=5, justify="center")
        ce6.place(x=110, y=470)
        ce7 = tb.Entry(self, width=5, justify="center")
        ce7.place(x=160, y=470)
        cl4 = tb.Label(self, text="Apri Porta", font="arial 12")
        cl4.place(x=250, y=450)
        ce8 = tb.Entry(self, width=6, justify="center")
        ce8.place(x=260, y=470)
        cl5 = tb.Label(self, text="Chiave", font="arial 12")
        cl5.place(x=10, y=510)
        ce9 = tb.Entry(self, width=6, justify="center")
        ce9.place(x=10, y=530)
        cl6 = tb.Label(self, text="E1", font="arial 12")
        cl6.place(x=80, y=510)
        ce10 = tb.Entry(self, width=6, justify="center")
        ce10.place(x=80, y=530)
        cl7 = tb.Label(self, text="E2", font="arial 12")
        cl7.place(x=150, y=510)
        ce11 = tb.Entry(self, width=6, justify="center")
        ce11.place(x=150, y=530)

    def apri_chat(self):
        finestra_chat = FinestraChat(self)
        finestra_chat.grab_set()


# ******************************************************
# Chat codificata
# ******************************************************


class FinestraChat(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        style = tb.Style("darkly")
        self.title("ChatCodificata")
        self.geometry("1380x600")
        global tw1
        global tw2
        global tw3
        global tw4
        global e1
        # ***********************************************************************************
        b11 = tb.Button(
            self,
            text="Pulisci",
            bootstyle="TButton, outline,success",
            command=puliscitw1,
        )
        b11.place(x=100, y=210)
        b14 = tb.Button(
            self,
            text="Pulisci",
            bootstyle="TButton, outline,success",
            command=puliscitw4,
        )
        b14.place(x=700, y=500)
        # ***********************************************************************************
        b1 = tb.Button(
            self,
            text="Codifica",
            bootstyle="TButton, outline,success",
            command=codifica,
        )
        b1.place(x=10, y=210)
        b4 = tb.Button(
            self,
            text="Decodifica",
            bootstyle="TButton, outline,success",
            command=decodifica,
        )
        b4.place(x=10, y=500)
        # ***********************************************************************************
        b3 = tb.Button(
            self, text="Invia", bootstyle="TButton, outline,success", command=manda_tw1
        )
        b3.place(x=700, y=210)
        # ***********************************************************************************
        tw1 = tb.Text(self, width=73, height=10, font="helvetica 12")
        tw1.place(x=10, y=10)
        tw2 = tb.Text(self, width=73, height=10, font="helvetica 12")
        tw2.place(x=10, y=300)
        tw3 = tb.Text(self, width=73, height=10, font="helvetica 12")
        tw3.place(x=700, y=10)
        tw4 = tb.Text(self, width=73, height=10, font="helvetica 12")
        tw4.place(x=700, y=300)
        # ***********************************************************************************
        e1 = tb.Entry(self)
        # ***********************************************************************************
        start_ricevi()

    # ***********************************************************************************
    # Button(self, text="Chiudi Chat", style='danger.Outline.TButton', command=self.chiudi_chat).pack(pady=10)
    # Aggiungi i widget necessari per la chat

    def chiudi_chat(self):
        self.destroy()


if __name__ == "__main__":
    finestra_principale = Finestra1()
    finestra_principale.mainloop()
