import tkinter
import customtkinter
import os

#  poetry run python ./lovepy/main.py

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
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
