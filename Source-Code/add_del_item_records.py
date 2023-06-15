import csv
import tkinter.ttk as ttk
from tkinter.ttk import Treeview
from tkinter import Toplevel,Label,Entry,Button
from tkinter import X,Y,BOTH,YES,END,FLAT,GROOVE,SUNKEN,RIGHT,VERTICAL,Scrollbar

def add_del_item_record():
    add_del_item_records_appl=Toplevel()
    add_del_item_records_appl.title('INSERT or DELETE ITEM(s): ')
    add_del_item_records_appl.geometry('600x326')
    add_del_item_records_appl.config(background='blue')

    item_name_label=Label(add_del_item_records_appl,text='ITEM_NAME: ',font=('Comic Sans MS',12,'bold'),bg='blue',fg='white',relief=FLAT)
    item_name_entry=Entry(add_del_item_records_appl,font=('Comic Sans MS',12,'bold'),bd=2,relief=SUNKEN)
    item_name_label.place(x=0,y=0)
    item_name_entry.place(x=122,y=0)

    item_price_label = Label(add_del_item_records_appl,text='ITEM_PRICE: ',font=('Comic Sans MS',12,'bold'),bg='blue',fg='white',relief=FLAT)
    item_price_entry = Entry(add_del_item_records_appl,font=('Comic Sans MS',12,'bold'),bd=2,relief=SUNKEN)
    item_price_label.place(x=0,y=40)
    item_price_entry.place(x=122,y=40)
            
    def insert_record():
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_id.txt','r') as item_id_file:
            item_id=int(item_id_file.read())
            with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//tree_row_id.txt','r') as tree_row_id_file:
                tree_row_id=int(tree_row_id_file.read())
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_records.csv','a',newline='') as file:
            file_writer=csv.writer(file)
            tree.insert('',tree_row_id,text='ITEM_'+str(item_id),values=(item_name_entry.get(),'Rs. '+str(item_price_entry.get())))
            item_record=item_id,item_name_entry.get(),item_price_entry.get(),1
            file_writer.writerow(item_record)
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_id.txt','w+') as item_id_file:
            item_id_file.write(str(item_id+1))
            with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//tree_row_id.txt','w+') as tree_row_id_file:
                tree_row_id_file.write(str(tree_row_id+1))
        item_name_entry.delete(0,END)
        item_price_entry.delete(0,END)
        
    def delete_record():
        row_id=tree.focus()
        item_to_be_del=tree.item(row_id)
        lines = list()
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_records.csv','r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == item_to_be_del['values'][0]:
                        lines.remove(row)
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_records.csv','w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        tree.delete(row_id)

    insert_record_button=Button(add_del_item_records_appl,text='INSERT ITEM...',command=insert_record,font=('Comic Sans MS',10,'bold'),bg='blue',fg='white',bd=5,relief=GROOVE)
    insert_record_button.place(x=450,y=0,width=150)

    delete_button = Button(add_del_item_records_appl,text='DELETE ITEM...',command=delete_record,font=('Comic Sans MS',10,'bold'),bg='blue',fg='white',bd=5,relief=GROOVE)
    delete_button.place(x=450,y=40,width=150)

    tree = Treeview(add_del_item_records_appl, columns=('#0','#1','#2'))
    tree.heading('#0',text='ITEM_ID')
    tree.heading('#1',text='ITEM_NAME')
    tree.heading('#2',text='ITEM_PRICE')
    tree.column('#0',stretch=YES)
    tree.column('#1',stretch=YES)
    tree.column('#2',stretch=YES)

    tree.place(x=0,y=100,width=601,height=227)

    ttk.Style().configure('Treeview',font=('Courier New',14,'bold'))
    ttk.Style().configure('Treeview.Heading',font=('Courier New',14,'bold'))

    area_scrollbar=Scrollbar(tree,orient=VERTICAL,width=15,command=tree.yview)
    area_scrollbar.pack(side=RIGHT,fill=Y)
    tree.configure(yscrollcommand=area_scrollbar.set)

    with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_records.csv','r') as items_file:
        item_records_reader=list(csv.DictReader(items_file))
        for item_row in item_records_reader[::-1]:
            item_id_csv=item_row['ITEM_ID']
            item_name_csv=item_row['ITEM_NAME']
            item_price_csv=item_row['ITEM_PRICE']
            tree.insert('',0,text='ITEM_'+item_id_csv,values=(item_name_csv,'Rs. '+item_price_csv))
            
    add_del_item_records_appl.resizable(False,False)
    add_del_item_records_appl.mainloop()
