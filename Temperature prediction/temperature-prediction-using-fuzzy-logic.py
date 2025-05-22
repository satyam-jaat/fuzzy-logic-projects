import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define fuzzy variables
room_temp = ctrl.Antecedent(np.arange(0, 41, 1), 'room_temp')
heater_power = ctrl.Antecedent(np.arange(0, 11, 1), 'heater_power')
final_temp = ctrl.Consequent(np.arange(0, 51, 1), 'final_temp')

# Membership functions
room_temp['cold'] = fuzz.trimf(room_temp.universe, [0, 0, 20])
room_temp['warm'] = fuzz.trimf(room_temp.universe, [10, 20, 30])
room_temp['hot'] = fuzz.trimf(room_temp.universe, [25, 40, 40])

heater_power['low'] = fuzz.trimf(heater_power.universe, [0, 0, 5])
heater_power['medium'] = fuzz.trimf(heater_power.universe, [3, 5, 7])
heater_power['high'] = fuzz.trimf(heater_power.universe, [5, 10, 10])

final_temp['cold'] = fuzz.trimf(final_temp.universe, [0, 0, 25])
final_temp['moderate'] = fuzz.trimf(final_temp.universe, [20, 30, 40])
final_temp['hot'] = fuzz.trimf(final_temp.universe, [35, 50, 50])

# Define fuzzy rules
rules = [
    ctrl.Rule(room_temp['cold'] & heater_power['low'], final_temp['cold']),
    ctrl.Rule(room_temp['cold'] & heater_power['medium'], final_temp['moderate']),
    ctrl.Rule(room_temp['cold'] & heater_power['high'], final_temp['hot']),
    
    ctrl.Rule(room_temp['warm'] & heater_power['low'], final_temp['cold']),
    ctrl.Rule(room_temp['warm'] & heater_power['medium'], final_temp['moderate']),
    ctrl.Rule(room_temp['warm'] & heater_power['high'], final_temp['hot']),
    
    ctrl.Rule(room_temp['hot'] & heater_power['low'], final_temp['moderate']),
    ctrl.Rule(room_temp['hot'] & heater_power['medium'], final_temp['hot']),
    ctrl.Rule(room_temp['hot'] & heater_power['high'], final_temp['hot']),
]

# Create control system
system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(system)

# Take user input
temp = float(input("Enter room temperature (0–40°C): "))
power = float(input("Enter heater power (0–10): "))

# Set inputs
sim.input['room_temp'] = temp
sim.input['heater_power'] = power

# Compute fuzzy output
sim.compute()
result = sim.output['final_temp']

# Print result
print(f"\n🔥 Predicted Final Temperature: {result:.1f}°C")

# Plot membership functions
def plot_membership_functions():
    room_temp.view()
    heater_power.view()
    final_temp.view()

# Plot control surface
def plot_control_surface():
    x = np.arange(0, 41, 1)
    y = np.arange(0, 11, 1)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    temp_sim = ctrl.ControlSystemSimulation(system)

    for i in range(len(x)):
        for j in range(len(y)):
            temp_sim.input['room_temp'] = x[i]
            temp_sim.input['heater_power'] = y[j]
            temp_sim.compute()
            Z[j, i] = temp_sim.output['final_temp']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Room Temperature (°C)')
    ax.set_ylabel('Heater Power')
    ax.set_zlabel('Predicted Final Temperature (°C)')
    ax.set_title('Fuzzy Control Surface')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    plt.show()

# Ask user whether to show visualizations
if input("\n📊 Show membership functions? (y/n): ").lower().startswith('y'):
    plot_membership_functions()

if input("🧮 Show control surface (3D)? (y/n): ").lower().startswith('y'):
    plot_control_surface()
