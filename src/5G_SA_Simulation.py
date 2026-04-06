import numpy as np
import matplotlib.pyplot as plt
import random
import math

# ==========================================
# 1. SIMULATION PARAMETERS & PHYSICS (v2.0)
# ==========================================
GRID_SIZE = 100         # 100x100 grid (e.g., 10m per cell = 1km x 1km)
P_TX = 25               # Lowered transmit power to force blind spots
N_PATH_LOSS = 3.5       # Path loss exponent for urban area
FREQ_GHZ = 28           # 28 GHz mmWave
BLOCKAGE_PENALTY = 25   # dB penalty for hitting a building
THRESHOLD = -90         # Minimum acceptable signal (dBm)

ALPHA = 10              # Cost weight for number of towers
BETA = 10000            # Massive penalty weight for uncovered area

# Define buildings as (x_min, x_max, y_min, y_max)
BUILDINGS = [
    (20, 30, 20, 60), (50, 70, 40, 50), (70, 85, 70, 90), (10, 25, 80, 95)
]

# ==========================================
# 2. CORE MATH & COST FUNCTION
# ==========================================
def is_blocked(tx_x, tx_y, rx_x, rx_y):
    """Simplified Line-of-Sight check."""
    for (xmin, xmax, ymin, ymax) in BUILDINGS:
        if xmin <= rx_x <= xmax and ymin <= rx_y <= ymax:
            return True 
    return False

def calculate_coverage(towers):
    """Calculates the best signal strength at every point on the grid."""
    coverage_map = np.full((GRID_SIZE, GRID_SIZE), -150.0)
    
    for tx_x, tx_y in towers:
        for rx_x in range(GRID_SIZE):
            for rx_y in range(GRID_SIZE):
                dist = math.hypot(tx_x - rx_x, tx_y - rx_y)
                if dist < 1: dist = 1
                
                pl = 20 * math.log10(dist) + 10 * N_PATH_LOSS * math.log10(dist)
                
                if is_blocked(tx_x, tx_y, rx_x, rx_y):
                    pl += BLOCKAGE_PENALTY
                    
                rx_power = P_TX - pl
                
                if rx_power > coverage_map[rx_x, rx_y]:
                    coverage_map[rx_x, rx_y] = rx_power
                    
    covered_cells = np.sum(coverage_map >= THRESHOLD)
    p_cov = covered_cells / (GRID_SIZE * GRID_SIZE)
    return coverage_map, p_cov

def cost_function(towers):
    """J = alpha*N + beta*(1 - P_cov)"""
    _, p_cov = calculate_coverage(towers)
    return ALPHA * len(towers) + BETA * (1 - p_cov), p_cov

# ==========================================
# 3. SIMULATED ANNEALING ENGINE (Dynamic)
# ==========================================
def run_simulated_annealing(initial_towers, t_init=1000, cooling_rate=0.90, max_iter=200):
    print("Starting Simulated Annealing (v2.0 - Dynamic Towers)...")
    current_towers = initial_towers.copy()
    current_cost, current_cov = cost_function(current_towers)
    
    best_towers = current_towers.copy()
    best_cost = current_cost
    
    T = t_init
    history_cost = []
    
    for i in range(max_iter):
        # 1. PERTURBATION: Move, Add, or Remove a tower
        new_towers = current_towers.copy()
        action = random.random()
        
        if action < 0.2 and len(new_towers) > 1:
            # 20% chance to remove a random tower (Saves CapEx cost!)
            new_towers.pop(random.randint(0, len(new_towers) - 1))
        elif action < 0.4:
            # 20% chance to add a new tower (Boosts coverage!)
            new_towers.append((random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)))
        else:
            # 60% chance to just move an existing tower
            idx = random.randint(0, len(new_towers) - 1)
            shift_x = random.randint(-15, 15)
            shift_y = random.randint(-15, 15)
            new_x = max(0, min(GRID_SIZE - 1, new_towers[idx][0] + shift_x))
            new_y = max(0, min(GRID_SIZE - 1, new_towers[idx][1] + shift_y))
            new_towers[idx] = (new_x, new_y)
            
        # 2. EVALUATE
        new_cost, new_cov = cost_function(new_towers)
        delta_J = new_cost - current_cost
        
        # 3. METROPOLIS ACCEPTANCE CRITERION
        if delta_J < 0:
            current_towers = new_towers.copy()
            current_cost = new_cost
            current_cov = new_cov
            if current_cost < best_cost:
                best_towers = current_towers.copy()
                best_cost = current_cost
        else:
            probability = math.exp(-delta_J / T)
            if random.random() < probability:
                current_towers = new_towers.copy() # Accept bad move
                current_cost = new_cost
                current_cov = new_cov
                
        history_cost.append(current_cost)
        
        # 4. COOLING
        T *= cooling_rate
        print(f"Iter {i}: Cost = {current_cost:.2f} | Coverage = {current_cov*100:.1f}% | Towers = {len(current_towers)} | Temp = {T:.2f}")

    return best_towers, history_cost

# ==========================================
# 4. EXECUTION & VISUALIZATION
# ==========================================
if __name__ == "__main__":
    np.random.seed(42)
    start_towers = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(12)]
    
    optimized_towers, cost_curve = run_simulated_annealing(start_towers)
    
    map_initial, cov_initial = calculate_coverage(start_towers)
    map_final, cov_final = calculate_coverage(optimized_towers)
    
    # --- PLOTTING ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    im1 = axes[0].imshow(map_initial.T, origin='lower', cmap='RdYlGn', vmin=-110, vmax=-50)
    axes[0].scatter([t[0] for t in start_towers], [t[1] for t in start_towers], c='blue', marker='^', s=100, label='Towers')
    for b in BUILDINGS: axes[0].add_patch(plt.Rectangle((b[0], b[2]), b[1]-b[0], b[3]-b[2], color='black', alpha=0.5))
    axes[0].set_title(f"Initial Random Placement ({cov_initial*100:.1f}% Cov)")
    axes[0].legend()
    
    im2 = axes[1].imshow(map_final.T, origin='lower', cmap='RdYlGn', vmin=-110, vmax=-50)
    axes[1].scatter([t[0] for t in optimized_towers], [t[1] for t in optimized_towers], c='blue', marker='^', s=100)
    for b in BUILDINGS: axes[1].add_patch(plt.Rectangle((b[0], b[2]), b[1]-b[0], b[3]-b[2], color='black', alpha=0.5))
    axes[1].set_title(f"SA Optimized Placement ({cov_final*100:.1f}% Cov)")
    
    axes[2].plot(cost_curve, color='purple', linewidth=2)
    axes[2].set_title("Simulated Annealing Convergence")
    axes[2].set_xlabel("Iterations")
    axes[2].set_ylabel("Cost Function (J)")
    axes[2].grid(True)
    
    plt.colorbar(im2, ax=axes.ravel().tolist()[:2], label="Signal Strength (dBm)")
    plt.show()