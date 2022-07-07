from fastapi import APIRouter, BackgroundTasks, Path, Request

import utilities
import analysis_queries
import models

router = APIRouter()

analysis_processes = {}

@router.get("/status/{process_id}", tags=["analysis"], response_model=models.StatusResponseModel)
def status(process_id: str):
    if process_id not in analysis_processes:
        return {"status": "UNKNOWN", "error": "This process_id does not exist."}
    return analysis_processes[process_id]

@router.post("/buffer/", tags=["analysis"], response_model=models.BaseResponseModel)
async def buffer(info: models.BufferModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.buffer,
        table=info.table,
        database=info.database,
        distance_in_kilometers=info.distance_in_kilometers,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

