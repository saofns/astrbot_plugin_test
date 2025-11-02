from astrbot.api.event import filter, AstrMessageEvent, EventMessageType, PlatformAdapterType
from astrbot.api.star import Context, Star, register
from astrbot.api import logger  # 严格使用框架提供的日志接口
from astrbot.api.message_components import Plain  # 消息组件，备用


@register(
    plugin_name="dongzhuo_auto_reply",  # 插件唯一标识（小写无空格）
    author="你的名字",
    description="QQ群内检测到'董卓'关键词时，自动回复'何意味'",
    version="1.0.0",
    repo_url="https://github.com/saofns/astrbot_plugin_test）"
)
class DongzhuoAutoReplyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        # 插件初始化日志（文档要求：便于调试插件生命周期）
        logger.info(f"[{self.__class__.__name__}] 董卓关键词回复插件已初始化")

    # 过滤器组合：仅监听群聊消息 + 兼容QQ个人号/官方接口（文档：多过滤器用AND逻辑）
    @filter.event_message_type(EventMessageType.GROUP_MESSAGE)
    @filter.platform_adapter_type(PlatformAdapterType.AIOCQHTTP | PlatformAdapterType.QQOFFICIAL)
    async def on_group_message_with_dongzhuo(self, event: AstrMessageEvent):
        """
        群聊消息监听逻辑：检测"董卓"关键词并回复
        文档参考：事件类型过滤（EventMessageType）、平台适配过滤（PlatformAdapterType）
        """
        # 1. 获取消息核心信息（文档：AstrMessageEvent属性）
        group_id = event.get_group_id()  # 群ID
        sender_id = event.get_sender_id()  # 发送者ID
        sender_name = event.get_sender_name()  # 发送者昵称
        message_content = event.message_str  # 纯文本消息（自动过滤表情/图片）

        # 2. 关键词检测（不区分大小写，增强兼容性）
        if "董卓" in message_content.lower():
            # 详细日志（文档建议：便于跟踪触发场景）
            logger.info(
                f"[{self.__class__.__name__}] "
                f"群{group_id}({sender_name},{sender_id}) "
                f"发送含关键词消息：{message_content}"
            )

            # 3. 发送回复（纯文本回复，文档：被动消息发送）
            # 若需带@效果，可改用chain_result：yield event.chain_result([Comp.At(qq=sender_id), Comp.Plain("何意味")])
            yield event.plain_result("何意味")

            # 可选：停止事件传播（避免其他插件重复处理此消息，文档：控制事件传播）
            # event.stop_event()

    async def terminate(self):
        """插件卸载/停用回调（文档：可选实现，用于资源清理）"""
        logger.info(f"[{self.__class__.__name__}] 董卓关键词回复插件已卸载")
