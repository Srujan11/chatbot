import openai

async def query_to_bing_gpt(query):
	print(f"{query} to AI")
	# Set up your OpenAI API credentials
	openai.api_key = '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'

	# Generate a completion using the OpenAI API
	response = openai.Completion.create(
	  engine="text-davinci-003",
	  prompt=query,
	  max_tokens=50,
	  n=1,
	  stop=None,
	  temperature=0.2
	)

	# Get the generated answer from the API response
	answer = response.choices[0].text.strip()
	print(answer)

	return answer
