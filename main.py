import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Álbum: coloque "/" e em seguida o nome do álbum com letras minúsculas trocando os espaços '
        'por "_".\n\nMúsica: Digite o nome da música.')


def am(update: Update, context: CallbackContext) -> None:
    arq = open("AM\lista_musicas_am.txt", "r", encoding='utf8')
    musicas_am = arq.read()
    arq.close()
    update.message.reply_text(musicas_am)


def musicas(update: Update, context: CallbackContext) -> None:
    if update.message.text == 'Do I Wanna Know?' or\
            update.message.text == 'do i wanna know' or\
            update.message.text == 'Do I Wanna Know' or\
            update.message.text == 'Do I Wanna Know ?':
        arq = open("AM\do_i_wanna_know.txt", "r", encoding='utf8')
        do_i_wanna_know = arq.read()
        arq.close()
        update.message.reply_text(do_i_wanna_know)

    elif update.message.text == 'R U Mine?' or\
            update.message.text == 'R U Mine' or\
            update.message.text == 'r u mine' or\
            update.message.text == 'r u mine?':
        arq = open("AM\\ru_mine.txt", "r", encoding='utf8')
        ru_mine = arq.read()
        arq.close()
        update.message.reply_text(ru_mine)

    elif update.message.text == 'One For The Road':
        arq = open("AM\one_for_the_road.txt", "r", encoding='utf8')
        one_for_the_road = arq.read()
        arq.close()
        update.message.reply_text(one_for_the_road)

    elif update.message.text == 'Arabella':
        arq = open("AM\\arabella.txt", "r", encoding='utf8')
        arabella = arq.read()
        arq.close()
        update.message.reply_text(arabella)

    elif update.message.text == 'I Want It All':
        arq = open("AM\i_want_it_all.txt", "r", encoding='utf8')
        i_want_it_all = arq.read()
        arq.close()
        update.message.reply_text(i_want_it_all)

    elif update.message.text == 'No. 1 Party Anthem':
        arq = open("AM\\no_1_party_anthem.txt", "r", encoding='utf8')
        no_1_party_anthem = arq.read()
        arq.close()
        update.message.reply_text(no_1_party_anthem)

    elif update.message.text == 'Mad Sounds':
        arq = open("AM\mad_sounds.txt", "r", encoding='utf8')
        mad_sounds = arq.read()
        arq.close()
        update.message.reply_text(mad_sounds)

    elif update.message.text == 'Fireside':
        arq = open("AM\\fireside.txt", "r", encoding='utf8')
        fireside = arq.read()
        arq.close()
        update.message.reply_text(fireside)

    elif update.message.text == "Why'd You Only Call Me When You're High?":
        arq = open("AM\wyocmwyh.txt", "r", encoding='utf8')
        wyocmwyh = arq.read()
        arq.close()
        update.message.reply_text(wyocmwyh)

    elif update.message.text == 'Snap Out Of It':
        arq = open("AM\snap_out_of_it.txt", "r", encoding='utf8')
        snap_out_of_it = arq.read()
        arq.close()
        update.message.reply_text(snap_out_of_it)

    elif update.message.text == 'Knee Socks':
        arq = open("AM\knee_socks.txt", "r", encoding='utf8')
        knee_socks = arq.read()
        arq.close()
        update.message.reply_text(knee_socks)

    elif update.message.text == 'I Wanna Be Yours':
        arq = open("AM\i_wanna_be_yours.txt", "r", encoding='utf8')
        i_wanna_be_yours = arq.read()
        arq.close()
        update.message.reply_text(i_wanna_be_yours)


def main() -> None:
    updater = Updater("") #token de acesso gerado pelo BotFather

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("am", am))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, musicas))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()