
import sqlite3
from telegram import Update,InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,InlineQueryHandler,MessageHandler, filters

conn = sqlite3.connect('films.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS films
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   year INTEGER,
                   director TEXT,
                   description TEXT)''')
conn.commit()

async def add_film(update, context):
    
    title = context.args[0]
    year = context.args[1]
    director = context.args[2]
    description = ' '.join(context.args[3:])
    cursor.execute("INSERT INTO films (title, year, director, description) VALUES (?, ?, ?, ?)",
                   (title, year, director, description))
    conn.commit()
    await update.message.reply_text('Фильм успешно добавлен в вашу фильмотеку!')

async def delete_film(update, context):
    title = ' '.join(context.args)
    cursor.execute("DELETE FROM films WHERE title=?", (title,))
    conn.commit()
    await update.message.reply_text('Фильм успешно удален из вашей фильмотеки!')


async def edit_film(update, context):
    title = context.args[0]
    field = context.args[1]
    value = ' '.join(context.args[2:])
    cursor.execute(f"UPDATE films SET {field}=? WHERE title=?", (value, title))
    conn.commit()
    await update.message.reply_text('Информация о фильме успешно обновлена!')


async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = 'Список команд:\n\n'
    message += '/addfilm <название> <год> <режиссер> <описание> - добавить новый фильм в вашу фильмотеку\n'
    message += '/deletefilm <название> - удалить фильм из вашей фильмотеки\n'
    message += '/viewfilms - просмотреть список фильмов в вашей фильмотеке\n'
    message += '/editfilm <название> <поле> <значение> - редактировать информацию о фильме в вашей фильмотеке\n'
    await update.message.reply_text(message)
    
async def view_films(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor.execute("SELECT * FROM films")
    films = cursor.fetchall()
    if len(films) == 0:
        update.message.reply_text('Ваша фильмотека пуста!')
        return
    message = 'Список фильмов в вашей фильмотеке:\n\n'
    for film in films:
        message += f'{film[1]} ({film[2]})\nРежиссер: {film[3]}\nОписание: {film[4]}\n\n'
    await update.message.reply_text(message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Добро пожаловать в вашу личную фильмотеку! Введите /help для получения списка команд.')

async def unknown(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ТАКИХ КОМАНДОВ НЕМА")




app = ApplicationBuilder().token("556541562:AAEHH95VNPvvc-S0HP_uWNyqkHZmumFZsro").build()
app.add_handler(CommandHandler("start", start))  #complit
app.add_handler(CommandHandler("help", help))#complit
app.add_handler(CommandHandler("addfilm", add_film))
app.add_handler(CommandHandler("deletefilm", delete_film))
app.add_handler(CommandHandler('viewfilms', view_films))#complit
app.add_handler(CommandHandler("editfilm", edit_film))
app.add_handler(MessageHandler(filters.COMMAND, unknown))#complit

app.run_polling()
