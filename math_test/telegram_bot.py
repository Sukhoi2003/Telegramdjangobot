import telebot
from django.core.management import execute_from_command_line
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'math_test_project.settings')
execute_from_command_line(['manage.py', 'runserver'])

bot = telebot.TeleBot('6649520704:AAHekAgprlEDpa_erRcvtIQDGF4ovnV2e5E')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Math Tests")
    bot.send_message(user_id, "Assalomu alaykum! Quyidagi tugmalardan birini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Math Tests")
def handle_math_tests(message):
    user_id = message.chat.id

    tests = MathTest.objects.all()
    test_text = "\n".join([f"{test.question}" for test in tests])
    bot.send_message(user_id, test_text)

if __name__ == "__main__":
    bot.polling()
