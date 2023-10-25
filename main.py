import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

# Function to update the text widget
def update_password_text():
    central_word = cword_entry.get()
    # You can generate the password and set it to passw_res_text here
    password = generate_password(central_word)
    passw_res_text.delete("1.0", "end")
    passw_res_text.insert("1.0", password)
    
    # Show the password label and text widget
    passw_label.pack(side="left")
    passw_res_text.pack(side="left")
    countdown(30)  # Start a 30-second countdown

# Replace this with your actual password generation logic
def generate_password(central_word):
    # Example password generation logic
    return central_word + "123"

# Function to hide password label and text
def hide_password():
    passw_label.pack_forget()
    passw_res_text.pack_forget()
    time_label.pack_forget()

# Function to update the countdown and hide password after 30 seconds
def countdown(time_left):
    if time_left <= 0:
        hide_password()
    else:
        time_str.set(f"Password available for {time_left} seconds")
        time_label.pack(side="left")  # Show the countdown label
        root.after(1000, countdown, time_left - 1)

# Function to show program information
def show_program_info():
    info_text = "This is a password generator program.\n\nYou can enter a central word, and the program will generate a secure password for you. The password will be available for 30 seconds."
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
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
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

# ENTRY
cword_label = ttk.Label(root, text="Central Word", background='#23283b', font=("Helvetica", 13), foreground="white")
cword_label.pack(side="top")
cword_entry = ttk.Entry(root, font=("Helvetica", 11))
cword_entry.pack(side="top")

# BLANK SPACE
blank_label = ttk.Label(root, background='#23283b')
blank_label.pack(side="top")

# BUTTON
generate_button = ttk.Button(root, text="Generate Password", command=update_password_text)
generate_button.pack(side="top")

time_str = tk.StringVar()
time_label = ttk.Label(root, textvariable=time_str, background='#23283b', font=("Helvetica", 12), foreground="white")

# ANSWER 
passw_label = ttk.Label(root, text="Secure Password: ", background='#23283b', font=("Helvetica", 13), foreground="white")
passw_res_text = tk.Text(root, height=1, width=20, font=("Helvetica", 13), background='#23283b', foreground="white")

# Create a small "?" button for program info
info_button = ttk.Button(root, text="?", command=show_program_info, width=1)
info_button.configure(style="Info.TButton")  # Create a custom style to make the button small
info_button.pack(side="bottom")

root.mainloop()
