from telebot import TeleBot
from telebot.types import Message
from removebg import RemoveBg

def any_user(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(message.chat.id, "Assalomu Alaykum, <b>BGcleaner telegram botiga xush "
                                      "kelibsiz!</b>\n\nRasmingizni yuboring👇")


def get_photo(message: Message, bot: TeleBot):
    # Rasmni olish
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    # Faylga yuklash
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    # Orqa fonni o'chirish
    rmbg = RemoveBg("ZLx3xgKRhHQimiHQBRWcZnDz", "error.log")
    rmbg.remove_background_from_img_file("image.jpg")

    # Foydalanuvchiga yuborish
    img = open("image.jpg" + "_no_bg.png", "rb")
    bot.send_photo(message.chat.id, img, 'RemoveBG')