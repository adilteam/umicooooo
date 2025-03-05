import requests
import json

# API m?lumatlar?
API_URL = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection"
X_API_KEY = "bc7cc0c7-d17c-420d-b838-ce63daaa6b7f"  # Birinci API acar? (x-api-key)
API_KEY = "932c5778-16aa-4174-a35b-811f19e328dc"  # Ikinci API acar? (ApiKey)
HEADERS = {
    "x-api-key": X_API_KEY,  # Birinci API acar? basl?qda ?lav? edildi
    "Content-Type": "application/json"
}

# Qiym?ti yenil?m?k ucun funksiya
def update_price_on_umico(gtin, new_price, old_price=None):
    """
    Bu funksiya Umico.az API vasit?sil? qiym?ti yenil?yir.
    """
    # JSON b?d?ni
    payload = {
        "product_offers": [
            {
                "gtin": gtin,  # Barkod
                "retail_price": new_price,  # Yeni qiym?t
                "old_price": old_price,  # Endirimsiz qiym?t (optional)
                "quantity": 1,  # Stokda olan miqdar
                "installment_enabled": True,  # Taksit secimi aktivdir
                "discount_effective_start_date": "12.12.2024 00:00:00",  # Kampaniya baslama tarixi
                "discount_effective_end_date": "12.12.2024 23:59:59",  # Kampaniya bitm? tarixi
                "api_key": API_KEY  # Ikinci API acar? JSON b?d?nind? ?lav? edildi
            }
        ]
    }

    # API sorgusu gond?rm?k
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    
    # Cavab? yoxlamaq
    if response.status_code == 200:
        print(f"Qiym?t ugurla yenil?ndi! Yeni qiym?t: {new_price} AZN")
        print("Task UUID:", response.json().get("task_uuid"))
    else:
        print(f"X?ta bas verdi: {response.status_code}, {response.text}")

# Test ucun ?sas funksiya
def main():
    gtin = "1234567098765487658765"  # Test ucun barkod
    new_price = 100.00  # Test ucun yeni qiym?t
    old_price = 120.00  # Test ucun kohn? qiym?t (optional)

    # Qiym?ti Umico.az-da yenil?
    update_price_on_umico(gtin, new_price, old_price)

# Skripti is? sal
if __name__ == "__main__":
    main()