from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='26cf3063ed3f4c30a6cfe3684300c30f')

def get_top_news(topic):
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
