#!/usr/bin/env python3
"""扫描 arXiv cs.RO 指定时间窗内与灵巧手相关的新论文（官方 API，非搜索摘要）。

用法:
    python3 scripts/arxiv_scan.py                 # 默认最近 7 天
    python3 scripts/arxiv_scan.py 20260922 20260928   # 指定 YYYYMMDD 区间

输出: Markdown 表格片段（可直接粘贴进 docs/latest-updates-*.md），并保存原始 XML。
依赖: 仅标准库（urllib）。
"""
import re
import sys
import html
import urllib.request
import datetime as dt

API = "https://export.arxiv.org/api/query"
# 灵巧手主线关键词（强匹配 = 直接进入表格）
STRONG = re.compile(r"(dexter|in-hand|multi-?finger|five-finger|tactile|whole-hand|"
                    r"fingertip|hand retarget|hand-object|teleop|glove|exoskeleton|"
                    r"grasp|wrist|haptic|anthropomorphic hand)", re.I)
# 弱匹配（操作类，仅统计）
WEAK = re.compile(r"(manipulat|world model|imitation|policy)", re.I)


def fetch(start: str, end: str, cat: str = "cs.RO", max_results: int = 500) -> str:
    q = (f"search_query=cat:{cat}+AND+submittedDate:%5B{start}0000+TO+{end}2359%5D"
         f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}")
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def parse(xml: str):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        i = re.search(r"<id>http://arxiv.org/abs/([^<]+)</id>", e)
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        p = re.search(r"<published>([^<]+)</published>", e)
        a = re.findall(r"<name>([^<]+)</name>", e)
        c = re.search(r"<arxiv:comment[^>]*>(.*?)</arxiv:comment>", e, re.S)
        if not (i and t):
            continue
        out.append({
            "id": i.group(1),
            "title": html.unescape(" ".join(t.group(1).split())),
            "date": p.group(1)[:10] if p else "?",
            "first_author": a[0] if a else "",
            "n_authors": len(a),
            "comment": html.unescape(" ".join(c.group(1).split()))[:120] if c else "",
        })
    return out


def main():
    today = dt.date.today()
    if len(sys.argv) >= 3:
        start, end = sys.argv[1], sys.argv[2]
    else:
        start = (today - dt.timedelta(days=7)).strftime("%Y%m%d")
        end = today.strftime("%Y%m%d")
    xml = fetch(start, end)
    open(f"arxiv_{start}_{end}.xml", "w", encoding="utf-8").write(xml)
    rows = parse(xml)
    strong = [r for r in rows if STRONG.search(r["title"])]
    weak = [r for r in rows if not STRONG.search(r["title"]) and WEAK.search(r["title"])]
    print(f"# arXiv {start}–{end} | cs.RO 共 {len(rows)} 篇 | 灵巧手相关 {len(strong)} 篇"
          f"（+操作类 {len(weak)} 篇）\n")
    print("| 论文 | 第一作者 | 公告日 | 链接 |")
    print("| --- | --- | --- | --- |")
    for r in strong:
        aid = re.sub(r"v\d+$", "", r["id"])
        print(f"| {r['title']} | {r['first_author']} 等 {r['n_authors']} 人 | {r['date']} "
              f"| [arXiv:{aid}](https://arxiv.org/abs/{aid}) |")
    print("\n> 机构字段 arXiv API 不提供，需逐篇核验（见 docs/verification-2026-09.md 的核验方法）。")


if __name__ == "__main__":
    main()
