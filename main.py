import os
import subprocess
import asyncio
from aiohttp import web

# دالة لتحميل وتشغيل نواة Xray في الخلفية
def run_xray():
    # تحميل وتشغيل Xray (ملف التنفيذ السريع لنظام لينكس)
    if not os.path.exists("xray"):
        os.system("curl -L -o xray.zip https://github.com/XTLS/Xray-core/releases/latest/download/Xray-linux-64.zip")
        os.system("unzip xray.zip xray")
        os.system("chmod +x xray")
    
    # تشغيل xray باستخدام ملف الـ config.json الذي أنشأناه
    subprocess.Popen(["./xray", "-config", "config.json"])

async def handle(request):
    return web.Response(text="VLESS Server is running successfully!")

async def main():
    # تشغيل Xray أولاً
    run_xray()
    
    app = web.Application()
    app.router.add_get("/", handle)
    
    port = int(os.environ.get("PORT", 10000))
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    print(f"VLESS Server started on port {port}")
    await asyncio.gather(*(asyncio.Event().wait(),))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
