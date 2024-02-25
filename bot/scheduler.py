import apscheduler.schedulers.asyncio
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from shared.db import client

jobstores = {
    "default": MongoDBJobStore("giveaways-bot", client=client, json=True)
}
# jobstores = {
#     "default": MemoryJobStore()
# }

# class SchedulerWrapper:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.scheduler = AsyncIOScheduler(jobstores=jobstores)
#             cls._instance.scheduler.start()
#             print("Scheduler started")
#         return cls._instance

#     def add_job(self, *args, **kwargs):
#         return self.scheduler.add_job(*args, **kwargs)

#     def shutdown(self):
#         self.scheduler.shutdown()


class SchedulerWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.scheduler = apscheduler.schedulers.asyncio.AsyncIOScheduler(
                jobstores=jobstores,
                job_defaults={'misfire_grace_time': 1},
                serializer="json"
            )
            cls._instance.scheduler.start()
        return cls._instance

    def add_job(self, *args, **kwargs):
        return self.scheduler.add_job(*args, **kwargs)

    def shutdown(self):
        self.scheduler.shutdown()

async def my_function(message) -> None:
    await message.answer("pong")

