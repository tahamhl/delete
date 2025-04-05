import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random

class SecureDeleteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Güvenli Dosya Üzerine Veri Yazma ve Silme Aracı")
        self.root.geometry("400x350")
        self.root.configure(bg="#282C34")

        # Başlık
        tk.Label(root, text="Güvenli Dosya Üzerine Veri Yazma ve Silme Aracı", font=("Helvetica", 16, "bold"), bg="#282C34", fg="#61AFEF").pack(pady=10)

        # Dosya Seçme Butonu
        tk.Button(root, text="Dosya Seç", command=self.select_file, bg="#61AFEF", fg="white", font=("Helvetica", 12, "bold"), relief="flat", cursor="hand2").pack(pady=10)
        
        # Seçilen Dosya Etiketi
        self.file_label = tk.Label(root, text="Seçilen Dosya: Yok", font=("Helvetica", 10), bg="#282C34", fg="white")
        self.file_label.pack()

        # Geçiş Sayısı Seçimi
        tk.Label(root, text="Geçiş Sayısı:", font=("Helvetica", 12), bg="#282C34", fg="#61AFEF").pack(pady=10)
        self.passes_entry = tk.Entry(root, font=("Helvetica", 12))
        self.passes_entry.insert(0, "3")
        self.passes_entry.pack(pady=5)

        # Dosyaya Veri Yazma Butonu
        tk.Button(root, text="Dosyaya Veri Yaz ve Sil", command=self.write_and_delete_data, bg="#E06C75", fg="white", font=("Helvetica", 12, "bold"), relief="flat", cursor="hand2").pack(pady=20)

        # Durum Mesajı
        self.status_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#282C34", fg="white")
        self.status_label.pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_label.config(text=f"Seçilen Dosya: {self.file_path}")
            messagebox.showinfo("Dosya Seçildi", f"Seçilen dosya: {self.file_path}")

    def write_and_delete_data(self):
        try:
            passes = int(self.passes_entry.get())
            if not os.path.exists(self.file_path):
                messagebox.showerror("Hata", "Dosya bulunamadı.")
                return
            
            # Dosyanın içeriğini sıfırlama
            file_size = os.path.getsize(self.file_path)
            with open(self.file_path, "wb") as f:  # Dosya yazma modunda açılır (bütün içerik silinir)
                f.write(b'\x00' * file_size)  # Dosya içeriği tamamen sıfırlanır

            # Ardından rastgele veriler yazma
            with open(self.file_path, "ba+", buffering=0) as f:
                for i in range(passes):
                    f.seek(0)  # Dosyanın başına gider
                    f.write(os.urandom(file_size))  # Dosyanın tamamına rastgele veriler yazılır
                    self.status_label.config(text=f"Geçiş {i + 1}/{passes} tamamlandı...")
                    self.root.update_idletasks()  # Durumu güncelle

            # Dosya Silme İşlemi
            os.remove(self.file_path)
            self.status_label.config(text="Dosya güvenli bir şekilde silindi.")
            messagebox.showinfo("Başarılı", "Dosyaya veri başarıyla yazıldı ve dosya güvenli bir şekilde silindi.")
        except Exception as e:
            messagebox.showerror("Hata", str(e))

# Arayüz başlatma
root = tk.Tk()
app = SecureDeleteApp(root)
root.mainloop()
