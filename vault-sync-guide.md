# Vault 同步方案指南

## 🎯 目标
实现服务器端 (/root/vault) 和本地 Obsidian 的双向同步

## 方案对比

### 方案 A：Remotely Save 插件 + 云存储（推荐）

**优点：**
- 无需手动操作，自动同步
- Obsidian 内完成
- 免费

**支持的服务：**
| 服务 | 免费额度 | 国内速度 |
|------|---------|---------|
| 坚果云 | 2GB/月流量 | ⭐⭐⭐⭐⭐ |
| OneDrive | 5GB | ⭐⭐⭐ |
| S3 兼容 | 按量付费 | ⭐⭐⭐⭐ |

**设置步骤：**
1. Obsidian → 设置 → 社区插件
2. 关闭安全模式
3. 搜索 "Remotely Save" → 安装 → 启用
4. 选择服务商并配置

---

### 方案 B：Git 同步

**服务器端（已准备好）：**
```bash
/root/vault/
├── .git/
├── .obsidian/plugins/claudian/
└── README.md
```

**你的操作：**
```bash
# 本地 Vault 目录
cd ~/ObsidianVault
git init
git remote add origin https://github.com/你的用户名/obsidian-vault.git
git pull origin master  # 获取服务器内容
```

**工作流：**
- 你修改后：`git add . && git commit -m "update" && git push`
- 我修改后：自动 push 到 GitHub
- 你想同步：`git pull`

---

### 方案 C：Syncthing（P2P 直连）

**优点：**
- 无需云端
- 实时同步
- 完全免费

**设置：**
1. 两边安装 Syncthing
2. 交换设备 ID
3. 共享 /root/vault 文件夹

---

## 推荐选择

**如果你想要最简单的：** → 方案 A（坚果云 + Remotely Save）
**如果你想要完全控制：** → 方案 B（Git）
**如果你不想用云服务：** → 方案 C（Syncthing）
