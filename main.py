import os
import google.genai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Gemini AI Setting - လုပ်ငန်းသုံးအတွက် အသိဉာဏ်ထည့်သွင်းခြင်း
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# AI ကို အရောင်းအဝယ်နှင့် လုပ်ငန်းပိုင်းတွင် ကျွမ်းကျင်သူအဖြစ် သတ်မှတ်ခြင်း
instruction = "မင်းက လုပ်ငန်းခွင်မှာ ကျွမ်းကျင်တဲ့ အကြံပေးတစ်ယောက်ပါ။ စီးပွားရေး၊ အရောင်းအဝယ်နဲ့ နည်းပညာပိုင်းတွေကို အသိဉာဏ်ရှိရှိ ယဉ်ကျေးစွာ ဖြေပေးရမယ်။"
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    try:
        # AI ထံမှ အဖြေတောင်းယူခြင်း
        response = model.generate_content(user_message)
        ai_reply = response.text
        await update.message.reply_text(ai_reply)
    except Exception as e:
        print(f"Error: {e}")
        await update.message.reply_text("တောင်းပန်ပါတယ်ခင်ဗျာ၊ အခုလောလောဆယ် AI စနစ် ခေတ္တအလုပ်မလုပ်နိုင်ဖြစ်နေပါတယ်။")

if __name__ == '__main__':
    # Railway Variables မှ Token ယူခြင်း
    bot_token = os.getenv("BOT_TOKEN")
    
    app = ApplicationBuilder().token(bot_token).build()
print("Bot starting...")
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Business AI Bot is active...")
    app.run_polling()
