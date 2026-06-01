class Header:
    @staticmethod
    def get_headers():
        from src.Router import Router
        api_key = Router.returnApiKey()
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }