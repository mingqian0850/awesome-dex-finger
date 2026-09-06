# 🆕 2026 下半年动态跟踪（2026-06 至 2026-08）

> 灵巧手领域最新动态：硬件新品、前沿论文、开源生态、行业事件。
> 调研时间窗 2026-06 ~ 2026-08-25，29 次 web_search 交叉验证。事件锚点：WAIC 2026（7 月·上海）、RSS 2026（7 月·悉尼）、WRC 2026（8 月·北京亦庄）、世界人形机器人运动会（8 月·北京）。

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
