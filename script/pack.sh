#!/bin/bash

# 打包脚本 - 将项目打包为zip文件，排除特定目录

echo "开始打包项目..."

# 定义项目根目录
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "项目根目录: $PROJECT_ROOT"

# 定义输出文件名
OUTPUT_FILE="$PROJECT_ROOT/SurviveP.zip"
echo "输出文件: $OUTPUT_FILE"

# 进入项目根目录
cd "$PROJECT_ROOT"

# 使用zip命令打包项目，排除指定目录
zip -r "$OUTPUT_FILE" . \
  -x "*.git*" \
  -x "*.github*" \
  -x "script*" \
  -x "SurviveP.zip"

echo "打包完成！"

ls -lh "$OUTPUT_FILE"