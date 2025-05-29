import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

turbidity = np.arange(0,11,2)
ph_level = np.arange(0,15,1)
water_quality = np.arange(0,11,1)

turbidity_low = fuzz.trapmf(turbidity, [0,0,2,4])
turbidity_medium = fuzz.trimf(turbidity, [2,5,8])
turbidity_high = fuzz.trapmf(turbidity, [6,8,10,10])

ph_low = fuzz.trapmf(ph_level, [0,0,4,6])
ph_medium = fuzz.trimf(ph_level, [4,7,10])
ph_high = fuzz.trapmf(ph_level, [8,10,14,14])

quality_poor = fuzz.trapmf(water_quality, [0,0,3,5])
quality_moderate = fuzz.trimf(water_quality, [3,5,7])
quality_good = fuzz.trapmf(water_quality, [6,8,10,10])

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(turbidity, turbidity_low, label="Low Turbidity")
plt.plot(turbidity, turbidity_medium, label="Medium Turbidity")
plt.plot(turbidity, turbidity_high, label="High Turbidity")
plt.xlabel("Turbidity")
plt.ylabel("Membership Function")
plt.legend()

plt.figure(figsize=(12,8))
plt.subplot(2,2,2)
plt.plot(ph_level, ph_low, label="Low PH Level")
plt.plot(ph_level, ph_medium, label="Medium PH Level")
plt.plot(ph_level, ph_high, label="High PH Level")
plt.xlabel("PH Level")
plt.ylabel("Membership Function")
plt.legend()

plt.figure(figsize=(12,8))
plt.subplot(2,2,3)
plt.plot(water_quality, quality_poor, label="Poor Water Quality")
plt.plot(water_quality, quality_moderate, label="Moderate Water Quality")
plt.plot(water_quality, quality_good, label="Good Water Quality")
plt.xlabel("Water Quality")
plt.ylabel("Membership Function")
plt.legend()

plt.show()

turbidity_input = 7
ph_input = 6

turbidity_level_low = fuzz.interp_membership(turbidity, turbidity_low, turbidity_input)
turbidity_level_medium = fuzz.interp_membership(turbidity, turbidity_medium,turbidity_input)
turbidity_level_high = fuzz.interp_membership(turbidity, turbidity_high,turbidity_input)

ph_level_low = fuzz.interp_membership(ph_level, ph_low, ph_input)
ph_level_medium = fuzz.interp_membership(ph_level, ph_medium, ph_input)
ph_level_high = fuzz.interp_membership(ph_level, ph_high, ph_input)

rule1 = min(turbidity_level_low, ph_level_medium)
rule2 = min(turbidity_level_medium, ph_level_medium)
rule3 = min(turbidity_level_high, ph_level_low)

water_quality_level = fuzz.defuzz(water_quality, quality_poor *rule1 + quality_moderate * rule2 + quality_good * rule3, 'centroid')

print(f"Water Quality: {water_quality_level}")

if water_quality_level <= 3:
  print("Poor Water Quality")
elif water_quality_level <= 7:
  print("Moderate Water Quality")
else:
  print("Good Water Quality")
