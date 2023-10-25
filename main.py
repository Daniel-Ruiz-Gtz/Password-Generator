import random
import string
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

def update_password_text():
    try:
        password_length = int(size_entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length (greater than 0).")
        else:
            password = generate_password(password_length)
            passw_res_text.delete("1.0", "end")
            passw_res_text.insert("1.0", password)
            passw_label.pack(side="left")
            passw_res_text.pack(side="left")
            countdown(15)  # Start the countdown timer with 30 seconds
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric password length.")

def generate_password(password_length):

    return password_length

def hide_password():
    passw_label.pack_forget()
    passw_res_text.pack_forget()
    time_label.pack_forget()

def countdown(time_left):
    if time_left <= 0:
        hide_password()
    else:
        time_str.set(f"Password available for {time_left} seconds")
        time_label.pack(side="left")
        root.after(1000, countdown, time_left - 1)

def show_program_info():
    info_text = "This is a password generator program.\n\nJust enter the length of the password, and the program will generate a secure password for you. The password will be available for 30 seconds."
    messagebox.showinfo("Password Generator", info_text)

# MAIN WINDOW
root = tk.Tk()
root.iconbitmap('public/icon.ico')
root.title('Password Generator')
window_width = 600
window_height = 400
root.configure(bg='#23283b')

# ALIGN CENTER
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# TITLE
image = Image.open("public/logo.png")
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo, background='#23283b')
image_label.pack(side="top")
title_label = ttk.Label(root, background='#23283b', text='Password Generator', font=("Helvetica", 30), foreground="white")
title_label.pack(side="top")

# BLANK SPACE
blank_label = ttk.Label(root, background='#23283b')
blank_label.pack(side="top")

# PASSWORD LENGTH ENTRY
size_label = ttk.Label(root, text="Password Length", background='#23283b', font=("Helvetica", 13), foreground="white")
size_label.pack(side="top")
size_entry = ttk.Entry(root, font=("Helvetica", 11))
size_entry.pack(side="top")

# BLANK SPACE
blank_label = ttk.Label(root, background='#23283b')
blank_label.pack(side="top")

# GENERATE BUTTON
generate_button = ttk.Button(root, text="Generate Password", command=update_password_text)
generate_button.pack(side="top")

time_str = tk.StringVar()
time_label = ttk.Label(root, textvariable=time_str, background='#23283b', font=("Helvetica", 12), foreground="white")

# ANSWER
passw_label = ttk.Label(root, text="Secure Password: ", background='#23283b', font=("Helvetica", 13), foreground="white")
passw_res_text = tk.Text(root, height=1, width=20, font=("Helvetica", 13), background='#23283b', foreground="white")

# INFO BUTTON
info_button = ttk.Button(root, text="?", command=show_program_info, width=1)
info_button.configure(style="Info.TButton")
info_button.pack(side="bottom")

root.mainloop()
