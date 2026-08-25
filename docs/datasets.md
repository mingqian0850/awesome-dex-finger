# 📊 数据集与基准

> 灵巧手/灵巧操作领域常用数据集与基准。arXiv 链接均已核实。

## 抓取数据集

| 数据集 | 机构 | 年份/会议 | 内容 | 链接 |
| --- | --- | --- | --- | --- |
| DexGraspNet | PKU EPIC | 2023 (ICRA) | 大规模灵巧抓取数据集：132 万+ 抓取、5355 个物体 × ShadowHand/Allegro；SDF 质量优化生成 | [arXiv:2210.02697](https://arxiv.org/abs/2210.02697) · [GitHub](https://github.com/PKU-EPIC/DexGraspNet) |
| DexGraspNet 2.0 | PKU EPIC | 2024 (CoRL) | 大规模合成杂乱场景生成式灵巧抓取，百万级物体实例，配套扩散抓取模型 | [arXiv:2410.23004](https://arxiv.org/abs/2410.23004) · [项目页](https://pku-epic.github.io/DexGraspNet2.0/) |
| DexYCB | NVIDIA | 2021 (CVPR) | 1000 个 RGB-D 视频序列、21 物体、20 受试者的人手抓取标注 | [arXiv:2104.04631](https://arxiv.org/abs/2104.04631) |

## 手-物交互数据集

| 数据集 | 机构 | 年份/会议 | 内容 | 链接 |
| --- | --- | --- | --- | --- |
| ARCTIC | ETH Zurich / MPI | 2023 (CVPR) | 双手-物体关节交互视频数据集，MANO 手网格 + SMPL 身体 + 物体关节 3D 标注 | [arXiv:2204.13662](https://arxiv.org/abs/2204.13662) · [GitHub](https://github.com/zc-alexfan/arctic) |
| OakInk | SJTU | 2022 (CVPR) | 大规模手-物交互知识库（真实捕获 + 合成增强） | [arXiv:2203.15709](https://arxiv.org/abs/2203.15709) |
| OakInk2 | SJTU / 穹彻智能 | 2024 (CVPR) | 双手复杂任务操作数据集 | [arXiv:2403.19417](https://arxiv.org/abs/2403.19417) |
| TACO | 多机构 | 2024 (CVPR) | 双手工具-动作-物体理解基准（网络视频），配套 TACO-RL 环境 | [arXiv:2401.08399](https://arxiv.org/abs/2401.08399) |

## 机器人操作数据集（预训练/评测）

| 数据集 | 机构 | 年份/会议 | 内容 | 链接 |
| --- | --- | --- | --- | --- |
| DROID | Stanford 等 | 2024 (RSS) | 76k 条真实演示轨迹、564 个场景的野外操作数据集 | [arXiv:2403.12945](https://arxiv.org/abs/2403.12945) |
| EgoDex | Apple | 2025 | 第一视角日常视频手物交互数据（MANO 轨迹），用于真实灵巧手训练 | [arXiv:2505.11709](https://arxiv.org/abs/2505.11709) · [GitHub](https://github.com/apple/ml-egodex) |
| DexCanvas | DEXROBOT | 2025 | 连接人类演示与机器人学习的灵巧操作数据集 | [arXiv:2510.15786](https://arxiv.org/abs/2510.15786) |

## 仿真与 RL 基准

| 基准 | 机构 | 内容 | 链接 |
| --- | --- | --- | --- |
| Bi-DexHands (DexterousHands) | PKU MARL | 20+ 双手灵巧操作任务（Isaac Gym）+ 人类演示 | [GitHub](https://github.com/PKU-MARL/DexterousHands) |
| VTDexManip | GIST AI Lab | 视觉-触觉预训练数据 + Isaac Gym 灵巧任务 | [GitHub](https://github.com/gist-ailab/VTDexManip) |
| ManiSkill2/3 | UCSD | 通用操作基准，含灵巧手任务 | [GitHub](https://github.com/mani-skill/ManiSkill) |
| ADROIT | UC Berkeley | Shadow Hand 4 任务 MuJoCo 基准 | [Farama/Gymnasium](https://robotics.farama.org/v1.2.1/envs/adroit_hand/) |
| mujoco_menagerie | Google DeepMind | MuJoCo 官方模型集（LEAP Hand、Allegro、Shadow Hand） | [GitHub](https://github.com/google-deepmind/mujoco_menagerie) |

> 💡 触觉数据集持续涌现，欢迎 PR 补充。
