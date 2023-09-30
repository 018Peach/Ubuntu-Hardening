import  customtkinter
import subprocess
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,fill="both",expand="true")

# label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Arial",24 ))
label = customtkinter.CTkLabel(master=frame, text="Login System")

label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=0, padx=0)



root.mainloop()
