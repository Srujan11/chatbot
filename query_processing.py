import asyncio, json
import re

from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def query_to_bing_gpt(query):
	print(f"{query} to AI")
	cookies = json.loads(open("bing_cookies_*.json", encoding="utf-8").read())

	bot = await Chatbot.create(cookies = cookies) # Passing cookies is "optional", as explained above

	response = await bot.ask(prompt=query, conversation_style=ConversationStyle.creative, simplify_response=True)

    # response = await bot.ask(prompt="who is the director of no time to die?", conversation_style=ConversationStyle.creative, simplify_response=True)
    # response = await bot.ask(prompt="what is the imdb rating of no time to die?", conversation_style=ConversationStyle.creative, simplify_response=True)
    # response = await bot.ask(prompt="imdb rating of no time to die?", conversation_style=ConversationStyle.creative, simplify_response=True)

    # print(json.dumps(response, indent=2)) # Returns

    # Define the pattern to match the substrings
	pattern = r"\[\^\d+\^\]"

    # Use re.sub() to remove the substrings
	new_string = re.sub(pattern, "", response["text"])

	print(new_string)

	await bot.close()

	return new_string
