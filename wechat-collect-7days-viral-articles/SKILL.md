---
name: wechat-collect-7days-viral-articles
description: Extract high-performing WeChat articles (100k+ reads) published within a recent time window, using multiple data sources such as APIs or web scraping.
version: 1.0.0
author: eastseao
tags: [wechat, content, trending, scraping, analysis]
---

# 🧠 WeChat Hot Article Extractor

## 📌 Overview
This skill extracts WeChat public account articles that meet the following criteria:

- Published within the last N days (default: 7)
- Read count ≥ specified threshold (default: 100,000)

Supports multiple data sources including:
- Newrank API
- GSData API
- Sogou WeChat Search (fallback)
- Custom database

---

## ⚙️ Input Schema

```json
{
  "days": 7,
  "min_read": 100000,
  "source": "auto",
  "keyword": "热点",
  "api_key": null
}