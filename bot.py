
import time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from data import gubun_list, incDec_list, defCnt_list, nowdate2

# bot info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# token
token = "token"


# /start message
def start(update, context):
    # username
    print(update.message.chat.username)
    t = '''
哈喽！%s 
各地区新冠肺炎确诊病例动态通知 Chat Bot!
/total 全国确诊病例数
/help 帮助
    ''' % update.message.chat.first_name  # username
    context.bot.send_message(chat_id=update.message.chat_id, text=t)


# /help  message
def help(update, context):
    print(update.message.chat.username)
    t = '''
通知您今天的新增病例数
请输入地区
仅支持广域市或道单位 
ex ) 光州，首尔，全南，济州
    '''
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
    time.sleep(0.3)


# 지역별 확진자 수
def get_message(update, context):
    msg = update.message.text

    for i in range(0, 18):
        if msg == gubun_list[i]:
            t = nowdate2 + '\n地区: ' + gubun_list[i] + '\n新增确诊病例数: ' + incDec_list[i] + ' 例\n累计确诊: ' + \
                defCnt_list[i] + ' 例'
            context.bot.send_message(chat_id=update.message.chat_id, text=t)
            return
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="/help 请参考帮助")


# 총 확진자 수
def total(update, context):
    print(update.message.chat.username)
    t = nowdate2 + '\n全国新增确诊病例数 ： ' + incDec_list[18] + ' 例\n累计确诊: ' + defCnt_list[18] + '例'
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
    time.sleep(0.3)


# error
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    total_handler = CommandHandler('total', total)
    dispatcher.add_handler(total_handler)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    message_handler = MessageHandler(Filters.text, get_message)
    dispatcher.add_handler(message_handler)

    # log all errors
    dispatcher.add_error_handler(logging.error)
    updater.start_polling(timeout=3)
    updater.idle()


if __name__ == '__main__':
    main()
