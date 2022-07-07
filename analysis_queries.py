import datetime

import main
import utilities
from routers import analysis


async def buffer(table: str, database: str, distance_in_kilometers: float, new_table_id: str, process_id: str):
    """
    Method to buffer any geometric table
    """

    start = datetime.datetime.now()

    pool = main.app.state.databases[f'{database}_pool']

    fields = await utilities.get_table_columns(
        table=table,
        database=database
    )
    
    fields = ','.join(fields)

    async with pool.acquire() as con:
        sql__query = f"""
        CREATE TABLE "{new_table_id}" AS
        SELECT {fields}, ST_Transform(ST_Buffer(ST_Transform(geom,3857), {distance_in_kilometers*1000}),4326) as geom
        FROM "{table}";
        """

        await con.fetch(sql__query)

        buffer_column_query = f"""
        ALTER TABLE {new_table_id}
        ADD COLUMN buffer_distance_in_kilometers float NOT NULL
        DEFAULT {distance_in_kilometers};
        """

        await con.fetch(buffer_column_query)

        analysis.analysis_processes[process_id]['status'] = "SUCCESS"
        analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start