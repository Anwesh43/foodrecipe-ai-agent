from pydantic_ai import Agent
from tools.food_recepie_tools import getRecepieDetailsForFoodItem, searchIngredientsFoodItem, writeHTML
from prompts.fr_system_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = [getRecepieDetailsForFoodItem, searchIngredientsFoodItem, writeHTML],
    system_prompt = SYSTEM_PROMPT
)

async def analyseFoodItem(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')