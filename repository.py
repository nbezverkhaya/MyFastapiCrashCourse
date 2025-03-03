
from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STaskRead


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump() #makes dict
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    async def get_all() -> list[STaskRead]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskRead.model_validate(task, from_attributes=True) for task in task_models]
            return task_schemas