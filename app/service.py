from text import menu_commands
from func_outline import OutlineManager, TestLimit, bytes_to_gb
from db import get_user_by_id


OUTLINE_MANAGER = OutlineManager()


async def is_vip(user_id: int) -> bool:
    user = await get_user_by_id(user_id)
    return user["is_vip"]


async def is_admin(user_id: int) -> bool:
    user = await get_user_by_id(user_id)
    return user["is_admin"]


async def service_full_access_key(
    user_id: int, 
    username: str,
    check:  bool = True
) -> tuple:
    if check and not await is_vip(user_id):
        return False, menu_commands["full_access_key"]["on_bad_message"]
    user_data = await OUTLINE_MANAGER.get_key(user_id)
    if user_data == OUTLINE_MANAGER.not_foud:
        user_data = await OUTLINE_MANAGER.create_key(
            key_id=user_id,
            name=username
        )
    message_text = menu_commands["full_access_key"]["message"].format(
        key=user_data["accessUrl"]
    )
    return True, message_text


async def service_demo_access_key(
    user_id: int, 
    username: str,
) -> str:
    if await is_vip(user_id):
        status, message_text = await service_full_access_key(
            user_id, username, check=False
        )
        return message_text
    user_data = await OUTLINE_MANAGER.get_key(user_id)
    if user_data == OUTLINE_MANAGER.not_foud:
        user_data = await OUTLINE_MANAGER.create_key(
            user_id,
            name=username,
            limit={"bytes": TestLimit.value},
        )
    message_text = menu_commands["demo_access_key"]["message"].format(
        test_limit=TestLimit.name, 
        key=user_data["accessUrl"]
    )
    return message_text


async def service_get_stastitics(user_id: int) -> str:
    transferred_data = await OUTLINE_MANAGER.get_transferred_data_per_user(user_id)
    user_data = await OUTLINE_MANAGER.get_key(user_id)
    if user_data == OUTLINE_MANAGER.not_foud:
        return menu_commands["stastitics"]["on_bad_message"]
    if data_limit := user_data.get("dataLimit", None):
        message_text = menu_commands["stastitics"]["message"].format(
            transferred_data=transferred_data,
            limit=bytes_to_gb(data_limit["bytes"])
        )
    else:
        message_text = menu_commands["stastitics"]["message_without_limit"].format(
            transferred_data=transferred_data
        )
    return message_text