from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

@register("dongzhuo_reply", "author", "董卓回复插件", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.keyword("董卓")
    async def dongzhuo_reply(self, event: AstrMessageEvent):
        chain = [
            Comp.At(qq=event.get_sender_id()),  # At发送者
            Comp.Plain(" 何意味")
        ]
        return event.chain_result(chain)
