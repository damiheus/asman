
from pyroSAR import identify

dosya_yolu = "S1A_IW_GRDH_1SDV_20210723T155034_20210723T155059_038907_049743_FA4D.zip"

try:
    sahne = identify(dosya_yolu)

 
    print("----- Dosya Başarıyla Okundu! -----")
    print(sahne)

    print("\n----- Bazı Önemli Bilgiler -----")
    print(f"Sensör: {sahne.sensor}")
    print(f"Çekim Modu: {sahne.acquisition_mode}")
    print(f"Yörünge: {sahne.orbit}")
    print(f"Çekim Başlangıç Zamanı: {sahne.start}")
    print(f"Polarizasyonlar: {sahne.polarizations}")

except FileNotFoundError:
    print(f"HATA: Dosya bulunamadı: {dosya_yolu}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
