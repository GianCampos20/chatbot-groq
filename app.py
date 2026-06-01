from flask import Flask, render_template, request, jsonify
import requests
import logging
import sys
import os
from src.Router import Router
from src.Header import Header
from src.Data_Bot import Data_Bot
from dotenv import load_dotenv

load_dotenv()

# Logs para Render
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

GROQ_BASE_URL = Router.baseUrl()


def get_bot_response(message):

    logger.debug("ENTRÓ EN get_bot_response")

    headers = Header.get_headers()
    data = Data_Bot.get_data(message)

    logger.debug(f"HEADERS: {headers}")
    logger.debug(f"DATA: {data}")

    try:
        response = requests.post(
            f"{GROQ_BASE_URL}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        logger.debug(f"STATUS: {response.status_code}")
        logger.debug(f"TEXT: {response.text}")

    except requests.exceptions.RequestException as e:
        logger.exception("ERROR EN REQUEST")
        return "Error de conexión con el modelo"

    if response.status_code != 200:
        return f"Error del modelo: {response.text}"

    try:
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        logger.exception("ERROR PARSEANDO RESPUESTA")
        return "Error al procesar la respuesta del bot"


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"response": "Mensaje vacío"}), 400

    bot_response = get_bot_response(user_message)

    return jsonify({"response": bot_response})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1000))
    app.run(host="0.0.0", port=port)