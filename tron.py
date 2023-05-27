import tkinter as tk
from tkinter import messagebox, simpledialog

def show_message(label, message):
    label.config(text='')
    for char in message:
        label.config(text=label['text'] + char)
        label.update()
        label.after(100)
    label.config(text=message)

def home_install():
    output_label.config(text='')
    show_message(output_label, 'Proceeding...')
    name = simpledialog.askstring('Name', 'What is your name?')
    output_label.config(text='')
    option_label.config(text='')
    home_button.pack_forget()
    pro_button.pack_forget()
    show_message(output_label, 'Tron Antivirus')
    show_message(output_label, 'Greetings {}!'.format(name))
    show_options()

def pro_install():
    output_label.config(text='')
    show_message(output_label, 'Charge = ₹2500/year')
    name = simpledialog.askstring('Name', 'What is your name?')
    output_label.config(text='')
    option_label.config(text='')
    home_button.pack_forget()
    pro_button.pack_forget()
    show_message(output_label, 'Tron Antivirus')
    show_message(output_label, 'Greetings {}!'.format(name))
    show_options()

def show_options():
    option_label.config(text='What may I do for you?')
    virus_scan_button.pack()
    account_protection_button.pack()
    firewall_button.pack()
    device_security_button.pack()

root = tk.Tk()
root.title('Tron Antivirus')
root.configure(bg='dark slate gray')

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{x}+{y}')
root.resizable(False, False)
root.attributes('-alpha', 0.95)  # Set window opacity

frame = tk.Frame(root, bg='dark slate gray', padx=20, pady=20, relief=tk.RIDGE, bd=5)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

output_label = tk.Label(frame, font=('Helvetica', 14), justify='center', bg='dark slate gray', fg='white')
output_label.pack(pady=10)

title_label = tk.Label(frame, text='Tron Antivirus', font=('Helvetica', 20), justify='center', bg='dark slate gray', fg='white')
title_label.pack()

button_frame = tk.Frame(frame, bg='dark slate gray')
button_frame.pack(pady=10)

home_button = tk.Button(button_frame, text='Home', width=10, height=2, command=home_install, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')
home_button.pack(side=tk.LEFT, padx=5)

pro_button = tk.Button(button_frame, text='Pro', width=10, height=2, command=pro_install, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')
pro_button.pack(side=tk.LEFT, padx=5)

option_label = tk.Label(frame, text='', font=('Helvetica', 14), justify='center', bg='dark slate gray', fg='white')

virus_scan_button = tk.Button(frame, text='Virus Scan', width=15, height=2, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')
account_protection_button = tk.Button(frame, text='Account Protection', width=15, height=2, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')
firewall_button = tk.Button(frame, text='Firewall', width=15, height=2, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')
device_security_button = tk.Button(frame, text='Device Security', width=15, height=2, relief=tk.GROOVE, bd=2, bg='dark gray', fg='white')

root.mainloop()
