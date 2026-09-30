from services.food_recepie_service import FoodRecepieService 

frs = FoodRecepieService()

def searchIngredientsFoodItem(foodItem : str):
    print(f"Calling searchIngredientsFoodItem tool for {foodItem}")
    return frs.searchIngredientsFoodItem(foodItem=foodItem)

def getRecepieDetailsForFoodItem(foodItemId : str): 
    print(f"Calling getRecepieDetailsForFoodItem tool {foodItemId}")
    return frs.getRecepieDetailsForFoodItem(foodItemId=foodItemId)
