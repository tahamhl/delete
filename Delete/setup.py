from cx_Freeze import setup, Executable

executables = [Executable("Delete.py", base="Win32GUI", targetName="SecureDeleteApp.exe")]

setup(
    name="SecureDeleteApp",
    version="1.0",
    description="Güvenli Dosya Üzerine Veri Yazma ve Silme Aracı",
    options={
        "build_exe": {
            "includes": ["tkinter", "os", "random"],  # Kullanılan tüm modülleri dahil edin
            "packages": ["tkinter"],  # Eğer başka paketler kullanıyorsanız bunları da ekleyin
            "include_files": []  # Eğer dış dosyalar (görseller, vb.) eklemeniz gerekiyorsa buraya yazabilirsiniz
        }
    },
    executables=executables
)
