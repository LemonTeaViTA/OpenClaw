#!/bin/bash
# PDF 归档辅助脚本 - 帮助移动下载的 PDF 到正确目录
# 用法：./download-pdfs.sh

DOWNLOAD_DIR="$HOME/Downloads"
WORKSPACE="/root/.openclaw/workspace/files"

echo "🔍 正在检查下载目录..."

# MySQL
if [ -f "$DOWNLOAD_DIR/面渣逆袭 MySQL 篇 V2.2.pdf" ]; then
    echo "✅ 找到 MySQL 篇，移动中..."
    mv "$DOWNLOAD_DIR/面渣逆袭 MySQL 篇 V2.2.pdf" "$WORKSPACE/mysql-notes/"
else
    echo "⏳ MySQL 篇：未找到（请先在飞书中下载）"
fi

# Redis
if [ -f "$DOWNLOAD_DIR/面渣逆袭 Redis 篇 V2.0.pdf" ]; then
    echo "✅ 找到 Redis 篇，移动中..."
    mv "$DOWNLOAD_DIR/面渣逆袭 Redis 篇 V2.0.pdf" "$WORKSPACE/redis-notes/"
else
    echo "⏳ Redis 篇：未找到（请先在飞书中下载）"
fi

# Spring
if [ -f "$DOWNLOAD_DIR/面渣逆袭 Spring 篇 V2.0 亮白版.pdf" ]; then
    echo "✅ 找到 Spring 篇，移动中..."
    mv "$DOWNLOAD_DIR/面渣逆袭 Spring 篇 V2.0 亮白版.pdf" "$WORKSPACE/spring-notes/"
else
    echo "⏳ Spring 篇：未找到（请先在飞书中下载）"
fi

echo ""
echo "📊 当前归档状态："
ls -lh "$WORKSPACE"/*/

echo ""
echo "💡 操作指南："
echo "1. 打开飞书桌面客户端"
echo "2. 找到今天的对话记录"
echo "3. 右键点击 3 个 PDF 文件 → 下载"
echo "4. 运行此脚本：bash /root/.openclaw/workspace/download-pdfs.sh"
