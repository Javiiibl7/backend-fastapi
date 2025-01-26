from fastapi import FastAPI

app = FastAPI()

@app.get("/", operation_id="get_root")
def read_root():
    return {"message": "¡Tu backend está funcionando correctamente!"}
from fastapi import FastAPI, UploadFile, File
import PyPDF2

app = FastAPI()

@app.post("/process-pdf", operation_id="process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        # Leer el contenido del PDF
        pdf_reader = PyPDF2.PdfReader(file.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Crear un resumen del contenido
        summary = text[:500] + "..." if len(text) > 500 else text
        return {
            "summary": summary,
            "message": "PDF procesado exitosamente."
        }
    except Exception as e:
        return {"error": str(e), "message": "Ocurrió un error al procesar el PDF."}

from fastapi import FastAPI
from twilio.rest import Client

app = FastAPI()

# Configuración de Twilio (reemplaza con tus datos)
TWILIO_ACCOUNT_SID = "tu_account_sid"
TWILIO_AUTH_TOKEN = "tu_auth_token"
TWILIO_PHONE_NUMBER = "tu_numero_de_twilio"

@app.post("/send-message", operation_id="send_message")
async def send_message(recipient: str, message: str):
    """
    Enviar un mensaje personalizado a través de Twilio.
    :param recipient: Número de teléfono del destinatario (formato internacional, ej. +34...).
    :param message: El contenido del mensaje.
    """
    try:
        # Configura el cliente de Twilio
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Envía el mensaje
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient
        )

        return {"message": "Mensaje enviado exitosamente."}
    except Exception as e:
        return {"error": str(e), "message": "Ocurrió un error al enviar el mensaje."}
