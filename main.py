from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("dongzhuo_cmd", "author", "董卓指令插件", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command("董卓")
    async def dongzhuo_command(self, event: AstrMessageEvent):
        """董卓指令 - 使用 /董卓 触发"""
        return event.plain_result("何意味")
    
    @filter.command("董卓", alias={"董太师", "董相国"})
    async def dongzhuo_with_alias(self, event: AstrMessageEvent):
        """支持多个别名：/董卓, /董太师, /董相国"""
        return event.plain_result("何意味")
