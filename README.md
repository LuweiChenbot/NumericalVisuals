# NumericalVisuals
This repository serves as a collection of numerical implementations exploring some mathematical models, mostly consists of small 
course projects from *MATH-UH 3413 Numerical Methods* and *MATH-UA 264 Nonlinear Dynamics*. 
## 1. Turing Patterns 🪸(Gray-Scott Model)
An implementation of the reaction-diffusion system modelded by the Gray-Scott equations. This simulation illustrates the instability in chemical reaction system, where
a stable equilibrium is broken by diffusion, creating life-like spots, coral like structures often seen in nature.\
The system solves for two chemical concentrations, $U$ and $V$, over a two-dimensional grid using the finite difference method:

$$
\begin{aligned}
\frac{\partial u}{\partial t} &= D_u \nabla^2 u - uv^2 + F(1 - u) \\
\frac{\partial v}{\partial t} &= D_v \nabla^2 v + uv^2 - (F + k)v
\end{aligned}
$$

Relevant Algorithm: Forward Euler time integration 

