import tkinter as tk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr(
                (ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a')
            )
            result += shifted_char
        else:
            result += char
    return result

def main():
    root = tk.Tk()
    root.title("Caesar Cipher")
    root.geometry("300x250")  
    
    tk.Label(root, text="Enter the message:").pack(pady=5)
    message_entry = tk.Entry(root, width=30)
    message_entry.pack(pady=5)

    tk.Label(root, text="Enter the shift value:").pack(pady=5)
    shift_entry = tk.Entry(root, width=10)
    shift_entry.pack(pady=5)

    encrypted_label = tk.Label(root, text="", fg="blue")
    encrypted_label.pack(pady=5)
    decrypted_label = tk.Label(root, text="", fg="green")
    decrypted_label.pack(pady=5)

    def on_submit():
        message = message_entry.get()
        try:
            shift = int(shift_entry.get())
            encrypted_message = caesar_cipher(message, shift)
            decrypted_message = caesar_cipher(encrypted_message, -shift)
            encrypted_label.config(text=f"Encrypted Message: {encrypted_message}")
            decrypted_label.config(text=f"Decrypted Message: {decrypted_message}")
        except ValueError:
            encrypted_label.config(text="Error: Invalid shift value.", fg="red")
            decrypted_label.config(text="")
    
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
