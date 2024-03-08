# Zombie Apocalypse Modeling

## Overview

This project provides a Python implementation for modeling a zombie apocalypse based on mathematical modeling principles. The approach used is inspired by the work of Munz et al. in 2009. The simulation involves three main components: humans, zombies, and deceased individuals, modeled as a system of first-order Ordinary Differential Equations (ODEs). The simulation allows users to explore the dynamics of the apocalypse under various parameters and scenarios.

## Mathematical Model

The system of ODEs is given by:
dS/dt = P - BSZ - dS
dZ/dt = BSZ + GR - ASZ
dR/dt = dS + ASZ - GR


Where:
- `S`: Number of humans
- `Z`: Number of zombies
- `R`: Number of deceased (both humans and zombies)
- `P`: Human birth rate (per day)
- `d`: Natural death probability (human dies from anything but a zombie)
- `B`: Infection probability (human becomes a zombie)
- `G`: Transition probability (deceased human is resurrected into a zombie)
- `A`: Zombie kill probability (human kills zombie)


## Dependencies
- NumPy
- SciPy
- Matplotlib