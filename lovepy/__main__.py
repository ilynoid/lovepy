import tkinter
import customtkinter
import os


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme(
    "blue"
) 

app = customtkinter.CTk() 
app.geometry("400x240")
app.title("Love me!")


def yes_toplevel() -> None:
    window = customtkinter.CTkToplevel(app)
    window.title("YAY!")
    window.geometry("400x240")
    customtkinter.CTkLabel(
        window, text="Love You More!", font=customtkinter.CTkFont(size=20)
    ).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    app.after(5000, app.destroy)


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="Yes", fg_color="green", command=yes_toplevel
)
button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(
    master=app, text="No", fg_color="red", command=lambda: os.system("shutdown /s /t 1")
)
button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
customtkinter.CTkLabel(
    app, text="Do You Love Me?", font=customtkinter.CTkFont(size=15)
).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
app.mainloop()
