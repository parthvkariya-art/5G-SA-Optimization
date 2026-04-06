# 5G mm-Wave Small Cell Optimization using Simulated Annealing (v3.0)

A Python-based simulation engine that models city grids to optimize the deployment of 5G mm-Wave base stations.

**Author:** Parth Vinod Kariya  
**Institution:** MAHE Bengaluru  

## 🚀 Project Overview (v3.0 - Dense Urban & ISD Constraints)
High-frequency 5G mm-Wave signals (24-100 GHz) suffer from severe atmospheric absorption and solid blockages. Traditional hexagonal macro-cell planning fails in urban "canyons," requiring dense Small Cell deployments.

In **v3.0**, we scale the complexity of the environment and the strictness of the algorithm. We introduce a highly dense urban grid, ultra-low transmit power, and an **Inter-Site Distance (ISD)** penalty. This forces the algorithm to not only find coverage but to build a perfectly distributed mesh network that avoids signal interference.

### ⚙️ Core Physics & Constraints (v3.0)
* **Dense Urban Environment:** A complex map of "urban canyons" with an increased path loss exponent ($N=4.2$) and ultra-low transmit power ($P_{TX} = 10$).
* **Inter-Site Distance Constraint:** A strict 5000-point penalty is applied if any two towers are placed closer than 15 meters to each other.
* **Cooling Schedule:** Because the mathematical terrain is now much harder to navigate, the Simulated Annealing engine has been stretched to 300 iterations with a slower cooling rate ($0.96$).

**Cost Function:**

$$
J = \alpha \cdot N + \beta \cdot (1 - P_{cov}) + \text{ISD\_Penalty}
$$

## 📊 Simulation Results (v3.0)
The algorithm successfully starts with a random, highly-shadowed layout in a dense city block. It dynamically adds towers to blast through the dead zones, and thanks to the ISD penalty, it spaces them perfectly apart. The convergence curve shows a prolonged, classic thermodynamic cooling process as it rejects bad placements.

![v3.0 Results](assets/version3(isd).png)
*(Left: Initial random placement failing in the dense city. Middle: SA optimized layout showing perfectly spaced, interference-free tower placement. Right: The extended thermodynamic cooling convergence curve).*

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
