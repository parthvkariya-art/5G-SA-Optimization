# 5G mm-Wave Small Cell Optimization using Simulated Annealing (v2.0)

A Python-based simulation engine that models city grids to optimize the deployment of 5G mm-Wave base stations.

**Author:** Parth Vinod Kariya  
**Institution:** MAHE Bengaluru  

## 🚀 Project Overview (v2.0 - Dynamic Allocation)
High-frequency 5G mm-Wave signals (24-100 GHz) suffer from severe atmospheric absorption and solid blockages. Traditional hexagonal macro-cell planning fails in urban "canyons," requiring dense Small Cell deployments.

In **v2.0**, we introduce realistic power constraints and **Dynamic Tower Allocation**. Instead of merely moving a fixed number of towers, the Simulated Annealing (SA) algorithm is now capable of adding new towers to fix dead-zones, and deleting redundant towers to save on Capital Expenditure (CapEx).

### ⚙️ Core Physics & Constraints (v2.0)
* **Propagation Model:** Log-Distance Path Loss with Line-of-Sight blockage penalties (25 dB drop).
* **Realistic Power Constraints:** Transmit power is lowered to a realistic small-cell level ($P_{TX} = 25$ dBm), forcing the creation of signal blind spots.
* **Dynamic Perturbation:** The algorithm uses a probability distribution to determine its next move:
  * **Add Tower:** Boosts coverage but incurs a heavy CapEx penalty ($\alpha \cdot N$).
  * **Remove Tower:** Saves CapEx but risks dropping signal coverage below the threshold.
  * **Move Tower:** Fine-tunes the network mesh.

**Cost Function:**
$$J = \alpha \cdot N + \beta \cdot (1 - P_{cov})$$

## 📊 Simulation Results (v2.0)
By lowering the transmit power, the initial 12 random towers fail to cover the map, creating massive signal shadows and a high initial cost. The SA algorithm aggressively adds towers to reach 100% coverage, and then dynamically **deletes redundant towers** to minimize the $\alpha \cdot N$ cost, successfully finding the lowest-cost configuration.

![v2.0 Results](assets/version2(dynamic).png)
*(Left: Initial placement with heavy blind spots due to realistic $P_{TX}$. Middle: Optimized layout. Right: The convergence curve showing rapid cost reduction as redundant towers are deleted).*

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
