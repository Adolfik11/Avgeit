
# Avgeit Telegram Bot — установка и запуск

## 1. Установка локально

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Создайте бота через BotFather → получите новый токен.

3. Установите переменную окружения:
**Windows (PowerShell):**
```
setx BOT_TOKEN "ВАШ_ТОКЕН"
```
**Mac/Linux:**
```
export BOT_TOKEN="ВАШ_ТОКЕН"
```

4. Запустите:
```
python bot.py
```

---

## 2. Установка на Render.com

1. Создайте GitHub репозиторий и загрузите туда файлы.

2. Перейдите в Render → **New → Background Worker**.

3. Настройки:
- **Build Command:**  
  ```
  pip install -r requirements.txt
  ```
- **Start Command:**  
  Будет взят из Procfile → `worker: python bot.py`

4. Перейдите в раздел **Environment Variables** и добавьте:
```
BOT_TOKEN = ваш_новый_токен
```

5. Нажмите **Create Worker**.

Бот запустится через Long Polling — вебхук не требуется.
