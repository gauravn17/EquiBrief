import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def summarize_text(full_text):
    """
    Summarize the given text using OpenAI's GPT-3.5-turbo model.
    
    Args:
        full_text (str): The text to summarize.
        
    Returns:
        str: The summarized text.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please summarize the following text:\n\n{full_text}"}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response['choices'][0]['message']['content']
    return summary