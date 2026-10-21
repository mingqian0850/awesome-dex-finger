# Dexterity updates: contact supervision and embodiment transfer

[Home](../README.md) · [中文](topic-progress-2026-10-21.zh-CN.md)

Checked **2026-10-21**. This is a recent topic increment, with paper, code-snapshot and announcement dates distinguished; historical entries were not all reverified. Method results are author-reported; selection and exercises are engineering guidance.

## Choose by the failure you observe

| Problem | Recent work | Method change | Inspect your data first |
| --- | --- | --- | --- |
| Plausible trajectories but too much/little force | FACT / EgoForce, Oct 13 | Predict future force while refining actions | Calibrated, synchronized force/tactile signals |
| Similar human/robot motion but different contact phases | TacOT, Oct 3 | Action–tactile dynamic matching guides representation alignment | Whether tactile timing distinguishes sliding, contact and release |
| Each hand requires another geometric mapping | EgoJEPA, Oct 14 | Shared latent representation with a robot-specific adapter | Enough target-robot data for adaptation |

## FACT: capture interaction forces as well as appearance

[FACT](https://arxiv.org/abs/2610.19155) introduces human tactile data through EgoForce and combines it with robot demonstrations. Visual-track-guided coarse planning precedes joint future-force prediction and action refinement, making anticipated interaction part of generation.

**Capture fields:** sensor type, units, clock, calibration revision, active region, saturation and missing samples. Distinguish visually inferred contact from measured force rather than giving them identical labels.

**Availability:** the [official project](https://fact-1-0.github.io/) labels both Code and Data as Coming Soon. Study signal design; do not assume EgoForce downloads or full training on 8GB VRAM are available.

## TacOT: align interaction phases, not just hand shapes

[TacOT](https://arxiv.org/abs/2610.04363) combines action/tactile dynamic time warping with soft optimal transport in a shared representation. Avoiding predefined frame pairs does not remove the need for reliable timing and tactile measurements.

**Useful when:** similar motion produces different friction, contact or slip. Label approach, first contact, loading and release; compare action-only correspondences with tactile-informed ones. Evaluate closed-loop behavior rather than smaller latent distance alone. The paper reports four real-world tasks; reproducible code/data release was not confirmed here.

## EgoJEPA: separate shared representations from execution

[EgoJEPA](https://arxiv.org/abs/2610.20904) learns latent actions from ego video and hand-motion differences, followed by robot adaptation. Shared action-effect representations can transfer while outputs still respect each hand's joints, ranges and controller interface. The [project](https://mengcaopku.github.io/EgoJEPA/) exists; full code/weight availability was not verified here.

**When comparing:** record human/robot data needs, target-hand adaptation, failure categories and object/scene splits. Results on familiar objects do not establish new-object or new-hand generalization.

## Exercise you can do now

For a hypothetical thin-walled-object grasp, list vision, joint state, commands, tactile/force signals, alignment and slip/deformation criteria. Mark unavailable sensors as unknown and explain which conclusion cannot be checked. No training is required; none of these methods guarantees industrial precision or reliability.
