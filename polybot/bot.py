import telebot
from loguru import logger
import os
import time
from telebot.types import InputFile
from img_proc import Img

class Bot:

    def __init__(self, token, telegram_chat_url):
        # create a new instance of the TeleBot class.
        # all communication with Telegram servers are done using self.telegram_bot_client
        self.telegram_bot_client = telebot.TeleBot(token)

        # remove any existing webhooks configured in Telegram servers
        self.telegram_bot_client.remove_webhook()
        time.sleep(0.5)

        # set the webhook URL
        self.telegram_bot_client.set_webhook(url=f'{telegram_chat_url}/{token}/', timeout=60, certificate=open('/home/ubuntu/cert-bot.crt', 'r'))

        logger.info(f'Telegram Bot information\n\n{self.telegram_bot_client.get_me()}')

    def send_text(self, chat_id, text):
        self.telegram_bot_client.send_message(chat_id, text)

    def send_text_with_quote(self, chat_id, text, quoted_msg_id):
        self.telegram_bot_client.send_message(chat_id, text, reply_to_message_id=quoted_msg_id)

    def is_current_msg_photo(self, msg):
        return 'photo' in msg

    def download_user_photo(self, msg):
        """
        Downloads the photos that sent to the Bot to `photos` directory (should be existed)
        :return:
        """
        if not self.is_current_msg_photo(msg):
            raise RuntimeError(f'Message content of type \'photo\' expected')

        file_info = self.telegram_bot_client.get_file(msg['photo'][-1]['file_id'])
        data = self.telegram_bot_client.download_file(file_info.file_path)
        folder_name = file_info.file_path.split('/')[0]

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        with open(file_info.file_path, 'wb') as photo:
            photo.write(data)

        return file_info.file_path

    def send_photo(self, chat_id, img_path):
        if not os.path.exists(img_path):
            raise RuntimeError("Image path doesn't exist")

        self.telegram_bot_client.send_photo(
            chat_id,
            InputFile(img_path)
        )

    def handle_message(self, msg):
        """Bot Main message handler"""
        logger.info(f'Incoming message: {msg}')
        self.send_text(msg['chat']['id'], f'Your original message: {msg["text"]}')


class QuoteBot(Bot):
    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')

        if msg["text"] != 'Please don\'t quote me':
            self.send_text_with_quote(msg['chat']['id'], msg["text"], quoted_msg_id=msg["message_id"])


class ImageProcessingBot(Bot):
    def handle_message(self, msg):
        try:
            logger.info(f'Incoming message: {msg}')
            if 'text' in msg:
                #Greet the user.
                if msg['text'].lower() == 'start' or 'hello' or 'hi':
                    self.send_text(msg['chat']['id'],
                                   "Hello! I'm the Image Processing Bot. You can send me photos with captions to apply various filters. Try sending a photo with a caption like 'Blur', 'Rotate', 'Concat', etc.")
                return
            #Check if the received message contains a photo using the is_current_msg_photo method inherited from the Bot class.
            if self.is_current_msg_photo(msg):
                #Download the photo sent by the user using the download_user_photo method inherited from the Bot class.
                #This method returns the file path of the downloaded photo.
                img_path = self.download_user_photo(msg)
                #Get the caption of the message provided by the user. If no caption is provided, it defaults to an empty string.
                #The .lower() method is used to convert the caption to lowercase for case-insensitive comparison.
                caption = msg.get('caption', '').lower()
                #If the caption is "blur", create an Img object with the downloaded image path,
                #apply the blur filter using the blur() method, and then send the processed image back to the user.
                if caption == 'blur':
                    img = Img(img_path)
                    img.blur()
                    new_img_path = img.save_img()  #Save the processed image and get the path of the new image file.
                    self.send_photo(msg['chat']['id'], new_img_path)  #Send the processed image back to the user.
                #If the caption is "contour", create an Img object with the downloaded image path,
                #apply the contour filter using the contour() method, and then send the processed image back to the user.
                elif caption == 'contour':
                    img = Img(img_path)
                    img.contour()
                    new_img_path = img.save_img()  #Save the processed image and get the path of the new image file.
                    self.send_photo(msg['chat']['id'], new_img_path)  #Send the processed image back to the user.
                #If the caption is "rotate", create an Img object with the downloaded image path,
                #apply the rotate filter using the rotate() method, and then send the processed image back to the user.
                elif caption == 'rotate':
                    img = Img(img_path)
                    img.rotate()
                    new_img_path = img.save_img()  # Save the processed image and get the path of the new image file.
                    self.send_photo(msg['chat']['id'], new_img_path)  #Send the processed image back to the user.
                #If the caption is "segment", create an Img object with the downloaded image path,
                #apply the segment filter using the segment() method, and then send the processed image back to the user.
                elif caption == 'segment':
                    img = Img(img_path)
                    img.segment()
                    new_img_path = img.save_img()
                    self.send_photo(msg['chat']['id'], new_img_path)
                #If the caption is "salt and pepper", create an Img object with the downloaded image path,
                #apply the salt and pepper filter using the salt_n_pepper() method, and then send the processed image back to the user.
                elif caption == 'salt and pepper':
                    img = Img(img_path)
                    img.salt_n_pepper()
                    new_img_path = img.save_img()
                    self.send_photo(msg['chat']['id'], new_img_path)
                #If the caption is "concat", create an Img object with the downloaded image path,
                #download it once more and create another Img object.
                #apply the concat filter using the concat() method, and then send the processed image back to the user.
                elif caption == 'concat':
                    other_img_path = self.download_user_photo(msg)
                    other_img = Img(other_img_path)
                    img = Img(img_path)
                    img.concat(other_img)
                    new_img_path = img.save_img()
                    self.send_photo(msg['chat']['id'], new_img_path)
                else:
                    #if the filter is not one of the defined, send an appropriate message to the user.
                    self.send_text(msg['chat']['id'],
                       "Unsupported filter. Please use one of the following: Blur, Contour, Rotate, Segment, Salt and Pepper, Concat")
            else:
                #Inform user to send a photo.
                self.send_text(msg['chat']['id'], "Please send a photo.")
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            self.send_text(msg['chat']['id'], "something went wrong... please try again")




















