import customtkinter as ctk

# aparencia da janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# definicao da janela
tela = ctk.CTk()
tela.geometry('500x400')
tela.title('Sistema do login')

# funcao valida login
def valida_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == 'guamosa' and senha == '123456':
        resultado_login.configure(text='Sucesso no login!', text_color='green')
    else:
        resultado_login.configure(text='Usuário ou senha incorretos', text_color='red')

def login_teclado(event):
    valida_login()

# label usuario
lbl_usuario = ctk.CTkLabel(tela, text='Usuário:')
lbl_usuario.pack(padx=10, pady=3)
# entrada usuario
entry_usuario = ctk.CTkEntry(tela, placeholder_text='Digite seu usuário')
entry_usuario.pack(pady=10)
# label senha
lbl_senha = ctk.CTkLabel(tela, text='Senha:')
lbl_senha.pack(padx=10, pady=3)
# entrada senha
entry_senha = ctk.CTkEntry(tela, placeholder_text='Digite sua senha', show='*')
entry_senha.pack(pady=10)
# associa5r teclado
entry_senha.bind('<Return>', login_teclado)
# guardar senha
check_senha = ctk.CTkCheckBox(tela, text='Lembrar Login')
check_senha.pack(pady=10)
# botao login
btn_login = ctk.CTkButton(tela, text='Login', command=valida_login)
btn_login.pack(padx=10, pady=10)
# botao sair
btn_sair = ctk.CTkButton(tela, text='Sair', command=exit)
btn_sair.pack(pady=10)
# resultado login
resultado_login = ctk.CTkLabel(tela, text='')
resultado_login.pack(pady=10)

tela.mainloop()