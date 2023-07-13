
from tkinter import *
import webbrowser as wb

obj=Tk(className=" Spotify search")
e=Entry(obj,font=("Times New Roman",25))
e.grid()



def search_():#searching
    query=e.get()
    wb.open("https://open.spotify.com/search"+query)
    

#creating button
b=Button(obj,text="Search",
         font=("Times New Roman",25),
         command=search_
         )

obj.mainloop()

