# coding:utf-8
from collections import deque


# 广搜，，一层一层地搜索，如果不是则将下一位中所有的人加入队列。同时用一个数组来保存检查过的人（元素）


graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph['bob'] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph['claire'] = ["thom", "jonny"]
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]  # 加入你的邻居
    seached = []  # 用于记录检查过的人

    while search_queue:  # 只要队列中仍存在未检查过的
        person = search_queue.popleft()  # 取出队列中的第一歌人
        if person not in search_queue:  # 仅当这个人没有检查过才搜索
            if person_is_seller(person):  # 检查是否为seller
                print person + "is a mango seller!"
                return True

            else:
                search_queue += graph[person]
                seached.append(person)  # 标记为搜索过

    return False

search("you")