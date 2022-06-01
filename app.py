from telegram import Bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("5522845545:AAF276GkvYD-NYtlDfaGAsyFNAqcLg8LV6Y",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "End time warriors is a global network with the vision of raising an army of God(Obadiah 1:21) from generation to generation to change and transform through the power of the Holy Spirit. An army going to bring into alignment anything not in the programming of Elohim. Jeremiah 1:9-12. And to cause the influence of Christ spread across the globe through all platforms available.\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /instagram - To get the instagram URL
    /website - To get the URL for our website
    /gmail - Send us email
    /meetings  - To get the endtime warriors telegram link""")
  
    
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "endtimewarroirs4@gmail.com")
  
  
def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://instagram.com/_endtimewarriors?r=nametag")
  
  
def website_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Website still in development")
  
  
def meetings(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Link to telegram group: https://t.me/endtimewarriorsprayergrp or Subscribe to our channel: https://t.me/endtimewarriors4\
            /Meeting Days ====== > Wednesdays: Prophetic Service @ 7pm\
                / Fridays: Prayer Night(Night of transformation and encounter @ 9pm)\
                    Saturdays: Unlocking the Bible @ 6:30pm\
                        You are warmly welcome to join us as we worship")
    
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('meetings', meetings))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
