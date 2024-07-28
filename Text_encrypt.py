import tkinter as tk
from tkinter import messagebox

def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text, shift):
    return encrypt_text(text, -shift)

def encrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted_text = encrypt_text(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        decrypted_text = decrypt_text(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

root = tk.Tk()
root.title("Text Encryption Using Ceaser Cipher")
root.configure(bg="black")
text_color="white"

input_label = tk.Label(root, text="Input Text" ,bg="black", fg=text_color)
input_label.pack()
input_text = tk.Text(root, height=4, width=40,bg="black", fg=text_color)
input_text.pack()

shift_label = tk.Label(root, text="Shift Value",bg="black", fg=text_color)
shift_label.pack()
shift_entry = tk.Entry(root,bg="black", fg=text_color)
shift_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack()
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.pack()
output_label = tk.Label(root, text="Output Text",bg="black", fg=text_color)
output_label.pack()
output_text = tk.Text(root, height=4, width=40,bg="black", fg=text_color)
output_text.pack()

# Start 
root.mainloop()
