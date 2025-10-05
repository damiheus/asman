
import os
from pyroSAR import identify, Archive
from pyroSAR.snap.util import geocode


SAR_DOSYA_YOLU = "S1A_IW_GRDH_1SDV_20210816T155035_20210816T155100_039257_04A28F_E1A9.SAFE.zip"


VERITABANI_ADI = "sar_katalogum.db"


CIKTI_KLASORU = "islenmis_haritalar"




try:
 


  
    print(f"'{os.path.basename(SAR_DOSYA_YOLU)}' dosyası okunuyor...")
    sahne = identify(SAR_DOSYA_YOLU)
    print("Dosya kimliği başarıyla okundu.")


    with Archive(VERITABANI_ADI) as arsiv:
        print(f"'{VERITABANI_ADI}' veritabanı açıldı.")
        
        arsiv.insert(sahne)
        print("Sahne meta verileri veritabanına başarıyla eklendi!")





    print("Bu işlem, bilgisayarınızın hızına bağlı olarak BİRKAÇ DAKİKA sürebilir. Lütfen bekleyin...")

    geocode(
        infile=SAR_DOSYA_YOLU,      
        outdir=CIKTI_KLASORU,       
        t_srs=4326,                 
        spacing=20                  
    )


    tam_cikti_yolu = os.path.abspath(CIKTI_KLASORU)
    print("\nİşlem başarıyla tamamlandı!")
    print(f"Sonuçlar şu klasöre kaydedildi: {tam_cikti_yolu}")



except FileNotFoundError:
    print(f"\n!!! HATA: Dosya bulunamadı !!!")
except RuntimeError as e:
    print(f"\n!!! CİDDİ HATA: Bir şeyler ters gitti !!!")
    print(f"Hata mesajı: {e}")
except Exception as e:
    print(f"\n!!! BEKLENMEDİK BİR HATA OLUŞTU !!!")
    print(f"Hata: {e}")
