import Pmw,time
from os import path
import PySimpleGUI as pg
from PIL import ImageTk,Image
from tkinter import Toplevel,ttk,Label,GROOVE,Entry,SUNKEN,Button,messagebox,colorchooser,END

def login_window():
    #############################################################################################
    ##################################### Register / Log-in frame Design ########################
    #############################################################################################
    
    log_window=Toplevel()
    log_window.title('ASK BILLING S/W  |  REGISTER / LOG-IN WINDOW')
    log_window.geometry('1366x768')
    log_window.state('zoomed')

    choose_bg_color='blue'
    log_window.configure(background=choose_bg_color)
    
    bg_img=ImageTk.PhotoImage(file="C://ASK-BILLING-S-W//IMGS//LOGIN_LOGO.png")
    bg_img_lbl=Label(log_window,image=bg_img,bg=choose_bg_color).place(x=350,y=425)

    help_msg=Pmw.Balloon(log_window)
    
    Label(log_window,text='  Register Here |   Login Here    ',font=('Comic Sans MS',55,'bold'),bg='skyblue',bd=15,relief=GROOVE).place(x=50,y=30)  
    reqd_fiels=Label(log_window,text='Fields marked with ** are required...!!',font=('Comic Sans MS',20,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=450,y=380)
    def login_window(log_window):
        #############################################################################################
        #################################### Registering user :- getting credentials ################
        #############################################################################################
        create_user_name_label=Label(log_window,text='Enter your user-name:**  ',font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=60,y=201)
        create_user_name=Entry(log_window,font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=SUNKEN)
        create_user_name.insert(0,'           GUEST')
        create_user_name.place(x=360,y=201)
        create_user_key_label=Label(log_window,text='Enter your pass-word:**  ',font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=60,y=301)
        create_user_key=Entry(log_window,font=('Comic Sans MS',18,'bold'),show='*',bg='skyblue',bd=7,relief=SUNKEN)
        create_user_key.insert(0,'ASK-BILLING-S/W-by-ASK')
        create_user_key.place(x=360,y=301)
##        forgot_pwd=
##        reset_pwd=
##        forgot_user_name=
##        reset_user_name=
        def register_user():
            user_name=create_user_name.get()
            user_key=create_user_key.get()
            user_data_file="C://ASK-BILLING-S-W//USER_DATA//log_file_of_user--"+user_name+'.txt'
            if user_name=='' and user_key=='':
                error_in_regn=messagebox.showerror('ERROR !!','user-name & pass-word fields are required...!!')
            elif user_name!='' and user_key!='':
                if path.exists(user_data_file)==False:
                    create_user_data_file=open(user_data_file,'w')
                    user_data=user_name+'\n'+user_key
                    create_user_data_file.write(user_data)
                    show_msg='You have been successfully registered.....!!\n\nYour user-details are as follows :\n'+'user-name: '+user_name+'\npass-word: '+user_key
                    regd=messagebox.showinfo('Successfull Registration !!',show_msg)
                    create_user_name.delete(0,END)
                    create_user_key.delete(0,END)
                else:
                    user_already_regd_error=messagebox.showerror('ERROR !!','''The details of user given is already registered...
Proceed to log-in page......''')
        regn_button=Button(log_window,text='Register !!',command=register_user,font=('Comic Sans MS',20,'bold'),fg="white",bg="#d77337",bd=10,relief=GROOVE)
        regn_button.place(x=270,y=450)
        help_msg.bind(regn_button,'Register your username and password \nto access billing dashboard...!!')
        log_window.bind('<Alt-R>',lambda EVENT: register_user())
        log_window.bind('<Alt-r>',lambda EVENT: register_user())
        ##############################################################################################
        ##################################### Registered user :- getting credentials #################
        ##############################################################################################
        regd_user_name_label=Label(log_window,text='Enter your user-name:**  ',font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=690,y=201)
        regd_user_name=Entry(log_window,font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=SUNKEN)
        regd_user_name.insert(0,'           GUEST')
        regd_user_name.place(x=990,y=201)
        regd_user_key_label=Label(log_window,text='Enter your pass-word:**  ',font=('Comic Sans MS',18,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=690,y=301)
        regd_user_key=Entry(log_window,font=('Comic Sans MS',18,'bold'),show='*',bg='skyblue',bd=7,relief=SUNKEN)
        regd_user_key.insert(0,'ASK-BILLING-S/W-by-ASK')
        regd_user_key.place(x=990,y=301)
        def login_user():                                                                                                                   
            user_name=regd_user_name.get()
            user_key=regd_user_key.get()
            user_data_file='C://ASK-BILLING-S-W//USER_DATA//log_file_of_user--'+user_name+".txt"
            if user_name=='' and user_key=='':
                error_in_login=messagebox.showerror('ERROR !!','user-name & pass-word fields are required...!!')
            elif user_name!='' and user_key!='':
                if path.exists(user_data_file)==True:
                    regd_user_data_file=open(user_data_file,'r')
                    regd_user_data=str(regd_user_data_file.read())
                    regd_user_data=regd_user_data.split('\n')
                    get_user_name=regd_user_data[0]
                    get_user_key=regd_user_data[1]
                    if get_user_name==user_name and get_user_key==user_key:
                        logged=messagebox.showinfo('Successfull Login !!','You have successfully logged onto the dashboard.....!!')
                        regd_user_name.delete(0,END)
                        regd_user_key.delete(0,END)

                        for i in range(1,103,1):
                            progress=pg.one_line_progress_meter('LOADING......',current_value=i,max_value=100,orientation='h')
                            time.sleep(0.01)
                        if progress==False:
                            log_window.state('withdrawn')
                            import BILLING_WINDOW
                    elif get_user_name!=user_name and get_user_key!=user_key:
                        error_in_login=messagebox.showerror('ERROR !!','INVALID user-name and pass-word...!!')
                        login_error_msg=messagebox.showerror('ERROR !!','Please check all the fields are filled correctly...')
                    elif get_user_name!=user_name:
                        error_in_login=messagebox.showerror('ERROR !!','INVALID user-name...!!')
                        login_error_msg=messagebox.showerror('ERROR !!','Please check all the fields are filled correctly...')
                    elif get_user_key!=user_key:
                        error_in_login=messagebox.showerror('ERROR !!','INVALID pass-word...!!')
                        login_error_msg=messagebox.showerror('ERROR !!','Please check all the fields are filled correctly...')
                else:
                    user_not_regd_error=messagebox.showerror('ERROR !!','''The details of user given are not registered...
Please register yourself first at the register page.....''')
        login_button=Button(log_window,text='Login !!',command=login_user,font=('Comic Sans MS',20,'bold'),fg="white",bg="#d77337",bd=10,relief=GROOVE)
        login_button.place(x=900,y=450)
        help_msg.bind(login_button,'Log-in with your username and password \n(given by you at the time of registration) \nto access billing dashboard...!!')
        log_window.bind('<Alt-L>',lambda EVENT: login_user())
        log_window.bind('<Alt-l>',lambda EVENT: login_user())
        def color():
            choose_bg_color=colorchooser.askcolor(title="Choose color for your background: ")
            log_window.configure(background=choose_bg_color[1])
            bg_img_lbl=Label(log_window,image=bg_img,bg=choose_bg_color[1]).place(x=350,y=425)
            reqd_fiels=Label(log_window,text='Fields marked with ** are required...!!',font=('Comic Sans MS',20,'bold'),bg='skyblue',bd=7,relief=GROOVE).place(x=450,y=380)
            regn_button=Button(log_window,text='Register !!',command=register_user,font=('Comic Sans MS',20,'bold'),fg="white",bg="#d77337",bd=10,relief=GROOVE).place(x=270,y=450)
            login_button=Button(log_window,text='Login !!',command=login_user,font=('Comic Sans MS',20,'bold'),fg="white",bg="#d77337",bd=10,relief=GROOVE).place(x=900,y=450)
        color_button=Button(log_window,text='Modify Back-ground Colour',command=color,font=('Comic Sans MS',13,'bold'),fg="white",bg="#d77337")
        color_button.place(x=1050,y=650)
        help_msg.bind(color_button,'Change background color...')
        log_window.bind('<Alt-C>',lambda EVENT: color())
        log_window.bind('<Alt-c>',lambda EVENT: color())

        log_window.bind('<Alt-X>',lambda EVENT: log_window.destroy())
        log_window.bind('<Alt-x>',lambda EVENT: log_window.destroy())
        log_window.mainloop()
    login_window(log_window)

pg.theme('SystemDefault')
for i in range(1,103,1):
    progress=pg.one_line_progress_meter('LOADING......',current_value=i,max_value=100,orientation='h')#,='LOADING... ASK BILLING S/W  |  REGISTER / LOG-IN WINDOW.....')
    time.sleep(0.05)
if progress==False:
    login_window()
