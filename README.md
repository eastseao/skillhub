# Wechat-SkillHub 微信公众号工具集-ClawSkill

<p align="center">
  <img src="https://img.shields.io/badge/微信公众号-AI内容工具集-blue?style=flat-square" alt="WeChat SkillHub">
  <img src="https://img.shields.io/badge/技能数量-10个-green?style=flat-square" alt="10 Skills">
  <img src="https://img.shields.io/badge/开源协议-MIT-yellow?style=flat-square" alt="MIT License">
</p>


<p align="center">
  <strong>微信公众号 AI 内容创作全流程工具集</strong><br>
  从内容采集、AI 洗稿、爆款文章生成，到排版美化、自动发布，一站式覆盖公众号运营完整链路。
</p>


---

## 📦 技能清单

| 序号 | 技能名称                                | 功能简介                                                     | 触发示例                    |
| :--: | :-------------------------------------- | :----------------------------------------------------------- | :-------------------------- |
|  1   | **deep-digest**                         | 深度解读 — 支持 PDF / 网页 / DOCX / 公众号文章 / YouTube 等多源内容的结构化摘要生成 | "深度解读这篇PDF"           |
|  2   | **wechat-basic-formatting**             | 将 Markdown 渲染为公众号样式 HTML，一键推送草稿箱。Node.js 18+，零外部依赖 | "把这篇文章推到公众号"      |
|  3   | **wechat-advanced-formatting**          | 专业级排版 — AI 辅助渲染、MPEC.md 格式、SPEC 规范、多种输出模式 | "高级排版"                  |
|  4   | **wechat-all-in-one-viral-engine**      | 爆款文全流程引擎 — 选题挖掘、10~20 个标题、大纲撰写、完整正文、AI 原创改写、封面图生成 | "生成一篇爆款文章"          |
|  5   | **wechat-collect-7days-viral-articles** | 提取近 N 天高阅读量公众号文章，可设最低阅读量阈值            | "收集7天内的爆文"           |
|  6   | **wechat-operation-toolkit**            | 公众号一站式工具包 — 集成搜索、下载、AI洗稿改写、发布四大功能 | "搜公众号文章" / "帮我洗稿" |
|  7   | **wechat-viral-writer**                 | 爆款标题生成器 + 热点选题 + 原创/洗稿重写 + 情绪驱动内容增强 | "生成爆款标题"              |
|  8   | **wechat-auto-publish**                 | 将现成文章直接发布到公众号草稿箱，基于微信公众号 API         | "发布到草稿箱"              |
|  9   | **deaify**                              | 深度去AI化 — 彻底去除AI生成文本的"机器痕迹"，让内容更像真实人类写作 | "去AI味" / "人性化改写"     |
|  10  | **novel-engine**                        | 单部小说长期连载生成系统 — 稳定世界观 + 爽点持续 + 防崩结构，支持百万字扩展 | "生成小说章节"              |

---

## 🚀 快速开始

### 一键安装全部技能（推荐）

```bash
npx skillhub install eastseao/skillhub
```

### 按需安装单个技能

```bash
npx skills add eastseao/skillhub@wechat-basic-formatting
npx skills add eastseao/skillhub@wechat-viral-writer
npx skills add eastseao/skillhub@deaify
npx skills add eastseao/skillhub@novel-engine
# ... 其他技能同理
```

---

## ⚙️ 环境依赖

| 技能                                | 依赖环境                       |
| :---------------------------------- | :----------------------------- |
| wechat-basic-formatting             | Node.js 18+                    |
| wechat-advanced-formatting          | Node.js（依赖见 package.json） |
| wechat-operation-toolkit            | Node.js，`npm install cheerio` |
| wechat-auto-publish                 | bash, curl, jq                 |
| deep-digest                         | Python 环境                    |
| wechat-collect-7days-viral-articles | Python 环境                    |
| wechat-viral-writer                 | Python 环境                    |
| wechat-all-in-one-viral-engine      | Python 环境                    |
| deaify                              | Python 环境                    |
| novel-engine                        | Python 环境                    |

---

## 🔧 配置说明

在技能配置文件中填入以下环境变量：

```bash
WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret
# 可选
WECHAT_AUTHOR=作者名称
DEFAULT_COVER_URL=https://example.com/cover.jpg
```

> ⚠️ **重要提醒**：使用发布功能前，请将服务器 IP 地址加入微信公众号后台的 API IP 白名单，否则 API 调用会失败（错误码 40164）。

---

## 🔄 典型工作流

### 工作流 A — 搜索 → 洗稿 → 发布

```bash
# 1. 搜索文章
node scripts/search/search_wechat.js "AI教程" -n 5 -c

# 2. 使用 wechat-operation-toolkit 进行洗稿改写

# 3. 使用 deaify 去除AI痕迹，让内容更自然

# 4. 保存为 Markdown（含 frontmatter：title + cover）

# 5. 发布到草稿箱
node scripts/publisher/publish.js article.md
```

### 工作流 B — 生成 → 改写 → 排版 → 发布

```
wechat-all-in-one-viral-engine → wechat-viral-writer → deaify → wechat-advanced-formatting → wechat-auto-publish
```

### 工作流 C — 采集 → 解读 → 创作 → 发布

```
wechat-collect-7days-viral-articles → deep-digest → 原创生成 → deaify → wechat-basic-formatting
```

### 工作流 D — 小说连载创作

```
novel-engine（世界观构建）→ novel-engine（章节生成）→ deaify（去AI化）→ 连载发布
```

---

## ⚠️ 使用须知

- 所有工具仅供个人学习与研究使用，请遵守相关版权法规。
- 搜索功能内置防封禁机制（随机 User-Agent、请求延迟），请勿高频使用。
- 微信公众号 API 需要有效的 AppID 和 AppSecret，以及正确的 IP 白名单配置。

---

## 📄 开源许可

本项目采用 **MIT License** 开源协议。

```
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
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

---

<p align="center">
  🔗 <a href="https://github.com/eastseao/skillhub">GitHub 仓库</a> · 
  👤 <a href="https://github.com/eastseao">@eastseao</a>
</p>

