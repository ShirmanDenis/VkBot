
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api import VkApi
from Server.VkServer import VkServer

def new_message_handler(event: VkBotMessageEvent, api_vk: VkApi):
    api = api_vk.get_api()
    text = event.obj.text
    if (event.from_chat):
        api.messages.send(
            chat_id=event.chat_id,
            random_id=123,
            message= f"I've got it! Your message: {text}"
        )

def register_handlers(server: VkServer):
    server.register_handler(VkBotEventType.MESSAGE_NEW, new_message_handler)

def get_token():
    with open("secure.txt", "r") as f:
        return f.readline()

if (__name__ == "__main__"):
    access_token = get_token()
    server = VkServer(access_token)
    register_handlers(server)
    server.listen('193738436')