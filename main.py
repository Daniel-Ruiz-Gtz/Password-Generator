import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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





root.mainloop()
