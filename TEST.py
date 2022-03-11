from tkinter import*
from PIL import ImageTk

class concour:
    def __init__(self,root):
        root=root
        root.title("concour")
        root.geometry("300x500")
        root.configure(bg="purple")


        


        var_nom = StringVar()
        var_prenom = StringVar()
        var_age = StringVar()
        var_contri = StringVar()
        var_Tcontri = StringVar()
        var_Tadherant = StringVar()

        nom = Label(root,text= "Nom:")
        nom.place(x=20, y= 50)
        nom_entry =Entry(root,border=3,textvariable=var_nom)
        nom_entry.place(x =115, y=50)
        nom_entry.config(relief=SUNKEN)
    
        prenom = Label(root,text= "Prenom:")
        prenom.place(x=20, y= 100)
        prenom_entry =Entry(root,border=3,textvariable=var_prenom)
        prenom_entry.place(x =115, y=100,)
        prenom_entry.config(relief=SUNKEN)

        age = Label(root,text= "Age:")
        age.place(x=20, y= 150)
        age_entry =Entry(root,border=3,textvariable=var_age)
        age_entry.place(x =115, y=150,)
        age_entry.config(relief=SUNKEN)

        contribution = Label(root,text= "Contribution:")
        contribution.place(x=20, y= 200)
        contribution_entry =Entry(root,border=3,textvariable=var_contri)
        contribution_entry.place(x =115, y=200,)
        contribution_entry.config(relief=SUNKEN)

        Tcontribution = Label(root,text= "Total contribution:")
        Tcontribution.place(x=5, y= 350)
        Tcontribution_entry =Entry(root,border=3,textvariable=var_Tcontri)
        Tcontribution_entry.place(x =125, y=350,width=160)
        Tcontribution_entry.config(relief=SUNKEN)

        Tadherant = Label(root,text= "Total adherant:")
        Tadherant.place(x=5, y= 400)
        Tadherant_entry =Entry(root,border=3,textvariable=var_Tadherant)
        Tadherant_entry.place(x =125, y=400,width=160)
        Tadherant_entry.config(relief=SUNKEN)

        nom = nom_entry.get()
        prenom = prenom_entry.get()
        age = age_entry.get()
        contribution = contribution_entry.get()

        

        dic=[]
        dic_nom=[]
        def valider():
            


            dict={
                "nom":nom_entry.get(),
                "prenom":prenom_entry.get(),
                "age":age_entry.get(),
                "contribution":(int(contribution_entry.get()))
            }
            print(dict)
            
            
            t= int(contribution_entry.get())
            dic.append(t)
            dic_nom.append(nom_entry.get())
            print(dic_nom)

            def total_element(list):
                count=0
                for element in dic_nom:
                    count+=1
                return count
            var_Tadherant.set(total_element(dic_nom))

            print("total est:",total_element(dic_nom))

            
            
            s=0
            for i in dic:
                s =s+i
            print(s)
            var_Tcontri.set(s)
             
    
            nom_entry.delete(0,END)
            prenom_entry.delete(0,END)
            age_entry.delete(0,END)
            contribution_entry.delete(0,END)

        btn= Button(root,text="Valider",width=10,bg="blue",command=valider)
        btn.place(x=100,y=250)
        
        
        
        
        
        
        

        
root=Tk()
obj=concour(root)
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

    
    














#self.lbl1= Label(self.root,image=self.image1)
#self.lbl1.place(x=0,y=0)

#self.image1= ImageTk.PhotoImage(file="stock.png") 