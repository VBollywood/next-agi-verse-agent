# Next AGI Verse - Content Agent

BLOG_NAME = "Next AGI Verse"


def create_article_plan(topic):
    return {
        "blog": BLOG_NAME,
        "topic": topic,
        "title": f"{topic}: Complete Guide",
        "sections": [
            "Introduction",
            "What is it?",
            "How it works",
            "Key features",
            "Advantages and limitations",
            "Real-world uses",
            "Frequently asked questions",
            "Conclusion",
        ],
    }


if __name__ == "__main__":
    topic = "AI Agents"
    plan = create_article_plan(topic)

    print("📝 Article Plan")
    print("Blog:", plan["blog"])
    print("Title:", plan["title"])

    print("\nSections:")
    for section in plan["sections"]:
        print("-", section)
