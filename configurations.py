import os

import motor.motor_asyncio

uri = ""

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGO_URL"))

db = client.get_database("test")
test_collection = db.get_collection("test-collection")