# Next AGI Verse - Main Agent

from content_agent import create_article_plan
from image_agent import create_image_prompt


def run_agent(topic):
    print("🤖 Next AGI Verse Agent")
    print("=" * 40)

    # 1. Content
    plan = create_article_plan(topic)

    print("\n📝 ARTICLE")
    print("Title:", plan["title"])

    for section in plan["sections"]:
        print("•", section)

    # 2. Image
    print("\n🖼️ IMAGE PROMPT")
    print(create_image_prompt(topic))

    print("\n✅ Planning complete")


if __name__ == "__main__":
    topic = "AI Agents"
    run_agent(topic)
