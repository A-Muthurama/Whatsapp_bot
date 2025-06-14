# 📰 WhatsApp News Bot using Twilio & NewsAPI

This Python bot automatically sends the latest news headlines on a selected topic (like “India Technology”) to your WhatsApp using Twilio and NewsAPI.

## 🚀 Features

- 🗞️ Fetches top 3 latest news headlines every hour
- 📤 Sends them via WhatsApp using Twilio API
- 🌍 Supports English language news from India
- 🛡️ Simple error handling and hourly scheduler

---

## 📦 Dependencies

- Python 3.x
- `requests`
- `twilio`
- `python-dotenv` (for environment variable loading)

---
Install dependencies:

```Terminal ( to install packages)
pip install requests twilio
---
🛠 Project Setup

1. Twilio WhatsApp API Setup

Go to: https://www.twilio.com/whatsapp

Activate the Sandbox and send the code (e.g., join xxxx) to +14155238886 via WhatsApp

Get your Account SID and Auth Token from the Twilio Console

Note down:
   Sandbox Number: +14155238886
   Your WhatsApp Number: +91xxxxxxxxxx

2. NewsAPI Setup

Go to: https://newsapi.org

Create a free account and get your API Key

Use this API endpoint:
https://newsapi.org/v2/everything?q=TOPIC&apiKey=YOUR_API_KEY
