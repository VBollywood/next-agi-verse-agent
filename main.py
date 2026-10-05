import os
import requests

BLOG_NAME = "Next AGI Verse"
BLOG_URL = "https://nextagiverse.blogspot.com/"

API_KEY = os.environ.get("GEMINI_API_KEY")


def ask_ai(topic):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        ""gemini-3.8-flash:generateContent?key=" + API_KEY" + API_KEY
    )

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"""
You are the AI content planning agent for the blog "{BLOG_NAME}".

Blog URL:
{BLOG_URL}

Create an original and useful article plan about:

{topic}

Return:

1. SEO title
2. Meta description
3. Article outline
4. Important facts that should be verified
5. Featured image concept
6. 5 FAQ questions

Rules:
- Do not copy other websites.
- Do not invent facts.
- Make the content useful for readers.
- Keep the language clear and easy to understand.
"""
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        json=data,
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]


def main():
    topic = "AI Agents"

    print("🤖 Next AGI Verse Agent")
    print("🌐 Blog:", BLOG_URL)
    print("🧠 Connecting to Gemini...")

    if not API_KEY:
        print("❌ GEMINI_API_KEY is missing")
        return

    try:
        answer = ask_ai(topic)

        print("\n========== AI RESULT ==========\n")
        print(answer)
        print("\n========== END ==========")

    except Exception as error:
        print("❌ Agent Error:")
        print(error)


if __name__ == "__main__":
    main()
