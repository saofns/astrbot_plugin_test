from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger  # 使用 astrbot 提供的 logger 接口


@register(
    "dongzhuo_reply",  # 插件唯一标识
    "你的名字",  # 作者
    "当群内消息包含董卓时自动回复何意味",  # 插件描述
    "1.0.0",  # 版本号
    "https://github.com/your-repo"  # 仓库地址（可留空）
)
class DongzhuoReplyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("董卓回复插件已初始化")

    # 监听所有消息事件
    @filter.message()
    async def reply_to_dongzhuo(self, event: AstrMessageEvent):
        """监听包含董卓的消息并自动回复"""
        # 获取消息纯文本内容（自动处理表情、图片等非文本内容）
        message_content = event.message_str
        
        # 检查消息中是否包含"董卓"（不区分全半角，这里用简单匹配）
        if "董卓" in message_content:
            logger.info(f"检测到包含董卓的消息：{message_content}")
            # 发送回复消息
            yield event.plain_result("何意味")

    async def terminate(self):
        """插件卸载时的清理操作"""
        logger.info("董卓回复插件已卸载")
