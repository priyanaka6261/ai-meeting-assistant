from transformers import pipeline

# load summarization model
summarizer = pipeline("text-generation", model="google/flan-t5-small")

def generate_summary(transcript):

    prompt = f"Summarize the following meeting discussion:\n{transcript}"

    result = summarizer(
        prompt,
        max_length=120
    )

    return result[0]["generated_text"]
