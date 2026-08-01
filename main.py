import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8670994653:AAFOmRKRGkaPmAG9Lccs9YCapDyivGp1YZU"

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
        keyboard.button(text="🔙 رجوع", callback_data="back_to_buy")
        keyboard.adjust(1)
        await message.answer(text, reply_markup=keyboard.as_markup(), parse_mode="Markdown")
        
    elif "الأسعار" in txt:
        await message.answer("قائمة الأسعار الحالية")
        
    elif "حسابي" in txt:
        await message.answer("معلومات حسابك")
        
    else:
        await message.answer(f"النص المستلم: {txt}")
@dp.callback_query(F.data == "asia_reed")
async def asia_reed_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="آسيا ريد 3 أشهر - 8000 دينار", callback_data="buy_asia_3m")
    keyboard.button(text="آسيا ريد شهرين - 6000 دينار", callback_data="buy_asia_2m")
    keyboard.button(text="آسيا ريد شهر - 4000 دينار", callback_data="buy_asia_1m")
    keyboard.button(text="رجوع 🔙", callback_data="back_to_buy")
    keyboard.adjust(1)
    
    await callback.message.edit_text(
        "📊 **باقات آسيا ريد:** 🇮🇶",
        reply_markup=keyboard.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()
@dp.callback_query(F.data == "back_to_buy")
async def back_to_buy_menu(callback: types.CallbackQuery):
    text = (
        "🛒 **شراء سيرفر**\n\n"
        "اختر نوع السيرفر المناسب لك 👇\n\n"
        "🇮🇶 **آسيا ريد**\n"
        "⚡ سرعة واستقرار عالي\n\n"
        "🎧 **أودي**\n"
        "🚀 أداء ممتاز للتصفح والألعاب\n"
        "____________________"
    )
    
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🇮🇶 آسيا ريد", callback_data="asia_reed")
    keyboard.button(text="🎧 أودي", callback_data="audi_server")
    keyboard.button(text="🔙 رجوع", callback_data="back_to_buy")
    keyboard.adjust(1)
    
    await callback.message.edit_text(
        text,
        reply_markup=keyboard.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
