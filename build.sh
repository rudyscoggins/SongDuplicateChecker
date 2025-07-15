#!/usr/bin/env bash
# Build the SongDuplicateChecker Docker image with a build timestamp.
set -e

docker build \
  --build-arg BUILD_TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  -t ghcr.io/rudyscoggins/songduplicatechecker:latest "$@" .
