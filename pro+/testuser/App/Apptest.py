import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import json
import subprocess
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("İSTİNDAT DUVARI 300 (Abim <3)")
        self.geometry("1000x900")

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights for responsiveness
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Frame for first form inputs and image
        form_image_frame1 = ttk.Frame(main_frame, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame1.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        form_frame1 = ttk.Frame(form_image_frame1, padding="10 10 10 10")
        form_frame1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        image_frame1 = ttk.Frame(form_image_frame1, padding="10 10 10 10")
        image_frame1.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame for second form inputs and image
        form_image_frame2 = ttk.Frame(main_frame, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame2.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        form_frame2 = ttk.Frame(form_image_frame2, padding="10 10 10 10")
        form_frame2.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        image_frame2 = ttk.Frame(form_image_frame2, padding="10 10 10 10")
        image_frame2.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Define form labels and entries for the first form
        labels1 = ["A1_LEN", "A2_LEN", "A3_LEN", "A10_LEN",
                   "B1_LEN", "B2_LEN", "B10_LEN",
                   "C1_LEN", "C2_LEN", "C3_LEN", "C4_LEN",
                   "D1_LEN", "D2_LEN", "D4_LEN", "D5_LEN",
                   "E10_LEN",
                   "H2_LEN", "H3_LEN", "H4_LEN", "H5_LEN",
                   "G_LEN",
                   "T_LEN", "TB1_LEN", "TB2_LEN",
                   ]

        self.entries1 = {}

        for idx, label in enumerate(labels1):
            row = idx // 3  # 2 sütun halinde düzenleme
            col = (idx % 3) * 3  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame1, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame1, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries1[label] = entry

        # Define form labels and entries for the second form
        labels2 = [
            "H1_LEN", "H2_LEN", "H3_LEN", "H4_LEN", "H5_LEN", "H6_LEN",
            "H7_LEN", "H9_LEN", "H10_LEN",
        ]

        self.entries2 = {}

        for idx, label in enumerate(labels2):
            row = idx // 3  # 2 sütun halinde düzenleme
            col = (idx % 3) * 3  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame2, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame2, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries2[label] = entry

        # Load and display the first image
        try:
            image1 = Image.open("pro+/pictures/HIS.jpg")
            image1 = image1.resize((400, 200), Image.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(image1)

            image_label1 = ttk.Label(image_frame1, image=self.photo1)
            image_label1.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label1 = ttk.Label(image_frame1, text="Image not found")
            error_label1.grid(row=0, column=0, padx=10, pady=10)

        # Load and display the second image
        try:
            image2 = Image.open("pro+/pictures/HIS2.jpg")  # İkinci resim yolu
            image2 = image2.resize((400, 200), Image.LANCZOS)
            self.photo2 = ImageTk.PhotoImage(image2)

            image_label2 = ttk.Label(image_frame2, image=self.photo2)
            image_label2.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label2 = ttk.Label(image_frame2, text="Image not found")
            error_label2.grid(row=0, column=0, padx=10, pady=10)

        # Button to save entries for first form
        button1 = ttk.Button(form_image_frame1, text="Çiz HIS", command=self.save_entries_form1)
        button1.grid(row=1, column=0, columnspan=2, pady=10)

        # Button to save entries for second form
        button2 = ttk.Button(form_image_frame2, text="Çiz HIS2", command=self.save_entries_form2)
        button2.grid(row=1, column=0, columnspan=2, pady=10)

        # Create a Text widget for output display
        self.output_text = ScrolledText(main_frame, wrap=tk.WORD, width=100, height=10)
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_entries_form1(self):
        # Change button color to green
        self.config(bg="green")

        # Get entries for form1
        data1 = {label: entry.get() for label, entry in self.entries1.items()}

        # Save to JSON file
        with open('input_data_form1.json', 'w') as f:
            json.dump(data1, f)

        self.output_text.insert(tk.END, "Form1 verisi dosyaya yazıldı.\n")

        # Execute HIS.py
        self.execute_script("HIS.py")

    def save_entries_form2(self):
        # Change button color to green
        self.config(bg="green")

        # Get entries for form2
        data2 = {label: entry.get() for label, entry in self.entries2.items()}

        # Save to JSON file
        with open('input_data_form2.json', 'w') as f:
            json.dump(data2, f)

        self.output_text.insert(tk.END, "Form2 verisi dosyaya yazıldı.\n")

        # Execute HIS2.py
        self.execute_script("HIS_2.py")

    def execute_script(self, script_name):
        try:
            # Determine the path to the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, script_name)

            result = subprocess.run(["python", "-Xfrozen_modules=off", script_path], check=True, capture_output=True, text=True)
            self.output_text.insert(tk.END, result.stdout + "\n")
        except subprocess.CalledProcessError as e:
            self.output_text.insert(tk.END, f"{script_name} çalıştırılamadı: {e}\n")
        except FileNotFoundError as e:
            self.output_text.insert(tk.END, f"Dosya bulunamadı: {e}\n")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
