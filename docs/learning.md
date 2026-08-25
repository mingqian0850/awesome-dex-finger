# 🧠 学习与控制方法详解

> 灵巧手/灵巧操作领域的学习与控制方法综述（截至 2025）。arXiv 链接均经核实；无法独立验证的条目只给项目页链接。

## 1. 强化学习 (RL) 与 Sim-to-Real

| 方法 | 机构 | 年份/会议 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| OpenAI Dactyl | OpenAI | 2018 | [Blog](https://openai.com/index/learning-dexterity/) | 里程碑：MuJoCo 中 PPO + 自动域随机化训练 Shadow Hand，首次实现灵巧手物体重定向的 sim-to-real |
| Solving Rubik's Cube with a Robot Hand | OpenAI | 2019 | [报道](https://www.technologyreview.com/2019/10/15/75292/a-robot-hand-taught-itself-to-solve-a-rubiks-cube-after-creating-its-own-training-regime) | 引入 Automatic Domain Randomization (ADR)，单/双手解魔方 |
| ADROIT | UC Berkeley | 2018 (RSS) | [arXiv:1709.10087](https://arxiv.org/abs/1709.10087) | Shadow Hand 4 任务 MuJoCo 基准 + DAPG 算法（RL + 演示初始化），至今仍是标准测试床 |
| Bi-DexHands | PKU MARL | 2022 (NeurIPS D&B) | [arXiv:2206.08686](https://arxiv.org/abs/2206.08686) · [GitHub](https://github.com/PKU-MARL/DexterousHands) | Isaac Gym 双臂灵巧手基准，20 个双手任务，H2O 框架用人类演示训练 |
| VTDexManip | GIST AI Lab | 2025 (ICLR) | [GitHub](https://github.com/gist-ailab/VTDexManip) | 视觉-触觉预训练 + 灵巧操作 RL 的数据集与基准 |
| ManiSkill2 / ManiSkill3 | UCSD | 2023 / 2025 | [GitHub](https://github.com/mani-skill/ManiSkill) | 通用操作基准（SAPIEN），含灵巧手任务（Trifinger 等），支持 RL 与模仿学习 |
| Isaac Gym / Isaac Lab | NVIDIA | 2022–2025 | [NVIDIA Blog](https://developer.nvidia.com/blog/spotlight-galbot-builds-a-large-scale-dexterous-hand-dataset-for-humanoid-robots-using-nvidia-isaac-sim) | 灵巧手 RL 训练的事实标准仿真栈，Isaac Lab 官方支持 Shadow/LEAP Hand 环境 |

## 2. 模仿学习与遥操作（数据采集）

| 方法 | 机构 | 年份/会议 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| AnyTeleop | UC San Diego | 2023 (RSS) | [arXiv:2307.04577](https://arxiv.org/abs/2307.04577) | 通用视觉遥操作：RGB 跟踪人手映射到任意臂+灵巧手，无需专用手套 |
| UMI (Universal Manipulation Interface) | Columbia | 2024 (RSS) | [arXiv:2402.10329](https://arxiv.org/abs/2402.10329) | 手持 GoPro"无机器人"演示采集，野外采集操作数据，配合 diffusion policy |
| ALOHA 2 | Stanford + Google DeepMind | 2024 | [项目页](https://aloha-2.github.io/) | 开源双臂移动操作平台（约 $20k），双臂模仿学习 |
| Open-TeleVision | UCSD / MIT | 2024 (CoRL) | [arXiv:2407.01512](https://arxiv.org/abs/2407.01512) · [GitHub](https://github.com/OpenTeleVision/TeleVision) | Vision Pro 沉浸式遥操作，支持跨洋远程双臂+灵巧手数据采集 |
| HumanPlus | Stanford | 2024 (RSS) | [arXiv:2406.10454](https://arxiv.org/abs/2406.10454) · [项目页](https://humanoid-ai.github.io/) | 人形机器人影子跟随遥操作 + 仿真 RL 训练闭环 |
| EgoDex | Apple | 2025 | [arXiv:2505.11709](https://arxiv.org/abs/2505.11709) · [GitHub](https://github.com/apple/ml-egodex) | 从第一视角日常视频学习灵巧操作，绕过专用遥操作设备 |
| Fast-UMI | — | 2024 | [arXiv:2409.19499](https://arxiv.org/abs/2409.19499) | 硬件无关、可扩展的 UMI 改进版 |
| OmniH2O | CMU/清华 | 2024 | [arXiv:2406.08858](https://arxiv.org/abs/2406.08858) | 全身人形遥操作 + RL，6-DOF 灵巧手复杂任务 |
| DexCap | 上交/清华 | 2024 | [arXiv:2403.07788](https://arxiv.org/abs/2403.07788) · [GitHub](https://github.com/j96w/DexCap) | 便携动捕手套 + 腕部点云相机，野外采集灵巧数据 |

## 3. 大模型 / VLA 与灵巧手结合

| 方法 | 机构 | 年份/会议 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| RT-2 | Google DeepMind | 2023 | [报道](https://www.qbitai.com/2023/07/72187.html) | 动作即文本 token 的 VLA 范式开创者（主要面向夹爪） |
| π0 | Physical Intelligence | 2024 | [arXiv:2410.24164](https://arxiv.org/abs/2410.24164) | Flow matching VLA，输出连续高维动作（双臂+灵巧手），叠衣服等灵巧任务 |
| GR00T N1 | NVIDIA | 2025 | [arXiv:2503.14734](https://arxiv.org/abs/2503.14734) | 开源人形机器人基础模型：VLM 大脑 + Diffusion Transformer 小脑，支持灵巧手动作 |
| RDT-1B | Tsinghua (thu-ml) | 2025 (ICLR) | [arXiv:2410.07864](https://arxiv.org/abs/2410.07864) · [项目页](https://rdt-robotics.github.io/rdt-robotics/) | 1.2B Diffusion Transformer，原生支持 128Hz 高频控制与 20+ DoF 双臂/灵巧手 |
| OpenVLA | Stanford / Google DeepMind | 2024 (CoRL) | [MLR](https://proceedings.mlr.press/v270/kim25c.html) | 开源 7B VLA 基线，广泛复用/微调 |
| DexVLA | — | 2025 (CoRL) | [arXiv:2502.05855](https://arxiv.org/abs/2502.05855) | VLM + plug-in diffusion expert，双臂灵巧平台零微调操作新物体 |
| DexGraspVLA | — | 2025 | [arXiv:2502.20900](https://arxiv.org/abs/2502.20900) | VLA 框架下的通用灵巧抓取 |

## 4. In-hand 灵巧操作代表性工作

| 方法 | 机构 | 年份/会议 | 链接 | 贡献 |
| --- | --- | --- | --- | --- |
| Dexterous Manipulation from Images | Google | 2023 (ICRA) | [arXiv:2212.09902](https://arxiv.org/abs/2212.09902) | 纯 RGB 图像真实世界灵巧 RL，6 任务约 70-100% 成功率 |
| UniDexGrasp / UniDexGrasp++ | PKU EPIC | 2023 (CVPR / ICCV) | [项目页](https://pku-epic.github.io/UniDexGrasp/) · [++ arXiv:2304.00464](https://arxiv.org/abs/2304.00464) | 通用灵巧抓取：多样抓取提议 + goal-conditioned 策略，sim-to-real 迁移 |
| DexPoint | 多机构 | 2022 | [arXiv:2211.09423](https://arxiv.org/abs/2211.09423) | 点云状态表征解决 sim-to-real 泛化 |
| Rotating without Seeing | — | 2023 (RSS) | [Semantic Scholar](https://www.semanticscholar.org/paper/Rotating-without-Seeing%3A-Towards-In-hand-Dexterity-Yin-Huang/ba38c19d132ec29a40e64bd3734bf4d6b0059637) | 仅靠触觉实现 Shadow Hand 的 in-hand 6D 旋转 |
| DexMimicGen | UT Austin | 2025 (ICRA) | [arXiv:2410.24185](https://arxiv.org/abs/2410.24185) · [项目页](https://rpl.cs.utexas.edu/publications/2025/05/19/jiang-icra25-dexmimicgen/) | 从少量人类演示自动生成大规模双臂灵巧数据 |
| LodeStar | Stanford | 2025 | [arXiv:2508.17547](https://arxiv.org/abs/2508.17547) | 合成数据增强实现长时程灵巧操作 |

## 5. 趋势总结

1. **从静态抓取走向动态 in-hand 操作**：研究重心从抓取位姿生成转向 in-hand 旋转、重定向与长程操作，强调对未见物体泛化。
2. **"仿真 → 数据 → 基础模型"三级流水线**：Isaac Gym/Lab/GR00T 大规模并行仿真 + 数据生成（DexGraspNet 2.0、DexMimicGen）+ 真实数据（DROID、EgoDex），最后 VLA 统一微调。
3. **VLA 动作表征拥抱灵巧手**：从"动作即文本 token"（RT-2）演进到 flow matching / diffusion 连续动作（π0、RDT-1B、GR00T N1），原生支持 16–24 DoF 高维灵巧手动作。
4. **视触融合兴起**：无视觉 in-hand 操作依赖触觉（Rotating without Seeing），视觉-触觉预训练成为新方向（VTDexManip）。
5. **数据飞轮加速闭合**：专用遥操作设备 → VR 沉浸式遥操作 → 无设备第一视角视频学习（EgoDex、HumanPlus），数据采集成本持续下降。

## 参考来源

- [arXiv:2307.04577 AnyTeleop](https://arxiv.org/abs/2307.04577)
- [arXiv:2402.10329 UMI](https://arxiv.org/abs/2402.10329)
- [arXiv:2410.24164 π0](https://arxiv.org/abs/2410.24164)
- [arXiv:2503.14734 GR00T N1](https://arxiv.org/abs/2503.14734)
