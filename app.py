from flask import Flask, request
from WhatsappService.whatsapp_service import enviar_a_whatsapp
from OpenaiService.openai_service import responder_con_gpt

app = Flask(__name__)

@app.route("/WhatsApp", methods=["POST"])
def recibir_mensaje():
    try:
        data = request.get_json()
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]
        texto = mensaje["text"]["body"]
        numero = mensaje["from"]

        print(f"📨 Texto recibido del usuario: {texto}")

        respuesta = responder_con_gpt(texto)
        mensaje_body = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "text",
            "text": {
                "body": respuesta
            }
        }

        enviado = enviar_a_whatsapp(mensaje_body)
        if enviado:
            print("✅ Mensaje enviado correctamente.")
        else:
            print("❌ Error al enviar el mensaje.")

    except Exception as e:
        print("❌ Error general:", e)

    return "EVENT_RECEIVED"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
