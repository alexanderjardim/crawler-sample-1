# Example Crawler

This repository contains a command line script writen in Python3 for downloading the png image files from a given url

## Usage

Execution
```
python -m download -u url -o outputdir [-l username -p password]
```

For help
```
python -m download -h
```

## Development

Run unit tests
```
python -m unittest discover
```

One can run a local server on port 8080 for manual tests with

```
docker-compose up
```
