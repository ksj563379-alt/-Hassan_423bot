import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ضع التوكن الذي نسخته من BotFather بين علامتي التنصيص بدلاً من هذه الكتابة
TOKEN = "8670994653:AAFOmRKRGkaPmAG9Lccs9YCapDyivGp1YZU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="📱 اشتراكاتي"),
        types.KeyboardButton(text="🛒 شراء سيرفر")
    )
    builder.row(
        types.KeyboardButton(text="🔄 تجديد الاشتراك"),
        types.KeyboardButton(text="💳 طرق الدفع")
    )
    builder.row(
        types.KeyboardButton(text="💰 الأسعار"),
        types.KeyboardButton(text="📖 طريقة الاستعمال")
    )
    builder.row(
        types.KeyboardButton(text="📞 تواصل معنا"),
        types.KeyboardButton(text="👤 حسابي")
    )
    builder.row(
        types.KeyboardButton(text="💰 محفظتي"),
        types.KeyboardButton(text="👥 دعوة أصدقاء")
    )
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "مرحباً بك في بوت إدارة الاشتراكات والسيرفرات 🚀\n"
        "اختر ما تريده من القائمة أدناه:"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu())

@dp.message(F.text == "📱 اشتراكاتي")
async def my_subscriptions(message: types.Message):
    sub_info = (
        "🏷 **اشتراكات vps**\n\n"
        "💰 السعر: 4000 دينار\n"
        "📅 المدة: 30 يوم\n"
        "⏳ الانتهاء: 2026-08-30 22:20:39\n"
        "⏳ المتبقي: 29 يوم\n"
        "🟢 الحالة: فعال\n\n"
        "🔗 **رابط VLESS:**\n"
        "`vless://ddfbbc5b-aa87-4b71-a6e6-a06632ff1688@169.58.71.159:8443?encryption=none&host=www.pubgmobile.com&path=%2FFayad-red-078343fb4eab&security=none&type=ws#user_574655271`"
    )
    
    builder = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="🔄 تجديد الاشتراك", callback_data="renew_sub")]
        ]
    )
    
    await message.answer(sub_info, reply_markup=builder, parse_mode="Markdown")

@dp.message(F.text)
async def handle_all_messages(message: types.Message):
    if message.text == "💰 الأسعار":
        await message.answer("قائمة الأسعار الحالية:\n- سيرفر لمدة 30 يوم: 4000 دينار")
    elif message.text == "👤 حسابي":
        await message.answer(f"معلومات حسابك:\nمعرف المستخدم: `{message.from_user.id}`", parse_mode="Markdown")
    else:
        await message.answer("تم اختيار: " + message.text)
@dp.message(F.text == "🛒 شراء سيرفر")
async def cmd_buy_server(message: types.Message):
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

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
