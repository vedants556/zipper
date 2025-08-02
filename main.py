import tkinter as tk
from tkinter import filedialog, messagebox
from zipper import compress_files, extract_zip
import os

class FileZipperGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Zipper")
        master.geometry("400x300")
        master.resizable(False, False)

        # Label
        self.label = tk.Label(master, text="File Zipper and Unzipper", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons
        self.compress_button = tk.Button(master, text="Select Files to Compress", command=self.select_files)
        self.compress_button.pack(pady=10)

        self.extract_button = tk.Button(master, text="Select ZIP to Extract", command=self.select_zip)
        self.extract_button.pack(pady=10)

        self.status = tk.Label(master, text="", fg="green")
        self.status.pack(pady=20)

        self.file_paths = []

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames(title="Select files")
        if self.file_paths:
            zip_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip files", "*.zip")])
            if zip_path:
                compress_files(self.file_paths, zip_path)
                self.status.config(text="Files compressed successfully!")
            else:
                self.status.config(text="Compression cancelled", fg="red")

    def select_zip(self):
        zip_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        if zip_path:
            extract_to = filedialog.askdirectory(title="Select folder to extract")
            if extract_to:
                extract_zip(zip_path, extract_to)
                self.status.config(text="Files extracted successfully!")
            else:
                self.status.config(text="Extraction cancelled", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileZipperGUI(root)
    root.mainloop()
