import random
import string
import uuid

import main

def get_new_table_id() -> str:
    """
    Method to return a new table id
    """
    letters = string.ascii_lowercase

    return ''.join(random.choice(letters) for i in range(50))

def get_new_process_id() -> str:
    """
    Method to return a new process id
    """

    return str(uuid.uuid4())

async def get_table_columns(table: str, database: str) -> list:
    """
    Method to return a list of columns for a table.
    """
    pool = main.app.state.databases[f'{database}_pool']

    async with pool.acquire() as con:


        sql_field_query = f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{table}'
        AND column_name != 'geom';
        """

        db_fields = await con.fetch(sql_field_query)

        fields = []

        for field in db_fields:
            fields.append(field['column_name'])

        return fields
