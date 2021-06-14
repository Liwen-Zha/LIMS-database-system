# This version of the project focuses on the backend design.
# Backend: neo4j database (later will be integrated into the Flask framework)
# Frontend: tkinter module

from tkinter import *
import time
import backend_2

def get_selected_data(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)

    input_type.delete(0,END)
    input_type.insert(END,selected_row[0])
    input_sID.delete(0,END)
    input_sID.insert(END,selected_row[1])
    input_loc.delete(0,END)
    input_loc.insert(END,selected_row[2])
    input_status.delete(0,END)
    input_status.insert(END,selected_row[3])
    input_q.delete(0,END)
    input_q.insert(END,selected_row[4])
    input_unit.delete(0,END)
    input_unit.insert(END,selected_row[5])
    input_custodian.delete(0,END)
    input_custodian.insert(END,selected_row[6])

def auto_delete():
    input_type.delete(0,END) 
    input_sID.delete(0,END)   
    input_loc.delete(0,END)   
    input_status.delete(0,END)  
    input_q.delete(0,END)   
    input_unit.delete(0,END)  
    input_custodian.delete(0,END)

now_time = ''
def get_time():
    global now_time
    now_time = time.strftime('%d/%m/%Y - %H:%M:%S',time.localtime(time.time()))
    show_time.configure(text=now_time)
    window.after(500, get_time)

def add_command():
    backend_2.insert(sample_type.get(), sample_ID.get(), storage_loc.get(), status.get(),
                     quantity.get(), unit.get(), custodian.get(), now_time)

    list.delete(0,END)
    list.insert(END,(sample_type.get(), sample_ID.get(), storage_loc.get(), status.get(),
                     quantity.get(), unit.get(), custodian.get(), 'Date & time:' + now_time))

    auto_delete()

def search_command():
    list.delete(0,END)

    search_result = backend_2.search(sample_type.get(), sample_ID.get(), storage_loc.get(), status.get(),
                                quantity.get(), unit.get(), custodian.get())
    if search_result:
        for row in backend_2.search(sample_type.get(), sample_ID.get(), storage_loc.get(), status.get(),
                                quantity.get(), unit.get(), custodian.get()): # now_time):
            list.insert(END,row)
    else:
        list.insert(END, 'Cannot search records with the entered criteria! Please re-enter.')
        auto_delete()

'''def check_command():
    ...'''

def view_command():
    list.delete(0,END)
    for row in backend_2.view():
        list.insert(END,row)

window = Tk()
window.title('LIMS - Sample logbook')
window.geometry("1000x300")

label_type = Label(window, text='Sample Type')
label_type.grid(row=0,column=0)
sample_type = StringVar()
input_type = Entry(window, textvariable=sample_type)
input_type.grid(row=0,column=1)

# Better way: automatically generate sample ID
label_sID = Label(window, text='Sample ID')
label_sID.grid(row=0,column=2)
sample_ID = StringVar()
input_sID = Entry(window, textvariable=sample_ID)
input_sID.grid(row=0,column=3)

'''label_genealogy = Label(window, text='Genealogy') # sample, subsample
label_genealogy .grid(row=1,column=0)
genealogy = StringVar()
input_genealogy = Entry(window, textvariable=genealogy)
input_genealogy.grid(row=1,column=1)

label_pID = Label(window, text='Parent ID')
label_pID .grid(row=1,column=2)
parent_ID = StringVar()
input_pID = Entry(window, textvariable=parent_ID)
input_pID.grid(row=1,column=3)'''

label_loc = Label(window, text='Storage Location')
label_loc.grid(row=1,column=0)
storage_loc = StringVar()
input_loc = Entry(window, textvariable=storage_loc)
input_loc.grid(row=1,column=1)

label_status = Label(window, text='Status') # in use, reserved, available
label_status.grid(row=1,column=2)
status = StringVar()
input_status = Entry(window, textvariable=status)
input_status.grid(row=1,column=3)

label_q = Label(window, text='Quantity')
label_q.grid(row=2,column=0)
quantity = StringVar()
input_q = Entry(window, textvariable=quantity)
input_q.grid(row=2,column=1)

label_unit = Label(window, text='Unit')
label_unit.grid(row=2,column=2)
unit = StringVar()
input_unit= Entry(window, textvariable=unit)
input_unit.grid(row=2,column=3)

label_custodian = Label(window, text='Custodian')
label_custodian.grid(row=3,column=0)
custodian = StringVar()
input_custodian= Entry(window, textvariable=custodian)
input_custodian.grid(row=3,column=1)

label_time = Label(window, text='Date & Time:', fg='blue', font=('Times', 16, 'bold', 'italic'))
label_time.grid(row=3,column=2)
show_time = Label(window, text='', fg='blue', font=('Times', 16, 'bold', 'italic'))
show_time.grid(row=3,column=3)
get_time()

list = Listbox(window,height=10,width=77)
list.grid(row=4,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(window)
sb.grid(row=4,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_data)

button_add = Button(window,text='Add log',width=15,pady=5,command=add_command)
button_add.grid(row=4,column=3)

button_search = Button(window,text='Search log',width=15,pady=5,command=search_command)
button_search.grid(row=5,column=3)

'''button_check = Button(window,text='Check sample',width=15,pady=5,command=check_command)
button_check.grid(row=6,column=3)'''

button_view = Button(window,text='View all logs',width=15,pady=5,command=view_command)
button_view.grid(row=7,column=3)

button_close = Button(window,text='Close',width=15,pady=5,command = window.destroy)
button_close.grid(row=8,column=3)

window.mainloop()

