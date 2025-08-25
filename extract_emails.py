import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os

def extract_emails_from_file(filepath):
    if not os.path.exists(filepath):
        messagebox.showerror("Error", f"File not found:\n{filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = sorted(set(re.findall(email_pattern, text)))

    if not emails:
        messagebox.showinfo("No Emails Found", "No email addresses were found in the file.")
        return

    output_path = os.path.join(os.path.dirname(filepath), "emails_extracted.txt")
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for email in emails:
            out_file.write(email + '\n')

    messagebox.showinfo("Success", f"{len(emails)} email(s) extracted and saved to:\n{output_path}")

def browse_file():
    filepath = filedialog.askopenfilename(
        title="Select Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    if filepath:
        extract_emails_from_file(filepath)

# --- GUI Setup ---
root = tk.Tk()
root.title("Email Extractor")
root.geometry("300x150")

label = tk.Label(root, text="Extract Emails from .txt File", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(root, text="Select File & Extract", command=browse_file, font=("Arial", 10))
button.pack(pady=10)

root.mainloop()
