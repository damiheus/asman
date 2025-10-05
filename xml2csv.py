import os
import csv
from pyroSAR.drivers import identify

def nasa_xml_to_csv(indir, outfile):
   
    all_metadata = []

    for item in os.listdir(indir):
        item_path = os.path.join(indir, item)
        
      
        if os.path.isdir(item_path):
            try:
          
                scene = identify(item_path)
                
             
                metadata = scene.meta
                
               
                metadata['source_file'] = item_path
                
                all_metadata.append(metadata)
                print(f"Başarıyla okundu: {item_path}")

            except Exception as e:
                print(f"Hata: {item_path} okunurken bir sorun oluştu - {e}")

    if not all_metadata:
        print("Hiçbir meta veri bulunamadı.")
        return

 
    header = set()
    for meta in all_metadata:
        header.update(meta.keys())
    header = sorted(list(header))

    with open(outfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        
  
        writer.writeheader()
        
        writer.writerows(all_metadata)

    print(f"\nCSV dosyası başarıyla oluşturuldu: {outfile}")


if __name__ == '__main__':
 
    input_directory = "S1A_IW_GRDH_1SDV_20210723T155034_20210723T155059_038907_049743_FA4D.SAFE/annotation/"
    
    output_csv_file = "nasa_sar_metadata.csv"

  
