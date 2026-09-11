# 🆕 2026 下半年动态跟踪（2026-06 至今）

> 灵巧手领域最新动态：硬件新品、前沿论文、开源生态、行业事件。
> **最新一轮：2026-09 月报**（50 次 web_search，最新条目 2026-09-11）｜历史：2026-06~08 双月报（29 次搜索）。
> 事件锚点：WAIC 2026（7 月·上海）、RSS 2026（7 月·悉尼）、WRC 2026（8 月·北京）、IROS 2026（9 月底·匹兹堡）、CoRL 2026（11 月·奥斯汀）。

---

# 📅 2026 年 9 月月报

## A. 新论文 / 模型（arXiv 2609.* 为主）

| 名称 | 时间 | 链接 | 一句话 |
| --- | --- | --- | --- |
| Dex-X | 2026-09 | [arXiv:2609.07747](https://arxiv.org/abs/2609.07747) | 从人类视频 + 仿真交互补齐接触信息，学视觉-触觉灵巧操作（本月最受关注之一） |
| DeCAL | 2026-09 | [arXiv:2609.09119](https://arxiv.org/abs/2609.09119) | 接触感知潜空间"共同想象"，解决灵巧 VLA 物理不可信问题 |
| GALATEA | 2026-09 | [arXiv:2609.10050](https://arxiv.org/abs/2609.10050) | 把生成式视频规划落地到仿真，训通用灵巧控制器 |
| **RoboTok** | 2026-09 | [arXiv:2609.03199](https://arxiv.org/abs/2609.03199) · [代码](https://github.com/Rice-RobotPI-Lab/RoboTok-Code) | **NVIDIA + 莱斯大学**：互联网级人类示范检索数据引擎 |
| WM-Craftnet | 2026-09 | [arXiv:2609.07002](https://arxiv.org/abs/2609.07002) | "世界通感模型"：视觉-触觉跨模态世界模型，提升手内操作泛化 |
| SEED-UMI | 2026-09 | [arXiv:2609.11753](https://arxiv.org/abs/2609.11753) | 人机共用同一套外骨骼做"一对一"灵巧示范 |
| 手内转笔/写字快速学习 | 2026-09 | [arXiv:2609.11775](https://arxiv.org/abs/2609.11775) | 实时雅可比估计实现快速学习（非大规模预训练路线） |
| Intervention-Aware World Models | 2026-09 | [arXiv:2609.06009](https://arxiv.org/abs/2609.06009) | 人类"干预/避免"信号并入世界模型做真机 RL |
| DUET-DINO | 2026-09 | [arXiv:2609.10506](https://arxiv.org/abs/2609.10506) | 跨视角世界模型用于潜空间规划 |
| Compact Visuotactile World Models | 2026-09 | [arXiv:2609.09597](https://arxiv.org/abs/2609.09597) | 紧凑视触觉世界模型（预测 + 奖励对齐 + 力约束） |
| OpenWAM | 2026-09 | [arXiv:2609.07398](https://arxiv.org/abs/2609.07398) | 开放模块化 world-action model 预训练底座 |
| **Benchmarking Dexterity of Multifingered Robot Hands（综述）** | 2026-09 | [arXiv:2609.05585](https://arxiv.org/abs/2609.05585) | 多指手"灵巧度"评测体系综述（本月少见的 benchmark 类） |
| Morphology and actuation as inductive biases | 2026-09 | [arXiv:2609.05206](https://arxiv.org/abs/2609.05206) | 把形态+驱动当归纳偏置研究（硬件-算法协同设计） |
| 模仿学习时间鲁棒性 | 2026-09 | [arXiv:2609.01453](https://huggingface.co/papers/2609.01453) | 跨执行速度的专家-学习者对比（可靠性实证） |
| CosmoH2G | 2026-09 | [arXiv:2609.07498](https://arxiv.org/abs/2609.07498) | 人手→夹爪迁移数据集与基线 |
| Potential-Guided Particle Steering | 2026-09 | [arXiv:2609.00555](https://arxiv.org/abs/2609.00555) | 面向"否定约束"（不要碰某处）的灵巧抓取合成 |
| Adaptive VL Grasping | 2026-09 | [arXiv:2609.04096](https://arxiv.org/abs/2609.04096) | 组合式基础模型先验 + 可泛化抓取合成 |
| One Demonstration, Many Objects | 2026-09 | [arXiv:2609.01938](https://arxiv.org/abs/2609.01938) | 局部接触几何实现一次示范泛化多物体 |
| MuJoCable | 2026-09 | [arXiv:2609.09612](https://arxiv.org/abs/2609.09612) | 腱驱动机器人降阶表面走线传动建模 |
| FWBC-VLA | 2026-09 | [arXiv:2609.03889](https://arxiv.org/abs/2609.03889) | 力感知全身补偿 VLA（接触丰富 loco-manipulation） |
| 形态感知人体动作重定向 | 2026-09 | [arXiv:2609.11357](https://arxiv.org/abs/2609.11357) | 轮式人形 loco-manipulation（与灵巧手 retargeting 同源） |
| HINT | 2026-09 | [arXiv:2609.02653](https://arxiv.org/abs/2609.02653) | 长时程操作中的人类意图注入 |

**8 月下旬补充（8 月报未覆盖）**

| 名称 | 时间 | 链接 | 一句话 |
| --- | --- | --- | --- |
| 腱驱五指手 + 分布式双模态触觉 | 2026-08 | [arXiv:2608.25547](https://arxiv.org/abs/2608.25547) | 8 月底最完整的灵巧手硬件论文（五指分布式触觉） |
| Motus2 | 2026-08 | [arXiv:2608.30237](https://arxiv.org/abs/2608.30237) | 自演化通用世界模型（专为灵巧操作） |
| 𝒩₀-Foundation | 2026-08 | [arXiv:2608.29601](https://arxiv.org/abs/2608.29601) | 触觉智能时代的触觉基础模型工作 |
| SoftVTBench | 2026-08 | [arXiv:2608.18701](https://arxiv.org/abs/2608.18701) | 变形感知视触觉数据集与 benchmark（柔性物体） |
| ViHaTeleop | 2026-08 | [arXiv:2608.16572](https://arxiv.org/abs/2608.16572) | 低成本轻量视触觉遥操作系统 |

## B. 硬件 / 开源 / 数据集（9 月）

| 名称 | 类型 | 机构 | 时间 | 链接 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| **TwinDEX** | 硬件+方法 | 自变量机器人 | 2026-09-02 | [IT之家](https://www.ithome.com/0/997/614.htm) · [极客公园](https://www.geekpark.net/news/369754) | 三指九自由度，宣称行业首次"零真机数据驱动灵巧操作"（数百条无本体数据） |
| **Allegro Hand V6 F** | 硬件 | Wonik Robotics（韩国） | 2026-09-02 | [朝鲜日报 Biz](https://biz.chosun.com/industry/business_info/2026/09/02/ZTRWP4RHAFBKTAJEWDJK2S47PM/) | 五指手，新增"读取全手接触数据"能力——**硬件厂商转向数据平台定位** |
| **HandEdit** | 数据集/基准 | 因时 + 上海交大 + 复旦 | 2026-09 | [OFweek](https://robot.ofweek.com/2026-09/ART-898890-8120-30701741.html) | 全球首个"第一视角人手→机器人手"图像编辑基准，覆盖 13 种灵巧手、约 2 亿样本 |
| **UnifoLM-WLA-1.0** | 开源模型 | 宇树 Unitree | 2026-09-10 | [智东西](https://www.zhidx.com/p/592980.html) · [品玩](https://www.pingwest.com/w/317294) | 人形基础模型全面开源：单模型 64 种任务、2500 小时真机数据 |
| Linker Hand O6 | 硬件 | 灵心巧手 | 2026-09-04 | [观点网](https://www.guandian.cn/article/20260904/597445.html) | 入选《财富》中国最佳设计榜，整手仅 370 克 |
| **DexWM** | 开源代码/数据 | Meta | 见来源 | [GitHub](https://github.com/facebookresearch/dexwm) · [arXiv:2512.13644](https://arxiv.org/abs/2512.13644) | 世界模型从人类视频学灵巧手-物交互，代码与数据集开源 |
| 中国灵巧手行业发展白皮书 | 行业报告 | MIR 睿工业 | 2026-09 | [亿欧](https://www.iyiou.com/news/202609021139838) | 首份系统梳理中国灵巧手梯队：**硬件趋同、软件模型开启行业 2.0** |
| 触觉传感器批量交付 | 供应链 | 福莱新材 → 灵心巧手 | 2026-09 | [中国证券网](https://www.cnstock.com/commonDetail/784099) | 3 万套+ 触觉传感器批量交付，触觉供应链放量 |

## C. 会议与行业动态（9 月）

**会议**
- **IROS 2026**：2026-09-27 ~ 10-01，美国**匹兹堡**（[官方](https://2026.ieee-iros.org/)）
- **CoRL 2026**：2026-11 美国**奥斯汀**；已公布 Workshop「**The UMI Arena**」——UMI/无本体数据采集成社区核心议题（[AIRoA](https://www.airoa.org/updates/20260821/649/)）
- **CIIF 2026 上海工博会**：9 月，机器人展区规模创历史新高（30 万㎡+、2800 家展商）
- **高工灵巧操作未来技术大会**：国内少数以"灵巧操作"为专题的技术大会

**标准**
- **灵巧手国家标准成型，预计 2026 年底公示**（[财联社](https://www.cls.cn/detail/2477896)）

**融资**
- **Sharpa**（上海）：累计融资超 **45 亿元**、估值约 **220 亿元**（禾赛创始团队二次创业）
- **超维动力**：超 5 亿元天使+轮（2026-09-11，前华为高管 + 港大教授）
- **睿研智控**：数千万元 Pre-A；**Xynova（曦诺未来）** 寻求新一轮融资，目标"灵巧操作领域的 Nvidia"
- 赛道整体：2026 年融资已达 **285.1 亿元**，呈"本体派 vs 供应商派"两极分化

**合作 / 量产**
- **比亚迪 × 帕西尼** 深度战略合作（汽车制造场景）；三星或入股帕西尼传闻
- **京东 × 灵巧智能 DexRobot** 三年战略合作；极佳视界 × 帕西尼
- **梅卡曼德** 2026-09-01 港交所上市（"具身智能眼-脑-手第一股"，超购 3835 倍）
- **Tesla Optimus V3 试产**：日产数十台，目标 9 月 1000 台/周、年底 2500 台/周（10 万台量产红线）
- 供应链放量：长盈精密机器人零部件交付 86 万件；小鹏机器人供应链国产化率超 80%

## D. 相比 8 月的最大变化

1. **数据范式三条新路径同时爆发**：TwinDEX（零真机数据）、RoboTok（互联网视频检索）、SEED-UMI（人机共用外骨骼）——脱离"真机遥操作"单一依赖
2. **硬件从"拼自由度"转向"拼触觉数据采集能力"**：Allegro V6 F 主打全手接触数据；白皮书结论"硬件趋同、软件开启 2.0"
3. **世界模型 × 灵巧操作形成完整方法族**：单月 7 项（Motus2/WM-Craftnet/GALATEA/DUET-DINO/Intervention-Aware/Compact Visuotactile/OpenWAM）
4. **行业进入"资本+标准+供应链"三重制度化**：融资 285 亿元、国家标准年底公示、比亚迪/京东场景绑定
5. **评测与可靠性议题首次被单独提出**：多指手灵巧度评测综述、模仿学习时间鲁棒性、SoftVTBench

---

# 📅 2026 年 6-8 月双月报

## 一、硬件新品（WAIC/WRC 发布潮 + 海外量产节点）

| 厂商 | 产品/事件 | 时间 | 要点 | 来源 |
| --- | --- | --- | --- | --- |
| 因时机器人 | **24 DoF 腱绳混驱灵巧手** 全球首发 | 2026-08 (WRC) | 24 DoF、腱绳+直驱混合驱动；同期登上世界人形机器人运动会仪式 | [经济观察网](https://jg-static.eeo.com.cn/article/info?id=ee5825ed95794922aec99426e11c98bb) |
| 兆威机电 | **ZWHAND B21** 首秀 | 2026-08 (WRC) | "电机藏在指节里"微型驱动；兆威机电港股上市获称"灵巧手龙头" | [WRC 展品页](https://www.worldrobotconference.com/expo/product/718.html) · [证券时报](https://www.stcn.com/article/detail/3667158.html) |
| 曦诺未来 Xynova | **Prima 1** 纯直驱灵巧手首发 | 2026-08-20 (WRC) | "纯直驱"方案线下首发，主打灵巧与可靠 | [中国工业报](https://www.cinn.cn/2026/08-21/z1zqNPxk.html) |
| 帕西尼 PaXini | **GEN4 自研触觉芯片** + 多维触觉传感器矩阵 | 2026-08 (WRC) | 从芯片到感知全自研，"全身感知"；现场演示自主拼小马等触觉任务 | [OFweek](https://robot.ofweek.com/2026-08/ART-898890-8120-30699603.html) |
| 万拿 Vanna / 均胜电子 | 任务型灵巧手 Std16A / 首款自研灵巧手 | 2026-07 (WAIC) | 零部件/新势力厂商切入灵巧手赛道 | [证券时报](https://stcn.com/article/detail/4027761.html) |
| 宇树 Unitree | Dex5-1 / Dex5-1P（触觉版）铺货，适配 H1-2/H2 | 2026 下半年 | 20 DoF 级五指手，触觉版面向零售/研究渠道 | [宇树官方](https://www.unitree.com/cn/mobile/Dex5-1) |
| NVIDIA × 宇树 | **Isaac GR00T 开源人形参考平台**（基于 H2） | 2026-06-01 | 面向高校的开源整机+灵巧手研究载体 | [CGTN](https://news.cgtn.com/news/2026-06-01/NVIDIA-Unitree-unveil-new-humanoid-powered-by-Isaac-GR00T-1NCWlv6VRde/index.html) |
| Tesla | **Optimus Gen 3 手部**：专利公开 + 爬坡量产 | 7 月底-8 月初 Fremont | 手部自由度较 Gen 2 翻倍（约 22 DoF/25 执行器，媒体口径）；Model S 产线改造为机器人产线 | [Teslarati 专利解析](https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/) · [it-boltwise](https://www.it-boltwise.de/optimus-gen-3-tesla-startet-roboter-fertigung-ab-ende-juli-in-fremont.html) |
| Figure AI | **Figure 03** 回归宝马工厂 | 2026-07 | 执行真实物流/部件分拣；Helix 02 手部引入触觉感知与手掌相机（分析） | [India Today](https://www.indiatoday.in/technology/news/story/bmw-deploys-figure-ai-humanoids-video-shows-robots-working-just-like-humans-2938041-2026-07-01) |
| 星动纪元 / 银河通用 | WRC 2026 全栈具身 + 物流落地 | 2026-08 | 快递分拣连续作业；Galbot 展示拧螺丝、切黄瓜等精细任务 | [pconline](https://www.pconline.com.cn/zhizao/2180/21806214.html) |
| 智元 AgiBot | WAIC 多款首发 + 运动会夺冠 | 2026-07/08 | 全量产机型出战世界人形机器人运动会，金牌/奖牌榜双第一 | [智元官网](https://www.agibot.com.cn/article/315/detail/188.html) |
| Shadow Robot | **无 2026 下半年新旗舰** | — | 仅 ICRA 2026 回顾；RSS 2026 时间检验奖颁给软体气动 RBO Hand 2 | [Shadow ICRA Recap](https://shadowrobot.com/icra-2026-recap/) |
| LEAP Hand | **未检索到 V3 发布** | — | 仅部署综述与 2026 开源灵巧手盘点提及 | [盘点](https://www.xcc.com/news/detail/5574855) |

## 二、前沿论文 / 模型

> arXiv ID 均来自搜索结果页面可直接复核；RSS/CoRL 录用以会议主页为准。

| 论文/模型 | 时间 | 链接 | 一句话 |
| --- | --- | --- | --- |
| InDex（Intent-Conditioned） | 2026-06 | [arXiv:2606.12109](https://papers.cool/arxiv/2606.12109) | 意图条件微调弥合 VLA 与高 DoF 手的形态鸿沟 |
| Wh0 | 2026-06 | [HF Papers](https://huggingface.co/papers/2606.22136) | 生成式世界模型批量合成第一人称人手操作数据 |
| DexFuture | 2026-06 | [HF Papers](https://huggingface.co/papers/2606.05699) | 分层未来状态瞄准，双手灵巧工具使用 |
| Unified Video-Action Joint Denoising | 2026-06 | [2606.03868](https://huggingface.co/buckets/huggingchat/papers-content/tree/2606/2606.03868.md) | 视频-动作联合去噪：同时做灵巧动作学习与数据生成 |
| MoDex | 2026-06 | [scirate](https://scirate.com/arxiv/2606.05407) | 顺序多物体灵巧抓取的扩散策略 |
| RealDexUMI / DexUMI | 2026-06 | [GitHub](https://github.com/real-stanford/DexUMI) · [arXiv:2606.06033](https://www.alphaxiv.org/overview/2606.06033) | 可穿戴"人手即通用操作接口"，降低采集门槛（Stanford） |
| T-Rex | 2026-06 | [arXiv:2606.17055](https://arxiv.org/html/2606.17055) | 触觉驱动反应式灵巧操作 + 数据集 |
| Mask2Real-WM | 2026-07 | [arXiv:2607.04546](https://arxiv.org/html/2607.04546) | 分割掩码当 sim2real 桥梁训练可控灵巧世界模型 |
| TouchWorld | 2026-07 | [arXiv:2607.07287](https://huggingface.co/papers/2607.07287) | 预测+反应式**触觉基础模型** |
| Open-AoE | 2026-07 | [arXiv:2607.14183](https://arxiv.org/html/2607.14183) | 开放第一人称操作数据集 + 工具链 |
| ReTouch | 2026-08 | [arXiv:2608.01824](https://arxiv.org/html/2608.01824) | 在线细化触觉预测，提升接触密集灵巧操作 |
| NestDex | 2026-08 | [scirate](https://scirate.com/arxiv/2608.13362) | 嵌套策略学习 + Copilot 辅助遥操作采数 |
| AdvDex | 2026-08 | [HF Papers](https://huggingface.co/papers/2608.14028) | 关节对齐动作 + 对抗学习，从人类示范学灵巧操作 |
| EMPIRE | 2026-08 | [arXiv:2608.22449](https://arxiv.org/abs/2608.22449) | 显式操作规划作为可学习中间表征（第一人称手部运动预测） |
| DexGrasp-Zero | RSS 2026 | [RSS 2026 程序](https://roboticsconference.org/2026/program/papers/) | 零样本跨具身灵巧抓取 |
| HUGS + 1M-HUGS | CoRL 2026 | [hugs-dex.github.io](https://hugs-dex.github.io/) | 人类先验指导的统一灵巧抓取合成（已录用 CoRL 2026） |
| EgoScale（趋势参考） | 2026-02 | [HF Papers](https://huggingface.co/papers/2602.16710) | NVIDIA GEAR：多样化第一人称人类数据扩展灵巧操作 |

## 三、开源与行业动态

**开源项目**
- [Dexora-VLA](https://github.com/flyingGH/Dexora-VLA)（ICRA 2026）：36 DoF 双臂双手扩散-Transformer VLA，开源
- [DexUMI](https://github.com/real-stanford/DexUMI)（Stanford）：可穿戴人手遥操作接口，开源
- [NVIDIA Isaac GR00T 参考平台](https://news.cgtn.com/news/2026-06-01/NVIDIA-Unitree-unveil-new-humanoid-powered-by-Isaac-GR00T-1NCWlv6VRde/index.html)：基于宇树 H2，开源整机

**数据集生态**
- 第一人称/ego 数据成共识方向：Wh0、Open-AoE、T-Rex Dataset（HF）、1M-HUGS（NYU 百万级人手抓取）、HRDexDB 等密集发布；[awesome-egocentric-atlas](https://huggingface.co/datasets/cy0307/awesome-egocentric-atlas) 索引持续更新

**行业事件 / 资本**
- 融资爆发：灵巧手赛道半年融资约 **250 亿元**、同比暴涨约 1500%（媒体口径）；灵心巧手寻求 **60 亿美元**估值；兆威机电港股上市获称"灵巧手龙头"
- 事件：WRC 2026（300+ 新品，灵巧手最热展区）、WAIC 2026、世界人形机器人运动会（"验收季"）；**CoRL 2026 将于 2026-11 在奥斯汀举行**

## 四、与上半年相比的最大变化

1. **从"单品秀"到"系统战 + 量产验收"**：真实产线任务（Tesla Fremont、Figure@宝马、物流分拣）成为新验收标准
2. **资本进入"非理性繁荣"前夜**：半年融资约 250 亿元、灵心巧手 60 亿美元估值
3. **驱动方案收敛分化**：腱绳混驱（因时 24 DoF）、指节藏电机（兆威 B21）、纯直驱（曦诺 Prima 1）；**触觉（而非自由度）成为差异化核心**（帕西尼 GEN4 芯片化）
4. **数据范式转向"人手数据 + 世界模型合成"**：Wh0/EgoScale/Open-AoE 用生成式世界模型批量合成第一人称人手操作数据
5. **触觉-世界模型合流**：TouchWorld/ReTouch 将触觉预测与世界模型结合，"视+触预测型世界模型"成为新研究主线（NVIDIA 与国内头部厂商同步押注）

## 调研局限说明

- Shadow Robot 与 LEAP Hand 未检索到 2026-06 后新旗舰
- Optimus Gen 3 手部精确 DoF（"翻倍/22 DoF/25 执行器"）为外媒口径，官方未公布完整规格
- "世界第一/首发/60 亿美元估值"等声明按厂商/媒体原口径转述并附来源，未逐条独立核证
