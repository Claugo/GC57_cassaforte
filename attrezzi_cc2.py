#Programma attrezzi CassaCriptata2
import os
from tkinter import messagebox
from tkinter import simpledialog
from math import gcd
from cryptography.fernet import Fernet
import customtkinter as tkc
from sympy import nextprime
from random import randint, seed
import time
import locale
import hashlib
from random import randint, seed


#****************************************************
#**            Password
#****************************************************

def hash_password(password):
    # Genera un salt casuale per aggiungere casualità all'hashing
    salt = os.urandom(32)

    # Combina la password con il salt e calcola l'hash
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Combina il salt e l'hash in un unico valore da memorizzare nel database
    hashed_password_hex = salt.hex() + hashed_password.hex()

    return hashed_password_hex

def verify_password(input_password, stored_password):
    # Estrae il salt dal valore memorizzato
    salt = bytes.fromhex(stored_password[:64])

    # Calcola l'hash della password di input con lo stesso salt
    hashed_input_password = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, 100000)

    # Confronta il salt e l'hash con il valore memorizzato
    return stored_password[64:] == hashed_input_password.hex()

def get_password_from_user():
    password = simpledialog.askstring("Password", "Inserisci la password:", show="*")
    return password

# Esempio di utilizzo
password = "Cla1Giu19"
hashed_password = hash_password(password)

# Verifica della password
input_password = get_password_from_user()

if verify_password(input_password, hashed_password):
    pass
else:
    messagebox.showerror("Errore", "La password inserita è errata.")
    quit()




T=int(time.time())
seed(T)

locale.setlocale(locale.LC_TIME, 'it_IT')

# Modes: system (default), light, dark

cartella1='f:\\DCP'
cartella2='f:\\DCP/DCP_drop'


def generate_key():
    return Fernet.generate_key()


def encrypt_file(key, input_file, output_file):
    cipher = Fernet(key)

    with open(input_file, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)
    
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)




def decrypt_file(key, input_file, output_file):
    cipher = Fernet(key)

    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)





#****************************************************
#*           Ricodifica archivio
#****************************************************

def ricodifica_archivio():
    if l1.cget("text")=='/':
        messagebox.showerror("Attenzione:"," Decomprimere prima l'archivio")
        return
    cancella=cartella1+'\\database_chiavi.txt'
    if os.path.exists(cartella1):
        os.remove(cancella)
    
    lista_file = os.listdir(cartella1)
    lista_file_dcp = [file for file in lista_file if os.path.isfile(os.path.join(cartella1, file))]
#    lista_file_dcp = [file for file in lista_file]
    for i in range(len(lista_file_dcp)):
        file_to_encrypt = lista_file_dcp[i]
        output_filename = cartella2+'/'+ file_to_encrypt + ".crp"
    
        nome_file=file_to_encrypt
        file_to_encrypt=cartella1+'/'+file_to_encrypt
        key = generate_key()
    
        encrypt_file(key, file_to_encrypt, output_filename)
        data=time.strftime('%A:%B:%Y')
        memorizza_key=key.decode('utf-8')+','+nome_file+','+str(data)
        apri_file_key=open(cartella1+'/database_chiavi.txt','a')
        apri_file_key.write(memorizza_key+'\n')
        apri_file_key.close()
        path=output_filename
        cancella=file_to_encrypt
        if os.path.exists(path):
            os.remove(cancella)


    apri_dati = simpledialog.askstring("USB", 'Inserisci la porta USB se diversa da D')
    if not apri_dati:
        apri_dati = 'd'

    usb_file=apri_dati+':\\dati_cassaforte_crp.txt'
    
    if os.path.exists(usb_file):
        leggif=open(usb_file,'r')
        leggi1 = leggif.readline().strip()
        leggi2 = leggif.readline().strip()
        leggi3 = leggif.readline().strip()
        leggi4 = leggif.readline().strip()
        leggi5 = leggif.readline().strip()
        leggi6 = leggif.readline().strip()
        leggi7 = leggif.readline().strip()
        m1=int(leggif.readline())
        m2=int(leggif.readline())
        m3=int(leggif.readline())
        m4=int(leggif.readline())
        m5=int(leggif.readline())
        leggif.close()
        
        
        
        path=cartella1+'/database_chiavi.txt'
        testo=''
        apri=open(path,'r')
        for i in range(10000):
            te=apri.readline()
            if te=='\n' or te=='':
                apri.close()
                break
            testo=testo+te
        testo=testo.strip()    
        p = (int(leggi1)**int(leggi3))
        q = (int(leggi1)**int(leggi4))
        nd=nextprime(p+randint(1,int(leggi5)*2**int(leggi6)))
        nd2=nextprime(q+randint(1,int(leggi5)*2**int(leggi6)))
        n = nd*nd2
        #******************* controllo di fattorizzazione
        chiave = int(leggi1)**int(leggi2)
        a=n%chiave
        b=n-a
        for i in range(10):
            r=gcd(a,b)
            if r!=1:
                break
            else:
                a=a+chiave
                b=b-chiave
        if r==1:    
            messagebox.showerror('Attenzione', 'Test non superato: Riprovare')
            return
        #******************* fine controllo    
        start1=str(nd)
        start2=len(start1)
        start=int(start1[start2-5]+start1[start2-4])
        ln=list(str(nd))
        if len(ln) % 2 == 0:
            pass
        else:
            ln.append('0')
        divln = []
        for i in range(0, len(ln), 2):
            c1 = int(ln[i])
            c2 = int(ln[i+1])
            c3 = c1*10+c2
            divln.append(c3)

        text=(testo)
        te = list(text)
        cont = start
        tcript=''

        for i in range(len(text)):
            if cont>=len(divln):
                cont=0
            if ord(te[i])>700:
                pass
            else:
                x=int(divln[cont])
                if x>=0 and x<25:
                    x=x+m1+ord(te[i])
                if x>=25 and x<40:
                    x=x+m2+ord(te[i])
                if x>=40 and x<50:
                    x=x+m3+ord(te[i])
                if x>=50 and x<75:
                    x=x+m4+ord(te[i])
                if x>=75 and x<100:
                    x=x+m5+ord(te[i])
                tcript=tcript+str(x)    
                cont=cont+1
            
        path=cartella2+"/database_chiavi.cr"
        scrivi=open(path,'w')
        scrivi.write(str(n)+'\n')
        scrivi.write(tcript+'\n')
        scrivi.close()
        messagebox.showinfo('OK', 'Database memorizzato con GC57 correttamente')
        
        path = cartella2+"/database_chiavi.cr"
        cancella=cartella1+"/database_chiavi.txt"
        if os.path.exists(path):
            os.remove(cancella)
  
    l3.configure(text='E')


#****************************************************
#*           decodifica archivio
#****************************************************


def decodifica_archivio():
    lista_file = os.listdir(cartella2)
    lista_file_crp = [file for file in lista_file if file.endswith('.crp')]
    apri_dati = simpledialog.askstring("USB", 'Inserisci la porta USB se diversa da D')
    if not apri_dati:
        apri_dati = 'd'
    #****************************************************
    #**  Cerca nella USB i dati di criptazione GC57
    #****************************************************
    file_path = os.path.join(apri_dati + ':', '\\dati_cassaforte_crp.txt')
    try:
        with open(file_path, 'r') as leggif:
            leggi1 = leggif.readline().strip()
            leggi2 = leggif.readline().strip()
            leggi3 = leggif.readline().strip()
            leggi4 = leggif.readline().strip()
            leggi5 = leggif.readline().strip()
            leggi6 = leggif.readline().strip()
            leggi7 = leggif.readline().strip()
            m1=int(leggif.readline())
            m2=int(leggif.readline())
            m3=int(leggif.readline())
            m4=int(leggif.readline())
            m5=int(leggif.readline())
    except FileNotFoundError:
        messagebox.showerror("Errore", "Dati su USB non trovati")
        return

    #****************************************************
    #** Vede se c'è il file criptato delle chiavi per decriptarlo
    #****************************************************

    path = cartella2+"/database_chiavi.cr"
    if os.path.exists(path):
        leggi=open(path,'r')
        n_semiprimo=leggi.readline()
        testo_criptato=leggi.readline()
        leggi.close()
        n_semiprimo=n_semiprimo.strip()
    
        testo_criptato=testo_criptato.strip()
        chiave = int(leggi1)**int(leggi2)
        n_semiprimo=int(n_semiprimo)
        a = n_semiprimo%chiave
        b=n_semiprimo-a
        for i in range(10):
            r = gcd(b, a)
            if r != 1:
                break
            a=a+chiave
            b=b-chiave    
        if r==1:
            messagebox.showerror('Attenzione', 'Chiave GC57 errata')
            return
        start1 = str(r)
        start2 = len(start1)
        start = int(start1[start2-5]+start1[start2-4])
        ln = list(str(r))
        if len(ln) % 2 == 0:
            pass
        else:
            ln.append('0')
            
        divln = []
        for i in range(0, len(ln), 2):
            c1 = int(ln[i])
            c2 = int(ln[i+1])
            c3 = c1*10+c2
            divln.append(c3)

        te=[]    
        d0=list(testo_criptato)
        for i in range(0,len(d0),3):
            d1=d0[i]
            d2=d0[i+1]
            d3=d0[i+2]
            te.append(d1+d2+d3)
        cont = start
        tdecript=''
        for i in range(len(te)):
            if cont >= len(divln):
                cont = 0
            x=int(divln[cont])
            if x>=0 and x<25:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m1))
            if x>=25 and x<40:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m2))
            if x>=40 and x<50:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m3))
            if x>=50 and x<75:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m4))
            if x>=75 and x<100:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m5))
            cont=cont+1        
        path = cartella1+"/database_chiavi.txt"
        scrivi=open(path,'w')
        scrivi.write(str(tdecript)+'\n')
        scrivi.close()
    else:
        messagebox.showerror("Attenzione", "database_chiavi non trovato\nil programma verrà chiuso")
        return

    for li in range(len(lista_file_crp)):
        file_to_decrypt = lista_file_crp[li]
        e2=lista_file_crp[li]
        if file_to_decrypt=='':
            messagebox.showerror('Errore:','Nessun file selezionato')
            break
        nome_originale=e2.replace('.crp','')
        apri=open(cartella1+'/database_chiavi.txt','r')
        for i in range(1000):
            stringa=apri.readline()
            stringa=stringa.strip()
            if stringa=='\n' or stringa=='':
                messagebox.showinfo('Ricerca Codice:','Nessun codice Trovato')
                apri.close()
    
            trovata=nome_originale in stringa
            if trovata==True:
                sp=stringa.split(',')
                chiave=sp[0].encode('utf-8')
                apri.close()
                break

        original_filename = cartella1+'/'+file_to_decrypt.replace('.crp', '')
        file_to_decrypt=cartella2+'/'+file_to_decrypt
        
        decrypt_file(chiave, file_to_decrypt, original_filename)
    
    l1.configure(text='E')
    messagebox.showinfo('Decodifica Archivio:','Archivio Decodificato')
    


#****************************************************
#*           Ricodifica solo database
#****************************************************

def ricodifica_solo_database():
    apri_dati = simpledialog.askstring("USB", 'Inserisci la porta USB se diversa da D')
    if not apri_dati:
        apri_dati = 'd'
  
#****************************************************
#**  Cerca nella USB i dati di criptazione GC57
#****************************************************

    file_path = os.path.join(apri_dati + ':', 'dati_cassaforte_crp.txt')
    try:
        with open(file_path, 'r') as leggif:
            leggi1 = leggif.readline().strip()
            leggi2 = leggif.readline().strip()
            leggi3 = leggif.readline().strip()
            leggi4 = leggif.readline().strip()
            leggi5 = leggif.readline().strip()
            leggi6 = leggif.readline().strip()
            leggi7 = leggif.readline().strip()
            m1=int(leggif.readline())
            m2=int(leggif.readline())
            m3=int(leggif.readline())
            m4=int(leggif.readline())
            m5=int(leggif.readline())
    except FileNotFoundError:
        messagebox.showerror("Errore", "Dati su USB non trovati")
        return
#****************************************************
#** Vede se c'è il file criptato delle chiavi per decriptarlo
#****************************************************

    path = cartella2+"/database_chiavi.cr"
    if os.path.exists(path):
        leggi=open(path,'r')
        n_semiprimo=leggi.readline()
        testo_criptato=leggi.readline()
        leggi.close()
        n_semiprimo=n_semiprimo.strip()
    
        testo_criptato=testo_criptato.strip()
        chiave = int(leggi1)**int(leggi2)
        n_semiprimo=int(n_semiprimo)
        a = n_semiprimo%chiave
        b=n_semiprimo-a
        for i in range(10):
            r = gcd(b, a)
            if r != 1:
                break
            a=a+chiave
            b=b-chiave    
        if r==1:
            messagebox.showerror('Attenzione', 'Chiave GC57 errata')
            return
        start1 = str(r)
        start2 = len(start1)
        start = int(start1[start2-5]+start1[start2-4])
        ln = list(str(r))
        if len(ln) % 2 == 0:
            pass
        else:
            ln.append('0')
            
        divln = []
        for i in range(0, len(ln), 2):
            c1 = int(ln[i])
            c2 = int(ln[i+1])
            c3 = c1*10+c2
            divln.append(c3)

        te=[]    
        d0=list(testo_criptato)
        for i in range(0,len(d0),3):
            d1=d0[i]
            d2=d0[i+1]
            d3=d0[i+2]
            te.append(d1+d2+d3)
        cont = start
        tdecript=''
        for i in range(len(te)):
            if cont >= len(divln):
                cont = 0
            x=int(divln[cont])
            if x>=0 and x<25:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m1))
            if x>=25 and x<40:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m2))
            if x>=40 and x<50:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m3))
            if x>=50 and x<75:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m4))
            if x>=75 and x<100:
                y=int(te[i])
                tdecript=tdecript+(chr(y-x-m5))
            cont=cont+1        
        path = cartella1+"/database_chiavi.txt"
        scrivi=open(path,'w')
        scrivi.write(str(tdecript)+'\n')
        scrivi.close()
    else:
        messagebox.showerror("Attenzione", "database_chiavi non trovato\nil programma verrà chiuso")
        return
    usb_file=apri_dati+':\\s_dati_cassaforte_crp.txt'
    
    if os.path.exists(usb_file):
        leggif=open(usb_file,'r')
        leggi1 = leggif.readline().strip()
        leggi2 = leggif.readline().strip()
        leggi3 = leggif.readline().strip()
        leggi4 = leggif.readline().strip()
        leggi5 = leggif.readline().strip()
        leggi6 = leggif.readline().strip()
        leggi7 = leggif.readline().strip()
        m1=int(leggif.readline())
        m2=int(leggif.readline())
        m3=int(leggif.readline())
        m4=int(leggif.readline())
        m5=int(leggif.readline())
        leggif.close()
        
        
        
        path=cartella1+'/database_chiavi.txt'
        testo=''
        apri=open(path,'r')
        for i in range(10000):
            te=apri.readline()
            if te=='\n' or te=='':
                apri.close()
                break
            testo=testo+te
        testo=testo.strip()    
        p = (int(leggi1)**int(leggi3))
        q = (int(leggi1)**int(leggi4))
        nd=nextprime(p+randint(1,int(leggi5)*2**int(leggi6)))
        nd2=nextprime(q+randint(1,int(leggi5)*2**int(leggi6)))
        n = nd*nd2
        #******************* controllo di fattorizzazione
        chiave = int(leggi1)**int(leggi2)
        a=n%chiave
        b=n-a
        for i in range(10):
            r=gcd(a,b)
            if r!=1:
                break
            else:
                a=a+chiave
                b=b-chiave
        if r==1:    
            messagebox.showerror('Attenzione', 'Test non superato: Riprovare')
            return
        #******************* fine controllo    
        start1=str(nd)
        start2=len(start1)
        start=int(start1[start2-5]+start1[start2-4])
        ln=list(str(nd))
        if len(ln) % 2 == 0:
            pass
        else:
            ln.append('0')
        divln = []
        for i in range(0, len(ln), 2):
            c1 = int(ln[i])
            c2 = int(ln[i+1])
            c3 = c1*10+c2
            divln.append(c3)

        text=(testo)
        te = list(text)
        cont = start
        tcript=''

        for i in range(len(text)):
            if cont>=len(divln):
                cont=0
            if ord(te[i])>700:
                pass
            else:
                x=int(divln[cont])
                if x>=0 and x<25:
                    x=x+m1+ord(te[i])
                if x>=25 and x<40:
                    x=x+m2+ord(te[i])
                if x>=40 and x<50:
                    x=x+m3+ord(te[i])
                if x>=50 and x<75:
                    x=x+m4+ord(te[i])
                if x>=75 and x<100:
                    x=x+m5+ord(te[i])
                tcript=tcript+str(x)    
                cont=cont+1
            
        path=cartella2+"/database_chiavi.cr"
        scrivi=open(path,'w')
        scrivi.write(str(n)+'\n')
        scrivi.write(tcript+'\n')
        scrivi.close()
        messagebox.showinfo('OK', 'Database memorizzato con GC57 correttamente')
        
        path = cartella2+"/database_chiavi.cr"
        cancella=cartella1+"/database_chiavi.txt"
        if os.path.exists(path):
            os.remove(cancella)
        
        nfi=apri_dati+':\\dati_cassaforte_crp.txt'
        rfi=apri_dati+':\\O_dati_cassaforte_crp.txt'
        os.rename(nfi, rfi)
    
        nfi=apri_dati+':\\s_dati_cassaforte_crp.txt'
        rfi=apri_dati+':\\dati_cassaforte_crp.txt'
        os.rename(nfi, rfi)

        l4.configure(text='E')
    
    else:
        pass
        
    
    

#****************************************************
#*           Interfaccia
#****************************************************



tkc.set_appearance_mode("system")
 #Themes: blue (default), dark-blue, green
tkc.set_default_color_theme('dark-blue')
app = tkc.CTk()  # create CTk window like you do with the Tk window
app.geometry("450x100")
app.title('Cassetta attrezzi CassaCriptata2')

py=20
px=280
b4 = tkc.CTkButton(width=70,master=app, text="Ricodifica Database", fg_color='brown',hover_color='blue',command=ricodifica_solo_database)
b4.place(x=px,y=py)
l4=tkc.CTkLabel(app,text='/',fg_color='transparent',font=('arial',16,'bold'))
l4.place(x=px+150,y=py)



px=10

b1 = tkc.CTkButton(width=70,master=app, text="Decodifica Archivio Completo", fg_color='green',hover_color='blue',command=decodifica_archivio)
b1.place(x=px,y=py)
l1=tkc.CTkLabel(app,text='/',fg_color='transparent',font=('arial',16,'bold'))
l1.place(x=px+200,y=py)


py=py+40
b3 = tkc.CTkButton(width=70,master=app, text="Ricodifica Archivio Completo", fg_color='green',hover_color='blue',command=ricodifica_archivio)
b3.place(x=px,y=py)
l3=tkc.CTkLabel(app,text='/',fg_color='transparent',font=('arial',16,'bold'))
l3.place(x=px+200,y=py)




app.mainloop()
