# 📄 SOTA 论文总表

> 按方向分类，年份倒序。arXiv 链接均经过核实；无法独立验证的条目只给项目页链接。完整展开见 [learning.md](learning.md) / [datasets.md](datasets.md) / [hardware.md](hardware.md)。

## 一、硬件设计与开源手

| 论文 | 机构 | 年份 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| Leap Hand V2 Advanced: Dexterous, Low-Cost Hybrid Rigid-Soft Hand | — | 2025 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11203038) | V2 进阶版，刚柔混合、更轻更强 |
| LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning | Stanford/CMU | 2023 (RSS 2024) | [arXiv:2309.06440](https://arxiv.org/abs/2309.06440) | 低成本 3D 打印拟人灵巧手，20 DOF 腱驱动，全套开源 |

## 二、强化学习与灵巧操作

| 论文 | 机构 | 年份 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| VTDexManip: Visual-Tactile Pre-training and RL | GIST AI Lab | 2025 (ICLR) | [GitHub](https://github.com/gist-ailab/VTDexManip) | 视觉-触觉预训练 + 灵巧操作 RL |
| Bi-DexHands: Towards Human-Level Bimanual Dexterous Manipulation with RL | PKU | 2022 (NeurIPS, TPAMI) | [arXiv:2206.08686](https://arxiv.org/abs/2206.08686) | 双手灵巧操作基准（Isaac Gym），20+ 任务 |
| ADROIT: Learning Dexterous Manipulation with DAPG | UC Berkeley | 2018 (RSS) | [arXiv:1709.10087](https://arxiv.org/abs/1709.10087) | Shadow Hand 灵巧操作基准 + DAPG |
| Learning Dexterous In-Hand Manipulation（Dactyl） | OpenAI | 2018 | [arXiv:1808.00177](https://arxiv.org/abs/1808.00177) | 开创性：Shadow Hand 手内旋转，RL + sim-to-real |
| Solving Rubik's Cube with a Robot Hand | OpenAI | 2019 | [Blog](https://openai.com/index/learning-dexterity/) | ADR 域随机化，单手解魔方 |

## 三、数据生成 / 模仿学习 / 遥操作

| 论文 | 机构 | 年份 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| AgiBot World Colosseo | 智元 AgiBot | 2025 | [arXiv:2503.06669](https://arxiv.org/abs/2503.06669) | 百万级真机灵巧操作数据集 + 数据采集平台 |
| ExoStart: Efficient Learning with Sensorized Exoskeleton Demonstrations | — | 2025 | [arXiv:2506.11775](https://arxiv.org/abs/2506.11775) | 外骨骼手套（复刻 DEX-EE 运动学）采集演示，高效灵巧学习 |
| EgoDex: Learning Dexterous Manipulation from Egocentric Video | Apple | 2025 | [arXiv:2505.11709](https://arxiv.org/abs/2505.11709) | 第一视角视频学习灵巧操作 |
| LodeStar: Long-horizon Dexterity via Synthetic Data Augmentation | Stanford | 2025 | [arXiv:2508.17547](https://arxiv.org/abs/2508.17547) | 合成数据增强实现长时程灵巧操作 |
| OmniH2O: Whole-Body Teleoperation and Learning | CMU/清华 | 2024 | [arXiv:2406.08858](https://arxiv.org/abs/2406.08858) | 全身人形遥操作 + RL，6-DOF 灵巧手操作 |
| DexCap: Portable Mocap Data Collection System | 上交/清华 | 2024 | [arXiv:2403.07788](https://arxiv.org/abs/2403.07788) | 便携动捕手套 + 腕部相机采集野外灵巧数据 |
| DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation | UT Austin | 2024 (ICRA 2025) | [arXiv:2410.24185](https://arxiv.org/abs/2410.24185) | 自动化生成双手灵巧操作模仿数据 |
| Fast-UMI: Scalable Hardware-Independent UMI | — | 2024 | [arXiv:2409.19499](https://arxiv.org/abs/2409.19499) | UMI 的硬件无关扩展 |
| UMI: Universal Manipulation Interface | Columbia | 2024 (RSS) | [arXiv:2402.10329](https://arxiv.org/abs/2402.10329) | 手持式野外数据采集 |
| Open-TeleVision | UCSD/MIT | 2024 (CoRL) | [arXiv:2407.01512](https://arxiv.org/abs/2407.01512) | Vision Pro 沉浸式遥操作 |
| HumanPlus | Stanford | 2024 (RSS) | [arXiv:2406.10454](https://arxiv.org/abs/2406.10454) | 人形机器人影子跟随遥操作 |
| AnyTeleop | UC San Diego | 2023 (RSS) | [arXiv:2307.04577](https://arxiv.org/abs/2307.04577) | 通用视觉遥操作，支持多种灵巧手 |
| Dexterous Functional Grasping | MIT/Stanford | 2023 (CoRL) | [arXiv:2312.02975](https://arxiv.org/abs/2312.02975) | 功能性抓取与工具使用策略学习 |
| DemoGrasp: Universal Dexterous Grasping from a Single Demonstration | — | 2025 | [arXiv:2509.22149](https://arxiv.org/abs/2509.22149) | 单演示即可泛化的灵巧抓取 |

## 四、基础模型 / VLA 与灵巧手

| 论文 | 机构 | 年份 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| DexVLA: VLM with Plug-In Diffusion Expert | — | 2025 (CoRL) | [arXiv:2502.05855](https://arxiv.org/abs/2502.05855) | 双臂灵巧零微调泛化 |
| DexGraspVLA: VLA Framework for General Dexterous Grasping | — | 2025 | [arXiv:2502.20900](https://arxiv.org/abs/2502.20900) | VLA 框架下的通用灵巧抓取 |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | NVIDIA | 2025 | [arXiv:2503.14734](https://arxiv.org/abs/2503.14734) | 开源人形基础模型，支持灵巧手双腕操作 |
| RDT-1B: Diffusion Transformer 双臂操作基础模型 | Tsinghua | 2025 (ICLR) | [arXiv:2410.07864](https://arxiv.org/abs/2410.07864) | 1.2B 参数，128Hz 高频控制 |
| π0: A Vision-Language-Action Flow Model | Physical Intelligence | 2024 | [arXiv:2410.24164](https://arxiv.org/abs/2410.24164) | 3.3B 流匹配 VLA，灵巧双手操作 |
| OpenVLA | Stanford/DeepMind | 2024 (CoRL) | [MLR](https://proceedings.mlr.press/v270/kim25c.html) | 开源 7B VLA 基线 |
| RT-2: Vision-Language-Action Model | Google DeepMind | 2023 | [报道](https://www.qbitai.com/2023/07/72187.html) | VLA 范式开创者 |

## 五、In-hand 灵巧操作

| 论文 | 机构 | 年份 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| AnyRotate: Gravity-Invariant In-Hand Rotation with Sim-to-Real Touch | — | 2024 (CoRL) | [arXiv:2405.07391](https://arxiv.org/abs/2405.07391) | 触觉驱动重力不变手内旋转，sim-to-real（Allegro） |
| Learning Visuotactile Skills with Two Multifingered Hands | 清华 | 2024 | [arXiv:2404.16823](https://arxiv.org/abs/2404.16823) | 双 Allegro 视觉-触觉技能学习 |
| UniDexGrasp++ | PKU EPIC | 2023 (ICCV) | [arXiv:2304.00464](https://arxiv.org/abs/2304.00464) | 几何感知课程 + 通用-专家迭代学习 |
| UniDexGrasp | PKU EPIC | 2023 (CVPR) | [项目页](https://pku-epic.github.io/UniDexGrasp/) | 通用灵巧抓取策略 |
| Rotating without Seeing | — | 2023 (RSS) | [Semantic Scholar](https://www.semanticscholar.org/paper/Rotating-without-Seeing%3A-Towards-In-hand-Dexterity-Yin-Huang/ba38c19d132ec29a40e64bd3734bf4d6b0059637) | 纯触觉 in-hand 6D 旋转 |
| Dexterous Manipulation from Images | Google | 2023 (ICRA) | [arXiv:2212.09902](https://arxiv.org/abs/2212.09902) | 纯视觉真实世界灵巧 RL |
| DexPoint | 多机构 | 2023 (CoRL) | [arXiv:2211.09423](https://arxiv.org/abs/2211.09423) | 点云表征泛化 |
| DexDeform | 清华等 | 2023 (ICLR) | [arXiv:2304.03223](https://arxiv.org/abs/2304.03223) | 人类演示 + 可微物理实现可变形物体灵巧操作 |

## 六、综述与反思

| 综述 | 年份 | 链接 |
| --- | --- | --- |
| The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey | 2025 | [arXiv:2507.11840](https://arxiv.org/abs/2507.11840) |
| Do Robots Really Need Anthropomorphic Hands? | 2025 | [arXiv:2508.05415](https://arxiv.org/abs/2508.05415) |
| A Review of the Research Status and Development Trends of Dexterous Hand Technology | — | [Semantic Scholar](https://www.semanticscholar.org/paper/A-Review-of-the-Research-Status-and-Development-of-Yan-Guo/7001358cecc2fa8f8370bcf3a46d942fd9320e6a) |
| Grasp Control of Dexterous Hands Based on Bibliometric Analysis: A Survey | 2025 | [Chinese J. Mechanical Engineering](https://link-hkg.springer.com/article/10.1186/s10033-025-01346-z) |
