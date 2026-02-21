from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def send_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(update.effective_user.id))

app = ApplicationBuilder().token("8587741574:AAGxlCojTnZ4B8Vq9IiFE5AfwU8L2lvgMiU").build()
app.add_handler(MessageHandler(filters.ALL, send_id))
app.run_polling()
