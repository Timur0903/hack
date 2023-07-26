import telegram
from django.conf import settings

def send_music_to_telegram(title, artist, audio_file_path):
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    chat_id = settings.TELEGRAM_CHAT_ID

    caption = f"New music added!\nTitle: {title}\nArtist: {artist}"
    bot.send_audio(chat_id=chat_id, audio=open(audio_file_path, 'rb'), caption=caption)
