import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

TOKEN = "8667998783:AAHsm_foWznXIvwk64h1zgH4-pIZZH3s3IA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ==================== (تعديل الأسعار من هنا بكل سهولة) ====================
# أسعار باقات آسيا ريد (بالدينار)
ASIA_3M_PRICE = "8000"
ASIA_2M_PRICE = "6000"
ASIA_1M_PRICE = "4000"

# أسعار باقات أودي (بالدينار)
AUDI_3M_PRICE = "3000"
AUDI_2M_PRICE = "3000"
AUDI_1M_PRICE = "3000"
# =========================================================================

def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🛒 شراء سيرفر")
    builder.button(text="📱 اشتراكاتي")
    builder.button(text="💳 طرق الدفع")
    builder.button(text="🔄 تجديد الاشتراك")
    builder.button(text="📖 طريقة الاستعمال")
    builder.button(text="💰 الأسعار")
    builder.button(text="👤 حسابي")
    builder.button(text="📞 تواصل معنا")
    builder.button(text="💰 محفظتي")
    builder.button(text="👥 دعوة أصدقاء")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "أهلاً بك عزيزي في بوت البيع والشراء 🤖\nاختر ما يناسبك من القائمة أدناه 👇",
        reply_markup=get_main_menu()
    )

@dp.message(F.text.contains("شراء"))
async def buy_server_command(message: types.Message):
    text = (
        "🛒 شراء سيرفر\n\n"
        "_________________________\n\n"
        "اختر نوع السيرفر المناسب لك 👇\n\n"
        "🇮🇶 آسيا ريد\n"
        "⚡ سرعة واستقرار عالي\n\n"
        "🎧 أودي\n"
        "🚀 أداء ممتاز للتصفح والألعاب\n"
        "_________________________"
    )
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🇮🇶 آسيا ريد", callback_data="asia_reed")
    keyboard.button(text="🎧 أودي", callback_data="audi_server")
    keyboard.button(text="🔙 رجوع", callback_data="back_home")
    keyboard.adjust(1)
    
    await message.answer(text, reply_markup=keyboard.as_markup())

@dp.callback_query(F.data == "asia_reed")
async def asia_reed_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f"آسيا ريد 3 أشهر - {ASIA_3M_PRICE} دينار", callback_data="buy_asia_3m")
    keyboard.button(text=f"آسيا ريد شهرين - {ASIA_2M_PRICE} دينار", callback_data="buy_asia_2m")
    keyboard.button(text=f"آسيا ريد شهر - {ASIA_1M_PRICE} دينار", callback_data="buy_asia_1m")
    keyboard.button(text="🔙 رجوع", callback_data="back_to_buy")
    keyboard.adjust(1)
    
    await callback.message.edit_text("📊 باقات آسيا ريد: 🇮🇶", reply_markup=keyboard.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "audi_server")
async def audi_server_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f"أودي 3 أشهر - {AUDI_3M_PRICE} دينار", callback_data="buy_audi_3m")
    keyboard.button(text=f"أودي شهرين - {AUDI_2M_PRICE} دينار", callback_data="buy_audi_2m")
    keyboard.button(text=f"أودي شهر - {AUDI_1M_PRICE} دينار", callback_data="buy_audi_1m")
    keyboard.button(text="🔙 رجوع", callback_data="back_to_buy")
    keyboard.adjust(1)
    
    await callback.message.edit_text(
        "🎧 اختر باقة أودي المناسبة لك 👇",
        reply_markup=keyboard.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "back_to_buy")
async def back_to_buy_menu(callback: types.CallbackQuery):
    text = (
        "🛒 شراء سيرفر\n\n"
        "_________________________\n\n"
        "اختر نوع السيرفر المناسب لك 👇\n\n"
        "🇮🇶 آسيا ريد\n"
        "⚡ سرعة واستقرار عالي\n\n"
        "🎧 أودي\n"
        "🚀 أداء ممتاز للتصفح والألعاب\n"
        "_________________________"
    )
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🇮🇶 آسيا ريد", callback_data="asia_reed")
    keyboard.button(text="🎧 أودي", callback_data="audi_server")
    keyboard.button(text="🔙 رجوع", callback_data="back_home")
    keyboard.adjust(1)
    
    await callback.message.edit_text(text, reply_markup=keyboard.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "back_home")
async def back_to_home(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("تم العودة للقائمة الرئيسية 🏠", reply_markup=get_main_menu())
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
