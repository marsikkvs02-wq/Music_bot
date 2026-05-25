import os
import yt_dlp
from aiogram import Router, types
from aiogram.types import FSInputFile
from utils.messages import API_ERROR, FILE_TOO_BIG

router = Router()

@router.callback_query(lambda c: c.data.startswith("dl_"))
async def download_track(callback: types.CallbackQuery):
    video_id = callback.data.replace("dl_", "")
    url = f"https://www.youtube.com/watch?v={video_id}"

    await callback.answer("Скачиваю...")

    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"downloads/{video_id}.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }],
            "quiet": True,
        }

        os.makedirs("downloads", exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        filepath = f"downloads/{video_id}.mp3"
        file_size = os.path.getsize(filepath)

        if file_size > 50_000_000:
            await callback.message.answer(FILE_TOO_BIG)
            os.remove(filepath)
            return

        audio = FSInputFile(filepath)
        await callback.message.answer_audio(audio, title=callback.message.text)

        os.remove(filepath)

    except Exception:
        await callback.message.answer(API_ERROR)
