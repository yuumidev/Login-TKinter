import tkinter as tk
from tkinter import messagebox

def login():
    email = entry_email.get()
    senha = entry_senha.get()

    if '@' not in email and len(senha) < 6:
        messagebox.showerror(title='Erro', message='Email e senha inválidos.')

    elif '@' not in email:
        messagebox.showerror(title='Erro', message='Email inválido.')

    elif len(senha) < 6:
        messagebox.showerror(title='Erro', message='Senha inválida.')


    else:
        messagebox.showinfo(title='Sucesso', message='Login realizado com sucesso!')


janela = tk.Tk()
janela.title('Login')
janela.configure(background='#003C43')

label_email = tk.Label(janela, text='Email:', background='#003C43', foreground='#E3FEF7')
label_email.grid(row=0, column=0, padx=5, pady=5)

entry_email = tk.Entry(janela, bg='#135D66', fg='#E3FEF7')
entry_email.grid(row=0, column=1, padx=5, pady=5)

label_senha = tk.Label(janela, text='Senha:', background='#003C43', foreground='#E3FEF7')
label_senha.grid(row=1, column=0, padx=5, pady=5)

entry_senha = tk.Entry(janela, show='*', bg='#135D66', fg='#E3FEF7')
entry_senha.grid(row=1, column=1, padx=5, pady=5)

botao_login = tk.Button(janela, text='Login', command=login, background='#135D66', foreground='#E3FEF7')
botao_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)

janela.mainloop()