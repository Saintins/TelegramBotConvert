# Telegram_bot_convert
Telegram bot with voice message recognition and generation. Speech to Text and Text to Speech.


### Опис
Telegram-бот з розпізнаванням та генерацією голосових повідомлень. Поки що протестований і працює тільки під Windows.


### Технології
aiogram, torch, vosk, silero, num2words, ffmpeg


### Алгоритм роботи
- Роспізнавання аудіо і голосових повідомлень: надсилаємо боту аудіо або голосове повідомлення, отримуємо текст.
- Генерація аудіо повідомлень: надсилаємо боту текст, отримуємо аудіо повідомлення.


### Команди
- /start - Приветствие, появляется при первом старте бота


### Запуск проекта
Клонуйте репозиторій та перейдіть в нього у командну строку:

```
git clone https://github.com/Saintins/TelegramBotConvert.git
cd tg_bot_stt_tts
```

Створіть і активуйте віртуальне занурення:

```
python -m venv venv
. env/Scripts/activate
```

Встановіть залежність із файлу requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Створіть файл .env та вкажіть токен вашого бота. Приклад є у .env_example. Процес створення телеграм бота та отримання токена не описаний.

Завантажте моделі та помістіть у необхідні папки. Де взяти моделі описано нижче.

Після завантаження моделей запустіть код bot.py в Python.


### Моделі Vosk и Silero, а також FFmpeg

***Vosk*** - оффлайн розпізнавання аудіо та отримання з нього тексту. Моделі доступні на сайті [проекту](https://alphacephei.com/vosk/models "Vosk - офлайн-розпізнавання аудіо"). Завантажте модель, розархівуйте та помістіть папку model з файлами у папку models/vosk.
- [vosk-model-ru-0.22       - 1.5 Гб](https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip "Модель vosk-model-ru-0.22 - 1.5 Гб") - краще розпізнає, але довше і важить багато.
- [vosk-model-small-ru-0.22 - 45 Мб](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip "Модель vosk-model-small-ru-0.22 - 45 Мб") - гірше розпізнає, але швидше та важить мало.

***Silero*** - оффлайн створення аудіо повідомлення з тексту.
У класі TTS проекту вказано [модель Silero v3.1 ru - 60 Мб](https://models.silero.ai/models/tts/ru/v3_1_ru.pt "Модель Silero v3.1 ru - 60 Мб"), яка сама скачається під час першого запуску проекту. Інші моделі можна завантажити [тут](https://github.com/snakers4/silero-models/blob/master/models.yml "Silero - оффлайн-создание аудио из текста") або на сайті [проекта](https://github.com/snakers4/silero-models "Silero - оффлайн-создание аудио из текста").

***FFmpeg*** - набір open-source бібліотек для конвертування аудіо- та відео в різних форматах.
Завантажте набір exe файлів із сайту [проекта](https://ffmpeg.org/download.html "FFmpeg - набор open-source библиотек для конвертирования аудио- и видео в различных форматах.")та помістіть файл ffmpeg.exe у папки models/vosk та models/silero.


### Автори
Олександр, Димитрій, Валентин 
