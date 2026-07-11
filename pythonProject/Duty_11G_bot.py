import logging
from datetime import datetime
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pytz
import sqlite3
import asyncio

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Настройки
TOKEN = "7590043137:AAHFmqbWG91v_vh4CyaCil3Ld34eCycmB5U"
DEADLINE_DATE = datetime(2025, 5, 25)
SKIP_NEXT_DAY = False

# Глобальная переменная для хранения chat_id
CHAT_ID = None


# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('duty_bot.db')
    cursor = conn.cursor()
    # Создаем таблицу, если она еще не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS duty_people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    return conn


# Функция для получения списка дежурных из базы данных
def get_duty_people():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM duty_people')
    people = [row[0] for row in cursor.fetchall()]
    conn.close()
    return people


# Функция для добавления нового дежурного в базу данных
def add_duty_person(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO duty_people (name) VALUES (?)', (name,))
        conn.commit()
        logger.info(f"Добавлен новый дежурный: {name}")
        return True
    except sqlite3.IntegrityError:
        logger.warning(f"Попытка добавить существующего дежурного: {name}")
        return False
    finally:
        conn.close()


# Функция для удаления дежурного из базы данных
def remove_duty_person(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM duty_people WHERE name = ?', (name,))
    conn.commit()
    removed = cursor.rowcount > 0
    conn.close()
    if removed:
        logger.info(f"Удален дежурный: {name}")
    else:
        logger.warning(f"Попытка удалить несуществующего дежурного: {name}")
    return removed


# Текущий индекс дежурного
current_duty_index = 0


# Функция для отправки сообщения о дежурстве
async def send_duty_message(context: ContextTypes.DEFAULT_TYPE):
    global current_duty_index, SKIP_NEXT_DAY

    if SKIP_NEXT_DAY:
        logger.info("Пропуск следующего дня 🏃‍♂️")
        SKIP_NEXT_DAY = False
        return

    today = datetime.now(pytz.timezone('Europe/Moscow')).date()

    if today >= DEADLINE_DATE.date():
        logger.info("Достигнута дата окончания работы бота. Завершение работы 🕒")
        return

    if today.weekday() == 6:  # Воскресенье
        logger.info("Сегодня воскресенье! Отдыхаем 😌")
        return

    duty_people = get_duty_people()
    if not duty_people:
        await context.bot.send_message(chat_id=CHAT_ID, text="Нет доступных дежурных 😔")
        return

    duty_person = duty_people[current_duty_index]
    message = f"✨ Сегодня {today.strftime('%d.%m.%Y')} дежурит {duty_person}! ✨"

    await context.bot.send_message(chat_id=CHAT_ID, text=message)

    current_duty_index = (current_duty_index + 1) % len(duty_people)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global CHAT_ID
    CHAT_ID = update.message.chat_id  # Сохраняем chat_id

    # Приветственное сообщение с описанием команд
    welcome_message = (
        "👋 Привет! Я бот для управления дежурством! 🤖\n\n"
        "Вот список доступных команд:\n"
        "/start - Начать работу с ботом и сохранить ваш chat_id 💬\n"
        "/test - Отправить тестовое сообщение с случайным дежурным 🎲\n"
        "/skip - Пропустить отправку сообщения на следующий день ⏭️\n"
        "/add <имя> - Добавить нового дежурного ➕\n"
        "/remove <имя> - Удалить дежурного ➖\n"
        "/list - Показать список всех дежурных 📋\n"
        "/stop - Остановить бота 🛑\n"
    )

    await update.message.reply_text(welcome_message)


# Команда /test
async def test_duty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    duty_people = get_duty_people()
    if not duty_people:
        await update.message.reply_text("Нет доступных дежурных 😔")
        return

    duty_person = random.choice(duty_people)
    await update.message.reply_text(f'🎲 Тестовое сообщение: сегодня дежурит {duty_person}!')


# Команда /skip
async def skip_next_day(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global SKIP_NEXT_DAY
    SKIP_NEXT_DAY = True
    await update.message.reply_text('⏭️ Следующий день будет пропущен.')


# Команда /add для добавления нового дежурного
async def add_duty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 1:
        await update.message.reply_text("⚠️ Пожалуйста, укажите имя дежурного.")
        return

    name = context.args[0]
    if add_duty_person(name):
        await update.message.reply_text(f'✅ Добавлен новый дежурный: {name}')
    else:
        await update.message.reply_text(f'❌ Дежурный с именем "{name}" уже существует.')


# Команда /remove для удаления дежурного
async def remove_duty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 1:
        await update.message.reply_text("⚠️ Пожалуйста, укажите имя дежурного.")
        return

    name = context.args[0]
    if remove_duty_person(name):
        await update.message.reply_text(f'🗑️ Дежурный "{name}" удален.')
    else:
        await update.message.reply_text(f'❌ Дежурный с именем "{name}" не найден.')


# Команда /list для вывода списка дежурных
async def list_duty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    duty_people = get_duty_people()
    if not duty_people:
        await update.message.reply_text("🤷‍♂️ Нет доступных дежурных.")
        return

    message = "📋 Список дежурных: " + ", ".join(duty_people) + "."
    await update.message.reply_text(message)


# Команда /stop для завершения работы бота
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🛑 Бот завершает работу. До свидания! 👋")
    logger.info("Бот завершает работу по команде /stop.")
    raise SystemExit("Бот завершил работу.")


# Функция для автоматического отключения бота в 10:00
async def auto_shutdown(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="⏰ Сейчас 10:00. Бот завершает работу. До свидания! 👋")
    logger.info("Бот завершает работу по расписанию (10:00).")
    raise SystemExit("Бот завершил работу.")


# Основная функция
async def main() -> None:
    global CHAT_ID

    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test_duty))
    application.add_handler(CommandHandler("skip", skip_next_day))
    application.add_handler(CommandHandler("add", add_duty))
    application.add_handler(CommandHandler("remove", remove_duty))
    application.add_handler(CommandHandler("list", list_duty))
    application.add_handler(CommandHandler("stop", stop))

    # Проверяем, есть ли chat_id
    if not CHAT_ID:
        logger.info("Ожидание получения chat_id...")

    # Планируем отправку сообщений в 8:30 утра каждый день
    job_queue = application.job_queue
    job_queue.run_daily(send_duty_message,
                        time=datetime.strptime('08:30', '%H:%M').time(),
                        days=(0, 1, 2, 3, 4, 5),  # Понедельник-Суббота
                        chat_id=CHAT_ID)

    # Планируем автоматическое отключение бота в 10:00
    job_queue.run_daily(auto_shutdown,
                        time=datetime.strptime('10:00', '%H:%M').time(),
                        days=(0, 1, 2, 3, 4, 5, 6),  # Каждый день
                        chat_id=CHAT_ID)

    # Запускаем бота
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Блокируем выполнение программы, чтобы бот продолжал работать
    while True:
        await asyncio.sleep(60)  # Ждём бесконечно, проверяя каждую минуту


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())