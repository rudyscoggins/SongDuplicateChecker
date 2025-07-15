# SongDuplicateChecker

This project displays the timestamp of the container build so you can tell
when the site was last updated. When building the Docker image, supply a
`BUILD_TIMESTAMP` argument (in ISO format) or it will default to `unknown`.

To build the Docker image with the current time automatically, run the
`build.sh` script:

```bash
./build.sh
```
