import requests
import time
from twilio.rest import Client

# API Keys and constants
TOPIC = "Artificial intelligence"
NEWS_API_KEY = "your_newsdata_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
FROM_WHATSAPP_NUMBER = "whatsapp:+14155238886"
TO_WHATSAPP_NUMBER = "whatsapp:+91xxxxxxxxxx"


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def get_latest_news():
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={TOPIC}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=3&"
        f"apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok" and data.get("articles"):
            messages = []
            for article in data["articles"]:
                title = article.get("title", "No Title")
                source = article.get("source", {}).get("name", "Unknown Source")
                pub_date = article.get("publishedAt", "No Date")[:10]
                link = article.get("url", "#")
                messages.append(f"🗞️ *{title}*\n📍{source} | 🕒 {pub_date}\n🔗 {link}")
            return "\n\n".join(messages)
        else:
            return "⚠️ No news found or API limit reached."

    except Exception as e:
        return f"❌ Error fetching news: {str(e)}"

def send_whatsapp_message(message):
    try:
        msg = client.messages.create(
            from_=FROM_WHATSAPP_NUMBER,
            body=message,
            to=TO_WHATSAPP_NUMBER
        )
        print(f"✅ Message sent. SID: {msg.sid}")
    except Exception as e:
        print(f" Error sending message: {str(e)}")

# Main loop - runs every 1 hour
while True:
    news = get_latest_news()
    send_whatsapp_message(news)
    time.sleep(3600)  # 1 hour
