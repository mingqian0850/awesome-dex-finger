# 💻 开源项目清单

> 灵巧手领域开源项目：开源硬件、仿真环境、算法框架、数据采集。
> Star 数为 2026-08 调研时点 GitHub API 实时值；许可证为 repo 根 LICENSE（`自定义` = 有 LICENSE 但非标准 SPDX）。

## 一、开源硬件（可 3D 打印 / 开源设计）

| 项目 | Stars | 许可证 | 特点 | 链接 |
| --- | --- | --- | --- | --- |
| AmazingHand (AH!) | 2299 | Apache-2.0 | 8-DoF 低成本 3D 打印灵巧手，配套 Arduino/ROS 代码，社区活跃 | [pollen-robotics/AmazingHand](https://github.com/pollen-robotics/AmazingHand) |
| Aero Hand Open | 916 | 自定义 | 可在家组装的 3D 打印灵巧手，舵机驱动，厂商同步售卖套件 | [TetherIA/aero-hand-open](https://github.com/TetherIA/aero-hand-open) |
| HOPEJr | 820 | 自定义 | 开源 DIY 人形机器人整机（含灵巧手方案） | [TheRobotStudio/HOPEJr](https://github.com/TheRobotStudio/HOPEJr) |
| BiDexHand | 249 | MIT | 16-DoF 仿生双手，开源机械设计 + 驱动 | [wengmister/BiDexHand](https://github.com/wengmister/BiDexHand) |
| RUKA / RUKA-v2 | 200 / 24 | MIT | 腱驱动开源灵巧手（ICRA 2025），"用学习指导手设计"；v2 增加手腕与指外展 | [ruka-hand/RUKA](https://github.com/ruka-hand/RUKA) |
| LEAP Hand (API/Sim) | 172 / 204 | MIT | 低成本 16-DOF 腱驱动拟人手（RSS 2023），CAD 全开源，支持 Manus 手套遥操作 | [leap-hand/LEAP_Hand_API](https://github.com/leap-hand/LEAP_Hand_API) · [LEAP_Hand_Sim](https://github.com/leap-hand/LEAP_Hand_Sim) |
| Wuji Hand (武机科技) | 196 | Apache-2.0 | 手内重定向 PPO 训练 + sim-to-real 部署全套代码（手本体为商业产品） | [wuji-technology/wuji-mjlab](https://github.com/wuji-technology/wuji-mjlab) |
| DexHand | 55 | 自定义 | 开源 DIY 人形手：机械图纸、BOM、装配教程；ROS2 见 dexhand_ros2_meta | [iotdesignshop/dexhand-mechanical-build](https://github.com/iotdesignshop/dexhand-mechanical-build) |
| RAPID Hand | 52 | 自定义 | 中山大学：低成本、感知集成、面向通用机器人自主性的灵巧操作平台 | [SYSU-RoboticsLab/RAPID-Hand](https://github.com/SYSU-RoboticsLab/RAPID-Hand) |
| Tactile SoftHand-A | 31 | 自定义 | 3D 打印、触觉、高欠驱动拟人软手（拮抗腱机构） | [HaoranLi-Data/Tactile_SoftHand_A](https://github.com/HaoranLi-Data/Tactile_SoftHand_A) |
| Shadow Robot 系列 | — | BSD-3 / GPL-2.0 | 硬件闭源；ROS 驱动、URDF、文档开源（sr_common、sr-ros-interface 等） | [shadow-robot org](https://github.com/shadow-robot) |
| Festo BionicSoftHand | — | 未知 | 气动软体手官方代码仓库；硬件不开源 | [Festo-se/festo-bionicsofthand-main](https://github.com/Festo-se/festo-bionicsofthand-main) |

## 二、仿真与模型文件

| 项目 | Stars | 内容 | 链接 |
| --- | --- | --- | --- |
| mujoco_menagerie | 3867 | MuJoCo 高质量模型合集：shadow_hand、shadow_dexee、leap_hand、aero_hand 等 | [google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie) |
| IsaacGymEnvs | 2952 | Isaac Gym 官方环境，含 ShadowHand OpenAI 任务（取物/重定向/压块等） | [isaac-sim/IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) |
| genie_sim | 1353 | 智元机器人仿真平台（支持灵巧手） | [AgibotTech/genie_sim](https://github.com/AgibotTech/genie_sim) |
| DexterousHands (Bi-DexHands) | 1084 | Isaac Gym 双灵巧手操作环境（NeurIPS 2022） | [PKU-MARL/DexterousHands](https://github.com/PKU-MARL/DexterousHands) |
| dex-urdf | 377 | 多款灵巧手（Shadow/LEAP/DexHand 等）统一 URDF 资源库 | [dexsuite/dex-urdf](https://github.com/dexsuite/dex-urdf) |
| Adroit | 80 | ShadowHand/ADROIT 的 MuJoCo 模型与环境（手内操作、开门等） | [vikashplus/Adroit](https://github.com/vikashplus/Adroit) |
| mjlab_hand | 48 | 基于 mjlab（Isaac Lab 平替）的灵巧手操作任务 | [ruoyiqiao/mjlab_hand](https://github.com/ruoyiqiao/mjlab_hand) |
| shadowhand-gym | 24 | Shadow Hand Gym 环境封装 | [szahlner/shadowhand-gym](https://github.com/szahlner/shadowhand-gym) |
| Gymnasium-Robotics | — | Farama 官方 Shadow Dexterous Hand 环境（HandReach/HandManipulate） | [robotics.farama.org](https://robotics.farama.org/envs/shadow_dexterous_hand/) |

## 三、算法框架 / 数据采集 / 数据集代码

| 项目 | Stars | 内容 | 链接 |
| --- | --- | --- | --- |
| AgiBot-World | 3157 | 智元百万级真机操作数据集（IROS 2025） | [OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World) |
| Humanoid-Gym | 2072 | 人形机器人端到端 RL 训练框架（零样本 sim2real，含灵巧手场景） | [roboterax/Humanoid-Gym](https://github.com/roboterax/Humanoid-Gym) |
| xr_teleoperate | 1630 | 宇树 XR 遥操作 | [unitreerobotics/xr_teleoperate](https://github.com/unitreerobotics/xr_teleoperate) |
| unitree_lerobot | 751 | 宇树 × LeRobot 灵巧手学习 | [unitreerobotics/unitree_lerobot](https://github.com/unitreerobotics/unitree_lerobot) |
| DexGraspNet | 461 | 大规模灵巧抓取数据集与抓取生成算法（ShadowHand + Isaac Gym） | [PKU-EPIC/DexGraspNet](https://github.com/PKU-EPIC/DexGraspNet) |
| DexCap | 387 | RSS 2024 可穿戴动捕数据采集系统（斯坦福） | [j96w/DexCap](https://github.com/j96w/DexCap) |
| hand_dapg | 326 | DAPG（RSS 2018，ShadowHand 旋转/取物）官方代码 | [aravindr93/hand_dapg](https://github.com/aravindr93/hand_dapg) |
| GenDexGrasp | 204 | 跨机器人灵巧抓取泛化（ShadowHand/Allegro/LEAP 等） | [tengyu-liu/GenDexGrasp](https://github.com/tengyu-liu/GenDexGrasp) |
| dexmv-sim | 200 | DexMV：从人类视频学习灵巧操作（ShadowHand 仿真） | [yzqin/dexmv-sim](https://github.com/yzqin/dexmv-sim) |
| UniDex | 176 | CVPR 2026 通用灵巧手控制基础套件 | [unidex-ai/UniDex](https://github.com/unidex-ai/UniDex) |
| dex-hand-teleop | 159 | 单手手部动捕到多手模型的遥操作重定向 | [yzqin/dex-hand-teleop](https://github.com/yzqin/dex-hand-teleop) |
| dex-retargeting | — | 人手运动到机器人手的运动重定向 | [dexsuite/dex-retargeting](https://github.com/dexsuite/dex-retargeting) |
| hamer | — | HaMeR 手部网格恢复基础模型（Meta, CVPR 2024, MIT） | [geopavlakos/hamer](https://github.com/geopavlakos/hamer) |
| wilor | — | WiLoR 端到端 3D 手部定位与重建（CVPR 2025） | [rolpotamias/wilor](https://github.com/rolpotamias/wilor) |
| digit360 | — | Meta 高精度模块化视触传感器（开源） | [facebookresearch/digit360](https://github.com/facebookresearch/digit360) |
| OpenHomie | — | 同构外骨骼座舱 + 人形全身遥操作（上海AI实验室） | [InternRobotics/OpenHomie](https://github.com/InternRobotics/OpenHomie) |
| DOGlove | — | 低成本开源力反馈动捕手套（清华, RSS 2025），代码见项目页 | [项目页](https://do-glove.github.io/) |

## 四、中文社区开源项目

| 机构 | 项目 | 说明 |
| --- | --- | --- |
| 智元 AgiBot | [agibot_x1_hardware](https://github.com/AgibotTech/agibot_x1_hardware)（1072★）· [x1_train](https://github.com/AgibotTech/agibot_x1_train)（1696★）· [x1_infer](https://github.com/AgibotTech/agibot_x1_infer)（1834★）· [genie_sim](https://github.com/AgibotTech/genie_sim)（1353★） | X1 人形机器人整机硬件设计开源（含灵巧手），训练/推理/仿真全链路 |
| 宇树 Unitree | [unitree_ros](https://github.com/unitreerobotics/unitree_ros)（1534★，含灵巧手 URDF/驱动）· [unitree_lerobot](https://github.com/unitreerobotics/unitree_lerobot)（751★）· [xr_teleoperate](https://github.com/unitreerobotics/xr_teleoperate)（1630★）· [dfx_inspire_service](https://github.com/unitreerobotics/dfx_inspire_service)（52★，Inspire RH56DFX 驱动） | G1 灵巧手（Inspire RH56DFX）SDK/驱动/仿真开源，硬件商业 |
| 因时 Inspire（社区） | [correlllab/rh56_controller](https://github.com/correlllab/rh56_controller)（20★）· [Sentdex/inspire_hands](https://github.com/Sentdex/inspire_hands)（63★） | RH56 系列驱动/控制器（社区维护），硬件闭源 |
| 灵心巧手 LinkerHand | [linkerhand-urdf](https://github.com/linker-bot/linkerhand-urdf)（59★，Apache-2.0） | 灵巧手 URDF 开源，硬件闭源 |
| DexRobot | [dexrobot_mujoco](https://github.com/DexRobot/dexrobot_mujoco)（60★）· [dexrobot_isaac](https://github.com/DexRobot/dexrobot_isaac)（23★）· [dexrobot_urdf](https://github.com/DexRobot/dexrobot_urdf)（11★） | URDF/仿真/Isaac Gym 训练环境开源，硬件商业 |
| 其他 | [Multi-Finger-Dexterous-Manipulator](https://github.com/zhangdong-cheku/Multi-Finger-Dexterous-Manipulator)（35★，MIT）· [BrainCo-Revo2-Dex-Retargeting](https://github.com/Bobyue0118/BrainCo-Revo2-Dex-Retargeting)（35★，MIT） | 社区个人开源 |

> 💡 帕西尼（PaXini）等厂商暂未发现公开 GitHub 仓库。
