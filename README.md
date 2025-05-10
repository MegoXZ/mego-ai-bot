# Mego AI Telegram Bot (for Railway)

## Features
- GPT-4 and GPT-4-Vision support
- Telegram bot interaction with text, images, and files

## Getting Started

### 1. Clone and Push to GitHub
```bash
git clone https://github.com/YOUR_USERNAME/mego-ai-bot.git
cd mego-ai-bot
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/mego-ai-bot.git
git push -u origin main
```

### 2. Deploy to Railway
- Go to [https://railway.app](https://railway.app)
- Click **New Project** > **Deploy from GitHub Repo**
- Add Environment Variables:
  - TELEGRAM_TOKEN
  - OPENAI_API_KEY

### 3. Set the Start Command
```
python main.py
```

You're good to go!
