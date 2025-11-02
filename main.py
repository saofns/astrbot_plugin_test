from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("dongzhuo_reply", "author", "董卓回复插件", "1.0.0", "https://github.com/saofns/astrbot_plugin_test")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("董卓回复插件已加载")
    
    @filter.keyword("董卓",alias={"董卓", "吕布","dongzhuo"})
    async def dongzhuo_reply(self, event: AstrMessageEvent):
        """当消息包含'董卓'时回复'何意味'"""
        logger.info("检测到董卓关键词，准备回复")
        event.stop_event()  # 重要！停止事件传播，不让 LLM 继续处理
        return event.plain_result("何意味")
