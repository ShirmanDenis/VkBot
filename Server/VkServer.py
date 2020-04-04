import vk_api
from vk_api import bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent

class VkServer:
    __vk_session = None
    __handlers = {
        VkBotEventType.MESSAGE_NEW: [],
        VkBotEventType.MESSAGE_TYPING_STATE: [],
    }
    def __init__(self, access_token: str):
        global vk_api
        self.vk_session = vk_api.VkApi(token=access_token)
    def listen(self, chat_id):
        global VkBotLongPoll
        longpoll = VkBotLongPoll(self.vk_session, chat_id)
        for event in longpoll.listen():
            handlers_by_event_type = self.__handlers.get(event.type)
            if (len(handlers_by_event_type) != 0):
                for h in handlers_by_event_type:
                    h(event, self.vk_session)
    def register_handler(self, event_type: VkBotEventType, handler):
        handlers_by_event_type = self.__handlers.get(event_type)
        if (handlers_by_event_type == None):
            raise NotImplementedError("This event type is not supported!")
        handlers_by_event_type.append(handler)