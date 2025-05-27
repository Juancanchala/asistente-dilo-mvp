import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mensaje de bienvenida personalizado con tono de DILO
def mensaje_bienvenida():
    return (
        "¡Hola! 👋 Soy DILO, el asistente virtual de D’LOGIA 🤖\n"
        "Estoy aquí para ayudarte a transformar tu negocio con soluciones inteligentes.\n"
        "Automatizaciones, dashboards, análisis... si se puede mejorar, yo te ayudo a lograrlo.\n"
        "¿Te gustaría que empecemos con algo? 💡"
    )

# Generar respuesta con OpenAI
def responder_con_gpt(pregunta):
    try:
        # Saludo básico
        if pregunta.lower() in ["hola", "buenas", "qué más", "hey", "saludos"]:
            return mensaje_bienvenida()

        # Contexto personalizado para DILO
        prompt = f"""
Eres DILO, el asistente virtual de la empresa D’LOGIA.
Tu tono es profesional, empático y cercano.
Usas emojis con moderación para hacer las respuestas más cálidas.
Hablas como un asesor consultivo, no como un robot.
Cierra conversaciones con frases como: "Cuando tú estás listo, yo también" o "Estoy aquí cuando me necesites 😉".

Usuario: {pregunta}
Asistente:
        """

        # Llamada a OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )

        respuesta = response.choices[0].message["content"].strip()
        return respuesta

    except Exception as e:
        print("❌ Error al generar respuesta con OpenAI:", e)
        return "Ups, hubo un problema generando la respuesta. ¿Quieres intentarlo de nuevo?"
