import os
import requests
import json
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

ACCESS_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

def enviar_a_whatsapp(body):
    try:
        url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }

        response = requests.post(url, data=json.dumps(body), headers=headers)

        if response.status_code == 200:
            return True
        else:
            print("❌ Error en WhatsApp API:", response.text)
            return False

    except Exception as e:
        print("❌ Excepción al enviar:", e)
        return False
