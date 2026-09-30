from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class FoodRecepieService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["FOODRECEPIE_BASE_URL"])

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "Error",
            "message": str(e)
        }
    
    def searchIngredientsFoodItem(self, foodItem : str):
        try:
            qpParams = {
                "s": foodItem
            }
            response = self.client.getCall("search.php", qpParams=qpParams)
            meals =  response["meals"]
            results = []
            for meal in meals:
                obj = {}
                obj["id"] = meal["idMeal"]
                obj["name"] = meal["strMeal"]
                results.append(obj)
            return results  
        except Exception as e:
            return self._handleError(e)

    def getRecepieDetailsForFoodItem(self, foodItemId : str):
        try:
            qpParams = {
                "i": foodItemId
            }
            response = self.client.getCall("lookup.php", qpParams=qpParams)
            return response
        except Exception as e:
            return self._handleError(e)
