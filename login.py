from customtkinter import *
from PIL import Image, ImageTk
import subprocess

app = CTk()
app.geometry("1000x700")


app.title("BULLSRC")
app.iconbitmap("logotipo-v1.ico")



def click_handler():
    username = label_Username.get()
    password = label_Password.get()
    error_label.configure(text="")
    if len(password) < 6:
        error_label.configure(text="Password must be at least 6 characters long.")
    else:
        print(f"Username: {username}")
        print(f"Password: {password}")
        
        # Após validação, esconde a janela
        app.withdraw()  # Esconde a janela de login
        try:
            subprocess.run(["python", "main.py"], check=True)  # Executa o arquivo main.py
        except subprocess.CalledProcessError as e:
            error_label.configure(text=f"Error while running main.py: {e}", text_color="red")
        finally:
            app.quit()  # Garante que o app seja finalizado após a execução do main.py

def show_register():
    btn_login.pack_forget()
    confirm_password_entry.pack(pady=10, after=label_Password)
    btn_register.pack(pady=10, after=confirm_password_entry)
    label_criarConta.configure(text="Already have an account?")
    Label_registo.configure(text="Back to Login")
    Label_registo.bind("<Button-1>", lambda e: show_login())

def register_handler():
    username = label_Username.get()
    password = label_Password.get()
    confirm_password = confirm_password_entry.get()
    error_label.configure(text="")
    if len(password) < 6:
        error_label.configure(text="Password must be at least 6 characters long.")
    elif password != confirm_password:
        error_label.configure(text="Passwords do not match.")
    else:
        print(f"Registration Successful: Username: {username}, Password: {password}")
        error_label.configure(text="Registration successful!", text_color="green")
        label_Username.delete(0, 'end')
        label_Password.delete(0, 'end')
        confirm_password_entry.delete(0, 'end')
        confirm_password_entry.pack_forget()
        btn_register.pack_forget()
        btn_login.pack(pady=20)
        label_criarConta.configure(text="Are you new here?")
        Label_registo.configure(text="Register")
        Label_registo.bind("<Button-1>", lambda e: show_register())

def show_login():
    confirm_password_entry.pack_forget()
    btn_register.pack_forget()
    btn_login.pack(pady=20)
    label_criarConta.configure(text="Are you new here?")
    Label_registo.configure(text="Register")
    Label_registo.bind("<Button-1>", lambda e: show_register())

entry_style = {
    "width": 300,
    "height": 40,
    "text_color": "black",
    "corner_radius": 40,
    "font": ("Arial", 16, "bold"),
    "fg_color": "#fff"
}

main_frame = CTkFrame(master=app, fg_color="#323232")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

user = Image.open("user.png")
user_resized = user.resize((300, 300))
user_path = CTkImage(user, size=(300, 300))

label_img_user = CTkLabel(master=main_frame, image=user_path, text="")
label_img_user.pack(pady=20)

label_Username = CTkEntry(master=main_frame, placeholder_text="Username", **entry_style)
label_Username.pack(pady=10)

label_Password = CTkEntry(master=main_frame, placeholder_text="Password", **entry_style, show="*")
label_Password.pack(pady=10)

confirm_password_entry = CTkEntry(master=main_frame, placeholder_text="Confirm Password", **entry_style, show="*")

error_label = CTkLabel(master=main_frame, text="", text_color="red", font=("Arial", 12, "italic"))
error_label.pack(pady=5)

btn_login = CTkButton(master=main_frame, text="Login", corner_radius=40, fg_color="#009d51", command=click_handler,
                       width=100, height=40, font=("Arial", 16, "bold"))
btn_login.pack(pady=20)

btn_register = CTkButton(master=main_frame, text="Register", corner_radius=40, fg_color="#0059b3", command=register_handler,
                         width=100, height=40, font=("Arial", 16, "bold"))

row_frame = CTkFrame(master=main_frame, fg_color="transparent") 
row_frame.pack()

label_criarConta = CTkLabel(master=row_frame, text="Are you new here?")
label_criarConta.pack(side="left", padx=5)

Label_registo = CTkLabel(master=row_frame, text="Register", text_color="blue", cursor="hand2")
Label_registo.pack(side="left", padx=5)
Label_registo.bind("<Button-1>", lambda e: show_register())

app.mainloop()
