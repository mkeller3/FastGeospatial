from fastapi import APIRouter, BackgroundTasks, Request

import utilities
import analysis_queries
import models

router = APIRouter()

analysis_processes = {}

@router.get("/status/{process_id}", tags=["analysis"])
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

@router.post("/dissolve/", tags=["analysis"], response_model=models.BaseResponseModel)
async def dissolve(info: models.BaseAnalysisModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.dissolve,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/dissolve_by_value/", tags=["analysis"], response_model=models.BaseResponseModel)
async def dissolve_by_value(info: models.DissolveByValueModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.dissolve_by_value,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        column=info.column,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/square_grids/", tags=["analysis"], response_model=models.BaseResponseModel)
async def square_grids(info: models.GridModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.square_grids,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        grid_size_in_kilometers=info.grid_size_in_kilometers,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/hexagon_grids/", tags=["analysis"], response_model=models.BaseResponseModel)
async def hexagon_grids(info: models.GridModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.hexagon_grids,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        grid_size_in_kilometers=info.grid_size_in_kilometers,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/bounding_box/", tags=["analysis"], response_model=models.BaseResponseModel)
async def bounding_box(info: models.BaseAnalysisModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.bounding_box,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/k_means_cluster/", tags=["analysis"], response_model=models.BaseResponseModel)
async def k_means_cluster(info: models.KMeansModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.k_means_cluster,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        number_of_clusters=info.number_of_clusters,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/center_of_each_polygon/", tags=["analysis"], response_model=models.BaseResponseModel)
async def center_of_each_polygon(info: models.BaseAnalysisModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.center_of_each_polygon,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/center_of_dataset/", tags=["analysis"], response_model=models.BaseResponseModel)
async def center_of_dataset(info: models.BaseAnalysisModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.center_of_dataset,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/find_within_distance/", tags=["analysis"], response_model=models.BaseResponseModel)
async def find_within_distance(info: models.FindWithinDistanceModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.find_within_distance,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        latitude=info.latitude,
        longitude=info.longitude,
        distance_in_kilometers=info.distance_in_kilometers,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/convex_hull/", tags=["analysis"], response_model=models.BaseResponseModel)
async def convex_hull(info: models.BaseAnalysisModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.convex_hull,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/aggregate_points_by_grids/", tags=["analysis"], response_model=models.BaseResponseModel)
async def aggregate_points_by_grids(info: models.AggregatePointsByGridsModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.aggregate_points_by_grids,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        distance_in_kilometers=info.distance_in_kilometers,
        grid_type=info.grid_type,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/aggregate_points_by_polygons/", tags=["analysis"], response_model=models.BaseResponseModel)
async def aggregate_points_by_polygons(info: models.PolygonsModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.aggregrate_points_by_polygons,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        polygons=info.polygons,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/select_inside/", tags=["analysis"], response_model=models.BaseResponseModel)
async def select_inside(info: models.PolygonsModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.select_inside,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        polygons=info.polygons,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/select_outside/", tags=["analysis"], response_model=models.BaseResponseModel)
async def select_outside(info: models.PolygonsModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.select_outside,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        polygons=info.polygons,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }

@router.post("/clip/", tags=["analysis"], response_model=models.BaseResponseModel)
async def clip(info: models.PolygonsModel, request: Request, background_tasks: BackgroundTasks):
    new_table_id = utilities.get_new_table_id()

    process_id = utilities.get_new_process_id()

    process_url = str(request.base_url)

    process_url += f"api/v1/analysis/status/{process_id}"

    analysis_processes[process_id] = {
        "status": "PENDING"
    }

    background_tasks.add_task(
        analysis_queries.clip,
        table=info.table,
        database=info.database,
        new_table_id=new_table_id,
        polygons=info.polygons,
        process_id=process_id
    )

    return {
        "process_id": process_id,
        "url": process_url
    }