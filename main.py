from customtkinter import *

app = CTk()
app.geometry("1000x700")


tabview = CTkTabview(master=app)
tabview.pack(fill="both", expand=True, padx=20, pady=00)

tabview.add("página inicial")
tabview.add("página")
tabview.add("perfil")




label_1 = CTkLabel(master=tabview.tab("página inicial"), text="This is tab 1")
label_1.pack(padx=20, pady=20)
btn_1 = CTkButton(master=tabview.tab("página inicial"), text="clica", corner_radius=32,
                 fg_color="transparent", hover_color="#4158D0",
                   border_color="#ffcc70", border_width=2, 
                   text_color="#ffcc70",)
btn_1.place(relx=0.5,rely=0.1, anchor="center")


label_2 = CTkLabel(master=tabview.tab("página"), text="This is tab 2")
label_2.pack(padx=20, pady=20)

label_3 = CTkLabel(master=tabview.tab("perfil"), text="This is tab 3")
label_3.pack(padx=20, pady=20)

app.mainloop()