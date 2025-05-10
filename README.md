# Mego AI Telegram Bot

## Features
- ChatGPT-style text conversations
- Image understanding via GPT-4-Vision
- Accepts files (optional future analysis)

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mego-ai-bot.git
cd mego-ai-bot
```

### 2. Setup Environment
```bash
cp .env.example .env
# Edit .env with your keys
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Bot
```bash
uvicorn main:app --reload
```

## Deploy to Railway
- Push your repo to GitHub
- Go to [https://railway.app](https://railway.app)
- New Project > Deploy from GitHub
- Set environment variables from your `.env`

You're done! Your Mego AI bot is live on Telegram.
