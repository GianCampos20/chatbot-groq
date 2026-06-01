import os
from dotenv import load_dotenv

# SOLO carga .env si existe (LOCAL)
load_dotenv()

class Router:

    @staticmethod
    def returnApiKey():
        api_key = os.getenv("GROO_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GROO_API_KEY no configurada (ni en .env ni en entorno)"
            )

        return api_key.strip()

    @staticmethod
    def baseUrl():
        return "https://api.groq.com/openai/v1"