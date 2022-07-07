from pydantic import BaseModel, Field

class BaseAnalysisModel(BaseModel):
    table: str = Field(
        default=None, title="Name of the table to perform analysis on."
    )
    database: str = Field(
        default=None, title="Name of the database the table belongs to."
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