# 🎮 灵巧手控制方法与数据采集方法

> 灵巧手落地两大核心问题：**怎么控制**、**数据从哪来**。本文梳理截至 2025 年的主流方案，链接均经核实。

---

## 一、灵巧手控制方法

### 1. 底层关节控制（硬件层）

| 方法 | 原理 | 代表硬件 | 适用场景 |
| --- | --- | --- | --- |
| 位置控制 | 关节角/腱长跟踪，最简单可靠 | 因时 RH56、Allegro | 日常操作、轨迹规划 |
| 力/力矩控制 | 关节力矩闭环，柔顺抓取 | 宇树力控手、Allegro 力矩版 | 易碎品、接触操作 |
| 阻抗/导纳控制 | 控制"刚度-阻尼"，人机安全交互 | OpenHand（模型无关阻抗） | 与人共融、未知环境 |
| 腱张力控制 | 腱驱动手的张力/位置混合控制 | Shadow Hand、LEAP Hand | 拟人手、高负载指尖力 |

### 2. 运动学与重定向（人手 → 机器手）

- **手部运动重定向（Retargeting）**：把人类手部姿态（MANO/动捕）映射到机器人手关节角，核心工具 [dexsuite/dex-retargeting](https://github.com/dexsuite/dex-retargeting)，支持 Shadow/Allegro/LEAP 等
- **逆运动学（IK）**：指尖目标位姿 → 关节角求解（如 LEAP V2 Advanced 官方 API 内置 IK）
- **主从映射**：手套/动捕设备直接做关节级主从跟随（Manus → LEAP Hand 官方支持，见 [Bidex_Manus_Teleop](https://github.com/leap-hand/Bidex_Manus_Teleop)）

### 3. 遥操作控制（人类在环）

| 方案 | 设备 | 特点 | 代表工作 |
| --- | --- | --- | --- |
| 数据手套 | Manus VR（工业级，支持 ROS2）、Dexmo、Rokoko Smartgloves | 精度高、低延迟；需佩戴设备 | [manus_ros2](https://github.com/iotdesignshop/manus_ros2) · LEAP + Manus 遥操作 |
| 视觉手部跟踪 | 普通 RGB 相机（MediaPipe ~40fps、WiLoR 离线网格） | 零设备、无需手套；精度受遮挡影响 | [AnyTeleop](https://arxiv.org/abs/2307.04577) · [NeuroMimic](https://github.com/flyingGH/NeuroMimic)（无标记遥操作 Shadow Hand） |
| VR 沉浸式遥操作 | Apple Vision Pro 等 | 主动视觉反馈、"转头看"机器人视角，支持跨洋 | [Open-TeleVision](https://arxiv.org/abs/2407.01512) |
| 外骨骼手套 | 机械同构外骨骼 | 传感器化演示 + 力反馈；运动学天然对齐机器人手 | [ExoStart](https://arxiv.org/abs/2506.11775) · [MILE](https://scirate.com/arxiv/2512.00324) |
| 影子跟随 | RGB 相机 + 人形机器人 | 人直接做动作，机器人"影子式"复现 | [HumanPlus](https://arxiv.org/abs/2406.10454) |

### 4. 自主控制（学习策略）

| 方法 | 说明 | 代表工作 |
| --- | --- | --- |
| 强化学习（RL） | PPO/SAC 在 Isaac Gym/Lab 大规模并行训练，域随机化迁移真机 | [Dactyl/ADR](https://openai.com/index/learning-dexterity/) · [Bi-DexHands](https://arxiv.org/abs/2206.08686) |
| 演示初始化 RL | 人类演示初始化 + RL 微调，解决稀疏奖励 | [ADROIT/DAPG](https://arxiv.org/abs/1709.10087) |
| 模仿学习 | 行为克隆（BC）、Diffusion Policy、ACT | UMI/DexMimicGen 训练管线 |
| VLA 基础模型 | 语言/视觉指令 → 灵巧手动作流 | [π0](https://arxiv.org/abs/2410.24164) · [GR00T N1](https://arxiv.org/abs/2503.14734) · [RDT-1B](https://arxiv.org/abs/2410.07864) · [DexVLA](https://arxiv.org/abs/2502.05855) |
| 触觉闭环控制 | 无视觉，纯触觉反馈驱动 in-hand 操作 | [Rotating without Seeing](https://www.semanticscholar.org/paper/Rotating-without-Seeing%3A-Towards-In-hand-Dexterity-Yin-Huang/ba38c19d132ec29a40e64bd3734bf4d6b0059637) · [AnyRotate](https://arxiv.org/abs/2405.07391) |

### 5. 仿真控制

| 仿真栈 | 特点 | 链接 |
| --- | --- | --- |
| Isaac Gym / Isaac Lab | 大规模并行 RL 事实标准，官方支持 Shadow/LEAP Hand | [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) |
| MuJoCo / MJX | 高保真物理 + GPU 加速，官方模型集含 4 款灵巧手 | [mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie) |
| SAPIEN / ManiSkill | 通用操作基准，含灵巧手任务 | [ManiSkill](https://github.com/mani-skill/ManiSkill) |

---

## 二、灵巧手数据采集方法

### 1. 遥操作采集（真实真机数据，质量最高）

| 方案 | 设备/系统 | 特点 | 代表工作 |
| --- | --- | --- | --- |
| 手套动捕 | Manus VR、Dexmo、Rokoko | 高精度手部轨迹，工业标准 | LEAP + Manus、DexCap |
| 视觉遥操作 | RGB 相机（AnyTeleop） | 免手套、低成本，可远程 | [AnyTeleop](https://arxiv.org/abs/2307.04577) |
| VR 遥操作 | Vision Pro（Open-TeleVision） | 沉浸式、可跨洋采集 | [Open-TeleVision](https://arxiv.org/abs/2407.01512) |
| 便携动捕 | 手套 + 腕部点云相机（DexCap） | 野外可穿戴，数据规模大 | [DexCap](https://arxiv.org/abs/2403.07788) · [GitHub](https://github.com/j96w/DexCap) |
| 外骨骼采集 | MILE、ExoStart | 传感器化 + 运动学对齐 | [MILE](https://scirate.com/arxiv/2512.00324) · [ExoStart](https://arxiv.org/abs/2506.11775) |
| 双臂采集平台 | ALOHA 2（约 $20k 开源） | 双臂 + 灵巧手扩展，标准化采集 | [ALOHA 2](https://aloha-2.github.io/) |
| 手持采集 | UMI（GoPro + 腕部夹具） | "无机器人"野外采集，人手直接示范 | [UMI](https://arxiv.org/abs/2402.10329) · [Fast-UMI](https://arxiv.org/abs/2409.19499) |

### 2. 无设备采集（视频学习，规模最大）

| 方案 | 原理 | 代表工作 |
| --- | --- | --- |
| 第一视角视频 | 佩戴相机日常活动 → MANO 手部轨迹自动提取 → 训练策略 | [EgoDex](https://arxiv.org/abs/2505.11709)（Apple） |
| 互联网视频 | 网络视频理解工具使用（TACO 等） | [TACO](https://arxiv.org/abs/2401.08399) |

### 3. 仿真/合成数据生成（规模最大、零成本）

| 方案 | 原理 | 代表工作 |
| --- | --- | --- |
| 抓取姿态合成 | SDF 质量优化 / 扩散模型生成百万级抓取 | [DexGraspNet](https://arxiv.org/abs/2210.02697) · [DexGraspNet 2.0](https://arxiv.org/abs/2410.23004) |
| 任务数据扩增 | 少量人类演示自动扩增 → 大规模任务数据 | [DexMimicGen](https://arxiv.org/abs/2410.24185) |
| 合成运动管线 | LLM/程序化生成动作 + 物理仿真验证（Isaac GR00T） | [NVIDIA 合成管线](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/) |
| 触觉数据 | 视觉-触觉预训练数据 | [VTDexManip](https://github.com/gist-ailab/VTDexManip) |

### 4. 大型真实数据集（可直接使用）

| 数据集 | 规模 | 采集方式 | 链接 |
| --- | --- | --- | --- |
| AgiBot World | 百万级真机操作数据 | 遥操作集群 + 规模化采集 | [OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World) |
| DROID | 76k 轨迹 / 564 场景 | 野外遥操作 | [arXiv:2403.12945](https://arxiv.org/abs/2403.12945) |
| DexCanvas | 灵巧操作数据 | 遥操作 + 策略评测 | [arXiv:2510.15786](https://arxiv.org/abs/2510.15786) |
| OakInk2 | 双手复杂任务 | 动捕 + 多相机 | [arXiv:2403.19417](https://arxiv.org/abs/2403.19417) |

---

## 四、深度相机方案：历史与现状

"深度相机 → 手部姿态 → 重定向 → 控制"常被问及是否已过时，答案是**端到端管线属早期方法，但深度感知本身仍在进化**：

| 时期 | 状态 | 说明 |
| --- | --- | --- |
| 2012–2018 | **早期主流** | Leap Motion（2012）/Kinect/RealSense + 传统方法做手部跟踪，大量"深度→姿态→重定向"遥操作论文（2022 年 IEEE 仍有 Leap Motion 工作） |
| 2019–2023 | **RGB 反超** | MediaPipe 等纯 RGB 方法零硬件成本 + 深度学习精度，成为姿态估计主流（AnyTeleop 等框架的基础） |
| 2024–今 | **深度"换岗"** | 深度/点云嵌入三个仍在发展的环节：① 数据采集标配（DexCap/UMI 腕部 RealSense 点云，要度量 3D 与物体几何）；② RGB-D 手重建与手-物交互（HandRT 等）；③ 多模态融合（视觉+IMU+触觉，如 DFKI 2025 的视觉-触觉手-物位姿估计） |

**关键事实**：外置相机（含深度）在手-物操作中会被手与物体遮挡（RAPID Hand 2025 明确指出），因此遮挡下触觉阵列成为主力、深度做辅助；而"重定向"本身仍是活跃研究方向（CrossDex ICLR'25、Learning to Transfer Human Hand Skills 2025 等）。

**选型直觉**：纯手姿态 → RGB 基础模型；需要度量 3D/物体几何 → 深度/点云；遮挡接触操作 → 触觉为主、深度为辅。

---

## 五、方案选择建议

| 你的场景 | 推荐组合 |
| --- | --- |
| **科研快速验证** | Isaac Gym/Lab + LEAP/Allegro 仿真 → RL（PPO）或 DexMimicGen 扩增 → sim-to-real |
| **低成本真机数据** | AnyTeleop（视觉遥操作，零设备）+ 开源手（LEAP Hand ~$2k） |
| **高质量工业数据** | Manus 手套 + DexCap 式便携动捕 + ALOHA 2 双臂平台 |
| **大规模野外数据** | EgoDex 式第一视角视频学习（无设备） |
| **产品化** | 遥操作数据集群（智元/银河通用模式）+ VLA 基础模型微调 |
| **触觉相关研究** | 帕西尼 DexH13 / 宇树 Dex3-1 + AnyRotate 式触觉闭环 |

## 参考来源

- [AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System](https://arxiv.org/abs/2307.04577)
- [DexCap: Scalable and Portable Mocap Data Collection System](https://arxiv.org/abs/2403.07788)
- [EgoDex: Learning Dexterous Manipulation from Egocentric Video](https://arxiv.org/abs/2505.11709)
- [NVIDIA: Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)
