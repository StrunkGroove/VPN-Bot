from datetime import datetime
from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from decorators import db_exception_handler


MONGODB_URL = getenv("MONGODB_URL")

mongo_client = AsyncIOMotorClient(MONGODB_URL)


class Collections:
    users = "users"


def get_mongo_collection(collection: str, db_name: str = "default"):
    return mongo_client[db_name][collection]


async def initialize_indexes() -> None:
    collection = get_mongo_collection(collection=Collections.users)
    await collection.create_index([("user_id", 1)], unique=True)


@db_exception_handler
async def create_user(user_id: int, username: str) -> None:
    collection = get_mongo_collection(collection=Collections.users)
    try:
        await collection.insert_one({
            "user_id": user_id,
            "username": username,
            "is_vip": False,
            "vip_end_date": None,
            "is_infinity_vip": False,
            "is_admin": False,
            "created_at": datetime.utcnow()
        })
    except DuplicateKeyError:
        pass


@db_exception_handler
async def get_user_by_id(user_id: int):
    collection = get_mongo_collection(collection=Collections.users)
    return await collection.find_one({"user_id": user_id})


@db_exception_handler
async def set_user_flag(user_id: int, flag: str, value: bool = True):
    collection = get_mongo_collection(collection=Collections.users)
    await collection.update_one(
        {"user_id": user_id},
        {"$set": {flag: value}}
    )


@db_exception_handler
async def get_count_users() -> int:
    collection = get_mongo_collection(collection=Collections.users)
    return await collection.count_documents({})
