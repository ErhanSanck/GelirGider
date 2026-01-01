import tkinter as tk
from tkinter import messagebox, ttk

class KarHesaplayici:
    def __init__(self, root):
        self.root = root
        self.root.title("Sınıf Finansal Takip Paneli")
        self.root.geometry("600x700")

        self.dersler = []
        self.ogrenciler = []

        # --- DERS BÖLÜMÜ ---
        tk.Label(root, text="DERS VE ÖĞRETMEN BİLGİLERİ", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_ders = tk.Frame(root)
        frame_ders.pack(pady=5)

        tk.Label(frame_ders, text="Ders Adı:").grid(row=0, column=0)
        self.ent_ders_adi = tk.Entry(frame_ders)
        self.ent_ders_adi.grid(row=0, column=1)

        tk.Label(frame_ders, text="Haftalık Saat:").grid(row=1, column=0)
        self.ent_saat = tk.Entry(frame_ders)
        self.ent_saat.grid(row=1, column=1)

        tk.Label(frame_ders, text="Saat Ücreti (TL):").grid(row=2, column=0)
        self.ent_ucret = tk.Entry(frame_ders)
        self.ent_ucret.grid(row=2, column=1)

        tk.Button(root, text="Ders Ekle", command=self.ders_ekle, bg="lightblue").pack(pady=5)

        # --- ÖĞRENCİ BÖLÜMÜ ---
        tk.Label(root, text="ÖĞRENCİ KAYIT BÖLÜMÜ", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_ogrenci = tk.Frame(root)
        frame_ogrenci.pack(pady=5)

        tk.Label(frame_ogrenci, text="Öğrenci Adı:").grid(row=0, column=0)
        self.ent_ogrenci_adi = tk.Entry(frame_ogrenci)
        self.ent_ogrenci_adi.grid(row=0, column=1)

        tk.Label(frame_ogrenci, text="Aylık Kayıt Ücreti:").grid(row=1, column=0)
        self.ent_kayit_ucreti = tk.Entry(frame_ogrenci)
        self.ent_kayit_ucreti.grid(row=1, column=1)

        tk.Button(root, text="Öğrenci Ekle", command=self.ogrenci_ekle, bg="lightgreen").pack(pady=5)

        # --- LİSTE GÖRÜNÜMÜ ---
        self.txt_ozet = tk.Text(root, height=10, width=70)
        self.txt_ozet.pack(pady=10)

        # --- HESAPLA BUTONU ---
        tk.Button(root, text="AYLIK KAR/ZARAR HESAPLA", command=self.final_hesapla, 
                  bg="orange", font=("Arial", 10, "bold")).pack(pady=10)

    def ders_ekle(self):
        try:
            ad = self.ent_ders_adi.get()
            saat = float(self.ent_saat.get())
            ucret = float(self.ent_ucret.get())
            aylik_maliyet = saat * ucret * 4
            self.dersler.append({"ad": ad, "maliyet": aylik_maliyet})
            self.txt_ozet.insert(tk.END, f"Ders Eklendi: {ad} (Aylık Gider: {aylik_maliyet} TL)\n")
            self.ent_ders_adi.delete(0, tk.END)
            self.ent_saat.delete(0, tk.END)
            self.ent_ucret.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sayısal değerleri doğru girin!")

    def ogrenci_ekle(self):
        try:
            ad = self.ent_ogrenci_adi.get()
            ucret = float(self.ent_kayit_ucreti.get())
            self.ogrenciler.append({"ad": ad, "gelir": ucret})
            self.txt_ozet.insert(tk.END, f"Öğrenci Eklendi: {ad} (Aylık Gelir: {ucret} TL)\n")
            self.ent_ogrenci_adi.delete(0, tk.END)
            self.ent_kayit_ucreti.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen ücret kısmına sayı girin!")

    def final_hesapla(self):
        toplam_gider = sum(d['maliyet'] for d in self.dersler)
        toplam_gelir = sum(o['gelir'] for o in self.ogrenciler)
        kar = toplam_gelir - toplam_gider

        sonuc = f"\n--- FİNANSAL ÖZET ---\n"
        sonuc += f"Toplam Aylık Gider: {toplam_gider:.2f} TL\n"
        sonuc += f"Toplam Aylık Gelir: {toplam_gelir:.2f} TL\n"
        sonuc += f"NET DURUM: {kar:.2f} TL "
        sonuc += " (KAR) ✅" if kar >= 0 else " (ZARAR) ❌"

        messagebox.showinfo("Hesaplama Sonucu", sonuc)
        self.txt_ozet.insert(tk.END, sonuc + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = KarHesaplayici(root)
    root.mainloop()
