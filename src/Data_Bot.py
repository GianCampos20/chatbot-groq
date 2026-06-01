class Data_Bot:
    
    def get_data(message):
        
        return {
        "model" : "llama-3.1-8b-instant",
        "messages" : [
            {"role" : "system", "content" : "Eres un asistente útil y simpático"},
            {"role" : "user", "content" : message}  
        ]
     }