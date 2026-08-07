import os
import asyncio
from aiohttp import web

# دالة استجابة بسيطة ليبقى السيرفر نشطاً على Render
async def handle(request):
    return web.Response(text="Bot is running successfully!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    
    # قراءة البورت المخصص من بيئة ريندر، أو استخدام البورت 10000 كافتراضي
    port = int(os.environ.get("PORT", 10000))
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    print(f"Server started on port {port}")
    
    # إبقاء السيرفر قيد التشغيل دائمًا
    await asyncio.gather(*(asyncio.Event().wait(),))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
