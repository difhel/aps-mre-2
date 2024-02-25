import datetime
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from bot.scheduler import SchedulerWrapper


router = Router()

# pylint: disable-next=too-few-public-methods
class BotStates(StatesGroup):
    test_state = State()


@router.message(BotStates.test_state)
async def test(message: Message):
    ...


async def my_function(message: Message) -> None:
    print("pong")
    await message.answer("pong")

@router.message(Command("schedule"))
async def schedule(message: Message, state: FSMContext):
    seconds_delay = int(message.text.split()[-1])
    job = SchedulerWrapper().add_job(
        my_function,
        "date",
        run_date=datetime.datetime.now() + datetime.timedelta(seconds=seconds_delay),
        args=[message]
    )
    print(job)
    await message.answer("Scheduled")
