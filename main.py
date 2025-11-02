from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口
import astrbot.api.message_components as Comp

@register("pic_sen", "author", "图片发送", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    
    @filter.command(“pic”)
    async def helloworld(self, event: AstrMessageEvent):
       chain = [
        Comp.At(qq=event.get_sender_id()), # At 消息发送者
        
       
        Comp.Image.fromFileSystem("https://imgchr.com/i/pVzbqV1"), # 从本地文件目录发送图片
        Comp.Plain("这是一个图片。")
    ]

   yield event.chain_result(chain)
