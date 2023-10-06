import openai
from django.shortcuts import render

# Set your OpenAI API key here
openai.api_key = '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'

def chatbot_response(request):
    user_input = request.GET.get('input_text', '')

    # Use GPT-3 to generate a response
    response = generate_response(user_input)

    return render(request, 'enroll/index.html', {'response': response})

def generate_response(user_input):
    # You can customize the prompt and other options as needed
    prompt = f"User: {user_input}\nChatGPT:"

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50  # Adjust the number of tokens as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)
