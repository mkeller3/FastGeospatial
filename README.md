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
| `GET` | `/api/v1/analysis/buffer` | [Buffer](#Buffer)  |
| `GET` | `/api/v1/analysis/dissolve` | [Dissolve](#Dissolve)  |
| `GET` | `/api/v1/analysis/dissolve_by_value` | [Dissolve By Value](#Dissolve-By-Value)  |
| `GET` | `/api/v1/analysis/rectangle_grids` | [Rectangle Grids](#Rectangle-Grids)  |
| `GET` | `/api/v1/analysis/hexagon_grids` | [Hexagon Grids](#Hexagon-Grids)  |
| `GET` | `/api/v1/analysis/bounding_box` | [Bounding Box](#Bounding-Box])  |
| `GET` | `/api/v1/analysis/k_means_cluster` | [K Means Cluster](#K-Means-Cluster)  |
| `GET` | `/api/v1/analysis/voronoi` | [Voronoi](#Voronoi)  |
| `GET` | `/api/v1/analysis/center_of_each_polygon` | [Center Of Each Polygon](#Center-Of-Each-Polygon)  |
| `GET` | `/api/v1/analysis/center_of_dataset` | [Center Of Dataset](#Center-Of-Dataset)  |
| `GET` | `/api/v1/analysis/find_within_distance` | [Find Within Distance](#Find-Within-Distance)  |
| `GET` | `/api/v1/analysis/point_to_points_distance` | [Point To Points Distance](#Point-To-Points-Distance)  |
| `GET` | `/api/v1/analysis/add_geomtry_columns` | [Add Geometry Columns](#Add-Geometry-Columns)  |
| `GET` | `/api/v1/analysis/convex_hull` | [Convex Hull](#Convex-Hull)  |
| `GET` | `/api/v1/analysis/aggregrate_points_by_grids` | [Aggregrate Points By Grid](#Aggregrate-Points-By-Grid)  |
| `GET` | `/api/v1/analysis/aggregrate_points_by_polygons` | [Aggregrate Points By Polygons](#Aggregrate-Points-By-Polygons)  |
| `GET` | `/api/v1/analysis/select_inside` | [Select Inside](#Select-Inside)  |
| `GET` | `/api/v1/analysis/select_outside` | [Select Outside](#Select-Outside)  |
| `GET` | `/api/v1/analysis/clip` | [Clip](#Clip)  |
| `GET` | `/api/v1/analysis/merge` | [Merge](#Merge)  |
| `GET` | `/api/v1/analysis/combine_datasets` | [Combine Datasets](#Combine-Datasets)  |

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

### Description

### Example Input
```json

```

### Example Output
```json

```

## Dissolve By Value

### Description

### Example Input
```json

```

### Example Output
```json

```

## Rectangle Grids

### Description

### Example Input
```json

```

### Example Output
```json

```

## Hexagon Grids

### Description

### Example Input
```json

```

### Example Output
```json

```

## Bounding Box

### Description

### Example Input
```json

```

### Example Output
```json

```

## K Means Cluster

### Description

### Example Input
```json

```

### Example Output
```json

```

## Voronoi

### Description

### Example Input
```json

```

### Example Output
```json

```

## Center Of Each Polygon

### Description

### Example Input
```json

```

### Example Output
```json

```

## Center Of Dataset

### Description

### Example Input
```json

```

### Example Output
```json

```

## Find Within Distance

### Description

### Example Input
```json

```

### Example Output
```json

```

## Point To Points Distance

### Description

### Example Input
```json

```

### Example Output
```json

```

## Add Geometry Columns

### Description

### Example Input
```json

```

### Example Output
```json

```

## Convex Hull

### Description

### Example Input
```json

```

### Example Output
```json

```

## Aggregrate Points By Grid

### Description

### Example Input
```json

```

### Example Output
```json

```

## Aggregrate Points By Polygons

### Description

### Example Input
```json

```

### Example Output
```json

```

## Select Inside

### Description

### Example Input
```json

```

### Example Output
```json

```

## Select Outside

### Description

### Example Input
```json

```

### Example Output
```json

```

## Clip

### Description

### Example Input
```json

```

### Example Output
```json

```

## Merge

### Description

### Example Input
```json

```

### Example Output
```json

```

## Combine Datasets

### Description

### Example Input
```json

```

### Example Output
```json

```