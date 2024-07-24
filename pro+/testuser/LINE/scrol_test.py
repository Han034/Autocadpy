import tkinter as tk

# Ana pencere oluşturma
root = tk.Tk()
root.title("Scrollbar Örneği")

# Text widget oluşturma
text = tk.Text(root, wrap="word", width=50, height=10)
text.pack(side="left", fill="both", expand=True)

# Scrollbar oluşturma
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side="right", fill="y")

# Scrollbar'ı Text widget'e bağlama
text.config(yscrollcommand=scrollbar.set)

# Text widget'e örnek metin ekleme
for i in range(100):
    text.insert("end", f"Satır {i+1}\n")

# Ana döngüyü başlatma
root.mainloop()
