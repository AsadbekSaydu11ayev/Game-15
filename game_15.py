import tkinter as tk
import random,math
from PIL import ImageTk,Image
import sys; sys.setrecursionlimit(5000)
def quit():
    sys.exit()

root = tk.Tk()
img = ImageTk.PhotoImage(file="game_15.jpg")
root.iconphoto(False,img)
root.title("Game 15")
root.geometry("400x400")
tk.Label(root,text="Game 15",font=35).pack(pady=10)
buttons = []
numbers = ["None",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(numbers)
var=tk.IntVar()

def aks():
    for i in buttons:
        i.config(state='disable')
    v = var.get()
    soni = 0
    for s in buttons:
        global k
        if s["text"] == "None":
            k = soni
        soni+=1
    if v == 0:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v+1].config(state='active')
        buttons[v+4].config(state='active')
        
    if v == 1:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[0].config(state='active')
        buttons[2].config(state='active')
        buttons[5].config(state='active')
    if v == 2:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[1].config(state='active')
        buttons[3].config(state='active')
        buttons[6].config(state='active')
    if v == 3:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[2].config(state='active')
        buttons[7].config(state='active')
    if v == 4:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[0].config(state='active')
        buttons[8].config(state='active')
        buttons[5].config(state='active')
    if v == 5:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[1].config(state='active')
        buttons[4].config(state='active')
        buttons[6].config(state='active')
        buttons[9].config(state='active')
    if v == 6:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[2].config(state='active')
        buttons[5].config(state='active')
        buttons[7].config(state='active')
        buttons[10].config(state='active')
    if v == 7:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[3].config(state='active')
        buttons[6].config(state='active')
        buttons[11].config(state='active')
    if v == 8:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[4].config(state='active')
        buttons[9].config(state='active')
        buttons[12].config(state='active')
    if v == 9:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[5].config(state='active')
        buttons[8].config(state='active')
        buttons[10].config(state='active')
        buttons[13].config(state='active')
    if v == 10:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[6].config(state='active')
        buttons[9].config(state='active')
        buttons[11].config(state='active')
        buttons[14].config(state='active')
    if v == 11:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[7].config(state='active')
        buttons[10].config(state='active')
        buttons[15].config(state='active')
    if v == 12:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[8].config(state='active')
        buttons[13].config(state='active')
    if v == 13:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[9].config(state='active')
        buttons[12].config(state='active')
        buttons[14].config(state='active')
    if v == 14:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[10].config(state='active')
        buttons[13].config(state='active')
        buttons[15].config(state='active')
    if v == 15:
        buttons[k].config(text=buttons[v]["text"])
        if buttons[v]["text"] != "None":
            buttons[v].config(state='active',text='None')
        buttons[v].config(state='active')
        buttons[11].config(state='active')
        buttons[14].config(state='active')
    sonlar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"None"]
    sonlar2 = []
    b=0
    yutuq.pack_forget()
    for num in buttons:
        sonlar2.append(num["text"])
    if sonlar == sonlar2:
        yutuq.pack(pady=10)
    
def rand():
    random.shuffle(numbers)
    c = 0
    for n in numbers:
        buttons[c].config(text=n)
        c+=1
    var.set(numbers.index("None"))  
    
    
    
c = 0
for i in range(4):
    m = tk.Frame(root)
    for n in range(4):
        button = tk.Radiobutton(m,text=numbers[c],command=aks,variable=var,
                                value=c,indicatoron=0,width=6,height=3,
                                state='disable',font=10)
        button.pack(side='left')
        buttons.append(button)
        c += 1
    m.pack()
var.set(numbers.index("None"))  
ro = tk.Frame()
yutuq = tk.Label(ro,text="Siz yutdingiz",fg='red',font=35)
ro.pack()
son = tk.Button(root,text='Chiqish',command=quit,fg='red',font=15)
son.pack(side='left',pady=10)
tk.Button(root,text="Qayta boshlash",font=15,command=rand).pack(side='left',padx=4)
tk.Button(root,text="Boshlash",font=15,command=aks).pack(side='left')

root.mainloop()