from fastapi.responses import Response, JSONResponse

class ApiResponse:
          
    @staticmethod
    def response(status_code:int, status: str, message: str, data:dict|list={}):
        response = {}
        response["status"] = status
        response["message"] = message
        response["data"] = data
        if status_code != 200:
            return JSONResponse(status_code=status_code, content=response)
        return response
    
    