import random
import json

def generate_titles(topic, count=20):
    templates = [
        "为什么{topic}的人，最后都赢了？",
        "{topic}，正在悄悄毁掉你",
        "我研究了100个{topic}的人，发现一个残酷真相",
        "{topic}：普通人翻身的唯一机会",
        "别再{topic}了，99%的人都错了",
        "{topic}背后，是一场认知碾压",
        "关于{topic}，这是我最痛的教训",
        "{topic}，才是你最大的底牌",
    ]
    
    return [random.choice(templates).format(topic=topic) for _ in range(count)]


def generate_article(topic):
    intro = f"你有没有发现，{topic}这件事，正在悄悄改变很多人的命运。"
    
    body = f"""
很多人以为{topic}很简单，但真正拉开差距的，是认知。

我见过太多人，在{topic}上走弯路：
有人拼命努力，却没有结果；
有人轻轻松松，却一路领先。

区别在哪？

在于他们是否看懂了底层逻辑。

普通人最大的问题，不是懒，而是盲目努力。
"""

    emotion = f"""
说实话，这个时代最残酷的地方在于：
你以为你在努力，其实只是自我感动。

真正厉害的人，早就用{topic}完成了跃迁。
"""

    ending = """
如果你也想改变现状，现在就要开始行动。

关注我，带你看懂更多底层逻辑。
"""

    return intro + body + emotion + ending


def run(input_data):
    topic = input_data.get("topic", "普通人翻身")
    
    titles = generate_titles(topic)
    article = generate_article(topic)
    
    return {
        "titles": titles,
        "article": article
    }


if __name__ == "__main__":
    result = run({"topic": "赚钱能力"})
    print(result)