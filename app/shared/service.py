from db.func import get_user_by_id


async def is_vip(user_id: int) -> bool:
    user = await get_user_by_id(user_id)
    return user["is_vip"]


async def is_admin(user_id: int) -> bool:
    user = await get_user_by_id(user_id)
    return user["is_admin"]
