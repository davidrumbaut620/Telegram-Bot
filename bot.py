import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el token desde el archivo .env
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    raise ValueError("El token no está definido en el archivo .env")

# Función que se ejecuta al recibir el comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hola, tu bot está funcionando correctamente. Estoy usando iSH en mi iPhone 16."
    )

# Función principal para configurar y ejecutar el bot
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot en ejecución...")
    app.run_polling()

if __name__ == '__main__':
    main()
