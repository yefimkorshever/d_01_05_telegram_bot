import os
import ptbot
from pytimeparse import parse

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def notify_progress(secs_left, chat_id, message_id, secs_total):
  notification = "Осталось {} секунд".format(secs_left)
  iteration = secs_total - secs_left
  bar = render_progressbar(secs_total, iteration)
  notification = f'{notification}\n{bar}'
  bot.update_message(chat_id, message_id, notification)

def choose(chat_id):
  answer = 'Время вышло'
  bot.send_message(chat_id, answer)
 

def wait(chat_id, question):
  sec = parse(question)
  message_id = bot.send_message(chat_id, 'Запускаю обратный отсчет')
  bot.create_countdown(sec, notify_progress, chat_id = chat_id, message_id = message_id, secs_total = sec)
  bot.create_timer(sec, choose, chat_id = chat_id)

TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
bot = ptbot.Bot(TG_BOT_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()