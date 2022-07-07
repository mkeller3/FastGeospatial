# FastGeospatial

FastGeospatial is a [PostGIS](https://github.com/postgis/postgis) geospatial api to enable geospatial queries on geographical data within a spatial database. FastGeospatial is written in [Python](https://www.python.org/) using the [FastAPI](https://fastapi.tiangolo.com/) web framework. 

---

**Source Code**: <a href="https://github.com/mkeller3/FastGeospatial" target="_blank">https://github.com/mkeller3/FastGeospatial</a>

---

## Requirements

FastGeospatial requires PostGIS >= 2.4.0.

## Configuration

In order for the api to work you will need to edit the `config.py` file with your database connections.

Example
```python

```

## Usage

### Running Locally

To run the app locally `uvicorn main:app --reload`

### Production
Build Dockerfile into a docker image to deploy to the cloud.

## API

| Method | URL | Description |
| ------ | --- | ----------- |
| `GET` | `/api/v1/analysis/status/{process_id}` | [Analysis Status](#Analysis-Status)  |
| `POST` | `/api/v1/analysis/buffer` | [Buffer](#Buffer)  |
| `POST` | `/api/v1/analysis/dissolve` | [Dissolve](#Dissolve)  |
| `POST` | `/api/v1/analysis/dissolve_by_value` | [Dissolve By Value](#Dissolve-By-Value)  |
| `POST` | `/api/v1/analysis/square_grids` | [Square Grids](#Square-Grids)  |
| `POST` | `/api/v1/analysis/hexagon_grids` | [Hexagon Grids](#Hexagon-Grids)  |
| `POST` | `/api/v1/analysis/bounding_box` | [Bounding Box](#Bounding-Box])  |
| `POST` | `/api/v1/analysis/k_means_cluster` | [K Means Cluster](#K-Means-Cluster)  |
| `POST` | `/api/v1/analysis/voronoi` | [Voronoi](#Voronoi)  |
| `POST` | `/api/v1/analysis/center_of_each_polygon` | [Center Of Each Polygon](#Center-Of-Each-Polygon)  |
| `POST` | `/api/v1/analysis/center_of_dataset` | [Center Of Dataset](#Center-Of-Dataset)  |
| `POST` | `/api/v1/analysis/find_within_distance` | [Find Within Distance](#Find-Within-Distance)  |
| `POST` | `/api/v1/analysis/point_to_points_distance` | [Point To Points Distance](#Point-To-Points-Distance)  |
| `POST` | `/api/v1/analysis/add_geomtry_columns` | [Add Geometry Columns](#Add-Geometry-Columns)  |
| `POST` | `/api/v1/analysis/convex_hull` | [Convex Hull](#Convex-Hull)  |
| `POST` | `/api/v1/analysis/aggregrate_points_by_grids` | [Aggregrate Points By Grid](#Aggregrate-Points-By-Grid)  |
| `POST` | `/api/v1/analysis/aggregrate_points_by_polygons` | [Aggregrate Points By Polygons](#Aggregrate-Points-By-Polygons)  |
| `POST` | `/api/v1/analysis/select_inside` | [Select Inside](#Select-Inside)  |
| `POST` | `/api/v1/analysis/select_outside` | [Select Outside](#Select-Outside)  |
| `POST` | `/api/v1/analysis/clip` | [Clip](#Clip)  |
| `POST` | `/api/v1/analysis/merge` | [Merge](#Merge)  |
| `POST` | `/api/v1/analysis/combine_datasets` | [Combine Datasets](#Combine-Datasets)  |

## Analysis Status
Any time an analysis is submitted it given a process_id to have the analysis run in the background. To check the
status of an analysis, you can call this endpoint with the process_id.

## Example Call
```shell
/api/v1/analysis/status/472e29dc-91a8-41d3-b05f-cee34006e3f7
```

## Example Output - Still Running
```json
{
    "status": "PENDING"
}
```

## Example Output - Complete
```json
{
    "status": "SUCCESS",
    "new_table_id": "shnxppipxrppsdkozuroilkubktfodibtqorhucjvxlcdrqyhh",
    "completion_time": "2022-07-06T19:33:17.950059",
    "run_time_in_seconds": 1.78599
}
```

## Buffer

![Buffer Image](/images/buffer.png "Buffer Image")

### Description
Buffer an geometric table with a buffer in kilometers.

### Example Input
```json
{
    "table": "zip_centroids",
    "database": "data",
    "distance_in_kilometers": 1
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Dissolve

![Dissolve Image](/images/dissolve.png "Dissolve Image")

### Description
Dissolve any geometric table into one single geometry.

### Example Input
```json
{
    "table": "states",
    "database": "data"
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Dissolve By Value
![Dissolve By Value Image](/images/dissolve_by_value.png "Dissolve By Value Image")

### Description
Dissolve any geometric table into geometries based off a column in the table.

### Example Input
```json
{
    "table": "states",
    "database": "data",
    "column": "sub_region"
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Square Grids
![Square Grids Image](/images/square_grids.png "Square Grids Image")

### Description
Generate square grids of any size based off of a tables geometry.

### Example Input
```json
{
    "table": "states",
    "database": "data",
    "grid_size_in_kilometers": "100"
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Hexagon Grids
![Hexagon Grids Image](/images/hexagon_grids.png "Hexagon Grids Image")

### Description
Generate hexagon grids of any size based off of a tables geometry.

### Example Input
```json
{
    "table": "states",
    "database": "data",
    "grid_size_in_kilometers": 100
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Bounding Box
![Bounding Box Image](/images/bounding_box.png "Bounding Box Image")

### Description
Generate a bounding box of a table.

### Example Input
```json
{
    "table": "states",
    "database": "data",
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## K Means Cluster
![K Means Cluster Image](/images/k_means_cluster.png "K Means Cluster Image")

### Description
Use [K Means Clustering](https://en.wikipedia.org/wiki/K-means_clustering) to group points based on their location.

### Example Input
```json
{
    "table": "zip_centroids",
    "database": "data",
    "number_of_clusters": 5
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Voronoi

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Center Of Each Polygon
![Center of Each Polygon Image](/images/center_of_each_polygon.png "Center of Each Polygon Image")

### Description
Find the center of each polygon for a given table.

### Example Input
```json
{
    "table": "states",
    "database": "data"
}
```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Center Of Dataset

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Find Within Distance

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Point To Points Distance

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Add Geometry Columns

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Convex Hull

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Aggregrate Points By Grid

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Aggregrate Points By Polygons

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Select Inside

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Select Outside

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Clip

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Merge

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```

## Combine Datasets

### Description

### Example Input
```json

```

### Example Output
```json
{
  "process_id": "c8d7b8d8-3e82-4f93-b441-55a5f51c4171",
  "url": "http://127.0.0.1:8000/api/v1/analysis/status/c8d7b8d8-3e82-4f93-b441-55a5f51c4171"
}
```