# 🖐️ Awesome Dexterous Hand / 灵巧手资源大全

> 持续更新的灵巧手（Dexterous Hand / Dexterous Manipulation）领域资源仓库：SOTA 论文、开源硬件、开源软件、数据集与 Awesome 列表。

灵巧手是具身智能（Embodied AI）与人形机器人（Humanoid Robot）的核心执行部件。本仓库持续收集该领域的研究与开源生态，最新人工增量核验为 2026-10-08，覆盖：

- 📄 **SOTA 论文**：硬件设计、强化学习、模仿学习、遥操作、大模型驱动灵巧操作
- 🦾 **硬件平台**：商用灵巧手（Shadow、Allegro、因时、帕西尼等）与开源硬件（LEAP Hand、AmazingHand、BiDexHand 等）
- 💻 **开源软件**：仿真环境（Isaac Gym/Lab、MuJoCo）、RL 训练框架、遥操作系统
- 📊 **数据集与基准**：DexGraspNet、OakInk、ARCTIC、DexYCB 等
- ⭐ **Awesome 列表**：社区维护的相关资源导航

## 📑 目录导航

| 文档 | 内容 |
| --- | --- |
| [docs/papers.md](docs/papers.md) | SOTA 论文总表（硬件 / 学习与控制 / 数据集，按年份分组） |
| [docs/hardware.md](docs/hardware.md) | 灵巧手硬件平台盘点（商用 + 开源） |
| [docs/learning.md](docs/learning.md) | 学习与控制方法详解（RL / 模仿学习 / 遥操作 / VLA） |
| [docs/control-and-data-collection.md](docs/control-and-data-collection.md) | 控制方法与数据采集方法（遥操作 / 视频学习 / 仿真合成） |
| [docs/datasets.md](docs/datasets.md) | 数据集与基准平台 |
| [docs/open-source.md](docs/open-source.md) | 开源项目清单（硬件 / 仿真 / 软件） |
| [docs/latest-updates-2026h2.md](docs/latest-updates-2026h2.md) | 最新动态跟踪（2026-10-08 核验增量 + 10-05 与更早历史记录） |
| [docs/verification-2026-09.md](docs/verification-2026-09.md) | 论文核验附录（arXiv API 级核验：机构、会议录用、标题纠正） |
| [awesome-lists.md](awesome-lists.md) | 相关 Awesome 列表导航 |
| [scripts/](scripts/README.md) | 🛠️ 更新脚本（arXiv 论文扫描 + GitHub 数据刷新） |

## ✨ 快速一览（经典资源与近期增量）

> 详细内容见各文档。

### 🦾 代表性开源硬件
- [LEAP Hand V1](https://v1.leaphand.com/) — CMU 的 RSS 2023 四指灵巧手，16 个电机驱动关节；V2 腱驱动系列需按独立版本查看
- [BiDexHand](https://github.com/wengmister/BiDexHand) — 16-DoF 仿生灵巧手
- [AmazingHand](https://github.com/pollen-robotics/AmazingHand) — 8-DoF 四指手，内置舵机与并联机构、无拉索；软件 Apache-2.0，机械设计 CC BY 4.0

### 📄 代表性论文
- [LEAP Hand](https://arxiv.org/abs/2309.06440)（RSS 2023）· [Bi-DexHands](https://arxiv.org/abs/2206.08686)（NeurIPS 2022）· [DexMimicGen](https://arxiv.org/abs/2410.24185)（ICRA 2025）
- VLA 基础模型：[π0](https://arxiv.org/abs/2410.24164)（Physical Intelligence, 2024）· [GR00T N1](https://arxiv.org/abs/2503.14734)（NVIDIA, 2025）· [RDT-1B](https://arxiv.org/abs/2410.07864)（清华, ICLR 2025）· [DexVLA](https://arxiv.org/abs/2502.05855)（CoRL 2025）

### ⭐ 代表性 Awesome 列表
- [awesome-humanoid-manipulation](https://github.com/Tsunami-kun/awesome-humanoid-manipulation) — 人形/灵巧/双手操作论文合集（最对口）
- [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) — 机器人操作论文大全
- [Awesome-Dexterous-Hands](https://github.com/CyanHaze/Awesome-Dexterous-Hands) — 灵巧手方向清单

> ⚠️ 注意：网传 `kingchou007/Awesome-Dexterous-Manipulation` 链接已失效（repo 404），请勿引用。

### 📊 代表性数据集
- [DexGraspNet](https://pku-epic.github.io/DexGraspNet/)（132 万+ 抓取）· [DexGraspNet 2.0](https://pku-epic.github.io/DexGraspNet2.0/)（CoRL 2024）· [DROID](https://arxiv.org/abs/2403.12945)（76k 轨迹）· [EgoDex](https://arxiv.org/abs/2505.11709)（Apple, 2025）

## 🤝 贡献

欢迎通过 Issue / PR 补充遗漏的资源。格式规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📜 说明

- 本仓库为资源索引，所有内容版权归原作者所有，链接指向原始出处。
- 论文信息以 arXiv / 官方项目页为准；引用时请核对原文。

## License

MIT
