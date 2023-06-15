from tkinter import Toplevel,StringVar,Entry,Button

def calc_window():
    global exp
    exp=''
    def press_clear():
        global exp
        exp=''
        exp_input.set('')
        
    def press(num):
        global exp
        exp+=num
        exp_input.set(exp)
        
    def press_equals():
        global exp
        result=str(eval(exp))
        exp_input.set(result)

    calc=Toplevel()
    calc.title('ASK BILLING S/W | CALCULATOR')
    calc.iconbitmap('C://ASK-BILLING-S-W//IMGS//BILLING_NOTIFICATION_LOGO.ico')
    calc.config(background='blue')

    exp_input=StringVar()
    exp_field= Entry(calc,font=('Comic Sans MS',14,'bold'),textvariable=exp_input,bd=30,bg='blue',fg='white')
    exp_input.set('   Enter the expression: ')
    exp_field.grid(columnspan=4)

    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='7',bg='blue',command=lambda: press('7')).grid(row=1,column=0)
    ##calc.bind('<7>',lambda EVENT: press('7'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='8',bg='blue',command=lambda: press('8')).grid(row=1,column=1)
    ##calc.bind('<8>',lambda EVENT: press('8'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='9',bg='blue',command=lambda: press('9')).grid(row=1,column=2)
    ##calc.bind('<9>',lambda EVENT: press('9'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='+',bg='blue',command=lambda: press('+')).grid(row=1,column=3)
    ##calc.bind('<+>',lambda EVENT: press('+'))

    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='4',bg='blue',command=lambda: press('4')).grid(row=2,column=0)
    ##calc.bind('<4>',lambda EVENT: press('4'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='5',bg='blue',command=lambda: press('5')).grid(row=2,column=1)
    ##calc.bind('<5>',lambda EVENT: press('5'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='6',bg='blue',command=lambda: press('6')).grid(row=2,column=2)
    ##calc.bind('<6>',lambda EVENT: press('6'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='-',bg='blue',command=lambda: press('-')).grid(row=2,column=3)
    ##calc.bind('<_>',lambda EVENT: press('-'))

    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='1',bg='blue',command=lambda: press('1')).grid(row=3,column=0)
    ##calc.bind('<1>',lambda EVENT: press('1'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='2',bg='blue',command=lambda: press('2')).grid(row=3,column=1)
    ##calc.bind('<2>',lambda EVENT: press('2'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='3',bg='blue',command=lambda: press('3')).grid(row=3,column=2)
    ##calc.bind('<3>',lambda EVENT: press('3'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='*',bg='blue',command=lambda: press('*')).grid(row=3,column=3)
    ##calc.bind('<*>',lambda EVENT: press('*'))

    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='0',bg='blue',command=lambda: press('0')).grid(row=4,column=0)
    ##calc.bind('<0>',lambda EVENT: press('0'))
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='C',bg='blue',command=lambda: press_clear()).grid(row=4,column=1)
    ##calc.bind('<BackSpace>',lambda: press_clear)
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='=',bg='blue',command=lambda: press_equals()).grid(row=4,column=2)
    ##calc.bind('<E>',lambda: press_equals)
    Button(calc,padx=16,bd=10,fg='white',font=('Comic Sans MS',14,'bold'),text='/',bg='blue',command=lambda: press('/')).grid(row=4,column=3)
    ##calc.bind('</>',lambda EVENT: press('/'))

    calc.resizable(False,False)
    calc.mainloop()
