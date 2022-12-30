from loader import bot
from loguru import logger
import handlers
from utils.set_bot_commands import set_default_commands

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")


@logger.catch()
def main():

    if __name__ == '__main__':
        set_default_commands(bot)
        bot.infinity_polling()


main()

