import customtkinter as ctkinter

ctkinter.set_appearance_mode("system")
ctkinter.set_default_color_theme("green")

root = ctkinter.CTk()
root.geometry("500x350")


def login():
    print("test")


frame = ctkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = ctkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = ctkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()