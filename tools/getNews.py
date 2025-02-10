import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import sys
sys.path.append("A:/Project Astra/play_audio.py")
from play_audio import eff

load_dotenv()
newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_top_news(topic):
    print(f"Fetching top news for topic: {topic}")
    eff("./sound_effects/fetching.mp3")
    try:
        top_headlines = newsapi.get_top_headlines(
            q=topic,
            sources='bbc-news,the-verge',
            language='en',
            page_size=2
        )

        if top_headlines['status'] == 'ok':
            articles = top_headlines['articles']
            news_summary = ""
            for article in articles:
                title = article['title']
                description = article['description']
                url = article['url']
                news_summary += f"Title: {title}\nDescription: {description}\nLink: {url}\n\n"
            return news_summary
        else:
            return "Sorry, I couldn't fetch the latest news right now."
    except Exception as e:
        return f"An error occurred: {e}"
