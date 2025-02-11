#!/usr/bin/env bash
OUT_DIR=custom_components/salute_stt
python3 -m grpc_tools.protoc -I proto --python_out=$OUT_DIR --pyi_out=$OUT_DIR --grpc_python_out=$OUT_DIR proto/{recognition,task,synthesis}.proto

sed -i -E 's/^(import task_pb2|import recognition_pb2|import synthesis_pb2)/from . \1/g' $OUT_DIR/*_pb2*.py
