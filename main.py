import tkinter as tk

def add(sym):
    expression = output_text.get() + str(sym)
    output_text.set(expression)

def solve():

    try:
        answer = str(eval(output_text.get()))
        output_text.set(answer)
    except:
        output_text.set('Error')

def clear():

    output_text.set('')

def delete():

    expression = output_text.get()

    output_text.set(expression[:-1])


if __name__ == '__main__':

    gui = tk.Tk()

    gui.geometry('500x650')

    gui.title('Basic Calculator')

    gui.configure(background='#2B2D42')

    output_text = tk.StringVar()

    output_frame = tk.Frame(gui, width=500, height=100, bg='#2B2D42')
    output_frame.pack(side='top')
    
    button_frame = tk.Frame(gui, width=500, height=500, bg='#2B2D42')
    button_frame.pack()

    output_box = tk.Entry(output_frame, textvariable=output_text, font=('lato', 15, 'bold'),  bg='#EDF2F4')
    output_box.pack(padx=10, pady=(20, 20), ipadx=65)

    padding_x = 5
    padding_y = 10

    tk.Button(button_frame, text='1', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('1')).grid(row=1, column=0, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='2', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('2')).grid(row=1, column=1, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='3', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('3')).grid(row=1, column=2, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='4', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('4')).grid(row=2, column=0, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='5', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('5')).grid(row=2, column=1, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='6', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('6')).grid(row=2, column=2, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='7', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('7')).grid(row=3, column=0, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='8', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('8')).grid(row=3, column=1, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='9', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('9')).grid(row=3, column=2, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='0', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('0')).grid(row=4, column=0, columnspan=2, padx=padding_x, pady=padding_y, ipadx=80, ipady=30)

    tk.Button(button_frame, text='.', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('.')).grid(row=4, column=2, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)

    tk.Button(button_frame, text='/', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('/')).grid(row=1, column=3, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='*', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('*')).grid(row=2, column=3, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='-', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('-')).grid(row=3, column=3, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)
    tk.Button(button_frame, text='+', font=('lato', 10, 'bold'), bg='#8D99AE', command=lambda: add('+')).grid(row=4, column=3, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)

    tk.Button(button_frame, text='=', font=('lato', 10, 'bold'), bg='#8D99AE', command=solve).grid(row=5, column=3, padx=padding_x, pady=padding_y, ipadx=30, ipady=30)

    tk.Button(button_frame, text=f'Clear ', font=('lato', 10, 'bold'), bg='#8D99AE', command=clear).grid(row=5, column=0, columnspan=2, padx=padding_x, pady=padding_y, ipadx=65, ipady=30)
    tk.Button(button_frame, text=f'Delete', font=('lato', 10, 'bold'), bg='#8D99AE', command=delete).grid(row=5, column=2, padx=padding_x, pady=padding_y, ipadx=12, ipady=30)

    # 1 character = 3 pixels

    gui.mainloop()