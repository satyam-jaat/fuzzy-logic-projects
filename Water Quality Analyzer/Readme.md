# 💧 Water Quality Analyzer Using Fuzzy Logic

A fuzzy logic-based system to assess water quality based on turbidity and pH level measurements.

---

## 🔍 Overview

This project demonstrates how **fuzzy logic** can be applied to model real-world uncertainties in determining the **quality of water**. The system processes two main water quality parameters — **turbidity** and **pH level** — to infer whether the water is **Poor**, **Moderate**, or **Good** in quality.

---

## 📌 Features

- ✅ Predicts water quality based on **fuzzy inference rules**
- ✅ Visualizes **fuzzy membership functions** for Turbidity, pH, and Water Quality
- ✅ Implements **realistic fuzzy rules** to simulate human-like decision-making
- ✅ Uses **`skfuzzy`**, a powerful fuzzy logic library in Python
- ✅ Simple and **modular code structure** for easy extension
- ✅ Outputs both **numerical quality score** and **linguistic quality category** (Poor/Moderate/Good)

---

## 🧪 Inputs

- **Turbidity**: Water cloudiness, measured on a scale from 0 to 10
- **pH Level**: Acidity or alkalinity of water, measured from 0 to 14

---

## 📤 Output

- **Water Quality Score**: A value between 0 and 10

---

## 🛠️ Requirements

- Python 3.x
- `numpy`
- `matplotlib`
- `scikit-fuzzy` (`skfuzzy`)

Install dependencies using:

```bash
pip install numpy matplotlib scikit-fuzzy
