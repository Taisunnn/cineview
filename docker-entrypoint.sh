#!/bin/bash

case "$1" in
    start)
        exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
        ;;
    debug)
        exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload
        ;;
    *)
        exec "$@"
        ;;
esac