import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "7820150993:AAEQw_Fbbg72Xdf5gN00bX6ksj5633"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def handle_all_messages(message: types.Message):
    txt = message.text.strip()
    
    if "شراء" in txt or "سيرفر" in txt:
        text = (
            "🛒 **شراء سيرفر**\n\n"
            "____________________\n\n"
            "اختر نوع السيرفر المناسب لك 👇\n\n"
            "🇮🇶 **آسيا ريد**\n"
            "⚡ سرعة واستقرار عالي\n\n"
            "🎧 **أودي**\n"
            "🚀 أداء ممتاز للتصفح والألعاب\n\n"
            "____________________"
        )
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text="🇮🇶 آسيا ريد", callback_data="asia_reed")
        keyboard.button(text="🎧 أودي", callback_data="audi_server")
        keyboard.button(text="🔙 رجوع", callback_data="back_home")
        keyboard.adjust(1)
        await message.answer(text, reply_markup=keyboard.as_markup(), parse_mode="Markdown")
        
    elif "الأسعار" in txt:
        await message.answer("قائمة الأسعار الحالية")
        
    elif "حسابي" in txt:
        await message.answer("معلومات حسابك")
        
    else:
        await message.answer(f"النص المستلم: {txt}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
