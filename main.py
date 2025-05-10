import os
import base64
from io import BytesIO
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import openai

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

app = FastAPI()
bot_app = Application.builder().token(TELEGRAM_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Mego AI. Send me a message, image, or file and I'll respond like ChatGPT!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_data = await file.download_as_bytearray()
    await update.message.reply_text("Received your file. (File analysis not yet implemented.)")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    img_bytes = await file.download_as_bytearray()
    b64_image = base64.b64encode(img_bytes).decode('utf-8')

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}}
                ]
            }
        ]
    )
    result = response['choices'][0]['message']['content']
    await update.message.reply_text(result)

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
bot_app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
bot_app.add_handler(MessageHandler(filters.PHOTO, handle_image))

@app.on_event("startup")
async def on_startup():
    bot_app.run_polling()
