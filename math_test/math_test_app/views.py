from django.shortcuts import render
from .models import MathTest
from .telegram_bot import bot, webhook


def index(request):
    tests = MathTest.objects.all()
    return render(request, 'math_test_app/index.html', {'tests': tests})
