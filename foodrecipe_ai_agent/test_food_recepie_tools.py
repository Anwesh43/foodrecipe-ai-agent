from tools.food_recepie_tools import getRecepieDetailsForFoodItem, searchIngredientsFoodItem
import json 
from typing import Dict 
def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data for {fileName}")

if __name__ == "__main__":
    items = searchIngredientsFoodItem("pizza")
    writeFile("test_pizza_data.json", items)
    if len(items) > 0:
        writeFile("test_food_item_dyn.json", getRecepieDetailsForFoodItem(items[0]["id"]))
