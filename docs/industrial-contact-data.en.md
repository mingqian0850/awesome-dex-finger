# Accurate placement, dexterity and contact data

[Home](../README.md) · [中文](industrial-contact-data.zh-CN.md)

Sources reviewed: 2026-10-20; compiled: 2026-10-21. Engineering recommendations are not reproduced experiments.


## Start with the task, not finger count

Accurate placement concerns position and orientation errors; multifinger dexterity may also involve contact allocation, slip and in-hand adjustment. Small objects do not necessarily require many fingers, while large objects may require complex contact control.

[Figure / BMW loading](https://www.figure.ai/news/production-at-bmw) and [Longcheer test loading](https://us.longcheer.com/en/col76/260.html) are process examples, not evidence that general precision assembly or human-level dexterity is solved.

## Which data supports which conclusions?

| Data | What can be inspected | Still needed |
| --- | --- | --- |
| Human hand keypoints/poses | Geometry, handedness, occlusion and estimation jumps | Target-hand kinematics, limits and contact feasibility |
| Object/tool poses | Relative motion and placement errors | Hidden contact, applied forces and product quality |
| Hand states and commands | Tracking, control mode and latency | Actual grasp stability and object slip |
| Force/torque or tactile signals | Contact events covered by sensors | Calibration, range, drift and visual synchronization |
| Fixture/test-equipment results | Process completion and quality criteria | Links to episodes, parts and action intervals |

This is capture guidance, not a claim that every dataset contains these signals. Unmeasured force is not zero; apparent visual stability does not replace contact measurements.

## Open references and exercise

Read hand mapping in [Dex Retargeting](https://github.com/dexsuite/dex-retargeting), and compare the parallel-gripper interface in [UMI](https://umi-gripper.github.io/). UMI gripper width is not a multifinger joint configuration or tactile feedback.

For grasp → align → insert/place → release, distinguish visual error, grasp failure, contact jamming and fixture-not-ready. List available evidence and missing sensors for each, producing a one-page data requirements table without training.

Continue: [five capture routes](https://github.com/mingqian0850/awesome_vla_deployment/blob/main/docs/02-data-sources.md).
