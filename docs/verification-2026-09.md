# 灵巧手/机器人操作论文核验报告（arXiv 2609.* / 2608.*）

> 📌 **本文件是 [latest-updates-2026h2.md](latest-updates-2026h2.md) 的核验附录**：所有 arXiv 号、标题、机构与会议录用状态均通过 **arXiv 官方 API 元数据 + 官方 HTML 全文作者块**核验，而非搜索摘要推测。
> 核验时点：2026-09-21（arXiv 最新公告 2026-09-18，编号 ≥ 2609.22100 尚未发布）。
> 核验口径：会议录用以 arXiv `comments` 字段与公开检索为准；**"未标注录用" ≠ "未被录用"**，仅表示无公开可核验声明。


**核验方法**：以 arXiv API 官方元数据（`export.arxiv.org/api/query`）为主源核对 arXiv 号、完整标题、作者列表与 `comments` 字段（该字段是录用声明的权威出处）；机构信息取自 arXiv 官方 HTML 全文（`arxiv.org/html/<id>`）作者块与官方 PDF 首页脚注；对论文未打印机构名的情况，另行 web_search 交叉核验，仍无法确认者一律标注"未能核验"。


---

## 一、主表

| 论文 | 机构 | 会议/状态 | 核验结果 | 来源链接 |
|---|---|---|---|---|
| 1. Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction（arXiv:2609.07747，v2） | **清华大学**（第一作者 Ruoqu Chen，通讯 Mengdi Xu）+ **上海期智研究院**；合作方 Sharpa、同济大学、中国人民大学 | arXiv `comments` **未标注录用**；未检索到 IROS/CoRL/RSS 2026 录用声明 → 视为预印本 | 确认（机构、arXiv 号均确认；录用状态为"未标注"，非拒绝） | [abs](https://arxiv.org/abs/2609.07747) · [html](https://arxiv.org/html/2609.07747v2) |
| 2. DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination（arXiv:2609.09119，v1） | **北京大学**（State Key Laboratory of Multimedia Information Processing, School of Computer Science）；合作 **北京智源人工智能研究院（BAAI）** | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.09119) · [html](https://arxiv.org/html/2609.09119v1) · [项目页](https://aureleopku.github.io/DeCAL/) |
| 3. GALATEA: Grounding Generated Video Plans in Simulation Towards Versatile Dexterous Controllers（arXiv:2609.10050，v1） | **加州大学伯克利分校（UC Berkeley）**（第一作者 Tianyue Wu）；合作 Sharpa、**香港大学** | `comments` 未标注录用 → 预印本。注：arXiv 正式标题**不含 "GALATEA:" 前缀**，GALATEA 为项目名 | 确认（arXiv 号正确；标题前缀与检索列表不一致，已在备注说明） | [abs](https://arxiv.org/abs/2609.10050) · [项目页](https://boyuan-an.github.io/GALATEA/) |
| 4. RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning（arXiv:2609.03199，v1） | **莱斯大学（Rice University）**（第一作者 Howard Qian、通讯 Kaiyu Hang）+ **NVIDIA**（Bowen Wen）——**用户猜测的"NVIDIA + 莱斯大学"正确** | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.03199) · [html](https://arxiv.org/html/2609.03199v1) · [代码库 Rice-RobotPI-Lab](https://github.com/Rice-RobotPI-Lab/RoboTok-Code) |
| 5. WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation（arXiv:2609.07002，v1） | **Sharpa Robotics**（全部 6 位作者均标注 Sharpa；新加坡灵巧手公司） | **Accepted to CoRL 2026** ✅（arXiv comments 原文） | 确认 | [abs](https://arxiv.org/abs/2609.07002) · [html](https://arxiv.org/html/2609.07002v1) · [Sharpa 报道](https://m.163.com/dy/article/L71R13K00511AQHO.html) |
| 6. SEED-UMI: Sharing the Exoskeleton between human and robot for onE-to-one Dexterous demonstration（arXiv:2609.11753，v1） | **北京大学**（State Key Laboratory of General Artificial Intelligence / 智能科学与技术学院；第一作者 Tengbo Yu，通讯 Hangxin Liu）+ **Delta Intelligence** | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.11753) · [html](https://arxiv.org/html/2609.11753v1) |
| 7. Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation（arXiv:2609.11775，v1） | **苏黎世联邦理工学院（ETH Zurich）**，Soft Robotics Lab, D-MAVT（第一作者 Kai Stewart，通讯 Robert K. Katzschmann） | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.11775) · [项目页](https://srl-ethz.github.io/rapid-dexterous-writing/) |
| 8. Intervention-Aware World Models with Real-World RL for Dexterous Manipulation（arXiv:2609.06009，v1） | **香港科技大学（广州）HKUST(GZ)**（第一作者 Jiaju Yin）+ **意大利技术研究院（IIT）** + 浙江大学 | **Accepted by CoRL 2026** ✅。注：**完整标题为 "How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation"**（用户清单标题被截去前半段） | 确认（录用与机构确认；标题需补全） | [abs](https://arxiv.org/abs/2609.06009) · [html](https://arxiv.org/html/2609.06009v1) |
| 9. DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning（arXiv:2609.10506，v1） | **纽伦堡工业大学（UTN, University of Technology Nuremberg）** Artificial Intelligence and Robotics Lab（第一作者 Nisarga Nilavadi）+ 慕尼黑工业大学（TUM）+ 卡尔斯鲁厄理工学院（KIT） | `comments`: "Preprint" → 明确为预印本 | 确认。注：**完整标题为 "...for Latent Planning in Robot Manipulation"** | [abs](https://arxiv.org/abs/2609.10506) · [html](https://arxiv.org/html/2609.10506v1) |
| 10. Benchmarking Dexterity of Multifingered Robot Hands: A Review and Perspective（arXiv:2609.05585，v1） | **美国西北大学（Northwestern University）**——NSF HAND Engineering Research Center / Center for Robotics and Biosystems（第一作者 Anthony Shilati，通讯 Kevin M. Lynch）；合作德州农工大学、卡内基梅隆大学、佛罗里达农工大学 | `comments`: 将于 **《Annual Review of Control, Robotics, and Autonomous Systems》Vol. 10 (2027)** 发表（期刊，非会议） | 确认 | [abs](https://arxiv.org/abs/2609.05585) · [html](https://arxiv.org/html/2609.05585v1) |
| 11. Morphology and actuation as inductive biases in robotic hand manipulation（arXiv:2609.05206，v1） | **帕兹马尼·彼得天主教大学（Pázmány Péter Catholic University）**，Faculty of Information Technology and Bionics，布达佩斯（第一作者 Zalán Tari） | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.05206) · [html](https://arxiv.org/html/2609.05206v1) |
| 12. A Tendon-Driven Five-Fingered Hand with Distributed Tactile Perception for Dexterous Manipulation（arXiv:2608.25547，v1） | **东南大学机械工程学院**（Southeast University, School of Mechanical Engineering，南京；Huayang Chen、通讯 Longhui Qin） | ⚠️ **既不是 IROS 2026，也不是 CoRL 2026**——`comments` 原文为 **"Accepted by International Conference on Service Robotics (ICoSR) 2026"** | 确认（并**纠正**用户清单中的会议名假设） | [abs](https://arxiv.org/abs/2608.25547) · [PDF 首页](https://arxiv.org/pdf/2608.25547) |
| 13. Motus2: A Self-Evolving General World Model for Dexterous Manipulation（arXiv:2608.30237，v1） | **生数科技（GensPI，论文标注单位 1）** + **清华大学**（单位 2；第一作者 Hongzhe Bi，通讯 Jun Zhu） | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2608.30237) · [html](https://arxiv.org/html/2608.30237v1) · [生数科技发布报道](https://qa.eetrend.com/content/2026-09/9b72188d-5bed-4da9-a1a7-87d64e9b2d07-100604113.html) |
| 14. 𝒩₀-Foundation: Towards the Age of Tactile Intelligence（arXiv:2608.29601，v1） | 作者署名即为机构：**NeoteAI Team + Fudan TEAI Team**。中文报道显示 NeoteAI = **新智具身（上海新智具身智能科技有限公司）**，联合**复旦大学**发布 Neo 系列 | `comments` 未标注录用 → 预印本 | 确认（**NeoteAI 归属新智具身**已由中文一手报道交叉验证） | [abs](https://arxiv.org/abs/2608.29601) · [html](https://arxiv.org/html/2608.29601v1) · [量子位报道](https://www.qbitai.com/2026/07/460962.html) |
| 15. SoftVTBench（arXiv:2608.18701，v1） | 单位 1 = **Tuojing Intelligence**（论文原文标注，第一作者 Bowen Jing）；另有 **清华大学**、伦敦国王学院、东南大学、Stevens Institute、香港科技大学（广州）等 13 家单位 | `comments` 未标注录用 → 预印本。注：**完整标题为 "SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation"** | 机构名**确认**（按论文原文）；**"Tuojing Intelligence" 的中文名未能核验**（未检索到可靠对应实体） | [abs](https://arxiv.org/abs/2608.18701) · [html](https://arxiv.org/html/2608.18701) |
| 16. ViHaTeleop（arXiv:2608.16572，v1） | **日本东北大学（Tohoku University）**大学院情报科学研究科（第一作者 Fucai Zhu，通讯 Koichi Hashimoto） | **Accepted to IROS 2026** ✅（`comments` 原文："Accepted to the 2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). 8 pages"） | 确认。注：**完整标题为 "ViHaTeleop: A Low-Cost, Lightweight Visual-Haptic Teleoperation System for Dexterous Manipulation Learning"** | [abs](https://arxiv.org/abs/2608.16572) · [html](https://arxiv.org/html/2608.16572v1) |
| 17. CosmoH2G（arXiv:2609.07498，v1） | **香港中文大学（深圳）SSE**（第一作者 Hongxiang Zhao、通讯 Xiaoguang Han）+ **GenuX** + FNii-Shenzhen | **SIGGRAPH Asia 2026** ✅（`comments` 原文 "SIGGRAPH Aisa 2026"，原文有拼写错误 Aisa→Asia）。**非** IROS/CoRL/RSS | 确认。注：完整标题为 "CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements" | [abs](https://arxiv.org/abs/2609.07498) · [html](https://arxiv.org/html/2609.07498v1) |
| 18. OpenWAM（arXiv:2609.07398，v1） | **新加坡国立大学（NUS）**（单位 1，第一作者 Yuran Wang，共同通讯 Lin Shao / Hang Zhao）+ 清华大学、北京大学、香港大学、浙江大学、香港中文大学、上海交通大学 | `comments` 未标注录用 → 预印本 | 确认。注：完整标题为 "OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining" | [abs](https://arxiv.org/abs/2609.07398) · [PDF 首页](https://arxiv.org/pdf/2609.07398) |
| 19. HINT: Human-Intent Inception for Long-Horizon Robot Manipulation（arXiv:2609.02653，v1） | **浙江大学**（单位 1；第一作者 Mingyu Mei、通讯 Zaixing He）+ 上海交通大学 + Noematrix + EndlessAI | `comments` 未标注录用 → 预印本 | 确认 | [abs](https://arxiv.org/abs/2609.02653) · [html](https://arxiv.org/html/2609.02653v1) |
| 20. Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation?（arXiv:2609.01453，v1） | **马里兰大学学院市分校（University of Maryland, College Park）** Institute for Systems Research（Clinton Enwerem、John S. Baras、Calin Belta） | `comments` 未标注录用 → 预印本。完整标题为 "...? An Expert–Learner Comparison Across Task Execution Speeds" | 确认 | [abs](https://arxiv.org/abs/2609.01453) · [PDF 首页](https://arxiv.org/pdf/2609.01453) |

**arXiv 号核对结论**：20 篇的 arXiv 号**全部正确**（均可通过 arXiv 官方 API 与摘要页解析，标题与作者一致）。仅 3 篇存在标题截断/前缀差异（#3、#8、#9、#15、#16、#17、#18、#20），已在表中逐一注明。

**会议录用汇总**：
- **CoRL 2026（已确认录用）**：#5 WM-Craftnet、#8 Intervention-Aware World Models
- **IROS 2026（已确认录用）**：#16 ViHaTeleop
- **其他会议/期刊**：#12 ICoSR 2026（**非 IROS/CoRL**）、#17 SIGGRAPH Asia 2026、#10 Annual Review of Control, Robotics, and Autonomous Systems Vol. 10 (2027)
- **仅预印本（arXiv comments 未标注任何录用，且未检索到公开录用声明）**：#1、#2、#3、#4、#6、#7、#9（明确标注 Preprint）、#11、#13、#14、#15、#18、#19、#20

---

## 二、新增论文（2026-09-12 之后）

检索窗口：2026-09-12 → 2026-09-18。cs.RO 该窗口共 525 篇，按标题关键词（dex / hand / finger / tactile / grasp / gripper / teleop / exoskeleton / glove 等）筛出 112 篇，以下为**灵巧手/多指手/手部触觉**核心相关者（按 arXiv 公告日倒序）。

| arXiv 号 | 公告日 | 标题 | 机构 | 会议/状态 |
|---|---|---|---|---|
| 2609.21514 | 09-18 | Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer | 香港中文大学 + 上海人工智能实验室 + Joy Future Academy + CPII (InnoHK) | 未标注录用 |
| 2609.21511 | 09-18 | 2nd Place Solution to the HANDS 2026 Workshop Challenge — Dexterous Grasp Motion Track | UNIST（韩国）+ University of Aberdeen + Fogsphere | HANDS 2026 Workshop 挑战赛参赛方案 |
| 2609.21045 | 09-17 | DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real | 德州大学奥斯汀分校 + 佛罗里达大学 + BrainCo | 未标注录用 |
| 2609.20649 | 09-17 | DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation | 香港科技大学（广州）+ Xspark AI + 北京大学 + 清华大学 + 香港大学 | **Accepted to IROS 2026 Workshop RoBoWoMo（Lightning Talk）** |
| 2609.20107 | 09-17 | AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations | IIIT-Hyderabad（Robotics Research Center）+ VJTI Mumbai + IISER Bhopal | 未标注录用 |
| 2609.19666 | 09-17 | Towards High-DoF Dexterous Manipulation through VLA Post-Training | Wuji Technology + 上海科技大学 | 未标注录用（期刊格式模板，投稿中） |
| 2609.19613 | 09-17 | TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation | 南加州大学（USC）+ 三菱电机研究实验室（MERL） | 未标注录用 |
| 2609.19196 | 09-16 | DITTO: Dexterous Interface for Transparent TeleOperation | 哥伦比亚大学（机械工程系 / 计算机科学系）+ 斯坦福大学（计算机科学系） | 未标注录用 |
| 2609.18763 | 09-16 | Gated Residual Body-Hand Coordination for Whole-Body Humanoid Teleoperation | 慕尼黑工业大学（TUM）+ Agile Robots SE | 未标注录用 |
| 2609.18504 | 09-16 | InterMASH: A Unified Geometric Representation for Grasp Synthesis | 中国科学技术大学 + 中科院工业人工智能研究所 + 深圳大学 | 未标注录用 |
| 2609.18174 | 09-16 | TacBPM: A Tactile-conditioned Behavior Prior Model for Dexterous Reorientation | **Sharpa**（通讯 jie.yin@sharpa.com） | 未标注录用 |
| 2609.18165 | 09-16 | LUMO: Designing Luminous Contact Morphology for Repeatable Whole-Finger Contact Observation | 德州大学奥斯汀分校 | 未标注录用 |
| 2609.18117 | 09-16 | OpenDexGrasp: Open-vocabulary Task-Oriented Dexterous Grasping | 北京大学（CFCS / 多媒体信息处理国家重点实验室）+ BIGAI + PrimeBot | **Accepted at CoRL 2026** |
| 2609.17404 | 09-15 | Residual Fault Adaptation for Dexterous In-Hand Manipulation Under Runtime Joint Faults | 香港科技大学 + 华中科技大学 | 未标注录用 |
| 2609.17172 | 09-15 | Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand | 苏黎世联邦理工学院（ETH Zurich）Soft Robotics Lab | 未标注录用 |
| 2609.16683 | 09-15 | Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions | 清华大学 IIIS / College AI + 大连理工大学 + 香港中文大学 | 未标注录用 |
| 2609.16586 | 09-15 | ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation | 中科院自动化所（CASIA）+ 中国科学院大学 + 新疆大学 | **Accepted at CoRL 2026** |
| 2609.16518 | 09-15 | Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array | Meta Reality Labs Research（美国） | 未标注录用 |
| 2609.16504 | 09-15 | UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data | **未能核验**（论文首页未打印机构，HTML 作者块为空） | 未标注录用 |
| 2609.16319 | 09-14 | ConGraspXL: Controllable Constraint-Conditioned Dexterous Grasping Motion Synthesis | 苏黎世联邦理工学院（ETH Zürich）+ 香港科技大学（广州） | 未标注录用（声明已投 IEEE） |
| 2609.15921 | 09-14 | Touch2Trace: Tactile-Driven Imitation Learning for Dexterous Cable Tracing | Analog Devices, Inc.（Dexterous AI Group） | **Accepted to CoRL 2026** |
| 2609.15910 | 09-14 | SlipSense: Multimodal Tactile Learning for Low-Latency and Generalized Slip Detection | Analog Devices, Inc.（Dexterous AI Group） | **Accepted to CoRL 2026** |
| 2609.15726 | 09-14 | Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands | 上海交通大学（标注单位 1）+ 复旦大学 + 香港大学 + Inspire Robots + 中关村学院 + COWARobot + 南洋理工大学 | 未标注录用（Technical Report） |
| 2609.14878 | 09-14 | Real-World Reinforcement Learning with MPC Scaffolding for Dexterous Manipulation | Honda Research Institute USA | 未标注录用 |
| 2609.14868 | 09-14 | Primitive-Informed Sampling-Based MPC for Multi-Fingered Dexterous Manipulation | Honda Research Institute USA | 未标注录用 |
| 2609.14173 | 09-12 | GIFT: Glove-Inferred Force Transfer（Force-Aware Human-to-Robot Skill Transfer from a Wearable Sensing Glove） | **未能核验**（论文首页无机构署名） | 未标注录用 |
| 2609.14156 | 09-12 | Visible Touch: Rendering Contact for Visuomotor Policies | 加州大学洛杉矶分校（UCLA） | **Accepted at CoRL 2026** |
| 2609.13761 | 09-12 | Learning In-Hand Object Reaching to General 6D Poses | 悉尼大学 + Sharpa + 香港大学 | 未标注录用 |

**窗口内其他相关但非手部核心的会议录用论文**（供参考）：2609.16864 TEMPO（UC Irvine，CoRL 2026）、2609.15976 MessyMem（Stanford，CoRL 2026）、2609.22062 Gripper-Aware Dense Packing（ISRR 2026）、2609.21817 Sim-to-Real VLA（IROS 2026 Workshop）、2609.19328 Morphing Aerial Robot（IROS 2026）。

**说明**：arXiv 索引中最新公告日为 **2026-09-18**（最后一篇 cs.RO 为 2609.22085）；编号 ≥ `2609.22100` 尚未发布。因此上表即为当前可得的最新批次；2026-09-19/20 为周末，arXiv 不公告，需等下一个工作日。

---

## 三、核验局限

1. 关于会议录用：本报告以 arXiv `comments` 字段与公开检索结果为准。**"未标注录用"不等于"未被录用"**——只是当前无公开可核验的录用声明。
2. 两篇（`2609.16504` UniDex-ViTac、`2609.14173` GIFT）论文原文首页未打印任何机构署名，未检索到可靠第三方信息，按要求写"未能核验"，未作任何猜测。
3. `2608.18701` SoftVTBench 的第 1 单位"Tuojing Intelligence"为论文原文所印英文名，其中文实体名未能通过检索确认。
4. `2609.07498` CosmoH2G 的 `comments` 原文将 SIGGRAPH Asia 误拼为 "SIGGRAPH Aisa"，本报告按会议实际名称记录。
