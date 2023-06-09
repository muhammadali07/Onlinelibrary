#! /usr/bin/env sh
set -e

if [ -f main.py ]; then
    DEFAULT_MODULE_NAME=main
fi

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
echo "$MODULE_NAME:$VARIABLE_NAME"
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${API_HTTP_PORT:-80}
LOG_LEVEL=${LOG_LEVEL:-info}

# Start Uvicorn with live reload for development
exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"