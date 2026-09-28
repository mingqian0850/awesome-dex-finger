#!/usr/bin/env bash
# 刷新本仓库所跟踪的 GitHub 项目 star / 许可证 / 推送时间（GitHub API 实时值）
# 用法: bash scripts/refresh_stars.sh [输出文件]
# 依赖: gh（已登录，需 repo 读取权限）
set -euo pipefail
OUT="${1:-stars.tsv}"

REPOS=(
  # —— 开源硬件 ——
  pollen-robotics/AmazingHand Chestnut-Robotics/aero-hand-open TheRobotStudio/HOPEJr
  wengmister/BiDexHand ruka-hand/RUKA ruka-hand-v2/RUKA-v2
  leap-hand/LEAP_Hand_API leap-hand/LEAP_Hand_Sim leap-hand/Bidex_Manus_Teleop
  wuji-technology/wuji-mjlab iotdesignshop/dexhand-mechanical-build
  SYSU-RoboticsLab/RAPID-Hand HaoranLi-Data/Tactile_SoftHand_A
  # —— 仿真 / 模型 ——
  google-deepmind/mujoco_menagerie isaac-sim/IsaacGymEnvs AgibotTech/genie_sim
  PKU-MARL/DexterousHands dexsuite/dex-urdf vikashplus/Adroit
  ruoyiqiao/mjlab_hand szahlner/shadowhand-gym
  # —— 算法 / 数据 / 感知 ——
  OpenDriveLab/AgiBot-World roboterax/Humanoid-Gym unitreerobotics/xr_teleoperate
  unitreerobotics/unitree_lerobot unitreerobotics/unifolm-wla PKU-EPIC/DexGraspNet
  j96w/DexCap aravindr93/hand_dapg tengyu-liu/GenDexGrasp yzqin/dexmv-sim
  unidex-ai/UniDex yzqin/dex-hand-teleop dexsuite/dex-retargeting
  geopavlakos/hamer rolpotamias/wilor facebookresearch/digit360
  facebookresearch/dexwm InternRobotics/OpenHomie Rice-RobotPI-Lab/RoboTok-Code
  flyingGH/dexmimicgen_tactile
  # —— 中文社区 ——
  AgibotTech/agibot_x1_hardware AgibotTech/agibot_x1_train AgibotTech/agibot_x1_infer
  unitreerobotics/unitree_ros unitreerobotics/dfx_inspire_service
  correlllab/rh56_controller Sentdex/inspire_hands linker-bot/linkerhand-urdf
  DexRobot/dexrobot_mujoco DexRobot/dexrobot_isaac DexRobot/dexrobot_urdf
  zhangdong-cheku/Multi-Finger-Dexterous-Manipulator Bobyue0118/BrainCo-Revo2-Dex-Retargeting
  # —— Awesome 列表 ——
  Tsunami-kun/awesome-humanoid-manipulation BaiShuanghao/Awesome-Robotics-Manipulation
  curieuxjy/Awesome_Manipulation CyanHaze/Awesome-Dexterous-Hands
  chang-xinhai/Awesome-Dexterous-Manipulation huangjund/awesome-UMI-Papers
  Growbotics-AI/awesome-open-source-robotics HaoxuanXU1024/awesome_dexterous_hand
  TX-Leo/Awesome-Robotic-Grasping
)

: > "$OUT"
for r in "${REPOS[@]}"; do
  if ! gh api "repos/$r" --jq '[.full_name, .stargazers_count, (.license.spdx_id // "none"), .pushed_at] | @tsv' >> "$OUT" 2>/dev/null; then
    printf '%s\tERR\tERR\tERR\n' "$r" >> "$OUT"
  fi
  sleep 0.12
done

echo "✅ 已写入 $OUT （$(wc -l < "$OUT") 个仓库，$(date -u '+%Y-%m-%d %H:%M UTC')）"
echo "📌 下一步：对照 docs/open-source.md 与 awesome-lists.md 中的数值，用编辑或脚本更新变化项。"
