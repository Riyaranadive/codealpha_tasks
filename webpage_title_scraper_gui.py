import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def extract_title():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Input Required", "Please enter a valid URL.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"

        with open("page_title.txt", "w", encoding="utf-8") as f:
            f.write(title)

        messagebox.showinfo("Success", f"Title saved to 'page_title.txt':\n\n{title}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", f"Failed to fetch the page:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Webpage Title Scraper")
root.geometry("400x200")

title_label = tk.Label(root, text="Enter Webpage URL:", font=("Arial", 12))
title_label.pack(pady=10)

url_entry = tk.Entry(root, width=50, font=("Arial", 10))
url_entry.pack(pady=5)
url_entry.insert(0, "https://example.com")  # Default example

extract_button = tk.Button(root, text="Extract Title", command=extract_title, font=("Arial", 11))
extract_button.pack(pady=20)

root.mainloop()
