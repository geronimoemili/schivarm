import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Abilita il logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Definisci una funzione di start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Ciao! Sono un bot di esempio. Inviami un messaggio e ti risponderò!')

# Definisci una funzione di echo
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Definisci una funzione di errore
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    # Inserisci il tuo token qui
    token = 'YOUR_TELEGRAM_BOT_TOKEN'

    # Crea l'Updater e passa il token del bot
    updater = Updater(token)

    # Ottieni il dispatcher per registrare gli handler
    dispatcher = updater.dispatcher

    # Comandi
    dispatcher.add_handler(CommandHandler("start", start))

    # Messaggi
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log degli errori
    dispatcher.add_error_handler(error)

    # Avvia il bot
    updater.start_polling()

    # Esegui il bot fino a quando non riceve un segnale di arresto
    updater.idle()

if __name__ == '__main__':
    main()
