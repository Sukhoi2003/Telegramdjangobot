import telebot
from telebot import types
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MathTest

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Matematik testlar uchun /test buyrug'ini jo'nating.")

@bot.message_handler(commands=['test'])
def send_test(message):
    tests = MathTest.objects.all()
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for test in tests:
        item = types.KeyboardButton(test.question)
        markup.add(item)
    bot.send_message(message.chat.id, "Testni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    try:
        selected_test = MathTest.objects.get(question=message.text)
        if str(selected_test.answer) == message.text:
            response = "To'g'ri javob!"
        else:
            response = "Noto'g'ri javob. To'g'ri javob: " + str(selected_test.answer)
        bot.send_message(message.chat.id, response)
    except MathTest.DoesNotExist:
        bot.send_message(message.chat.id, "Bunday test mavjud emas. /test buyrug'ini qayta jo'nating.")

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})

