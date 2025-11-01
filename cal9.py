"""
Streamlit Scientific Calculator (Casio fx-991EX Inspired)
----------------------------------------------------------
Features:
- Arithmetic and scientific functions (sin, cos, tan, log, ln, exp, sqrt, factorial, power)
- π, e constants
- Memory (M+, M-, MR, MC)
- LCD-style display and Casio-like button layout
- Clean, visually appealing Streamlit UI

Run:
    pip install streamlit numpy
    streamlit run scientific_calculator.py
"""

import streamlit as st
import math
import numpy as np
from datetime import datetime

# Streamlit Page Setup
st.set_page_config(page_title="Casio fx-991EX", page_icon="🧮", layout="centered")

# -------------------------- Custom Styling --------------------------
st.markdown("""
    <style>
        body {
            background-color: #101010;
        }
        .calculator {
            background: linear-gradient(180deg, #222 0%, #111 100%);
            border-radius: 25px;
            padding: 25px;
            width: 380px;
            margin: auto;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.5);
        }
        .lcd {
            background: linear-gradient(180deg, #ccffcc 0%, #b5ffb5 100%);
