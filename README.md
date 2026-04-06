# 5G mm-Wave Small Cell Optimization using Simulated Annealing

A Python-based simulation engine that models dense urban environments and uses the Simulated Annealing (SA) metaheuristic to optimize the deployment of 5G mm-Wave base stations.

**Author:** Parth Vinod Kariya
**Institution:** MAHE Bengaluru

## 🚀 Project Overview
High-frequency 5G mm-Wave signals (24-100 GHz) suffer from severe atmospheric absorption and solid blockages. Traditional hexagonal macro-cell planning fails in urban "canyons." 

This project simulates a highly dense city grid and deploys a Simulated Annealing algorithm to find the exact global optimum for base station placements. It successfully balances minimizing Capital Expenditure (CapEx) while enforcing a strict 99% signal coverage threshold.

### ⚙️ Core Physics & Constraints
* **Propagation Model:** Log-Distance Path Loss with severe Line-of-Sight blockage penalties (30 dB drop through concrete).
* **Cost Function:** $J = \alpha \cdot N + \beta \cdot (1 - P_{cov}) + \text{ISD\_Penalty}$
  * Heavily penalizes signal dead zones.
  * Enforces an Inter-Site Distance (ISD) constraint to prevent overlapping towers and signal interference.

## 📊 Simulation Results
The algorithm successfully starts with a random, highly-shadowed layout and dynamically adds, shifts, and removes towers to achieve **>99% coverage** with minimum infrastructure.

![Optimization Results](assets/ofigure%20v2.png)
*(Left: Initial random placement with heavy blind spots. Middle: SA optimized layout routing signals around buildings. Right: The thermodynamic cooling convergence curve).*

## 💻 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/parthvkariya-art/5G-SA-Optimization.git](https://github.com/parthvkariya-art/5G-SA-Optimization.git)
   cd 5G-SA-Optimization

2.Create and activate a virtual environment:
   python -m venv venv
.\venv\Scripts\activate   # On Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run the simulation:
python src/5G_SA_Simulation.py

References & Acknowledgements
The mathematical models and algorithmic constraints utilized in this simulation were adapted from the following literature and standards:

Simulated Annealing Algorithm: S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, "Optimization by Simulated Annealing," Science, vol. 220, no. 4598, pp. 671-680, 1983.

5G mm-Wave Channel Modeling: 3GPP, "Study on channel model for frequencies from 0.5 to 100 GHz," 3rd Generation Partnership Project (3GPP), Technical Report (TR) 38.901.

Urban Blockage Penalties: ITU-R, "Prediction of clutter loss," International Telecommunication Union, Recommendation ITU-R P.2108-1, 2021.