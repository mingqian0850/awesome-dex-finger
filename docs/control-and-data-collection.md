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

## 三、深度相机方案：历史与现状

"深度相机 → 手部姿态 → 重定向 → 控制"常被问及是否已过时，答案是**端到端管线属早期方法，但深度感知本身仍在进化**：

| 时期 | 状态 | 说明 |
| --- | --- | --- |
| 2012–2018 | **早期主流** | Leap Motion（2012）/Kinect/RealSense + 传统方法做手部跟踪，大量"深度→姿态→重定向"遥操作论文（2022 年 IEEE 仍有 Leap Motion 工作） |
| 2019–2023 | **RGB 反超** | MediaPipe 等纯 RGB 方法零硬件成本 + 深度学习精度，成为姿态估计主流（AnyTeleop 等框架的基础） |
| 2024–今 | **深度"换岗"** | 深度/点云嵌入三个仍在发展的环节：① 数据采集标配（DexCap/UMI 腕部 RealSense 点云，要度量 3D 与物体几何）；② RGB-D 手重建与手-物交互（HandRT 等）；③ 多模态融合（视觉+IMU+触觉，如 DFKI 2025 的视觉-触觉手-物位姿估计） |

**关键事实**：外置相机（含深度）在手-物操作中会被手与物体遮挡（RAPID Hand 2025 明确指出），因此遮挡下触觉阵列成为主力、深度做辅助；而"重定向"本身仍是活跃研究方向（CrossDex ICLR'25、Learning to Transfer Human Hand Skills 2025 等）。

**选型直觉**：纯手姿态 → RGB 基础模型；需要度量 3D/物体几何 → 深度/点云；遮挡接触操作 → 触觉为主、深度为辅。

---

## 四、2025-2026 前沿方法（SOTA 现状）

> 本节回答"现在最前沿的方法是什么"。内容基于 2026-08 调研，链接均已核实。

### 1. 手部感知：从"姿态估计"到"基础模型 + 3DGS + 多模态"

**RGB 手部基础模型（事实标准）**

| 模型 | 机构 | 年份 | 特点 | 链接 |
| --- | --- | --- | --- | --- |
| HaMeR | Meta (FAIR) | CVPR 2024 | 全 Transformer（ViT-H + MANO 解码器），in-the-wild 鲁棒标杆，EgoExo4D Hand Pose Challenge 冠军，开源 MIT | [arXiv:2312.05251](https://huggingface.co/papers/2312.05251) · [GitHub](https://github.com/geopavlakos/hamer) |
| WiLoR | Imperial College | CVPR 2025 | 端到端"定位+重建"，比 HaMeR 轻量、接近实时（Apple Silicon 可实时网格推理） | [arXiv:2409.12259](https://huggingface.co/papers/2409.12259) · [CVPR OA](https://openaccess.thecvf.com/content/CVPR2025/html/Potamias_WiLoR_End-to-end_3D_Hand_Localization_and_Reconstruction_in-the-wild_CVPR_2025_paper.html) |
| SMPLer-X / SMPLest-X | 上海AI Lab / SJTU | 2024 / 2025 | 全身（含手部）表达性姿态/形状基础模型，Scaling ViT | [SMPLest-X arXiv:2501.09782](https://arxiv.org/abs/2501.09782) · [项目页](http://caizhongang.com/projects/SMPLer-X/) |
| ReJSHand | — | 2025 | 实时手部姿态+网格重建（refined joint & skeleton features） | [arXiv:2503.05995](https://huggingface.co/papers/2503.05995) |
| Handy | Imperial College | CVPR 2023 | MANO 之外的高保真手部形状/外观统计模型 | [GitHub](https://github.com/rolpotamias/handy) |
| HaWoR | — | CVPR 2025 | 第一视角**世界坐标系**手部运动重建（SLAM+手姿态解耦），面向 XR/机器人 | [GitHub](https://github.com/ThunderVVV/HaWoR) |
| Dyn-HaMR | — | 2025 | 动态相机下的 4D 交互手部运动恢复（HaMeR 后续线） | [GitHub](https://github.com/ZhengdiYu/Dyn-HaMR) |
| GeoHand / DreamHand | — | 2026 | 几何先验（MoGe 深度 token）单目重建 / 视频扩散模型遮挡鲁棒手部恢复 | [GeoHand](https://ar5iv.labs.arxiv.org/html/2605.17354) · [DreamHand](https://arxiv.org/html/2608.20308v1) |
| MediaPipe Hands | Google | 工业基线 | 实时 2D/3D 关键点（Apple Silicon ~40fps），遥操作最常用组件 | [实测参考](https://github.com/flyingGH/hand-tracking-experiments) |

**手-物交互重建：进入 3DGS 时代**

| 方法 | 年份/会议 | 特点 | 链接 |
| --- | --- | --- | --- |
| HOLD | CVPR 2024 | 视频中类别无关的手+物 3D 重建（MPI） | [项目页](https://is.mpg.de/ps/en/projects/hold-inferring-3d-hand-and-object-shape-from-video) |
| HOISDF | CVPR 2024 | 全局 SDF 约束的 3D 手-物姿态估计 | [论文页](https://mlanthology.org/cvpr/2024/qi2024cvpr-hoisdf/) |
| BIGS | CVPR 2025 | 3DGS 双手类别无关交互重建 | [CVPR OA](https://openaccess.thecvf.com/content/CVPR2025/papers/On_BIGS_Bimanual_Category-agnostic_Interaction_Reconstruction_from_Monocular_Videos_via_3D_CVPR_2025_paper.pdf) |
| GHOST / ArGS | CVPR 2026 | 3DGS 快速类别无关 HOI 重建 / 单目铰接操纵阶段性 3DGS | [GHOST](https://www.openaccess.thecvf.com/content/CVPR2026F/html/Aboukhadra_GHOST_Fast_Category-Agnostic_Hand-Object_Interaction_Reconstruction_from_RGB_Videos_Using_CVPRF_2026_paper.html) · [ArGS](https://github.com/ru1ven/ARGS) |
| EasyHOI | CVPR 2025 | 用大规模基础模型在野外重建手-物交互 | [CVPR OA](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_EasyHOI_Unleashing_the_Power_of_Large_Models_for_Reconstructing_Hand-Object_CVPR_2025_paper.html) |
| CHOIR | 2026 | 接触感知的 4D 手-物交互重建 | [arXiv:2605.20992](https://ar5iv.labs.arxiv.org/html/2605.20992) |
| UniHOPE | 2025 | 统一"仅手部"与"手-物"姿态估计 | [arXiv:2503.13303](https://ar5iv.labs.arxiv.org/html/2503.13303) |
| EgoGrasp / HOPformer | 2026 | 第一视角世界坐标系手-物交互估计 / 野外第一视角 3D 手-物姿态 | [EgoGrasp](https://ar5iv.labs.arxiv.org/html/2601.01050) · [HOPformer](https://github.com/Sid2697/HOPformer) |
| HOT3D（数据集） | Meta | CVPR 2025 | Project Aria 第一视角手+物追踪数据集（公开） | [项目页](https://facebookresearch.github.io/hot3d/) · [arXiv:2411.19167](https://huggingface.co/buckets/huggingchat/papers-content/tree/2411/2411.19167.md) |
| H2O / AnyHand（数据集） | — | 2021 / 2026 | 第一视角双手-物 RGBD 数据集（6D 位姿）/ 大规模合成 RGB-D 手部数据集 | [H2O](https://www.openaccess.thecvf.com/content/ICCV2021/html/Kwon_H2O_Two_Hands_Manipulating_Objects_for_First_Person_Interaction_Recognition_ICCV_2021_paper.html) · [AnyHand](https://browse-export.arxiv.org/pdf/2603.25726) |
| HandOccNet | CVPR 2022 | 遮挡鲁棒 3D 手部网格估计经典基线 | [GitHub](https://github.com/henrycjh/HandOccNet) |

**多模态融合与触觉（遮挡下的"救命稻草"）**

| 方法 | 模态 | 年份 | 特点 | 链接 |
| --- | --- | --- | --- | --- |
| ViTaSCOPE | 视觉+触觉 | RSS 2025 | 视触隐式表示，in-hand 位姿+外接触点联合估计 | [arXiv:2506.12239](https://ui.adsabs.harvard.edu/abs/2025arXiv250612239L/abstract) |
| In-Hand Object Pose via Visual-Tactile Fusion | 视觉+触觉 | 2025 | 视触融合 in-hand 6D 位姿（DFKI） | [arXiv:2506.10787](https://arxiv.org/pdf/2506.10787) |
| AVI-HT / VIHand | 视觉+IMU | 2026 / ACM MM 2025 | 自适应视觉-IMU 融合 3D 手部追踪 | [AVI-HT](https://arxiv.org/pdf/2605.21714.pdf) · [VIHand](https://dl.acm.org/doi/10.1145/3746027.3758215) |
| GelSight Mini / DIGIT 360 | 触觉硬件 | 2024- | 商用"人分辨率"视触传感器（GelSight）/ Meta 模块化视触传感器 | [GelSight](https://www.gelsight.com/products/gelsightmini/) · [DIGIT 360](https://github.com/facebookresearch/digit360) |
| GelSLAM | 触觉 | 2025 | 触觉 SLAM：长时程 6DoF 物体位姿追踪 | [arXiv:2508.15990](https://ar5iv.labs.arxiv.org/html/2508.15990) |
| Reactive Diffusion Policy | 视觉+触觉策略 | 2025 | 慢-快视触策略（接触丰富操作） | [arXiv:2503.02881](https://arxiv.org/html/2503.02881) |
| 视触融合追踪 | 视觉+触觉 | 2025 | Science Robotics 封面：视触结合使追踪精度提升 94% | [报道](https://www.leaderobot.com/news/5106) |

**机器人侧应用事实标准（"单目 RGB 手部估计 + 重定向"闭环）**

- **AnyTeleop**：MediaPipe 手指关键点 + RGB 手腕姿态 + [dex-retargeting](https://github.com/dexsuite/dex-retargeting) 优化重定向（[arXiv:2307.04577](https://arxiv.org/abs/2307.04577)）
- **DexCap**：胸前 RGB-D（L515→D435）场景点云 + 手背 T265 SLAM + 电磁动捕手套（[GitHub](https://github.com/j96w/DexCap)）
- **EgoDex**：EPIC-KITCHENS 第一视角视频 → 人手姿态 → 灵巧手重定向 → 教师策略蒸馏（[GitHub](https://github.com/apple/ml-egodex)）
- **UniDex**（CVPR 2026）：第一视角人类视频驱动的通用灵巧手控制基础套件（[GitHub](https://github.com/unidex-ai/UniDex)）
- **EgoInfinity**：web-scale 4D 手-物数据引擎（[S2](https://www.semanticscholar.org/paper/EgoInfinity%3A-A-Web-Scale-4D-Hand-Object-Interaction-Wang-Ren/a65ce32514cdfede235cca1605b3b6fae98303c6)）
- **HaMeR 系视觉遥操作**：[hand-hamer-vision-teleop](https://github.com/craft-hand/hand-hamer-vision-teleop)；[Parse-Augment-Distill](https://ar5iv.labs.arxiv.org/html/2509.20286) 明确用 HaMeR 提取手部姿态做策略蒸馏
- **XR 遥操作**：[OpenTeach](https://mlanthology.org/corl/2024/iyer2024corl-open/)（CoRL 2024）、Unitree [televuer](https://github.com/unitreerobotics/televuer)

> ⚠️ 调研说明：网传独立手部模型 "ManoPose" 经 56 次搜索未能验证（同名 ManiPose 为人体姿态模型），请勿引用。

### 2. 控制：VLA 进入"灵巧手原生"时代

| 模型 | 机构 | 年份 | 说明 |
| --- | --- | --- | --- |
| [π0.5](https://arxiv.org/abs/2504.16054) | Physical Intelligence | 2025 | π0 升级版，开放世界泛化，开源实现 [openpi](https://github.com/Physical-Intelligence/openpi) |
| GR00T N1.5 | NVIDIA | 2025-2026 | N1 升级：Eagle 2.5 VLM + DiT flow matching 双系统 |
| [Helix](https://www.figure.ai/news/helix-02-bedroom-tidy) | Figure AI | 2025 | 快慢脑双系统 VLA，已进入 Helix 02 迭代 |
| [UniHM](https://mlanthology.org/iclr/2026/zhang2026iclr-unihm/) | — | ICLR 2026 | 统一灵巧手操作的 VLM 框架 |
| [RLDX-1](https://www.rlwrld.ai/en/rldx-1) | RLWRLD（韩国） | 2026 | "灵巧优先"（Dexterity-First）机器手基础模型，GTC Taipei 2026 发布 |

### 3. 数据采集系统：从"实验室"到"数据工厂"

| 系统 | 机构 | 年份 | 特点 | 链接 |
| --- | --- | --- | --- | --- |
| AnyTeleop v3 | UCSD/PKU | 2025 更新 | 视觉标记手部姿态通用遥操作，免专用硬件，仍是开源基线 | [arXiv HTML](https://arxiv.org/html/2307.04577v3) |
| Open-TeleVision | UCSD | CoRL 2024 | Quest 3 VR + 主动视觉反馈，跨洲际双臂+手采集，被宇树等采用 | [GitHub](https://github.com/OpenTeleVision/TeleVision) |
| UMI on Legs | Columbia/Stanford | 2025 | UMI 接口装轮式底盘，移动采集 | [GitHub](https://github.com/real-stanford/umi-on-legs) |
| Fast-UMI + FastUMI-100K | 上海AI实验室 | CoRL 2025 | 硬件无关 UMI + 10 万级开源 UMI 风格数据集 | [alphaXiv](https://www.alphaxiv.org/abs/2409.19499v2) · [FastUMI-100K](https://ar5iv.labs.arxiv.org/html/2510.08022) |
| DexCap | Stanford | RSS 2024 | 磁动捕手套 + 腕部动捕 + 点云，"人戴手套采集"路线开创者 | [项目页](https://dex-cap.github.io/) · [GitHub](https://github.com/j96w/dexcap/) |
| DexWild（DexCap 下一代） | DexCap 团队 | RSS 2026 | 户外/真实环境动捕采集 + 人机联合训练 | [HF Papers](https://huggingface.co/papers/2505.07813) |
| MILE | — | 2025-12 | **机械同构外骨骼** + 指尖视触觉，采集侧与部署手同构，策略零缝隙迁移 | [HF Papers](https://huggingface.co/papers/2512.00324) |
| HOMIE | 上海AI实验室 | 2025 | 同构外骨骼座舱 + 人形全身遥操作（loco-manipulation），开源 | [ar5iv](https://ar5iv.labs.arxiv.org/html/2502.13013) · [OpenHomie](https://github.com/InternRobotics/OpenHomie) |
| DOGlove | 清华 | RSS 2025 | 低成本开源**力反馈**动捕手套 | [项目页](https://do-glove.github.io/) |
| ExoStart | Google DeepMind | 2025 | 传感化外骨骼演示 + few-shot 高效学习 | [scirate](https://scirate.com/arxiv/2506.11775) |
| CaFe-TeleVision | — | 2025 | Open-TeleVision 粗到细、人体工学优化版 | [Semantic Scholar](https://www.semanticscholar.org/paper/CaFe-TeleVision%3A-A-Coarse-to-Fine-Teleoperation-for-Tang-Chen/5e303a1515045172e020ff570db2174cd354d529) |
| IntuitCap | — | 2025 | 60-DOF 上半身动捕系统，全身数据采集 | [IEEE](https://xplorestaging.ieee.org/document/11355263) |
| RealDexUMI | — | 2026 | 可穿戴 UMI：腕部相机 + 手套，免外部动捕与 SLAM（arXiv ID 未能独立验证，见项目页） | 见项目页 |

### 4. 触觉数据采集（视触融合）

| 系统 | 年份 | 特点 | 链接 |
| --- | --- | --- | --- |
| OpenTouch | 2025-12 | 大规模**全手触觉**数据：手部大面积触觉阵列被动接触采集 | [arXiv:2512.16842](https://arxiv.org/html/2512.16842) |
| AnyTouch | ICLR 2025 | 跨多种视触传感器（GelSight/Digit 等）的统一触觉表示预训练 | [GitHub](https://github.com/GeWu-Lab/AnyTouch) |
| AnyRotate | CoRL 2025 | 触觉合成数据 + sim-to-real 的手内旋转 | [PMLR](https://proceedings.mlr.press/v270/yang25c.html) |
| ManiFeel | 2025-2026 | 视触操作策略学习基准 | [Semantic Scholar](https://www.semanticscholar.org/paper/ManiFeel%3A-Benchmarking-and-Understanding-Policy-Luu-Zhou/a521740d5d3453564c165bd6d6f4927e0470b86e) |

### 5. 数据飞轮：大规模真机 + 合成 + 视频三线并行

- **真机数据飞轮（开源基准）**：AgiBot World Colosseo（百万级真机轨迹、217 任务、IROS 2025，[项目页](https://opendrivelab.com/AgiBot-World/)）；[AgiBot World 2026 世界模型数据集](https://www.agibot.com.cn/article/315/detail/167.html)（行业首个面向世界模型的具身数据集）
- **合成数据第二引擎**：NVIDIA GR00T N1.5 + [GR00T-Mimic 合成操作运动生成](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/transfer1/gr00t-mimic/inference.html) + [世界基础模型生成合成轨迹](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/) + R²D² 工作流；NVIDIA 将物理 AI 定义为"数据工厂"业务（NVIDIA×LG 共建）
- **VLA 反向重塑数据需求**：Figure Helix 用约 **1000 小时高质量遥操作数据**训出双系统 VLA（S7 慢语义 + S8 快动作）；[Project Go-Big](https://www.figure.ai/news/project-go-big) 用互联网视频预训练压缩真机数据需求；1X 设 [World Model Lab](https://www.1x.tech/discover/1x-world-model-lab)（"车队学习 > 制造"）；π0.5 走"部署即采集"商业数据飞轮
- **视频学习主流化**：[EgoDex](https://huggingface.co/papers/2505.11709)（ICLR 2026，数万小时 egocentric 视频预训练跨具身手模型）、[OSCAR](https://wuzy2115.github.io/oscar-project-page/)（CMU，骨架条件世界动作模型统一人类+机器人视频）、ViViDex（RSS 2024，第三人称视频）、DexMan（人类+生成视频联合学习）、DemoBot（第三人称视频学双手操作）、DexNDM（银河通用&清华，神经动力学模型从视频学习）

### 6. 前沿共识（2025-2026）

1. **手部感知默认栈 = RGB 基础模型（HaMeR/WiLoR）+ 腕部深度点云 + 指尖触觉**，单一传感器不再够用
2. **控制默认栈 = VLA 基础模型微调**（π0.5/GR00T N1.5/Helix），RL 退居"技能级"补充
3. **采集硬件 SOTA = 外骨骼/手套 + 视触融合**（MILE/DOGlove/DexWild 路线：采集装置与部署手同构、传感化、户外化）
4. **数据默认栈 = 合成（GR00T）+ 遥操作集群 + 视频学习三线并行**；"约千小时高质量遥操作 + 视频预训练"成为可复制配方（Helix 实证）
5. **触觉成为下一个"模态"**：Octopi-1.5 视触语言模型 + OpenTouch 全手触觉数据预示"触觉 LLM"方向

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
