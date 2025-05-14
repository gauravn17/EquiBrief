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
    try:
        if len(full_text) > 12000:
            # Chunk large text for map-reduce summarization
            chunks = chunk_text(full_text)
            intermediate_summaries = []
            for chunk in chunks:
                summary = summarize_text(chunk)
                intermediate_summaries.append(summary)
            return summarize_text("\n".join(intermediate_summaries))
        
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
        return response['choices'][0]['message']['content']
    
    except openai.error.OpenAIError as e:
        return f"[ERROR] OpenAI API error: {e}"

def chunk_text(text, max_tokens=2000):
    """Split long text into chunks that stay within the token limit."""
    paragraphs = text.split("\n\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current + para) < max_tokens * 4:
            current += para + "\n\n"
        else:
            chunks.append(current)
            current = para + "\n\n"
    if current:
        chunks.append(current)
    return chunks
