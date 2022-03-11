

from ast import Call
from itertools import count
from logging import root
from tkinter import*
from subprocess import call

from turtle import color, title, width
from typing import Counter
from PIL import ImageTk
import random




class appli:

    def __init__(self,root) :
        self.root=root
        self.root.title("STORIA PALACE")
        self.root.geometry("1500x1500")

        labeltitre = Label(self.root,borderwidth=3
        ,font=("Sans serif",35),background="black",foreground="white")
        labeltitre.place(x=0,y=0,width=2000)

        btn= Button(labeltitre,text="ACCUEIL", width=10,height=1,background="gainsboro")
        btn.place(x=550,y=10)

        btn2= Button(labeltitre,text="RESERVATION", width=10,height=1,background="gainsboro")
        btn2.place(x=800,y=10)

        btn3= Button(labeltitre,text="ACCUEIL", width=10,height=1,background="gainsboro")
        btn3.place(x=900,y=10)

        """self.image1= ImageTk.PhotoImage(file="stock.png") 
        self.lbl1= Label(self.root,image=self.image1)
        self.lbl1.place(x=0,y=0)"""

        def Visite_hotel(self,win):
            self.root.destroy()
            self.win=win
            self.win.geometry('1500x1500')
            self.win.title("ENOTEL BEA")
            self.win.configure(bg='lavender')
            

            labeltitre = Label(self.win,borderwidth=3
            ,text="",font=("Sans serif",35),background="black",foreground="white")
            labeltitre.place(x=0,y=0,width=2000)
            
            def accueil():
                
                
                call(self.root)
            btn_win1= Button(labeltitre,text="ACCUEIL", width=10,height=1,background="gainsboro",command=accueil)
            btn_win1.place(x=700,y=10)
        btn1= Button(labeltitre,text="VISITE", width=10,height=1,background="gainsboro",command=Visite_hotel)
        btn1.place(x=700,y=10)
root=Tk()
obj=appli(root)
root.mainloop()  









    
    
    



























"""print("exercice 1")

def etrait_ensemble_des_voyelles(mot):
    
    voyelle = ("a","e","i","o","u","y")
    contener = []
    
    for i in mot:
        if i in voyelle:
            contener.append(i)
    return contener;

a = etrait_ensemble_des_voyelles("richard")
print(a)"""
    




 
    

"""from tkinter import LEFT, RIGHT
from turtle import*
reset()
a = 0
title
while a < 50:
    a = a + 1
    forward (100)
   
    
    color("green")

count = 0
text = 'ENOTEL BEACH-----**-----'






colors =['pink','red','blue','ponder blue','green']
def slider():
    
    
    if(len(text)<count):
        count=0
        text=''
    text=text+text[count]
    titre.configure(text=text)
    color=random.choice(colors)
    titre.config(bg=color)
    count+=1
    windowc.after(400,slider)"""

    
    

        