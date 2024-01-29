# calcolo del campo in cui può operare la fattorizzazione
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.widgets import Button
from ttkbootstrap.constants import *
from tkinter import messagebox
from sympy import nextprime
from math import gcd, log
from random import randint,seed
import time
from tkinter import simpledialog

e_chiave=None
es1=None
es2=None
aumenta=None



def trasforma_primo():
    var1=e1.get()
    if var1=='':
        messagebox.showerror('Attenzione', 'Nessun numero trovato')
        return
    if var1.isnumeric() == False:
        messagebox.showerror('Attenzione', 'Non possono esserci lettere')
        return
    var1=int(var1)
    var=nextprime(var1)
    e1.delete(0,END)
    e1.insert(0,str(var))



def calcola_campo():
    var1=e1.get()
    var2=e2.get()
    var3=e3.get()
    if var1=='' or var2=='' or var3=='':
        messagebox.showerror('Attenzione', 'Campi non compilati')
        return
    if var1.isnumeric() == False or var2.isnumeric()==False or var3.isnumeric==False:
        messagebox.showerror('Attenzione', 'Non possono esserci lettere')
        return
    global e_chiave,es1,es2,aumenta

    var1=int(var1)
    var2=int(var2)
    var3=int(var3)
    #**** imposto il seme di ricerca random
    T=int(time.time())
    seed(T)
    dim_Bitp=var2
    ni=var1
    calcolo_bit=2**dim_Bitp
    dim_Bitr=int(log(calcolo_bit,ni))+1
    n=ni**dim_Bitr
    dim_Bit=int(log(n,2))
    e8.delete(0,END)
    e8.insert(0,str(dim_Bit))
    e_chiave=dim_Bitr//2
    ee1=var3//2
    ee2=var3-ee1
    es1=e_chiave-ee1
    es2=e_chiave+ee2
    chiave=ni**e_chiave
    if es1+es2==dim_Bitr:
        pass
    elif es1+es2>dim_Bitr:
        es1=es1-1
    else:
        es2=es2+1    
    if es1<4:
        messagebox.showerror('Attenzione', 'Diminuire la differenza tra Esponenti')
        return
    trovato=0
    campo=500
    p1=ni**es1
    q1=ni**es2
    for i in range(19):
        p=nextprime(p1+randint(1,2**campo))
        q=nextprime(q1+randint(1,2**campo))
        n=p*q
        a=n%chiave
        b=n-a
        for ii in range(10):
            r=gcd(a,b)
            if r!=1:
                trovato=1
                break
        if trovato==1 or campo==0:
            break
        campo-=25    
    if r==1:
        messagebox.showerror('Attenzione', 'Nessun Campo Trovato')
        return
    else:
        aumenta=1
        fine=0
        for ii in range(10):
            p=nextprime(p1+randint(1,aumenta*(2**campo)))
            q=nextprime(q1+randint(1,aumenta*(2**campo)))
            n=p*q
            a=n%chiave
            b=n-a
            for i in range(10):
                r=gcd(a,b)
                if r!=1 and i==0:
                    aumenta=aumenta*10
                else:
                    fine=1
                break
            if fine==1:
                break
        if aumenta>10:
            aumenta=aumenta//10        
    e4.delete(0,END)
    ee4=('ni**'+str(e_chiave))
    e4.insert(0,str(ee4))
    e5.delete(0,END)
    ee5=('p=nextprime ('+'ni**'+str(es1)+'+randint('+'1,'+str(aumenta)+'*(2**'+str(campo)+')')
    e5.insert(0,ee5)
    e6.delete(0,END)
    ee6=('q=nextprime ('+'ni**'+str(es2)+'+randint('+'1,'+str(aumenta)+'*(2**'+str(campo)+')')
    e6.insert(0,ee6)
    e7.delete(0,END)
    e7.insert(0,str(campo))
    e9.delete(0,END)
    e9.insert(0,str(var1))
    

def crea_dati_cassaforte_crp():
    
    verifica=e4.get()
    if verifica=='':
        messagebox.showerror('Attenzione', 'Creare prima il codice')
        return
    
    apri_dati = simpledialog.askstring("USB",'D')
    if not apri_dati:
        apri_dati = 'd'

    global e_chiave,es1,es2,aumenta
    scrivi=open(apri_dati+':\\dati_cassaforte_crp.txt','w')
    scrivi.write(e9.get()+'\n') 
    scrivi.write(str(e_chiave)+'\n') 
    scrivi.write(str(es1)+'\n') 
    scrivi.write(str(es2)+'\n') 
    scrivi.write(str(aumenta)+'\n') 
    scrivi.write(e7.get()+'\n') 
    scrivi.write(e8.get()+'\n')
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.close()
    messagebox.showinfo('Salva','Salvataggio Dati Riuscito')



def S_crea_dati_cassaforte_crp():
    
    verifica=e4.get()
    if verifica=='':
        messagebox.showerror('Attenzione', 'Creare prima il codice')
        return
    
    apri_dati = simpledialog.askstring("USB",'D')
    if not apri_dati:
        apri_dati = 'd'

    global e_chiave,es1,es2,aumenta
    scrivi=open(apri_dati+':\\s_dati_cassaforte_crp.txt','w')
    scrivi.write(e9.get()+'\n') 
    scrivi.write(str(e_chiave)+'\n') 
    scrivi.write(str(es1)+'\n') 
    scrivi.write(str(es2)+'\n') 
    scrivi.write(str(aumenta)+'\n') 
    scrivi.write(e7.get()+'\n') 
    scrivi.write(e8.get()+'\n')
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.close()
    messagebox.showinfo('Salva','Salvataggio Dati Riuscito')
 
    

def crea_dati_cassaforte_trc():
    
    verifica=e4.get()
    if verifica=='':
        messagebox.showerror('Attenzione', 'Creare prima il codice')
        return
    
    apri_dati = simpledialog.askstring("USB",'D')
    if not apri_dati:
        apri_dati = 'd'

    global e_chiave,es1,es2,aumenta
    scrivi=open(apri_dati+':\\dati_cassaforte_trc.txt','w')
    scrivi.write(e9.get()+'\n') 
    scrivi.write(str(e_chiave)+'\n') 
    scrivi.write(str(es1)+'\n') 
    scrivi.write(str(es2)+'\n') 
    scrivi.write(str(aumenta)+'\n') 
    scrivi.write(e7.get()+'\n') 
    scrivi.write(e8.get()+'\n')
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.close()
    messagebox.showinfo('Salva','Salvataggio Dati Riuscito')


def S_crea_dati_cassaforte_trc():
    
    verifica=e4.get()
    if verifica=='':
        messagebox.showerror('Attenzione', 'Creare prima il codice')
        return
    
    apri_dati = simpledialog.askstring("USB",'D')
    if not apri_dati:
        apri_dati = 'd'

    global e_chiave,es1,es2,aumenta
    scrivi=open(apri_dati+':\\s_dati_cassaforte_trc.txt','w')
    scrivi.write(e9.get()+'\n') 
    scrivi.write(str(e_chiave)+'\n') 
    scrivi.write(str(es1)+'\n') 
    scrivi.write(str(es2)+'\n') 
    scrivi.write(str(aumenta)+'\n') 
    scrivi.write(e7.get()+'\n') 
    scrivi.write(e8.get()+'\n')
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.write(str(randint(101,500))+'\n') 
    scrivi.close()
    messagebox.showinfo('Salva','Salvataggio Dati Riuscito')

root=tb.Window(themename='cyborg')
root.title('Analizzatore Campo')
root.geometry('600x530')
#** parte superiore
l1=tb.Label(text='Inserire un numero digitato Casualmente\no che ne conoscete gli attributi: Tipo RSA',font='arial 12')
l1.place(x=10,y=30)
e1=tb.Entry(width=50)
e1.place(x=10,y=80)
b1 = tb.Button(text="Trasforma in Un Fattore Primo", style='success.Outline.TButton',command=trasforma_primo)
b1.place(x=10,y=110)
b2=tb.Button(text='Crea Codice',style='success.Outline.TButton',command=calcola_campo)
b2.place(x=200,y=110)
l2=tb.Label(text='Bit',font='arial 12')
l2.place(x=400,y=55)
e2=tb.Entry(width=5)
e2.place(x=400,y=80)
l3=tb.Label(text='Differenza Minima Tra due Esponenti',font='arial 12')
l3.place(x=10,y=160)
e3=tb.Entry(width=3)
e3.place(x=270,y=160)
#************************************************************************
l0=tb.Label(text='*********************** NB: tutti i campi sopra devono essere compilati ***************************')
l0.place(x=1,y=200)
#************************************************************************
l9=tb.Label(text='ni    =',font='arial 12')
l9.place(x=10,y=230)
e9=tb.Entry(width=(60))
e9.place(x=100,y=230)

#************************************************************************
yy=60
l4=tb.Label(text='Chiave =',font='arial 12')
l4.place(x=10,y=230+yy)
e4=tb.Entry(width=(60))
e4.place(x=100,y=230+yy)
l5=tb.Label(text='p      =',font='arial 12')
l5.place(x=10,y=270+yy)
e5=tb.Entry(width=(60))
e5.place(x=100,y=270+yy)
l6=tb.Label(text='q      =',font='arial 12')
l6.place(x=10,y=310+yy)
e6=tb.Entry(width=(60))
e6.place(x=100,y=310+yy)
l7=tb.Label(text='Campo  =',font='arial 12')
l7.place(x=10,y=350+yy)
e7=tb.Entry(width=(5))
e7.place(x=100,y=350+yy)
l8=tb.Label(text='Bit    =',font='arial 12')
l8.place(x=10,y=390+yy)
e8=tb.Entry(width=(5))
e8.place(x=100,y=390+yy)
#************************************************************************
b3=tb.Button(text='Crea Dati per Cassaforte trc',style='primary,Outline',command=crea_dati_cassaforte_trc)
b3.place(x=180,y=470)

#b4=tb.Button(text='Crea Dati per S-Cassaforte trc',style='primary,Outline',command=S_crea_dati_cassaforte_trc)
#b4.place(x=180,y=500)

b3=tb.Button(text='Crea Dati per Cassaforte crp',style='secondary,Outline',command=crea_dati_cassaforte_crp)
b3.place(x=400,y=470)

b4=tb.Button(text='Crea Dati per S-Cassaforte crp',style='secondary,outline',command=S_crea_dati_cassaforte_crp)
b4.place(x=400,y=500)

root.mainloop()
