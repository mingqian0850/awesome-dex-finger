# 🛠️ 更新脚本

本目录提供两个脚本，把仓库的「更新」流程标准化——**以后刷新只需跑这两条命令**。

## 1. `arxiv_scan.py` — 扫描 arXiv 新论文（官方 API）

```bash
python3 scripts/arxiv_scan.py                    # 默认最近 7 天
python3 scripts/arxiv_scan.py 20260922 20260928  # 指定 YYYYMMDD 区间
```

- 直接查询 **arXiv 官方 API**（`cat:cs.RO` + `submittedDate`），**不依赖搜索引擎摘要**，避免标题截断/漏检
- 输出可直接粘贴进 `docs/latest-updates-2026h2.md` 的 Markdown 表格（含第一作者、作者数、公告日、链接）
- 同时保存原始 XML（`arxiv_<start>_<end>.xml`）以便复核
- ⚠️ arXiv API **不提供机构字段**，机构需按 `docs/verification-2026-09.md` 的方法逐篇核验（arXiv 官方 HTML 作者块 / PDF 首页）
- ⚠️ arXiv 在周末不公告，周一跑通常只能拿到上周五批次；**周五晚或周一晚**跑覆盖最全

## 2. `refresh_stars.sh` — 刷新 GitHub 数据（官方 API）

```bash
bash scripts/refresh_stars.sh            # 输出 stars.tsv
bash scripts/refresh_stars.sh out.tsv    # 指定输出文件
```

- 通过 `gh api` 批量拉取仓库的 **star 数 / 许可证 / 最后推送时间**
- 覆盖仓库中跟踪的全部项目（开源硬件、仿真、算法、中文社区、Awesome 列表，共 60+ 个）
- 需要 `gh` 已登录（`gh auth status` 确认；只需 repo 读取权限）
- 拿到 `stars.tsv` 后，对照 `docs/open-source.md` 与 `awesome-lists.md` 更新变化项

## 建议的更新节奏

| 频率 | 动作 |
| --- | --- |
| 每周 | 跑两个脚本 → 更新数值 + 追加论文表格 |
| 每月 | 追加/整理一个「月报」小节，并把机构与会议录用状态核验一遍 |
| 有大会时（ICRA/IROS/CoRL/RSS、WRC/WAIC）| 会后 1-2 天内单独追加「现场速报」小节 |

## 核验原则（本仓库一贯口径）

1. **arXiv 号必须来自 arXiv/HF Papers 页面**或 API，不编造
2. **机构无法核验就写"未能核验"**，绝不猜测
3. **会议录用以 arXiv `comments` 字段或官方页为准**；"未标注录用" ≠ "未被录用"
4. 每条尽量附来源 URL，便于复核
