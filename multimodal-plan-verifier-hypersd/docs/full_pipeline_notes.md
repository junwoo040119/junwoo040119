# Full Pipeline Notes

This build removes all mock paths and assumes real local models for:
- planner
- verifier
- simulator

To reduce VRAM pressure, each model is unloaded after use.
Use scenario_01 first before trying the whole set.
