from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("dongzhuo_reply", "author", "董卓回复插件", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    async def handle_message(self, event: AstrMessageEvent):
        """处理所有消息"""
        message_text = event.get_plain_text()
        
        if "董卓" in message_text:
            logger.info(f"检测到董卓，消息内容: {message_text}")
            return event.plain_result("何意味")
        
        return None
