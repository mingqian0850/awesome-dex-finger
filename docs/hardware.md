# 🦾 灵巧手硬件平台盘点

> 覆盖商用/在售灵巧手与代表性开源硬件。参数为调研时点（2026-08）媒体/社区口径，最终以官方规格书为准。

## 一、国际品牌

| 名称 | 厂商 | 自由度 | 驱动方式 | 特点 | 链接 |
| --- | --- | --- | --- | --- | --- |
| Shadow Dexterous Hand | Shadow Robot（英国） | 20 DOF / 24 关节 | 腱驱动（早期气动 Air Muscle，现电机） | 最经典拟人灵巧手，科研界事实标准，可配 BioTac 触觉指尖；约 $100k 级 | [robotsguide](https://robotsguide.com/robots/shadow) · [规格 PDF](https://shadowrobot.com/wp-content/uploads/2025/09/shadow_dexterous_hand_e_technical_specification.pdf) |
| DEX-EE | Shadow Robot + 布里斯托大学 | 12 DOF | 腱驱动 | Shadow 低成本版，面向遥操作与 RL 研究，指尖力约 8-18 N | [originofbots](https://www.originofbots.com/humanoid-robot-hand/dex-ee-dexterous-hand-by-shadow-robot-company-robot-hand-specifications) |
| Allegro Hand V4/V5 | Wonik Robotics（韩国） | 16 DOF（四指） | 内置直流电机 + 齿轮 | 学术界使用最广的手之一，ROS 生态成熟；约 $20k 量级 | [Wonik 官网](https://www.wonikrobotics.com/robotics-hand) |
| Tesla Optimus 手 | 特斯拉 | 22 DOF（v2 升级版） | 腱绳驱动 + 前臂电机舱、液冷 | 2024-11 展示升级版（演示为遥操作），公开 5 份灵巧手专利 | [electrek](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/) |
| Figure 02 手 | Figure AI | 约 16 DOF（媒体口径） | 电机/腱（未完全公开） | 第四代手部装置，已进入宝马工厂 | [sina](https://finance.sina.cn/2024-08-09/detail-inchywqp7825307.d.html) |
| Bionic Soft Hand | Festo（德国） | 多指柔性 | 气动柔性 | 气动软体灵巧手 | [GitHub](https://github.com/Festo-se/festo-bionicsofthand-main) |

## 二、国内厂商

| 名称 | 厂商 | 自由度 | 驱动方式 | 特点 | 链接 |
| --- | --- | --- | --- | --- | --- |
| RH56 系列 | 因时机器人（北京） | 6 主动 DOF / 12 关节 | 微型直线舵机/齿轮 | 国产科研主流五指手，适配宇树 G1/H1 | [产品页](https://www.inspire-robots.com/product/14.html) · [手册](https://en.inspire-robots.com/wp-content/uploads/2024/02/INSPIRE-ROBOTS-THE-DEXTEROUS-HAND-RH56-SERIES-USER-MANUAL.pdf) |
| Dex3-1 / Dex5 | 宇树 Unitree | Dex5: 20 DOF、94 触觉触点 | 电机直驱 + 力控 | Dex3-1 三指力控可选触觉/RGB 相机版；Dex5 为 2025 新品 | [Dex3-1](https://www.unitree.com/cn/Dex3-1) · [Dex5 报道](https://www.163.com/dy/article/JS2Q5RC50511B8LM.html) |
| DexH13 | 帕西尼 PaXini（深圳） | 13 DOF（五指） | 电机 + 多维触觉 | 多维触觉（力/温度/材质），2025 年获比亚迪超亿元投资 | [paxini.com](https://www.paxini.com/cn/dex/gen2) |
| OmniHand | 智元机器人（稚晖君团队） | 高自由度 | 电机 | 2025 系列，灵动款 <¥1 万，配合 AgiBot World 数据集 | [agibot.com.cn](https://www.agibot.com.cn/article/188/detail/33.html) |
| XHAND 1 / PRO | 星动纪元（Robot Era） | 12 / 21 DOF | 全主动全直驱 | 触觉（温度/压力），PRO 为 21 DOF 全直驱 | [产品页](https://www.pnprobotics.com/en/sys-pd/78.html) |
| 银河通用灵巧手 | 银河通用 Galbot（北京） | 22 DOF / 30+ 电机（媒体口径） | 电机 | 2025-11 联合清华发布灵巧手模型 DexNDM，手掌任意朝向手内旋转 | [qbitai](https://www.qbitai.com/2025/11/352819.html) |
| Astribot S1 手 | 星尘智能（深圳） | 高自由度 | 绳驱（腱绳） | S1 人形机器人绳驱 AI 灵巧手，家务操作演示 | [robothub](https://www.robothub.app/zh/robots/astribot-s1) |
| TRX-Hand | 腾讯 Robotics X | 五指高自由度 | 电机 + 触觉 | 2023 自研灵巧手与机械臂，调酒演示 | [ithome](https://next.ithome.com/archiver/688/887.htm) |
| 中科硅纪灵巧手 | Inspirit 中科硅纪（南京） | 高自由度行业级 | 电机 + 触觉 | 行业级量产，向福莱新材采购 20 万套触觉传感器 | [36kr](https://eu.36kr.com/zh/p/3582198041312137) |
| OHand / BrainRobotics | 傲意 OYMotion / 强脑 BrainCo | 多自由度 | 肌电 sEMG + 电机 | 医疗级智能仿生手（假肢方向），同步推出机器人灵巧手 | [oymotion.com](https://www.oymotion.com/product16) |

## 三、开源硬件（详见 [open-source.md](open-source.md)）

| 名称 | 特点 | 链接 |
| --- | --- | --- |
| LEAP Hand (V1/V2 Advanced) | 约 $2000、16-DOF 腱驱、3D 打印全开源，学术圈标准配置 | [leaphand.com](https://www.leaphand.com/) |
| AmazingHand | 8-DoF 低成本 3D 打印手（Apache-2.0），2299★ | [pollen-robotics/AmazingHand](https://github.com/pollen-robotics/AmazingHand) |
| Aero Hand Open | 可在家组装的 3D 打印手，916★ | [TetherIA/aero-hand-open](https://github.com/TetherIA/aero-hand-open) |
| BiDexHand | 16-DoF 仿生双手（MIT），249★ | [wengmister/BiDexHand](https://github.com/wengmister/BiDexHand) |
| RUKA | 腱驱动开源手（ICRA 2025），200★ | [ruka-hand/RUKA](https://github.com/ruka-hand/RUKA) |

## 四、技术趋势

1. **腱驱 vs 全直驱双轨并行**：高性能路线延续腱绳驱动（Optimus 前臂动力舱专利、Shadow、Astribot 绳驱）；量产路线转向全直驱/齿轮直驱（XHAND1 12 全主动全直驱、因时微型舵机、宇树力控）
2. **自由度与触觉内卷**：DOF 从 6→12→20→22 快速爬升；多维触觉（力/温度/材质）从选配变标配；高盛调研指出**数据、寿命、散热**是行业三大瓶颈
3. **价格陡降与开源化**：Shadow $100k 级 → LEAP $2k → 智元 OmniHand <¥1 万；开源硬件 + 开源数据（AgiBot World）重构研究生态
4. **算法侧三线融合**：仿真 RL → 遥操作数据采集 → VLA 大模型；手内旋转（DexNDM）等复杂技能开始被通用模型化
5. **工程化优先**：液冷散热、触觉传感器国产量产、高载荷方案；行业讨论聚焦"成本/性能/可靠性不可能三角"

## 参考来源

- [Dexterous Robot Hand Comparison: Allegro vs LEAP vs Inspire](https://www.roboticscenter.ai/learn/dexterous-hand-comparison)
- [Shadow Dexterous Hand E 技术规格](https://shadowrobot.com/wp-content/uploads/2025/09/shadow_dexterous_hand_e_technical_specification.pdf)
- [Wonik Robotics Allegro Hand](https://www.wonikrobotics.com/robotics-hand)
