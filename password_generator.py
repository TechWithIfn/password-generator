import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip 
class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # Variables
        self.password_length = tk.IntVar(value=12)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = ttk.Label(self.master, text="Password Generator", font=("Arial", 16))
        title_label.pack(pady=10)

        # Length Selection
        length_label = ttk.Label(self.master, text="Select Password Length:")
        length_label.pack()

        length_spinbox = ttk.Spinbox(self.master, from_=8, to=32, textvariable=self.password_length)
        length_spinbox.pack(pady=5)

        # Checkboxes for complexity options
        complexity_frame = ttk.LabelFrame(self.master, text="Include Characters", padding=(10, 5))
        complexity_frame.pack(pady=10)

        ttk.Checkbutton(complexity_frame, text="Lowercase Letters", variable=self.include_lowercase).pack(anchor='w')
        ttk.Checkbutton(complexity_frame, text="Uppercase Letters", variable=self.include_uppercase).pack(anchor='w')
        ttk.Checkbutton(complexity_frame, text="Digits", variable=self.include_digits).pack(anchor='w')
        ttk.Checkbutton(complexity_frame, text="Symbols", variable=self.include_symbols).pack(anchor='w')

        # Generate Button
        generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        # Password Display
        password_display = ttk.Entry(self.master, textvariable=self.generated_password, font=("Arial", 14), justify="center", state="readonly")
        password_display.pack(pady=5)

        # Copy Button
        copy_button = ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(pady=10)

    def generate_password(self):
        length = self.password_length.get()
        
        if length < 8:
            self.generated_password.set("Length must be at least 8")
            return

        # Define character sets based on user selection
        character_sets = []
        
        if self.include_lowercase.get():
            character_sets.append(string.ascii_lowercase)
        
        if self.include_uppercase.get():
            character_sets.append(string.ascii_uppercase)
        
        if self.include_digits.get():
            character_sets.append(string.digits)
        
        if self.include_symbols.get():
            character_sets.append(string.punctuation)

        if not character_sets:
            self.generated_password.set("Select at least one character type")
            return

        # Ensure at least one character from each selected category is included
        password = []
        
        for charset in character_sets:
            password.append(random.choice(charset))

        # Fill the rest of the password length with random choices from all selected characters
        all_characters = ''.join(character_sets)
        
        password += random.choices(all_characters, k=length - len(password))

        # Shuffle the resulting password list to ensure randomness
        random.shuffle(password)

        # Convert list to string and set it to the variable for display
        self.generated_password.set(''.join(password))

    def copy_to_clipboard(self):
        pyperclip.copy(self.generated_password.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()