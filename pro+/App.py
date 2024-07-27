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
        self.geometry("1200x800")

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights for responsiveness
        main_frame.grid_columnconfigure(0, weight=3)  # 3/4 for form and image
        main_frame.grid_columnconfigure(1, weight=1)  # 1/4 for output text
        main_frame.grid_rowconfigure(0, weight=1)

        # Notebook (tabbed interface)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        # Frames for each tab
        self.frame_his = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his2 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his3 = ttk.Frame(self.notebook, padding="10 10 10 10")  # HIS3 için yeni bir frame
        self.frame_his_TIP2 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his2_TIP2 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his3_TIP2 = ttk.Frame(self.notebook, padding="10 10 10 10")

        self.notebook.add(self.frame_his, text='A-A')
        self.notebook.add(self.frame_his2, text='B-B')
        self.notebook.add(self.frame_his3, text='PLAN')  # HIS3 sekmesi
        self.notebook.add(self.frame_his_TIP2, text='A-A(T2)')
        self.notebook.add(self.frame_his2_TIP2, text='B-B(T2)')
        self.notebook.add(self.frame_his3_TIP2, text='PLAN(T2)')

        self.create_form_his(self.frame_his)
        self.create_form_his2(self.frame_his2)
        self.create_form_his3(self.frame_his3)  # HIS3 formunu oluştur
        self.create_form_his_TIP2(self.frame_his_TIP2)
        self.create_form_his2_TIP2(self.frame_his2_TIP2)
        self.create_form_his3_TIP2(self.frame_his3_TIP2)

        # Create a Text widget for output display
        self.output_text = ScrolledText(main_frame, wrap=tk.WORD, width=40, height=30)
        self.output_text.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

    def create_form_his(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS.jpg")
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries
        labels = ["B1_LEN","H2_LEN","A2_LEN",
                    "H3_LEN","A3_LEN","H4_LEN", "H5_LEN",
                    "G_LEN", "B2_LEN","A1_LEN","C1_LEN",
                    "C4_LEN","C3_LEN","C2_LEN", "D4_LEN",
                    "D2_LEN","D1_LEN","D5_LEN","TB1_LEN", 
                    "TB2_LEN"
                  ]

        self.entries1 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries1[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS", command=self.save_entries_form1)
        button.grid(row=2, column=0, pady=10)

    def create_form_his2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS2.jpg")  # İkinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo2 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo2)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries
        labels = ["H12X","H9_LEN","H9X_LEN",
                  "H5_LEN","H5X_LEN","H6_LEN",
                  "H4_LEN",
                  "H10_LEN","H10X_LEN","H3_LEN", 
                    "H15_LEN","H2_LEN","H7_LEN",
                  "H16_LEN","H17_LEN","Q100"
                  ]

        self.entries2 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries2[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS2", command=self.save_entries_form2)
        button.grid(row=2, column=0, pady=10)

    def create_form_his3(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image (dummy image for HIS3 as an example)
        try:
            image = Image.open("pro+/pictures/HIS3.jpg")  # Üçüncü resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo3 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo3)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries (dummy labels for HIS3 as an example)
        labels = ["H4_LEN", "H5_LEN", "H6_LEN",
                    "H8_LEN","H11_LEN", "H11X_LEN",
                    "H3_LEN", "H3X_LEN",
                    "H1_LEN",  "H10_LEN","H9_LEN",
                    "H2_LEN","H12_LEN", "H7_LEN",
                    "H13_LEN", "H40_LEN", "H30_LEN"]

        self.entries3 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries3[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS3", command=self.save_entries_form3)
        button.grid(row=2, column=0, pady=10)

    def create_form_his_TIP2(self,parent):

        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS_TIP2.jpg")  # İkinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo4 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo4)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Define form labels and entries
        labels = [
            "B1_LEN","H2_LEN","A2_LEN",
                    "H3_LEN","A3_LEN","H4_LEN", "H5_LEN",
                    "G_LEN", "B2_LEN","A1_LEN","C1_LEN",
                    "C4_LEN","C3_LEN","C2_LEN", "D4_LEN",
                    "D2_LEN","D1_LEN","D5_LEN","TB1_LEN", 
                    "TB2_LEN","H6_LEN"

                  ]

        self.entries4 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries4[label] = entry
        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS_TIP2", command=self.save_entries_form4)
        button.grid(row=2, column=0, pady=10)
    
    def create_form_his2_TIP2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS2_TIP2.jpg")  # İkinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo5 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo5)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries
        labels = ["H2_LEN","H3_LEN","H4_LEN","H4X_LEN","H5_LEN","H5X_LEN","H6_LEN","H7_LEN","H9_LEN","H9X_LEN","H10_LEN","H10X_LEN","H15_LEN","H16_LEN","H17_LEN","H18_LEN","H19_LEN","H19X_LEN","H20_LEN","H20X_LEN","Q100"
                  ]

        self.entries5 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries5[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS2_TIP2", command=self.save_entries_form5)
        button.grid(row=2, column=0, pady=10)

    def create_form_his3_TIP2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS3_TIP2.jpg")  # İkinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo6 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo6)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries
        labels = ["H9_LEN","H10_LEN","H1_LEN","H3_LEN","H4_LEN","H11_LEN","H13_LEN","H12_LEN","H14_LEN","H7_LEN","H12X_LEN","H3X_LEN","H2_LEN","H8_LEN","H40_LEN","H30_LEN"

                  ]

        self.entries6 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries6[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS3_TIP2", command=self.save_entries_form6)
        button.grid(row=2, column=0, pady=10)

    def save_entries_form1(self):
        # Get entries for form1
        data1 = {label: entry.get() for label, entry in self.entries1.items()}

        # Save to JSON file
        with open('input_data_form1.json', 'w') as f:
            json.dump(data1, f)

        self.output_text.insert(tk.END, "Form1 verisi dosyaya yazıldı.\n")

        # Execute HIS.py
        self.execute_script("HIS.py")

    def save_entries_form2(self):
        # Get entries for form2
        data2 = {label: entry.get() for label, entry in self.entries2.items()}

        # Save to JSON file
        with open('input_data_form2.json', 'w') as f:
            json.dump(data2, f)

        self.output_text.insert(tk.END, "Form2 verisi dosyaya yazıldı.\n")

        # Execute HIS2.py
        self.execute_script("HIS_2.py")

    def save_entries_form3(self):

        # Get entries for form3
        data3 = {label: entry.get() for label, entry in self.entries3.items()}

        # Save to JSON file
        with open('input_data_form3.json', 'w') as f:
            json.dump(data3, f)

        self.output_text.insert(tk.END, "Form3 verisi dosyaya yazıldı.\n")

        # Execute HIS3.py
        self.execute_script("HIS_3.py")

    def save_entries_form4(self):
        # Get entries for form1
        data4 = {label: entry.get() for label, entry in self.entries4.items()}

        # Save to JSON file
        with open('input_data_form1_TIP2.json', 'w') as f:
            json.dump(data4, f)

        self.output_text.insert(tk.END, "Form1 verisi dosyaya yazıldı.\n")

        # Execute HIS.py
        self.execute_script("HIS_TIP2.py")
    def save_entries_form5(self):
        # Get entries for form1
        data5 = {label: entry.get() for label, entry in self.entries5.items()}

        # Save to JSON file
        with open('input_data_form2_TIP2.json', 'w') as f:
            json.dump(data5, f)

        self.output_text.insert(tk.END, "Form1 verisi dosyaya yazıldı.\n")

        # Execute HIS.py
        self.execute_script("HIS_2_TIP2.py")
    def save_entries_form6(self):
        # Get entries for form1
        data6 = {label: entry.get() for label, entry in self.entries6.items()}

        # Save to JSON file
        with open('input_data_form3_TIP2.json', 'w') as f:
            json.dump(data6, f)

        self.output_text.insert(tk.END, "Form1 verisi dosyaya yazıldı.\n")

        # Execute HIS.py
        self.execute_script("HIS_3_TIP2.py")

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
