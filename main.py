from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

@register("pic_sen", "author", "图片发送", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command("pic")  # 使用英文引号
    async def helloworld(self, event: AstrMessageEvent):
        chain = [
            Comp.At(qq=event.get_sender_id()),  # At 消息发送者
            Comp.Plain(" "),
            # 注意：修正图片加载方法
            Comp.Image.fromURL("https://s21.ax1x.com/2025/11/02/pVzbqV1.jpg"),  # 使用英文引号
            Comp.Plain("这是一个图片。")  # 使用英文引号
        ]
        
        return event.chain_result(chain)
