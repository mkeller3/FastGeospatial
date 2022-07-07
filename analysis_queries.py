import datetime

import main
import utilities
from routers import analysis


async def buffer(table: str, database: str, distance_in_kilometers: float, new_table_id: str, process_id: str):
    """
    Method to buffer any geometric table
    """

    start = datetime.datetime.now()

    try:

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
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def dissolve(table: str, database: str, new_table_id: str, process_id: str):
    """
    Method to dissolve any geometric table into one geometry.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT ST_Union(geom) as geom
            FROM "{table}";
            """

            await con.fetch(sql__query)

            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def dissolve_by_value(table: str, database: str, new_table_id: str, column: str, process_id: str):
    """
    Method to dissolve any geometric table into one geometry based off a column.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT DISTINCT("{column}"), ST_Union(geom) as geom
            FROM "{table}"
            GROUP BY "{column}";
            """

            await con.fetch(sql__query)

            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def square_grids(table: str, database: str, new_table_id: str, grid_size_in_kilometers: int, process_id: str):
    """
    Method to genreate square grids based off a given table.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT ST_Transform((ST_SquareGrid({grid_size_in_kilometers*1000}, ST_Transform(a.geom, 3857))).geom,4326) as geom
            FROM {table} a;
            """

            await con.fetch(sql__query)

            size_column_query = f"""
            ALTER TABLE {new_table_id}
            ADD COLUMN grid_size_in_kilometers float NOT NULL
            DEFAULT {grid_size_in_kilometers};
            """

            await con.fetch(size_column_query)

            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def hexagon_grids(table: str, database: str, new_table_id: str, grid_size_in_kilometers: int, process_id: str):
    """
    Method to genreate hexagon grids based off a given table.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT ST_Transform((ST_HexagonGrid({grid_size_in_kilometers*1000}, ST_Transform(a.geom, 3857))).geom,4326) as geom
            FROM {table} a;
            """

            await con.fetch(sql__query)

            size_column_query = f"""
            ALTER TABLE {new_table_id}
            ADD COLUMN grid_size_in_kilometers float NOT NULL
            DEFAULT {grid_size_in_kilometers};
            """

            await con.fetch(size_column_query)

            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def bounding_box(table: str, database: str, new_table_id: str, process_id: str):
    """
    Method to genreate a bounding box based off a given table.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT ST_Envelope(ST_Union(geom)) as geom
            FROM {table};
            """

            await con.fetch(sql__query)
            
            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def k_means_cluster(table: str, database: str, new_table_id: str, number_of_clusters: int, process_id: str):
    """
    Method to genreate clusters based off a k means_clustering.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        fields = await utilities.get_table_columns(
            table=table,
            database=database
        )

        fields = ','.join(fields)

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT ST_ClusterKMeans(geom, {number_of_clusters}) over () as cluster_id, {fields}, geom
            FROM {table};
            """

            await con.fetch(sql__query)
            
            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start

async def center_of_each_polygon(table: str, database: str, new_table_id: str, process_id: str):
    """
    Method to gfind center of each polygon based off a given table.
    """

    start = datetime.datetime.now()

    try:

        pool = main.app.state.databases[f'{database}_pool']

        fields = await utilities.get_table_columns(
            table=table,
            database=database
        )

        fields = ','.join(fields)

        async with pool.acquire() as con:
            sql__query = f"""
            CREATE TABLE "{new_table_id}" AS
            SELECT {fields}, ST_Centroid(geom) geom
            FROM {table};
            """

            await con.fetch(sql__query)
            
            analysis.analysis_processes[process_id]['status'] = "SUCCESS"
            analysis.analysis_processes[process_id]['new_table_id'] = new_table_id
            analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
            analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start
    except Exception as error:
        analysis.analysis_processes[process_id]['status'] = "FAILURE"
        analysis.analysis_processes[process_id]['error'] = str(error)
        analysis.analysis_processes[process_id]['completion_time'] = datetime.datetime.now()
        analysis.analysis_processes[process_id]['run_time_in_seconds'] = datetime.datetime.now()-start