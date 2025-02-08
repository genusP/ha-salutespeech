#!/usr/bin/env bash
SCRIPT_PATH=$(realpath $0)
SCRIPT_DIR=$(dirname $SCRIPT_PATH)
OUT_DIR=$SCRIPT_DIR/custom_components/salute_stt
.venv/bin/python -m grpc_tools.protoc -I $SCRIPT_DIR/proto --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR $SCRIPT_DIR/proto/{recognition,task,synthesis}.proto

sed -i -E 's/^(import task_pb2|import recognition_pb2|import synthesis_pb2)/from . \1/g' $OUT_DIR/*_pb2*.py
