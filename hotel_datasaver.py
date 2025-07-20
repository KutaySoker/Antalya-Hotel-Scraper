import json
import pandas as pd

def json_to_excel(json_file, excel_file):
    # JSON dosyasını oku
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Eğer JSON içeriği bir liste değilse listeye dönüştür
    if isinstance(data, dict):
        data = [data]
    
    # Beklenen sütunlar
    expected_columns = ["name", "classification", "email", "phone", "website"]
    
    # Pandas DataFrame'e çevir
    df = pd.DataFrame(data)
    
    # Sadece gerekli kolonları seç (olmayanları boş bırakır)
    for col in expected_columns:
        if col not in df.columns:
            df[col] = None
    df = df[expected_columns]
    
    # Excel dosyasına yaz
    df.to_excel(excel_file, index=False)
    print(f"✅ {excel_file} başarıyla oluşturuldu.")

if __name__ == "__main__":
    json_to_excel("filtered_hotels.json", "filtered_hotels.xlsx")
