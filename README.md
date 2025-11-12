# Particle Swarm Optimization — Hidden Intelligence in Bird Flight

<p align="center">
  <img width="270" height="270" alt="PSO exploring a radial landscape" src="https://github.com/user-attachments/assets/274cee89-42ff-4493-a0a9-4eaead45132d" />
  <img width="270" height="270" alt="PSO particles converging" src="https://github.com/user-attachments/assets/0b0f7acb-6dd6-4214-afd5-d54697c144e0" />
  <img width="270" height="270" alt="Swarm on multi-modal terrain" src="https://github.com/user-attachments/assets/b50c88c2-343a-40a8-a68c-dedb4c424372" />
</p>

Minimal, hackable PSO playground built with `pygame`, `numpy`, and `matplotlib`. Tweak the fitness function, watch the swarm react, and keep iterating.

## Quickstart

```bash
# using uv (recommended)
uv sync
uv run python main.py

# or plain pip
pip install -e .
python main.py
```

You need Python 3.13+ because this repo leans on the latest `pygame` wheels.

## What You Get

- Vectorized PSO core with inertia/cognitive/social parameters exposed at the top of `main.py`.
- A 3D surface preview (`preview_3d()`) so you can sanity-check the objective before the swarm launches.
- A grab bag of alternate functions (Gaussian, Rastrigin, Ackley, Griewank, etc.) ready to uncomment.
- Color-mapped heat field rendered via `pygame` for instant feedback at 60 FPS.

## Customize the Experiment

- **Objective**: swap the lambda assigned to `f(x, y)` or plug in your own function. Keep it vectorizable for fast previews.
- **Swarm behavior**: tune `a`, `b`, `b_hat`, and `c` to explore constriction vs. exploration regimes.
- **Grid resolution**: adapt `WINDOW_SIZE` and `PARTICLE_SIZE` to trade off fidelity vs. speed.
- **Visualization**: comment out `preview_3d()` if you want to skip the Matplotlib surface step.

## Read More

- [Full write-up on the underlying ideas](https://blog.bernardoolisan.com/posts/pso)
- `_reading6 1995 particle swarming.pdf` for the original Kennedy & Eberhart paper.
