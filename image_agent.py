# Next AGI Verse - Image Agent

def create_image_prompt(topic):
    prompt = f"""
Create a professional blog featured-image concept for:

Topic: {topic}

Style:
- futuristic AI technology
- premium editorial look
- clean composition
- 16:9 landscape
- suitable for a technology blog
- no watermark
- no unnecessary text
"""
    return prompt.strip()


if __name__ == "__main__":
    topic = "Artificial General Intelligence"
    print("🖼️ Image Prompt:")
    print(create_image_prompt(topic))
