from tkinter import *
from tkinter import messagebox
from tkinter import ttk


all_data=[]


def search_table():
    search_number=number_search_var.get().strip()
    owner_search=owner_search_var.get().strip()
    for row in table.get_children():
        table.delete(row)
    for item in all_data:
        number_match=search_number in (item[0])
        owner_match=owner_search in (item[1])
        if number_match and owner_match:
            table.insert("", "end", values=item)

def select_sim_cards(event):

    table_row=table.focus()
    if not table_row:
        return
    selected=table.item(table_row)["values"]
    number.set(selected[0])
    operator.set(selected[1])
    owner.set(selected[2])
    register_data.set(selected[3])
    charge.set(selected[4])
def save_click():
    info={
        "number":number.get(),
        "owner":owner.get(),
        "operator":operator.get(),
        "register_data":register_data.get(),
        "charge":charge.get(),

    }
    all_data.append(info)
    print(all_data)
    number.set(0)
    owner.set("")
    operator.set("")
    register_data.set("")
    charge.set(0)

    table.insert("", END, values=tuple(info.values()))


def remove_click():
    selected_item=table.focus()
    if not selected_item:
        print("you didnt select the item")
        return
    table.delete(selected_item)
    print("removed")

def edit_click():
    selected_item = table.focus()
    if not selected_item:
        print("you didnt select the item")
        return
    table.item(selected_item,values=(number.get(),owner.get(),operator.get(),register_data.get(),charge.get()))
    print("edited")

window=Tk()
window.title("simcards")
window.configure(background="orange")
window.geometry("710x400")
window.resizable(False, False)


#number

Label(window, text="number",bg="orange").place(x=20,y=20)
number=IntVar()
Entry(window, textvariable=number).place(x=85,y=20)
number.set(0)


#owner
Label(window, text="owner",bg="orange").place(x=20,y=50)
owner=StringVar()
Entry(window, textvariable=owner).place(x=85,y=50)
owner.set("")

#register_data
Label(window, text="register_data",bg="orange").place(x=0,y=80)
register_data=StringVar()
Entry(window, textvariable=register_data).place(x=85,y=80)
register_data.set("")


#operator
Label(window, text="operator",bg="orange").place(x=20,y=110)
operator=StringVar()
Entry(window, textvariable=operator).place(x=85,y=110)

operator.set("")

#charge
Label(window, text="charge",bg="orange").place(x=20,y=140)
charge=StringVar()
Entry(window, textvariable=charge).place(x=85,y=140)
charge.set(0)




#number_search_var
Label(window, text="number_search_var",bg="orange").place(x=225,y=10)
number_search_var=StringVar()
Entry(window, textvariable=number_search_var).place(x=340,y=10)



#owner_search_var
Label(window, text="owner_search_var",bg="orange").place(x=485,y=10)
owner_search_var=StringVar()
Entry(window, textvariable=owner_search_var).place(x=585,y=10)

#Buttons
Button(window,text="save",command=save_click,width=6,bg="orange").place(x=20,y=300)
Button(window,text="remove",command=remove_click,width=6,bg="orange").place(x=80,y=300)
Button(window,text="edit",command=edit_click,width=6,bg="orange").place(x=140,y=300)
Button(window,text="search",command=search_table,width=6,bg="orange").place(x=400,y=330)



table=ttk.Treeview(window,height=12,columns=(0,1,2,3,4),show="headings")

table.column(0, width=70)
table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=80)
table.column(4, width=80)

table.heading(0, text="number")
table.heading(1, text="owner")
table.heading(2, text="register_data")
table.heading(3, text="operator")
table.heading(4, text="charge")

table.bind("<<TreeviewSelect>>",select_sim_cards)
table.place(x=250, y = 60)








window.mainloop()