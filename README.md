# 5G mm-Wave Small Cell Optimization using Simulated Annealing (v1.0)

A Python-based baseline simulation engine that models city grids to optimize the deployment of 5G mm-Wave base stations.

**Author:** Parth Vinod Kariya
**Institution:** MAHE Bengaluru

## 🚀 Project Overview (Baseline Version)
High-frequency 5G mm-Wave signals (24-100 GHz) suffer from severe atmospheric absorption and solid blockages. Traditional hexagonal macro-cell planning fails in urban "canyons," requiring dense Small Cell deployments.

This repository hosts **v1.0 (Proof of Concept)**, establishing the core mathematical model. We utilize the Simulated Annealing (SA) metaheuristic to find optimal placements.

### ⚙️ Core Physics & Constraints (v1.0 Baseline)
* **Propagation Model:** Log-Distance Path Loss with severe Line-of-Sight blockage penalties (25 dB drop).
* **High Power:** This baseline assumes high transmit power (40 dBm), making total signal coverage trivially easy.
* **Perturbation Logic:** In this initial version, the algorithm can only *move* existing towers; it cannot dynamically add or remove them.

**Cost Function:**
$$J = \alpha \cdot N + \beta \cdot (1 - P_{cov})$$

The algorithm seeks to minimize this function, where $N$ is the static number of towers and $P_{cov}$ is the coverage percentage.

## 📊 Simulation Results (v1.0)
Due to the high transmit power, the initial random towers easily achieve 100% signal coverage even with simple building shadows. Because of this over-engineered state, moving towers slightly has almost no impact on total cost, leading to a **completely flat cost function**.

![v1.0 Results](assets/version1(unoptimized).png)
*(Left: Initial random placement already achieving high coverage. Middle: Iterated placement with minimal change. Right: A high, flat cost curve showing algorithm stagnation at a local minimum).*

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
