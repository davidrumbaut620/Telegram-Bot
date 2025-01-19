from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Token del bot
TOKEN = '6705477288:AAG6o1otav_OCfC23pRBKhYoFnCwV-ZTMS8'

# Función que se ejecuta al recibir el comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hola, este es el token del bot: 6705477288:AAG6o1otav_OCfC23pRBKhYoFnCwV-ZTMS8. Estoy usando iSH en mi iPhone 16."
    )

# Función principal para configurar y ejecutar el bot
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot en ejecución...")
    app.run_polling()

if __name__ == '__main__':
    main()
