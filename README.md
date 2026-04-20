# Wechat-SkillHub

## 微信公众号 AI 内容工具集 · WeChat Official Account AI Content Toolkit

[![GitHub](https://img.shields.io/badge/GitHub-eastseao%2Fskillhub-blue?style=flat-square&logo=github)](https://github.com/eastseao/skillhub)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

🔗 **GitHub**: https://github.com/eastseao/skillhub

### 概览

**skillhub** 是由 [@eastseao](https://github.com/eastseao) 维护的微信公众号 AI 内容创作工具集，收录了 **8 个生产级 Skill（技能包）**。从内容采集、AI 洗稿、爆款文章生成，到排版美化、自动发布，覆盖了公众号运营的完整链路。

---

### 技能一览

| #    | 技能名                                | 功能简介                                                     | 触发词示例                                   |
| ---- | ------------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| 1    | `deep-digest-1.0.0`                   | 深度解读 — 支持 PDF / 网页 / DOCX / 公众号文章 / YouTube 等多源内容的结构化摘要生成 | "深度解读这篇PDF" / "summarize this article" |
| 2    | `wechat-basic-formatting`             | 将 Markdown 渲染为公众号样式 HTML，一键推送草稿箱。Node.js 18+，零外部依赖 | "把这篇文章推到公众号" / "发布到微信公众号"  |
| 3    | `wechat-advanced-formatting`          | 专业级排版 — AI 辅助渲染、MPEC.md 格式、SPEC 规范、多种输出模式（article.md / article.ai.draft.html / HTML / Markdown） | "高级排版" / "编辑公众号"                    |
| 4    | `wechat-all-in-one-viral-engine`      | 爆款文全流程引擎 — 选题挖掘、10~20 个标题、大纲撰写、完整正文、AI 原创改写、数据分析日报、封面图生成 | "生成一篇爆款文章" / "帮我写公众号文章"      |
| 5    | `wechat-collect-7days-viral-articles` | 提取近 N 天高阅读量公众号文章（News API / GSData API / 搜狗微信 / 自定义数据库），可设最低阅读量阈值 | "收集7天内的爆文" / "抓取热门文章"           |
| 6    | `wechat-operation-toolkit`            | 公众号一站式工具包 — 集成搜索、下载、AI洗稿改写、发布四大功能，Node.js 环境 | "搜公众号文章" / "帮我洗稿" / "下载这篇文章" |
| 7    | `wechat-viral-writer`                 | 爆款标题生成器（10~30 个）+ 热点选题 + 原创/洗稿重写 + 情绪驱动内容增强 + 带货/引流转化文案植入 | "生成爆款标题" / "写一篇情绪文"              |
| 8    | `wechat-auto-publish`                 | 将现成文章（标题+摘要+HTML）直接发布到公众号草稿箱，基于微信公众号 API | "发布到草稿箱" / "publish to draft"          |

---

### 安装方式

**一键安装全部技能（推荐）：**

```bash
npx skillhub install eastseao/skillhub
```

**按需安装单个技能：**

```bash
npx skills add eastseao/skillhub@wechat-basic-formatting
npx skills add eastseao/skillhub@wechat-viral-writer
# ... 其他技能同理
```

---

### 环境依赖

| 技能                                  | 依赖                           |
| ------------------------------------- | ------------------------------ |
| `wechat-basic-formatting`             | Node.js 18+                    |
| `wechat-advanced-formatting`          | Node.js（依赖见 package.json） |
| `wechat-operation-toolkit`            | Node.js，`npm install cheerio` |
| `wechat-auto-publish`                 | bash, curl, jq                 |
| `deep-digest-1.0.0`                   | Python 环境                    |
| `wechat-collect-7days-viral-articles` | Python 环境                    |
| `wechat-viral-writer`                 | Python 环境                    |
| `wechat-all-in-one-viral-engine`      | Python 环境                    |

---

### 微信公众号 API 配置

在技能配置文件中填入以下环境变量：

```bash
WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret
# 可选
WECHAT_AUTHOR=作者名称
DEFAULT_COVER_URL=https://example.com/cover.jpg
```

> ⚠️ **重要提醒：** 使用发布功能前，请将服务器 IP 地址加入微信公众号后台的 **API IP 白名单**，否则 API 调用会失败（错误码 `40164`）。

---

### 典型工作流

**工作流 A — 搜索 → 洗稿 → 发布**

1. 搜索文章：`node scripts/search/search_wechat.js "AI教程" -n 5 -c`
2. 选中目标文章，使用 `wechat-operation-toolkit` 进行洗稿改写
3. 保存为 Markdown（含 frontmatter：title + cover）
4. 发布：`node scripts/publisher/publish.js article.md`

**工作流 B — 生成 → 改写 → 排版 → 发布**

1. 使用 `wechat-all-in-one-viral-engine` 生成爆款文章（选题 → 标题 → 大纲 → 正文）
2. 使用 `wechat-viral-writer` 洗稿改写
3. 使用 `wechat-advanced-formatting` 排版美化
4. 使用 `wechat-auto-publish` 推送到草稿箱

**工作流 C — 采集 → 解读 → 创作 → 发布**

1. 使用 `wechat-collect-7days-viral-articles` 采集近7天爆文
2. 使用 `deep-digest-1.0.0` 深度解读内容
3. 基于解读洞察生成原创文章
4. 使用 `wechat-basic-formatting` 发布

---

### ⚠️ 免责声明

- 所有工具**仅供个人学习与研究使用**，请遵守相关版权法规。
- 搜索功能内置防封禁机制（随机 User-Agent、请求延迟），**请勿高频使用**。
- 微信公众号 API 需要有效的 AppID 和 AppSecret，以及正确的 IP 白名单配置。



---



<details>
<summary><strong>▶ MIT License</strong></summary>


MIT License

Copyright (c) 2026-present eastseao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</details>

---


