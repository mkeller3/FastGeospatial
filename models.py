from pydantic import BaseModel, Field

class BaseAnalysisModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )

class StatusResponseModel(BaseModel):
    status: str = Field(
        default="SUCCESS"
    )
    new_table_id: str = Field(
        default="shnxppipxrppsdkozuroilkubktfodibtqorhucjvxlcdrqyhh",
        title="50 character new table_id in postgresql."
    )
    completion_time: str = Field(
        default="2022-07-06T19:33:17.950059"
    )
    run_time_in_seconds: float = Field(
        default=1.78599
    )

class BaseResponseModel(BaseModel):
    process_id: str = Field(
        default="472e29dc-91a8-41d3-b05f-cee34006e3f7"
    )
    url: str = Field(
        default="http://127.0.0.1:8000/api/v1/analysis/status/472e29dc-91a8-41d3-b05f-cee34006e3f7"
    )

class BadResponseModel(BaseModel):
    status: str = Field(
        default="FAILURE"
    )
    completion_time: str = Field(
        default="2022-07-06T19:33:17.950059"
    )
    run_time_in_seconds: float = Field(
        default=1.78599
    )

class BufferModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    distance_in_kilometers: float = Field(
        default=None, title="Size of buffer in kilometers."
    )

class DissolveByValueModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    column: str = Field(
        default=None, title="Column used to dissolve geometry."
    )

class GridModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    grid_size_in_kilometers: float = Field(
        default=None, title="Size of grids in kilometers."
    )

class KMeansModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    number_of_clusters: int = Field(
        default=None, title="Number of clusters to group points together."
    )

class FindWithinDistanceModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    latitude: float = Field(
        default=None, title="Starting Latitude."
    )
    longitude: float = Field(
        default=None, title="Starting Latitude."
    )
    distance_in_kilometers: float = Field(
        default=None, title="Size to search in kilometers."
    )

class PolygonsModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    polygons: str = Field(
        default=None, title="Name of the table of polygons."
    )

class AggregatePointsByGridsModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
    )
    distance_in_kilometers: float = Field(
        default=None, title="Size to search in kilometers."
    )
    grid_type: str = Field(
        default=None, title="Type of grid to use."
    )