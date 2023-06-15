import os,csv,time,numpy as np
############################# GUI MODULES #############################
######################### Main GUI Construction 
from tkinter import Menu,Frame,LabelFrame,Tk,messagebox,ttk,Toplevel,simpledialog
from ttkwidgets import CheckboxTreeview
######################### Relief Modules
from tkinter import FLAT,RIDGE,GROOVE,RAISED,SUNKEN
######################### Interaction Modules
from tkinter import Label,Entry,Text,scrolledtext,Button,Scrollbar
######################### Text,Treeview Modules
from tkinter import YES,NO,END,NORMAL,DISABLED
from prettytable import PrettyTable
######################### Scrollbar Modules
from tkinter import X,Y,BOTH,CENTER,RIGHT,VERTICAL
####################### NOTIFICATION MODULES ###########################
import gmail
from gmail import Message
from plyer import notification
######################## PDF & IMAGE MODULES ###########################
from fpdf import FPDF
from PIL import ImageTk,Image
########################################################################
##########################################from tkinter import filedialog

def billing_window():
    billing=Toplevel()
    billing.geometry('1366x768')
    billing.state('zoomed')
    billing.title('ASK BILLING S/W | BILLING DASHBOARD')
    billing.iconbitmap("C://ASK-BILLING-S-W//IMGS//BILLING_NOTIFICATION_LOGO.ico")
    billing.config(background='blue')
    bg_color='blue'
    title=LabelFrame(billing,bg=bg_color,bd=20,relief=RIDGE,width=1370,height=140)
    title.place(x=0,y=0,width=1366)
    ttk.Style().theme_use('vista')

    #######################################################################################
    ###################################### ORGANISATION LOGO ##############################
    #######################################################################################
    
    logo_image=ImageTk.PhotoImage(Image.open("C://ASK-BILLING-S-W//IMGS//BILLING_LOGO.png"))
    logo_img_label=Label(billing,image=logo_image,bg='blue',bd=5,relief=RAISED)
    logo_img_label.place(x=23,y=27,width=125,height=87)

    def print_organisation_name():
        organisation_name_label=Label(title,text='    ASK BILLING SOFTWARES    ',font=('Comic Sans MS',31,"bold"),pady=10,bd=5,relief=RAISED,bg=bg_color,fg="white")
        organisation_name_label.place(x=138,y=6)
    print_organisation_name()

    gst_no_label=Label(title,text='GST NUMBER: ',font=('Comic Sans MS',22,'bold'),bd=5,relief=FLAT,bg=bg_color,fg="white")
    gst_no_label.place(x=1089,y=5)
    gst_no=Label(title,text='ASK-BILLING-123',font=('Comic Sans MS',18,'bold'),bd=5,relief=FLAT,bg=bg_color,fg="white")
    gst_no.place(x=1078,y=45)
    
    current_date=time.strftime(' %d-%m-%Y ')
    date_label=Label(title,text=current_date,font=('Comic Sans MS',20,"bold"),bd=5,relief=RIDGE,bg=bg_color,fg="white")
    date_label.place(x=875,y=25)

    #######################################################################################
    #####################################  CUSTOMER DETAILS AREA ##########################
    #######################################################################################
    cust_details_frame=LabelFrame(billing,bd=10,relief=RIDGE,text=' CUSTOMER-DETAILS ',font=('Comic Sans MS',15,"bold"),fg="gold",bg=bg_color)
    cust_details_frame.place(x=0,y=137,width=1366,height=112)

    cust_name_label=Label(cust_details_frame,text="Customer Name: ",bd=5,bg=bg_color,fg="white",font=('Comic Sans MS',14,"bold"),relief=GROOVE)
    cust_name_label.place(x=1,y=15)
    cust_name_entry=Entry(cust_details_frame,bd=2,font=('Comic Sans MS',14,'bold'),relief=SUNKEN)
    cust_name_entry.place(x=175,y=15,width=200,height=39)
    cust_name_entry.insert(0,'   customer-name')
    cust_name_entry.config(state=DISABLED)

    cust_gst_label=Label(cust_details_frame,text='GST NO.: ',bd=5,bg=bg_color,fg="white",font=("Comic Sans MS",14,"bold"),relief=GROOVE)
    cust_gst_label.place(x=385,y=15)
    cust_gst_no_entry=ttk.Combobox(cust_details_frame,font=('Comic Sans MS',14,'bold'))
    cust_gst_no_entry['values']=('Not-Attempted')
    cust_gst_no_entry.current(0)
    cust_gst_no_entry.place(x=497,y=15,width=170,height=39)
    cust_gst_no_entry.config(state=DISABLED)
    
    cust_mob_no_label=Label(cust_details_frame,text="Mobile No.",bd=5,bg=bg_color,fg="white",font=('Comic Sans MS',14,"bold"),relief=GROOVE)
    cust_mob_no_label.place(x=677,y=15)
    mob_intl_code_combobox=ttk.Combobox(cust_details_frame,font=('Comic Sans MS',14,"bold"))
    mob_intl_code_combobox['values']=('+91','+1','+49')
    mob_intl_code_combobox.place(x=791,y=15,width=60,height=39)
    mob_intl_code_combobox.current(0)
    mob_intl_code_combobox.config(state='readonly')
    cust_mob_no_entry=Entry(cust_details_frame,width=10,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
    cust_mob_no_entry.place(x=852,y=15,width=128,height=39)

    cust_bill_label=Label(cust_details_frame,text="Bill no.",bd=5,bg=bg_color,fg="white",font=('Comic Sans MS',14,"bold"),relief=GROOVE)
    cust_bill_label.place(x=992,y=15,width=100)
    cust_bill_no_label=Entry(cust_details_frame,font=('Comic Sans MS',14,'bold'),bd=5,relief=GROOVE)
    cust_bill_no_label.place(x=1093,y=15,width=100,height=39)

    def update_cust_bill_no():
        bill_no_file=open('C://ASK-BILLING-S-W//AUTO_BILL_NO.txt','r')
        global bill_no_file_data
        bill_no_file_data=str(bill_no_file.read())
        bill_no_file_data=bill_no_file_data.split(' ')
        global cust_bill_no
        cust_bill_no=bill_no_file_data[0]
        cust_bill_no_label.config(state=NORMAL)
        cust_bill_no_label.delete(0,END)
        cust_bill_no_label.insert(0,'  '+cust_bill_no)
        cust_bill_no_label.config(state=DISABLED)
    update_cust_bill_no()
    
    def search_customer():
        if cust_mob_no_entry.get()=='':
            messagebox.showerror('ERROR !! ( Code - 101 )','MOBILE NO. IS REQUIRED...!!!')
        elif cust_mob_no_entry.get()!='':
            if len(cust_mob_no_entry.get())<10 or len(cust_mob_no_entry.get())>10:
                messagebox.showerror('ERROR !! ( Code - 102 )','Mobile No. is of 10 digits\n Please enter Mobile No. details correctly...')
            elif len(cust_mob_no_entry.get())==10:
                cust_mob_no_found=False
                with open('C://ASK-BILLING-S-W//AUTO_FILL_CUST_DETAILS.csv','r') as read_cust_detail_file:
                    cust_records_reader=list(csv.DictReader(read_cust_detail_file))
                    for cust_detail_row in cust_records_reader:
                        cust_mob_no_csv=cust_detail_row['CUSTOMER_MOBILE_NO.']
                        cust_name_csv=cust_detail_row['CUSTOMER_NAME']
                        cust_gst_no_csv=cust_detail_row['CUSTOMER_GST_NO.']
                        if "'"+cust_mob_no_entry.get()==cust_mob_no_csv:
                            cust_name_entry.config(state=NORMAL)
                            cust_name_entry.delete(0,END)
                            cust_name_entry.insert(0,cust_name_csv)
                            cust_name_entry.config(state='readonly')
                            cust_gst_no_entry.config(state=NORMAL)
                            cust_gst_no_entry.delete(0,END)
                            cust_gst_no_entry.insert(0,cust_gst_no_csv)
                            cust_gst_no_entry.config(state='readonly')
                            cust_mob_no_found=True
                if cust_mob_no_found==False:
                    with open('C://ASK-BILLING-S-W//AUTO_FILL_CUST_DETAILS.csv','a',newline='') as cust_detail_file:
                        if cust_name_entry.get()=='' or cust_name_entry.get()=='   customer-name':
                            cust_name_entry.config(state=NORMAL)
                            cust_name_entry.delete(0,END)
                            cust_gst_no_entry.config(state=NORMAL)
                            messagebox.showerror('ERROR !! ( Code - 101 )','PLEASE FILL NAME FOR FIRST-TIME CUSTOMERS...!!!')
                        elif cust_name_entry.get()!='':
                            file_writer=csv.writer(cust_detail_file)
                            cust_record="'"+cust_mob_no_entry.get(),cust_name_entry.get(),cust_gst_no_entry.get()
                            file_writer.writerow(cust_record)
    search_cust_details=Button(cust_details_frame,text="Search",command=search_customer,bd=5,font=('Comic Sans MS',18,'bold'),bg=bg_color,fg='white')
    search_cust_details.place(x=1218,y=15,width=100,height=49)

    #######################################################################################
    #####################################  ITEM DETAILS AREA  #############################
    #######################################################################################
    item_details_frame=LabelFrame(billing,bd=10,relief=RIDGE,text=' ITEM-DETAILS ',labelanchor='n',font=('Comic Sans MS',15,'bold'),fg='gold',bg=bg_color)
    item_details_frame.place(x=0,y=250,width=666,height=350)
    tree=CheckboxTreeview(item_details_frame,columns=('#0','#1'))
    tree.heading('#0',text='ITEM_NAME')
    tree.heading('#1',text='ITEM_PRICE (Rs.)')
    tree.heading('#2',text='QUANTITY')
    tree.column('#0',stretch=YES)
    tree.column('#1',stretch=YES,anchor='center')
    tree.column('#2',stretch=YES,anchor='center')
    
    tree.place(x=0,y=0,width=646,height=259)

    ttk.Style().configure('Treeview',font=('Courier New',14,'bold'))
    ttk.Style().configure('Treeview.Heading',font=('Courier New',14,'bold'))
    
    item_details_area_scrollbar=Scrollbar(tree,orient=VERTICAL,width=15,command=tree.yview)
    item_details_area_scrollbar.pack(side=RIGHT,fill=BOTH)
    tree.configure(yscrollcommand=item_details_area_scrollbar.set) 

    def update_quantity():
        update_quantity_row_id=tree.focus()
        new_quantity=simpledialog.askinteger('Input','Enter the new quantity: ')
        tree.set(update_quantity_row_id,'#2',new_quantity)
    def update_tree():
        for item_id_del in tree.get_children():
            tree.delete(item_id_del)
        with open('C://ASK-BILLING-S-W//ADD_DEL_ITEMS//item_records.csv','r') as items_file:
            item_records_reader=list(csv.DictReader(items_file))
            for item_row in item_records_reader[::-1]:
                item_name_csv=item_row['ITEM_NAME']
                item_price_csv=item_row['ITEM_PRICE']
                item_quantity_csv=item_row['QUANTITY']
                tree.insert('',0,text=item_name_csv,values=(item_price_csv,item_quantity_csv))
    update_tree()
    def select_tree():
        for check_item_id in tree.get_children():
            tree.change_state(check_item_id,'checked')
    def present_item_detail_popup(event): 
            try:
                tree_popup.tk_popup(event.x_root,event.y_root) 
            finally: 
                tree_popup.grab_release() 
    tree.bind("<Button-3>",present_item_detail_popup)
    tree_popup=Menu(billing,tearoff = 0)
    tree_popup.add_command(label='UPDATE ITEMS...',command=update_tree)
    tree_popup.add_command(label='SELECT ALL ITEMS...',command=select_tree)
    
    search_cust_details=Button(item_details_frame,text='UPDATE ITEMS',command=update_tree,bd=5,font=('Comic Sans MS',18,'bold'),bg=bg_color,fg='white')
    search_cust_details.place(x=0,y=260,width=290,height=49)
    search_cust_details=Button(item_details_frame,text='UPDATE QUANTITY',command=update_quantity,bd=5,font=('Comic Sans MS',18,'bold'),bg=bg_color,fg='white')
    search_cust_details.place(x=291,y=260,width=356,height=49)

    #######################################################################################
    #####################################  BILL DETAILS AREA  #############################
    #######################################################################################
    bill_details_frame=LabelFrame(billing,bd=10,relief=RIDGE,text=' BILL-DETAILS ',labelanchor='ne',font=('Comic Sans MS',15,'bold'),fg='gold',bg=bg_color)
    bill_details_frame.place(x=0,y=600,width=666,height=87)

    sub_total_label=Label(bill_details_frame,text='SUB-TOTAL: ',font=('Comic Sans MS',12,'bold'),bg=bg_color,fg='white',bd=5,relief=GROOVE)
    sub_total_label.place(x=0,y=5)
    show_sub_total=Entry(bill_details_frame,width=10,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
    show_sub_total.place(x=126,y=6,width=90)
    show_sub_total.insert(0,'sub-total')
    show_sub_total.config(state=DISABLED)
    tax_label=Label(bill_details_frame,text='TAX @ 5%: ',font=('Comic Sans MS',12,'bold'),bg=bg_color,fg='white',bd=5,relief=GROOVE)
    tax_label.place(x=218,y=5)
    show_tax=Entry(bill_details_frame,width=10,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
    show_tax.place(x=332,y=6,width=75)
    show_tax.insert(0,'tax')
    show_tax.config(state=DISABLED)
    total_amt_label=Label(bill_details_frame,text='TOTAL-AMT: ',font=('Comic Sans MS',12,'bold'),bg=bg_color,fg='white',bd=5,relief=GROOVE)
    total_amt_label.place(x=410,y=5)
    show_total_amt=Entry(bill_details_frame,width=10,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
    show_total_amt.place(x=540,y=6,width=103)
    show_total_amt.insert(0,'total-amt')
    show_total_amt.config(state=DISABLED)
    
    #######################################################################################
    #####################################  BILL UTILITY AREA  #############################
    #######################################################################################
    bill_area_frame=LabelFrame(billing,text=' BILL-AREA ',labelanchor='n',font=('Comic Sans MS',15,'bold'),bg=bg_color,fg='gold',bd=10,relief=RIDGE)
    bill_area_frame.place(x=671,y=250,width=694,height=378)
   
    def bill_util_area():     
        txtarea=Text(bill_area_frame,wrap='none',bg=bg_color,fg='white',font=('Courier New',12,'bold'),bd=10,relief=FLAT) 
        txtarea.pack(fill=BOTH,expand=True)
        txtarea_Y_scrollbar=Scrollbar(txtarea,orient='vertical',width=15,command=txtarea.yview)
        txtarea_Y_scrollbar.pack(side=RIGHT,fill=Y)
        txtarea.configure(yscrollcommand=txtarea_Y_scrollbar.set)
        txtarea_X_scrollbar=Scrollbar(txtarea,orient='horizontal',width=15,command=txtarea.xview)
        txtarea_X_scrollbar.pack(side='bottom',fill=X)
        txtarea.configure(xscrollcommand=txtarea_X_scrollbar.set)
        txtarea.config(state=DISABLED)

        bill=PrettyTable()
        
        bill_util_area_frame=LabelFrame(billing,bd=10,relief=RIDGE,bg="blue")
        bill_util_area_frame.place(x=672,y=631,width=490,height=55)
        def total():
            global tree_data_list
            tree_data_list=[]
            tree_data=tree.get_checked()
            for tree_item in tree_data:
                tree_data_list.append([tree.item(tree_item)['text'],tree.item(tree_item)['values'][0],tree.item(tree_item)['values'][1]])
        def clear_all_fields():
            cust_name_entry.config(state=NORMAL)
            cust_name_entry.delete(0,END)
            cust_name_entry.insert(0,'   customer-name')
            cust_name_entry.config(state=DISABLED)
            cust_mob_no_entry.config(state=NORMAL)
            cust_mob_no_entry.delete(0,END)
            cust_gst_no_entry.config(state=NORMAL)
            cust_gst_no_entry.delete(0,END)
            cust_gst_no_entry.current(0)
            cust_gst_no_entry.config(state=DISABLED)
            show_sub_total.config(state=NORMAL)
            show_sub_total.delete(0,END)
            show_tax.config(state=NORMAL)
            show_tax.delete(0,END)
            show_total_amt.config(state=NORMAL)
            show_total_amt.delete(0,END)
            bill_no_file=open("C://ASK-BILLING-S-W//AUTO_BILL_NO.txt",'r')
            bill_no_file_data=str(bill_no_file.read())
            bill_no_file_data=bill_no_file_data.split(' ')
            update_cust_bill_no()
            txtarea.config(state=NORMAL)
            txtarea.delete('1.0',END)
            txtarea.config(state=DISABLED)
            bill.clear_rows()
            update_tree()
        clear_btn=Button(bill_util_area_frame,text="CLEAR",bg=bg_color,fg="white",command=clear_all_fields,width=7,font=('Comic Sans MS',12,))
        clear_btn.place(x=0,y=0,height=35)
        
        def build_bill_data_and_save():
            def bill_template():
                cust_mob_no=mob_intl_code_combobox.get()+'-'+cust_mob_no_entry.get()
                txtarea.insert(END,'           Welcome to ASK BILLING SOFTWARES !!')
                txtarea.insert(END,'\n             23, RAJPUR ROAD, DELHI - 110054')
                txtarea.insert(END,f'\n               GST NO. : ASK-BILLING-123')
                txtarea.insert(END,f'\n\n Bill No. : {cust_bill_no}')
                txtarea.insert(END,f'            DATE     :  {current_date}')
                txtarea.insert(END,f'\n GST No.  : {cust_gst_no_entry.get()}')
                txtarea.insert(END,f'   Mob. No. : {cust_mob_no}')
                txtarea.insert(END,f'\n Customer Name : {cust_name_entry.get()}')
                txtarea.insert(END,'\n')
                
            def bill_data():
                txtarea.config(state=NORMAL)
                bill_template()
                total()
                list=[]
                item_count=1
                bill.field_names=['S.NO.','ITEM-NAME','QUANTITY','PRICE (Rs.)','AMOUNT (Rs.)']
                for bill_item_headers in tree_data_list:
                    bill.add_row([str(item_count)+'.',bill_item_headers[0],bill_item_headers[2],bill_item_headers[1],str(int(bill_item_headers[2])*int(bill_item_headers[1]))])
                    item_count+=1
                    list.append(int(bill_item_headers[2])*int(bill_item_headers[1]))
                sub_total=sum(list)
                tax=int((5/100)*sum(list))
                total_amt=sum(list)+tax
                txtarea.insert(END,bill)
                txtarea.insert(END,f'\n\tSUB-TOTAL: Rs. {sub_total}    +    TAX @ 5%: Rs. {tax}')
                txtarea.insert(END,f'\n\t       = TOTAL AMOUNT: Rs. {total_amt}')
                def update_bill_details():
                    show_sub_total.config(state=NORMAL)
                    show_sub_total.delete(0,END)
                    show_sub_total.insert(0,str(sub_total))
                    show_sub_total.config(state=DISABLED)
                    
                    show_tax.config(state=NORMAL)
                    show_tax.delete(0,END)
                    show_tax.insert(0,str(tax))
                    show_tax.config(state=DISABLED)
                    
                    show_total_amt.config(state=NORMAL)
                    show_total_amt.delete(0,END)
                    show_total_amt.insert(0,str(total_amt))
                    show_total_amt.config(state=DISABLED)
                update_bill_details()
                txtarea.insert(END,f'\n\n           Thank you for purchasing with us...!!')
                txtarea.insert(END,f'\n                Please Come again.....!!')
            def generate_bill():        
                invoice_data=txtarea.get('1.0',END)
                global invoice_file_path
                invoice_file_path='C://ASK-BILLING-S-W//INVOICES_GENERATED//invoice_for_'+cust_bill_no
                invoice=open(invoice_file_path+'.txt','w')
                invoice.write(str(invoice_data))
                invoice.close()
                txtarea.config(state=DISABLED)

                invoice_pdf=FPDF('P','mm',np.array([165,250]))
                invoice_pdf.add_page()
                invoice_pdf.set_font('COURIER',size=12)
                invoice_txt=open(invoice_file_path+'.txt','r')
                for invoice_txt_data in invoice_txt:
                    invoice_pdf.cell(200,5,txt=invoice_txt_data,ln=1)
                invoice_pdf.output(invoice_file_path+'.pdf')
                notification.notify(title='Bill No.: '+cust_bill_no+' Saved',message='Bill No.: '+cust_bill_no+' saved at '+invoice_file_path+'.pdf',
                                    app_name='ASK BILLING S/W BILLING Notifier',timeout=100,toast=True,
                                    app_icon="C://ASK-BILLING-S-W//IMGS//BILLING_NOTIFICATION_LOGO.ico")
                invoice_txt.close()
                os.remove(invoice_file_path+'.txt')
                
                bill_no_data=open('C://ASK-BILLING-S-W//AUTO_BILL_NO.txt','w')
                bill_no_data.write(str(int(bill_no_file_data[0])+1))
            search_customer()
            total()
            if cust_mob_no_entry.get()!='' and len(cust_mob_no_entry.get())==10 and tree_data_list!=[]:
                bill_data()
                generate_bill()
            elif tree_data_list==[]:
                messagebox.showerror('ERROR !! ( Code - 101 )','PLEASE SELECT ONE OR MORE ITEMS.....!!!')        
        
        generate_bill_and_save=Button(bill_util_area_frame,text="GENERATE BILL",command=build_bill_data_and_save,bg=bg_color,fg="white",width=15,font=('Comic Sans MS',12))
        generate_bill_and_save.place(x=86,y=0,height=35)
        
        exit_btn=Button(bill_util_area_frame,text="EXIT",bg=bg_color,fg="white",command=billing.destroy,width=7,font=('Comic Sans MS',12))
        exit_btn.place(x=389,y=0,height=35)

        def send_mail():
            mail_app=Toplevel()
            mail_app.title('ASK BILLING S/W | SEND e- BILL...')
            mail_app.config(background='blue')
            mail_app.geometry('595x213')

            def send_bill():
                mail_text=f'''<h2>Hello, With reference to your shopping at ASK BILLING S/W on {current_date},
            we have sent you the BILL attached with this mail to confirm your BILL and the payment against it...</h2>

            <h3>Thanks,
            Team ASK BILLING S/W</h3>'''
                attachment=invoice_file_path+'.pdf'
                gmail_entry= gmail.GMail(f'ASK BILLING S/W <{from_mail.get()}>',from_password.get())
                msg = Message(f'Re: e-Bill for your shopping with ASK BILLING S/W dated {current_date}',to=to_mail.get(),html=mail_text,attachments=[attachment])
                gmail_entry.send(msg)
                notification.notify(title='Bill No.: '+cust_bill_no+' SENT...',message='Bill No.: '+cust_bill_no+f' sent to {to_mail.get()}',
                                    app_name='ASK BILLING S/W e-mail Notifier',timeout=100,toast=True,
                                    app_icon="C://ASK-BILLING-S-W//IMGS//BILLING_NOTIFICATION_LOGO.ico")

            def reset_entries():
                from_mail.delete(0,'end')
                from_password.delete(0,'end')
                to_mail.delete(0,'end')

            Label(mail_app, text="Sender's email",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=0)
            from_mail= Entry(mail_app,width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
            from_mail.place(x=253,y=0,height=36)

            Label(mail_app, text="Sender's email password: ",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=41)
            from_password= Entry(mail_app,show="*",width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
            from_password.place(x=253,y=41,height=36)

            Label(mail_app, text="Receiver's email",width=20,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=5,relief=RIDGE).place(x=0,y=90)
            to_mail= Entry(mail_app,width=28,font=('Comic Sans MS',14,'bold'),bd=2,relief=SUNKEN)
            to_mail.place(x=253,y=90,height=36)

            Button(mail_app, text="SEND e- BILL", command=send_bill,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE).place(x=0, y=150,width=295)
            Button(mail_app, text="RESET ENTRIES", command=reset_entries,font=('Comic Sans MS',14,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE).place(x=299,y=150,width=297)

            mail_app.resizable(False,False)
            mail_app.mainloop()
        send_mail_button=Button(bill_util_area_frame,text='SEND e- BILL',bg=bg_color,fg="white",command=send_mail,width=12,font=('Comic Sans MS',12,))
        send_mail_button.place(x=251,y=0,height=35)
        
        def present_bill_util_popup(event): 
            try:
                bill_util_popup.tk_popup(event.x_root,event.y_root) 
            finally: 
                bill_util_popup.grab_release() 
        txtarea.bind("<Button-3>",present_bill_util_popup)
        tree_popup=Menu(billing,tearoff = 0)
        tree_popup.add_command(label='UPDATE ITEMS...',command=update_tree)
        bill_util_popup=Menu(billing,tearoff = 0)
        bill_util_popup.add_command(label='CLEAR BILL-AREA',command=lambda: clear_all_fields())
        bill_util_popup.add_command(label='GENERATE BILL',command=lambda: build_bill_data_and_save())
    
    def reset_numbering():
        new_numbering=simpledialog.askstring('Input','Enter the no. to start bill numbering from: ')
        if new_numbering==None:
            messagebox.showerror('ERROR !! ( Code - 101 )','Please fill the starting no. for\n automatic bill numbering...!!')
        elif new_numbering!='':
            with open('C://ASK-BILLING-S-W//AUTO_BILL_NO.txt','w') as bill_numbering_file:
                bill_numbering_file.write(new_numbering)
        update_cust_bill_no()
    menubar = Menu(billing)
    def add_del_items():
        import add_del_item_records
        add_del_item_records.add_del_item_record()
    menubar.add_cascade(label='INSERT or DELETE ITEM(s)',command=add_del_items)
    menubar.add_separator()
    menubar.add_cascade(label='Reset Bill Numbering',command=reset_numbering)
    billing.config(menu=menubar)
    
    popup_menu = Menu(billing,tearoff = 0)
    popup_menu.add_command(label='DEVELOPED BY:') 
    popup_menu.add_separator()
    popup_menu.add_command(label='    KONARK MITTAL')
    popup_menu.add_command(label='    SUJAL JINDAL')
    popup_menu.add_command(label='    AARYAN SAHU')
    
    def present_developers_popup(event): 
        try:
            popup_menu.tk_popup(event.x_root,event.y_root) 
        finally: 
            popup_menu.grab_release() 
    billing.bind("<Button-3>",present_developers_popup)
    def calc():
        import CALC
        CALC.calc_window()
    Button(billing,text="CALCULATOR",command=calc,font=('Comic Sans MS',17,"bold"),bd=5,relief=GROOVE,bg=bg_color,fg="white").place(x=1169,y=632,width=190,height=50)
    billing.bind('<Alt-C>',lambda EVENT: calc())
    billing.bind('<Alt-c>',lambda EVENT: calc())
    menubar.add_separator()
    menubar.add_cascade(label='CALCULATOR',command=calc)
    def help_ask():
        help_window=Toplevel()
        help_window.geometry('350x200')
        help_window.title('ASK BILLING S/W | HELP')
        help_txtarea=scrolledtext.ScrolledText(help_window,bg=bg_color,fg='white',font=('Courier New',12,'bold'),bd=10,relief=FLAT) 
        help_txtarea.pack(fill=BOTH,expand=True)
        help_txtarea.insert(END,'''        ASK BILLING S/W

CREATED FOR
CBSE CLASS-XII
COMPUTER SCIENCE PROJECT BY:-

    1. KONARK MITTAL
    2. SUJAL JINDAL
    3. AARYAN SAHU

1. BEST VIEWED IN 1366x768 SCRE    -EN RESOLUTION''')
        help_window.resizable(False,False)
        help_txtarea.config(state=DISABLED)
    menubar.add_separator()
    menubar.add_cascade(label='HELP',command=help_ask)
    bill_util_area()
    billing.mainloop()
billing_window()
