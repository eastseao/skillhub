# skillhub — 微信公众号 AI 内容工具集

# skillhub — WeChat Official Account AI Content Toolkit

[![GitHub](https://img.shields.io/badge/GitHub-eastseao%2Fskillhub-blue?style=flat-square&logo=github)](https://github.com/eastseao/skillhub)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

> 🔗 **GitHub 仓库** | https://github.com/eastseao/skillhub
> 🌐 **English README** — see below after 中文说明

---

## 📖 简介 | Introduction

`skillhub` 是由 **@eastseao** 维护的微信公众号 AI 内容创作工具集，收录了 8 个专注于微信公众号内容生产全流程的 Skill（技能包）。从内容采集、AI 洗稿、爆款文章生成，到排版美化、自动发布，覆盖了公众号运营的完整链路。

**This repository** is a curated collection of WeChat Official Account (公众号) AI content creation skills maintained by **@eastseao**. It provides 8 production-ready skills covering the full lifecycle: content collection, AI rewriting, viral article generation, formatting, and auto-publishing.

---

## 🧩 技能总览 | Skills Overview

| #    | 技能名                                    | 功能简介                                                     | 触发词示例                                   |
| ---- | ----------------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| 1    | **`deep-digest-1.0.0`**                   | 深度解读技能 — 支持 PDF / 网页 / DOCX / 微信公众号文章 / YouTube 等多源内容的结构化摘要生成 | "深度解读这篇PDF" / "summarize this article" |
| 2    | **`wechat-basic-formatting`**             | 将 Markdown 渲染为公众号样式 HTML，并一键推送到公众号草稿箱。Node.js 18+，零外部依赖 | "把这篇文章推到公众号" / "发布到微信公众号"  |
| 3    | **`wechat-advanced-formatting`**          | 高级排版 — 支持 AI 辅助渲染、MPEC.md 格式、SPEC 规范、多种输出模式（article.md / article.ai.draft.html / HTML / Markdown） | "高级排版" / "编辑公众号"                    |
| 4    | **`wechat-all-in-one-viral-engine`**      | 公众号爆款文全流程引擎 — 包含选题、标题生成（10~20个）、大纲撰写、原创改写、数据分析日报、封面图生成等完整工作流 | "生成一篇爆款文章" / "帮我写公众号文章"      |
| 5    | **`wechat-collect-7days-viral-articles`** | 提取近 N 天高阅读量公众号文章（支持 News API / GSData API / 搜狗微信 / 自定义数据库），可设置最低阅读量阈值 | "收集7天内的爆文" / "抓取热门文章"           |
| 6    | **`wechat-operation-toolkit`**            | 公众号一站式工具包 — 集成文章搜索、下载、AI洗稿改写、发布四大功能，Node.js 环境 | "搜公众号文章" / "帮我洗稿" / "下载这篇文章" |
| 7    | **`wechat-viral-writer`**                 | 爆款标题生成器（10~30个）+ 热点选题 + 原创/洗稿重写 + 情绪驱动内容增强 + 带货/引流转化植入 | "生成爆款标题" / "写一篇情绪文"              |
| 8    | **`wechat-auto-publish`**                 | 将现成的文章内容（标题+摘要+HTML）直接发布到微信公众号草稿箱，基于微信公众号 API | "发布到草稿箱" / "publish to draft"          |

---

## 🚀 快速开始 | Quick Start

### 安装所有技能 | Install All Skills

```bash
# 使用 skillhub CLI 安装（推荐）
npx skillhub install eastseao/skillhub

# 或逐个安装单个技能
npx skills add eastseao/skillhub@wechat-basic-formatting
npx skills add eastseao/skillhub@wechat-viral-writer
```

### 环境依赖 | Prerequisites

| 技能                                  | 依赖                             |
| ------------------------------------- | -------------------------------- |
| `wechat-basic-formatting`             | Node.js 18+                      |
| `wechat-advanced-formatting`          | Node.js，依赖包见 `package.json` |
| `wechat-operation-toolkit`            | Node.js，`npm install cheerio`   |
| `wechat-auto-publish`                 | bash, curl, jq                   |
| `deep-digest-1.0.0`                   | Python 环境                      |
| `wechat-collect-7days-viral-articles` | Python 环境                      |
| `wechat-viral-writer`                 | Python 环境                      |
| `wechat-all-in-one-viral-engine`      | Python 环境                      |

### 微信公众号 API 配置 | WeChat Official Account API Setup

发布类技能需要配置微信公众号凭证：

```bash
# 在技能配置文件中填入以下环境变量
WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret

# 可选
WECHAT_AUTHOR=作者名称
DEFAULT_COVER_URL=https://example.com/cover.jpg
```

> ⚠️ **重要提醒**：使用发布功能前，请将本机 **IP 地址** 加入微信公众号后台的 **API IP 白名单**，否则 API 调用会失败（错误码 40164）。

---

## 📦 各技能详解 | Skills Detail

### 1. 🧠 deep-digest-1.0.0 — 深度内容解读

**多源内容结构化摘要生成器**

支持输入类型：

- 🌐 网页 URL（Web）
- 📄 PDF 文档
- 📝 DOCX 文档
- 📱 微信公众号文章（WeChat）
- 🎬 YouTube 视频

输出格式：结构化摘要、关键要点、相关链接等。

```
deep_digest "<URL>" --mode insight
```

---

### 2. 📤 wechat-basic-formatting — 基础发布

**Markdown → 公众号草稿箱，一键完成**

- 读取本地 Markdown 文件
- 渲染为微信公众号兼容的 HTML（内联样式）
- 自动推送至公众号草稿箱
- 无需生成本地 HTML 文件

```bash
# 首次：查看当前 IP（用于加白名单）
node scripts/publish.cjs --file article.md

# 确认后正式推送
node scripts/publish.cjs --file article.md --confirmed
```

---

### 3. 🎨 wechat-advanced-formatting — 高级排版

**专业级公众号排版，支持多种输入输出格式**

支持输入格式：

- `article.md` — Markdown 文章
- `article.ai.draft.html` — AI 辅助编辑格式
- `SPEC.md` — 排版规格定义文件
- `MPEC.md` — 微信公众号编辑内容格式

支持输出模式：

| 模式                    | 说明                         |
| ----------------------- | ---------------------------- |
| `article.md`            | Markdown 输出                |
| `article.ai.draft.html` | AI 辅助编辑 HTML             |
| `article.ai.html`       | 含 SPEAC 区块的 HTML         |
| `article.html`          | 纯 HTML 输出                 |
| `wechat-copy`           | 微信公众号复制格式（剪贴板） |

```bash
# 方式一：通过编辑助手网页工具
open https://edit.shiker.tech/copy.html?id=xxx

# 方式二：通过 AI 渲染
node html-to-wechat-copy.js <path-to-article.md>

# 方式三：获取预览 URL
node wechat-preview-urls.js
```

---

### 4. 🧨 wechat-all-in-one-viral-engine — 爆款文全流程引擎

**从选题到成品文章，完整闭环**

```
skill: wechat-article-pro-plus
```

| 步骤     | 内容                         |
| -------- | ---------------------------- |
| 选题     | 热点挖掘                     |
| 标题     | 10~20 个爆款标题生成         |
| 大纲     | 文章结构规划                 |
| 正文     | 完整文章撰写                 |
| 改写     | 原创度提升                   |
| 数据分析 | 日报生成（阅读量/分享/评论） |
| 封面图   | 封面 + 插图生成              |

所有步骤均支持 Python 环境下的自动化运行。

---

### 5. 📊 wechat-collect-7days-viral-articles — 爆文采集器

**提取近 N 天高阅读量公众号文章**

支持数据源：

- 📰 News API
- 📈 GSData API
- 🔍 搜狗微信搜索（备选）
- 🗄️ 自定义数据库

```json
{
  "days": 7,
  "min_read": 100000,
  "source": "auto",
  "keyword": "AI",
  "api_key": null
}
```

---

### 6. 📦 wechat-operation-toolkit — 一站式工具包

**四大功能模块，覆盖运营全流程**

| 模块   | 功能                                 | 命令示例                                         |
| ------ | ------------------------------------ | ------------------------------------------------ |
| 🔍 搜索 | 搜狗微信搜索，解析真实链接，抓取正文 | `node search_wechat.js "关键词" -n 15 -c`        |
| 📰 下载 | 下载文章内容/图片/视频到本地         | `node download.js "文章URL" --output ./articles` |
| ✍️ 洗稿 | AI 去痕迹 + 原创改写                 | "帮我洗稿这篇文章"                               |
| 📱 发布 | Markdown → 公众号草稿箱              | `wenyan publish -f article.md -t lapis`          |

---

### 7. 💥 wechat-viral-writer — 爆款写作器

**情绪驱动 + 带货转化**

- 📌 爆款标题（10~30 个）
- 🔥 热点选题挖掘
- ✏️ 原创 / 洗稿重写
- 💢 情绪驱动内容增强
- 🛒 带货 / 引流转化文案植入

```
输入：主题 + 风格（情绪/理性/带货）+ 目标（涨粉/转化/阅读量）
输出：爆款标题 + 完整文章结构 + 成品文章 + 转化文案
```

---

### 8. 📬 wechat-auto-publish — 自动发布

**仅负责发布，不负责内容生成**

将现成的文章（标题+摘要+HTML）推送至公众号草稿箱。

```bash
source ./scripts.sh

# 获取 token
TOKEN=$(get_wechat_token)

# 上传封面图
MEDIA_RESPONSE=$(upload_wechat_image "$TOKEN" "$cover_image_path")
THUMB_MEDIA_ID=$(echo "$MEDIA_RESPONSE" | jq -r '.media_id')

# 创建草稿
DRAFT_JSON=$(mktemp)
jq -n \
    --arg title "$title" \
    --arg author "${WECHAT_AUTHOR:-koo AI}" \
    --arg digest "$digest" \
    --arg content "$content_html" \
    --arg thumb_media_id "$THUMB_MEDIA_ID" \
    '{ articles: [{ title: $title, author: $author, digest: $digest, content: $content, thumb_media_id: $thumb_media_id, need_open_comment: 1, only_fans_can_comment: 0 }] }' > "$DRAFT_JSON"

DRAFT_RESPONSE=$(create_draft "$TOKEN" "$DRAFT_JSON")
```

---

## 🔧 完整工作流示例 | Complete Workflow Examples

### 示例一：搜索 → 洗稿 → 发布

```
1. 搜索文章
   node scripts/search/search_wechat.js "AI教程" -n 5 -c

2. 选择目标文章，执行洗稿改写（使用 wechat-operation-toolkit）

3. 保存为 Markdown（含 frontmatter：title + cover）

4. 发布
   node scripts/publisher/publish.js article.md
```

### 示例二：爆款文章生成 → 发布

```
1. 生成爆款文章（使用 wechat-all-in-one-viral-engine）
   - 选题 → 标题 → 大纲 → 正文

2. 洗稿改写（使用 wechat-viral-writer）

3. 排版美化（使用 wechat-advanced-formatting）

4. 发布到草稿箱（使用 wechat-auto-publish）
```

### 示例三：热点采集 → 深度解读 → 发布

```
1. 采集近7天爆文（使用 wechat-collect-7days-viral-articles）

2. 深度解读内容（使用 deep-digest-1.0.0）

3. 基于解读生成原创文章

4. 发布（使用 wechat-basic-formatting）
```

---

## ⚠️ 使用声明 | Disclaimer

- 所有工具仅供**个人学习与研究**使用，请遵守相关版权法规
- 搜索功能内置防封禁机制（随机 User-Agent、请求延迟），请勿高频使用
- 微信公众号 API 需要有效的 AppID 和 AppSecret，以及正确的 IP 白名单配置

**All tools are for personal learning and research purposes only. Please comply with applicable copyright laws. The search feature includes anti-blocking mechanisms (random UA, request delay); please avoid high-frequency usage.**

---

## 📄 License

本项目未明确声明 License，使用前请参考 GitHub 仓库中的 LICENSE 文件。

**Please refer to the LICENSE file in the repository before use.**

---

*由 AI 辅助生成 README · Generated with AI assistance · https://github.com/eastseao/skillhub*
