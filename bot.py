
    import logging
    import os

    from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
    from telegram.ext import (
        ApplicationBuilder,
        CommandHandler,
        ContextTypes,
        CallbackQueryHandler,
    )
    from telegram.error import TelegramError

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger = logging.getLogger(__name__)

    FORUM_CHAT_ID = "@avgeit"

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("✅ Вступить в форум", url="https://t.me/avgeit")],
            [InlineKeyboardButton("➡️ Продолжить", callback_data="continue_after_forum")],
        ]
        markup = InlineKeyboardMarkup(keyboard)

        text = (
            "👋 Добро пожаловать в <b>Avgeit AI</b>\n\n"
            "☑️ Для работы вступите в форум участников крипто‑приложения!\n\n"
            "После вступления нажмите «Продолжить»."
        )

        await update.message.reply_text(text, reply_markup=markup, parse_mode="HTML")

    async def handle_continue(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id

        try:
            member = await context.bot.get_chat_member(FORUM_CHAT_ID, user_id)
            subscribed = member.status in ("member", "administrator", "creator")
        except TelegramError:
            subscribed = False

        if not subscribed:
            await query.message.reply_text(
                "⚠️ Вы ещё не подписаны на форум.
"
                "Подпишитесь: https://t.me/avgeit
"
                "После этого снова нажмите «Продолжить»."
            )
            return

        keyboard = [
            [InlineKeyboardButton("🚀 Запустить", callback_data="launch_app")],
            [InlineKeyboardButton("💬 Менеджер", url="https://t.me/avgeit_meneger")],
        ]
        markup = InlineKeyboardMarkup(keyboard)

        text = (
            "🤖 <b>Avgeit</b> — приложение нового поколения для обучения AI‑агентов "
            "торговле на бирже.\n\n"
            "🏁 Минимальный старт — <b>100₽</b>.\n"
            "🚀 Децентрализация токенов.\n"
            "📱 Начни и открой свой вклад."
        )

        await query.message.reply_text(text, reply_markup=markup, parse_mode="HTML")

    async def launch_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(
            "🧩 Мини‑приложение Avgeit WebApp скоро будет подключено."
        )

    async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "ℹ️ Команды:\n/start — начать\n/help — помощь"
        )

    def main():
        token = os.getenv("BOT_TOKEN")
        if not token:
            raise RuntimeError("Переменная окружения BOT_TOKEN не установлена!")

        app = ApplicationBuilder().token(token).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_cmd))
        app.add_handler(CallbackQueryHandler(handle_continue, pattern="^continue_after_forum$"))
        app.add_handler(CallbackQueryHandler(launch_app, pattern="^launch_app$"))

        app.run_polling(allowed_updates=["message", "callback_query"])

    if __name__ == "__main__":
        main()
