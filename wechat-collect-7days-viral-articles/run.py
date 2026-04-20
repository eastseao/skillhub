import datetime

def run(params):
    days = params.get("days", 7)
    min_read = params.get("min_read", 100000)

    # 1. 时间范围
    now = datetime.datetime.now()
    start_time = now - datetime.timedelta(days=days)

    # 2. 模拟数据（可替换为API）
    articles = [
        {
            "title": "AI行业大爆发",
            "account": "科技前沿",
            "time": now - datetime.timedelta(days=1),
            "read": 120000,
            "link": "https://mp.weixin.qq.com/s/xxx"
        },
        {
            "title": "城市经济趋势",
            "account": "财经观察",
            "time": now - datetime.timedelta(days=3),
            "read": 95000,
            "link": "https://mp.weixin.qq.com/s/yyy"
        }
    ]

    # 3. 过滤
    filtered = []
    seen = set()

    for a in articles:
        if a["time"] >= start_time and a["read"] >= min_read:
            key = a["title"]
            if key not in seen:
                seen.add(key)
                filtered.append(a)

    # 4. 排序
    filtered.sort(key=lambda x: x["time"], reverse=True)

    # 5. 输出
    md = "| 序号 | 标题 | 公众号 | 发布时间 | 阅读量 | 链接 |\n"
    md += "|------|------|----------|----------|--------|------|\n"

    for i, a in enumerate(filtered, 1):
        md += f"| {i} | {a['title']} | {a['account']} | {a['time'].strftime('%Y-%m-%d')} | {a['read']} | {a['link']} |\n"

    return md