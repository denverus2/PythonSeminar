import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import google.auth
from googleapiclient.discovery import build


TOKEN = '556541562:AAEHH95VNPvvc-S0HP_uWNyqkHZmumFZsro'

 

# Создаем объект telegram.Bot с использованием токена

bot = telegram.Bot(token=TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для работы со справочником контактов Google.')

def search(update: Update, context: CallbackContext) -> None:
    # Получаем доступ к API Google Contacts
    creds, _ = google.auth.default()
    service = build('people', 'v1', credentials=creds)

    # Выполняем поиск контакта
    name = ' '.join(context.args)
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses',
        q=name
    ).execute()

    # Отправляем результаты поиска пользователю
    for person in results.get('connections', []):
        names = person.get('names', [])
        emails = person.get('emailAddresses', [])
        if names and emails:
            update.message.reply_text(f"Имя: {names[0]['displayName']}, Email: {emails[0]['value']}")

def main() -> None:
    updater = Updater(bot, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()