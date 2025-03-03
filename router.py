from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from repository import TaskRepository
from schemas import STaskRead, STaskAdd, STaskID

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskID: # To make swager easy to use
    task_id = await TaskRepository.add_one(task)

    return JSONResponse(content={"data": True, "task id": task_id}, status_code=200)

@router.get("")
async def get_tasks() -> list[STaskRead]:
    tasks= await TaskRepository.get_all()

    return tasks