from agents.food_recepie_agent import analyseFoodItem
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseFoodItem(prompt=prompt))