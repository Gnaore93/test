



from calendar import c
from shutil import ExecError
from tkinter import*
import sqlite3
from subprocess import call
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from turtle import color, left, onclick, pos, position, right, title





window_ins = Tk()
window_ins.geometry('400x400+100+150')
window_ins.title("INSCRIPTION UTILISATEUR")
window_ins.configure(bg='gainsboro')

nom = Label(window_ins,text= "Nom:")
nom.place(x=5, y= 50)
nom_entry =Entry(window_ins,border=3)
nom_entry.place(x =100, y=50)
nom_entry.config(relief=SUNKEN)

prenom = Label(window_ins,text= "Prenoms:")
prenom.place(x=5, y= 100,)
Prenom_entry =Entry(window_ins,border=3)
Prenom_entry.place(x =100, y=100)
Prenom_entry.config(relief=SUNKEN)

email = Label(window_ins,text= "Email:")
email.place(x=5, y= 150,)
Email_entry =Entry(window_ins,border=3)
Email_entry.place(x =100, y=150)
Email_entry.config(relief=SUNKEN)

mot_de_passe = Label(window_ins,text= "Mot de passe:")
mot_de_passe.place(x=5, y= 200,)
Mdps_entry =Entry(window_ins,show="*",border=3)
Mdps_entry.place(x =100, y=200)
Mdps_entry.config(relief=SUNKEN)

conf_mdp = Label(window_ins,text= "Confirmation mdp:")
conf_mdp.place(x=5, y= 250,)
CONF_Mdp_entry =Entry(window_ins,show="*",border=3)
CONF_Mdp_entry.place(x =110, y=250)
CONF_Mdp_entry.config(relief=SUNKEN)

labeltitre = Label(window_ins,borderwidth=3,relief=SUNKEN
,text="Formulaire de connexion",font=("Sans serif",25),background="blue",foreground="white")
labeltitre.place(x=0,y=0,width=400)





def inscription():

    conn=sqlite3.connect('myBD_inscription.db')

    cur =conn.cursor()

    nom = nom_entry.get()
    prenom = Prenom_entry.get()
    email = Email_entry.get()
    mot_de_passe = Mdps_entry.get()
    conf_mdp = CONF_Mdp_entry.get()


    if (nom == "" or prenom == "" or email == "" or mot_de_passe == "" or conf_mdp == ""):
        messagebox.showerror("erreur","veuillez renseigner tout les shamps")


    elif (mot_de_passe != conf_mdp):
        messagebox.showerror("invalide","mot de pass non confirmer")

    elif (nom == nom_entry.get()  and prenom == Prenom_entry.get() and email == Email_entry.get() and mot_de_passe == Mdps_entry.get() and conf_mdp == Mdps_entry.get() ):
        messagebox.showerror("succes","inscription succes")
    else:
        try:
            conn= sqlite3.connect("database.db")
            sql_cursor=conn.cursor()
            sql_cursor.execute("""" CREATE TABLE IF NOT EXISTS inscription(
            nom text,
            prenom text,
            email text,
            mot de passe text,
            confirme mot de passe text,
            

            )""")
        
            cur.execute("INSERT INTO customer VALUES(:ref,:nam,:prenom,:email,:mot de passe,:email,)",(
                nom.get(),
                prenom.get(),
                email.get(),
                mot_de_passe.get(),
                conf_mdp.get(),
                
            ))
            conn.commit()
            conn.close()
        except Exception:
            pass
            window_ins.destroy()



        windowc = Tk()
        windowc.geometry('600x300+380+200')
        windowc.title("CONNEXION UTILISATEUR")
        windowc.configure(bg='lavender')



        uti = Label(windowc,text= "Utilisateur:")
        uti.place(x=5, y= 10,)
        uti_entry =Entry(windowc,border=3)
        uti_entry.place(x =100, y=10)
        uti_entry.config(relief=SUNKEN)

        mot_passe_c = Label(windowc,text= "Mot de passe:")
        mot_passe_c.place(x=5, y= 50,)
        Mdp_entry =Entry(windowc,border=3)
        Mdp_entry.place(x =100, y=50)
        Mdp_entry.config(relief=SUNKEN)
            
     
    
    def connecter():
        
        uti= uti_entry.get()
        mot_passe_c= Mdp_entry.get()
        

        if (uti =="" or mot_passe_c==""):
            messagebox.showinfo("erreur","veuillez renseigner tout les champs svp")

        elif ( Mdp_entry != 123 ):
            messagebox.showinfo("mot de passe incorect")
        elif (Mdp_entry== 123):
            messagebox.showerror("connexion validee")
        
                    

            uti_entry.delete(0,END)
            Mdp_entry.delete(0,END)   
            
        btnc = Button(windowc,text="Connexion",font=("Arial",16),fg="red",command=connecter)    
        btnc.place(x=150,y=250,width=100)
            
btn_ins = Button(window_ins,text="Valider",font=("Arial",16),fg="red",command=inscription)    
btn_ins.place(x=150,y=300,width=80)      
       

        
        

   
    



  
 
mainloop()







    
    
    



























"""print("exercice 1")

def etrait_ensemble_des_voyelles(mot):
    
    voyelle = ("a","e","i","o","u","y")
    contener = []
    
    for i in mot:
        if i in voyelle:
            contener.append(i)
    return contener;

a = etrait_ensemble_des_voyelles("richard")
print(a)
    




 
    

from turtle import*
reset()
a = 0

while a < 50:
    a = a + 1
    forward (100)
    left(90)
    color("green")"""


    

        