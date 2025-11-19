#!/bin/bash

# 自动检测系统资源并选择合适的Java启动参数

echo "正在检测系统资源..."

# 获取系统总内存（GB）
total_memory=$(free -g | awk '/^Mem:/{print $2}')
echo "系统总内存: ${total_memory}G"

# 获取CPU核心数
cpu_cores=$(nproc)
echo "CPU核心数: ${cpu_cores}"

# 根据系统资源确定堆内存大小
if [ $total_memory -ge 16 ]; then
    heap_size="${total_memory}G"
elif [ $total_memory -ge 8 ]; then
    heap_size="${total_memory}G"
else
    heap_size="4G"
fi

echo "分配堆内存: ${heap_size}"

# 根据CPU核心数调整G1垃圾收集器参数
if [ $cpu_cores -ge 8 ]; then
    G1NewSizePercent=30
    G1MaxNewSizePercent=40
    G1HeapRegionSize=8M
    G1ReservePercent=20
else
    G1NewSizePercent=25
    G1MaxNewSizePercent=35
    G1HeapRegionSize=4M
    G1ReservePercent=15
fi

# 构建Java启动命令
JAVA_OPTS="-Xmx${heap_size} \
-XX:+UseG1GC \
-XX:+ParallelRefProcEnabled \
-XX:MaxGCPauseMillis=200 \
-XX:+UnlockExperimentalVMOptions \
-XX:+DisableExplicitGC \
-XX:+AlwaysPreTouch \
-XX:G1HeapWastePercent=5 \
-XX:G1MixedGCCountTarget=4 \
-XX:InitiatingHeapOccupancyPercent=15 \
-XX:G1MixedGCLiveThresholdPercent=90 \
-XX:G1RSetUpdatingPauseTimePercent=5 \
-XX:SurvivorRatio=32 \
-XX:+PerfDisableSharedMem \
-XX:MaxTenuringThreshold=1 \
-Dusing.aikars.flags=https://mcflags.emc.gs \
-Daikars.new.flags=true \
-XX:G1NewSizePercent=${G1NewSizePercent} \
-XX:G1MaxNewSizePercent=${G1MaxNewSizePercent} \
-XX:G1HeapRegionSize=${G1HeapRegionSize} \
-XX:G1ReservePercent=${G1ReservePercent}"

echo "启动参数已配置完成，正在启动服务器..."
echo "Java opts: ${JAVA_OPTS}"

# 启动服务器
java ${JAVA_OPTS} -jar ../leaves.jar --nogui