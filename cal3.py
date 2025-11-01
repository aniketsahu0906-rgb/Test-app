"""
Streamlit Scientific Calculator (Casio fx-991EX Style)
File: streamlit_scientific_calculator.py

How to use:
1. Install Streamlit: pip install streamlit
2. Run: streamlit run streamlit_scientific_calculator.py
3. Upload to GitHub as a single file or with requirements.txt containing `streamlit`, `numpy`.

This app replicates the layout and functions of a Casio fx-991-style calculator.
Includes:
- Basic arithmetic (+, -, ×, ÷)
- Scientific functions (sin, cos, tan, log, ln, exp, sqrt, factorial, power)
- Memory (M+, M-, MR, MC)
- Constants (π, e)
- Expression input and evaluation
- Calculation history

"""

import streamlit as st
import math
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Casio fx-991EX Calculator", page_icon="🧮", layout="centered")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "memory" not in st.session_state:
    st.session_state.memory = 0.0

# --- Header ---
st.title("🧮 Casio fx-991EX Style Scientific Calculator")
st.caption("A full-featured Streamlit scientific calculator inspired by Casio 991EX.")

# --- Input Area ---
st.markdown("### Enter Expression")
expression = st.text_input("Expression (e.g. sin(pi/4) + log(10))", value="", placeholder="Type your math expression here...")

# --- Buttons Layout (Casio-style grid) ---
col_layout = [
    ["7", "8", "9", "/", "sin"],
    ["4", "5", "6", "*", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "(", ")", "+"],
    ["π", "e", "^", "√", "log"],
    ["ln", "exp", "!", "%", "C"]
]

st.markdown("### Keypad")

for row in col_layout:
    cols = st.columns(len(row))
    for i, key in enumerate(row):
        if cols[i].button(key):
            if key == "C":
                expression = ""
            elif key == "π":
                expression += "math.pi"
            elif key == "e":
                expression += "math.e"
            elif key == "√":
                expression += "math.sqrt("
            elif key == "sin":
                expression += "math.sin("
            elif key == "cos":
                expression += "math.cos("
            elif key == "tan":
                expression += "math.tan("
            elif key == "log":
                expression += "math.log10("
            elif key == "ln":
                expression += "math.log("
            elif key == "exp":
                expression += "math.exp("
            elif key == "!":
                expression += "math.factorial("
            else:
                expression += key

st.markdown(f"**Expression:** `{expression}`")

# --- Evaluate Expression ---
if st.button("= Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
        st.session_state.history.append((expression, result, datetime.now()))
    except Exception as e:
        st.error(f"Error: {e}")

# --- Memory Buttons ---
colM1, colM2, colM3, colM4 = st.columns(4)

if colM1.button("M+"):
    try:
        st.session_state.memory += float(result)
        st.success(f"Memory: {st.session_state.memory}")
    except Exception:
        st.error("No valid result to add to memory.")

if colM2.button("M-"):
    try:
        st.session_state.memory -= float(result)
        st.success(f"Memory: {st.session_state.memory}")
    except Exception:
        st.error("No valid result to subtract from memory.")

if colM3.button("MR"):
    st.info(f"Memory Recall: {st.session_state.memory}")

if colM4.button("MC"):
    st.session_state.memory = 0.0
    st.success("Memory cleared.")

# --- History ---
st.markdown("### Calculation History")
if len(st.session_state.history) == 0:
    st.write("No calculations yet.")
else:
    for expr, res, ts in reversed(st.session_state.history[-10:]):
        st.write(f"`{ts.strftime('%H:%M:%S')}` — **{expr}** = `{res}`")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Casio-style Calculator | Built with Streamlit. Push this file to GitHub with a requirements.txt containing 'streamlit' and 'numpy'.")
