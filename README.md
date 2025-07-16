# SongDuplicateChecker

SongDuplicateChecker is a small FastAPI service that reads from the same music
library used by [SongRipper](https://github.com/rudyscoggins/SongRipper).  The
application simply reports a random file from the library and when the running
container was built.

## Running with Docker

Use the provided `docker-compose.yml` to build and start the service.  It
mounts your music collection under `/music` and exposes the app on port `5443`.

```bash
docker compose up --build
```

## Environment Variables

- `DATA_DIR` – directory for any application data (default: `/data`).
- `NAS_PATH` – path to the music library inside the container (default:
  `/music`).

These can be customised in `docker-compose.yml` or when starting the container
manually.

The `build.sh` script sets a `BUILD_TIMESTAMP` argument so the web page can show
when the image was created.
