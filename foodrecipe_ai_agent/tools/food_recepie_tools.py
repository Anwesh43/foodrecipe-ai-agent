from services.food_recepie_service import FoodRecepieService 

frs = FoodRecepieService()

def searchIngredientsFoodItem(foodItem : str):
    print(f"Calling searchIngredientsFoodItem tool for {foodItem}")
    return frs.searchIngredientsFoodItem(foodItem=foodItem)

def getRecepieDetailsForFoodItem(foodItemId : str): 
    print(f"Calling getRecepieDetailsForFoodItem tool {foodItemId}")
    return frs.getRecepieDetailsForFoodItem(foodItemId=foodItemId)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool to save in {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"Writing html to {fileName}, don't display html"
    }