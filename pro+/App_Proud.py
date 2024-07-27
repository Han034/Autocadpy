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
        self.frame_his3 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his_tip2 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his2_tip2 = ttk.Frame(self.notebook, padding="10 10 10 10")
        self.frame_his3_tip2 = ttk.Frame(self.notebook, padding="10 10 10 10")

        self.notebook.add(self.frame_his, text='A-A')
        self.notebook.add(self.frame_his2, text='B-B')
        self.notebook.add(self.frame_his3, text='PLAN')
        self.notebook.add(self.frame_his_tip2, text='A-A TIP2')
        self.notebook.add(self.frame_his2_tip2, text='B-B TIP2')
        self.notebook.add(self.frame_his3_tip2, text='PLAN TIP2')

        self.create_form_his(self.frame_his)
        self.create_form_his2(self.frame_his2)
        self.create_form_his3(self.frame_his3)
        self.create_form_his_tip2(self.frame_his_tip2)
        self.create_form_his2_tip2(self.frame_his2_tip2)
        self.create_form_his3_tip2(self.frame_his3_tip2)

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

        # Load and display the image
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

        # Define form labels and entries
        labels = ["H9_LEN","H10_LEN",
                  "H1_LEN","H3_LEN",
                  "H3X_LEN","H4_LEN",
                  "H5_LEN","H6_LEN",
                  "H11_LEN","H11X_LEN",
                  "H12_LEN","H7_LEN",
                  "H8_LEN","H2_LEN",
                  "H13_LEN","FRKY_LEN",
                  "FRKD_LEN","H14_LEN",
                  "H12X_LEN","H40_LEN",
                  "H30_LEN"]

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

    def create_form_his_tip2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS_tip2.jpg")  # Dördüncü resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo4 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo4)
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

        self.entries4 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries4[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS TIP2", command=self.save_entries_form4)
        button.grid(row=2, column=0, pady=10)

    def create_form_his2_tip2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS2_tip2.jpg")  # Beşinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo5 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo5)
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

        self.entries5 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries5[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS2 TIP2", command=self.save_entries_form5)
        button.grid(row=2, column=0, pady=10)

    def create_form_his3_tip2(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS3_tip2.jpg")  # Altıncı resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo6 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo6)
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

        self.entries6 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries6[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS3 TIP2", command=self.save_entries_form6)
        button.grid(row=2, column=0, pady=10)

    def create_form_his_tip1(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS_tip1.jpg")  # Yedinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo7 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo7)
            image_label.grid(row=0, column=0, padx=10, pady=10)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            error_label = ttk.Label(image_frame, text="Image not found")
            error_label.grid(row=0, column=0, padx=10, pady=10)

        # Define form labels and entries
        labels = ["H9_LEN","H10_LEN",
                  "H1_LEN","H3_LEN",
                  "H3X_LEN","H4_LEN",
                  "H5_LEN","H6_LEN",
                  "H11_LEN","H11X_LEN",
                  "H12_LEN","H7_LEN",
                  "H8_LEN","H2_LEN",
                  "H13_LEN","FRKY_LEN",
                  "FRKD_LEN","H14_LEN",
                  "H12X_LEN","H40_LEN",
                  "H30_LEN"]

        self.entries7 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries7[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS TIP1", command=self.save_entries_form7)
        button.grid(row=2, column=0, pady=10)

    def create_form_his2_tip1(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS2_tip1.jpg")  # Sekizinci resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo8 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo8)
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

        self.entries8 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries8[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS2 TIP1", command=self.save_entries_form8)
        button.grid(row=2, column=0, pady=10)

    def create_form_his3_tip1(self, parent):
        # Frame for form inputs and image
        form_image_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief="sunken")
        form_image_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        image_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        image_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        form_frame = ttk.Frame(form_image_frame, padding="10 10 10 10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Load and display the image
        try:
            image = Image.open("pro+/pictures/HIS3_tip1.jpg")  # Dokuzuncu resim yolu
            image = image.resize((800, 400), Image.LANCZOS)  # Adjust size to fit larger area
            self.photo9 = ImageTk.PhotoImage(image)

            image_label = ttk.Label(image_frame, image=self.photo9)
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

        self.entries9 = {}

        for idx, label in enumerate(labels):
            row = idx // 6  # 3 sütun halinde düzenleme
            col = (idx % 6) * 2  # Her etiket ve giriş için 2 sütun

            ttk.Label(form_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(form_frame, width=10)
            entry.grid(row=row, column=col + 1, padx=5, pady=2)
            self.entries9[label] = entry

        # Button to save entries
        button = ttk.Button(form_image_frame, text="Çiz HIS3 TIP1", command=self.save_entries_form9)
        button.grid(row=2, column=0, pady=10)

    def save_entries_form3(self):
        for label, entry in self.entries3.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form4(self):
        for label, entry in self.entries4.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form5(self):
        for label, entry in self.entries5.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form6(self):
        for label, entry in self.entries6.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form7(self):
        for label, entry in self.entries7.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form8(self):
        for label, entry in self.entries8.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

    def save_entries_form9(self):
        for label, entry in self.entries9.items():
            value = entry.get()
            print(f"{label}: {value}")
        # Add your saving logic here

if __name__ == "__main__":
    app = Application()
    app.mainloop()
