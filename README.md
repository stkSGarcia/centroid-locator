# Centroid Locator Backend

## Install

```shell
cd centroid-locator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run web service

```shell
source .venv/bin/activate
flask --app impl/server run [--debug]
```

## APIs

```text
Path: /parse
Method: GET, POST
Form: file=File
Response: JSON

Path: /locate
Method: GET, POST
Form:   file=File
        dist=int
        min_radius=int
        max_radius=int
Response: JSON
```
