"""
Casio fx-991EX Style Scientific Calculator
------------------------------------------
Built with Streamlit and Python

Features:
- Arithmetic and scientific functions (sin, cos, tan, log, ln, exp, sqrt, factorial, power)
- π, e constants
- Memory functions (M+, M-, MR, MC)
- LCD-style display and Casio-inspired layout
- Clean, beautiful UI ready for GitHub and Streamlit Cloud deployment
"""

import streamlit as st
import math
import numpy as np
from datetime import datetime

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(page_title="Casio fx-991EX", page_icon="🧮", layout="centered")

# ---------------------------- CUSTOM STYLE ----------------------------
st.markdown("""
    <style>
        body {
            background-color: #101010;
        }
        .calculator {
            background: linear-gradient(180deg, #222 0%, #111 100%);
            border-radius: 25px;
            padding: 25px;
            width: 390px;
            margin: auto;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
        }
        .lcd {
            background: linear-gradient(180deg, #cfffcc 0%, #b5ffb5 100%);
            border: 2px solid #555;
            border-radius: 10px;
            padding: 18px;
            text-align: right;
            font-size: 1.6rem;
            font-family: 'Consolas', monospace;
            color: #000;
            margin-bottom: 20px;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        }
        .stButton>button {
            height: 52px !important;
            width: 100% !important;
            border-radius: 10px !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            border: none !important;
            transition: 0.2s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.07);
            box-shadow: 0 0 8px rgba(255,255,255,0.4);
        }
        .num { background-color: #303030 !important; color: #fff !important; }
        .op { background-color: #505050 !important; color: #fff !important; }
        .func { background-color: #0078ff !important; color: white !important; }
        .spec { background-color: #ff8c00 !important; color: white !important; }
        .eq { background-color: #4caf50 !important; color: white !important; }
        h1, h2, h3, h4, h5, h6, p {
            color: white !important;
            text-align: center !important;
        }
        .memory {
            color: #ffeb3b;
            text-align: center;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------- STATE ----------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""
if "result" not in st.session_state:
    st.session_state.result = ""
if "history" not in st.session_state:
    st.session_state.history = []
if "memory" not in st.session_state:
    st.session_state.memory = 0.0

# ---------------------------- CALCULATOR DISPLAY ----------------------------
st.markdown("<div class='calculator'>", unsafe_allow_html=True)
st.markdown(f"<div class='lcd'>{st.session_state.expr or '0'}</div>", unsafe_allow_html=True)

# ---------------------------- BUTTON LAYOUT ----------------------------
layout = [
    ["7","8","9","/","sin"],
    ["4","5","6","*","cos"],
    ["1","2","3","-","tan"],
    ["0",".","(",")","+"],
    ["π","e","^","√","log"],
    ["ln","exp","!","%","C"]
]

# ---------------------------- BUTTON GRID ----------------------------
for row in layout:
    cols = st.columns(5)
    for i, key in enumerate(row):
        cls = "num"
        if key in ["+","-","*","/","^","%"]: cls = "op"
        elif key in ["sin","cos","tan","√","log","ln","exp"]: cls = "func"
        elif key in ["π","e","C","!"]: cls = "spec"

        if cols[i].button(key, key=f"{row}-{i}", use_container_width=True):
            if key == "C":
                st.session_state.expr = ""
            elif key == "π":
                st.session_state.expr += "math.pi"
            elif key == "e":
                st.session_state.expr += "math.e"
            elif key == "√":
                st.session_state.expr += "math.sqrt("
            elif key == "sin":
                st.session_state.expr += "math.sin("
            elif key == "cos":
                st.session_state.expr += "math.cos("
            elif key == "tan":
                st.session_state.expr += "math.tan("
            elif key == "log":
                st.session_state.expr += "math.log10("
            elif key == "ln":
                st.session_state.expr += "math.log("
            elif key == "exp":
                st.session_state.expr += "math.exp("
            elif key == "!":
                st.session_state.expr += "math.factorial("
            else:
                st.session_state.expr += key

# ---------------------------- CALCULATE ----------------------------
if st.button("=", use_container_width=True):
    try:
        st.session_state.result = eval(st.session_state.expr)
        st.session_state.history.append((st.session_state.expr, st.session_state.result, datetime.now()))
        st.session_state.expr = str(st.session_state.result)
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------------------- MEMORY ----------------------------
st.markdown("---")
st.subheader("Memory")
m1, m2, m3, m4 = st.columns(4)
if m1.button("M+"): st.session_state.memory += float(st.session_state.result or 0)
if m2.button("M-"): st.session_state.memory -= float(st.session_state.result or 0)
if m3.button("MR"): st.session_state.expr += str(st.session_state.memory)
if m4.button("MC"): st.session_state.memory = 0.0
st.markdown(f"<div class='memory'>Memory: {st.session_state.memory}</div>", unsafe_allow_html=True)

# ---------------------------- HISTORY ----------------------------
st.markdown("---")
st.subheader("History")
if len(st.session_state.history) == 0:
    st.write("No calculations yet.")
else:
    for expr, res, ts in reversed(st.session_state.history[-10:]):
        st.write(f"`{ts.strftime('%H:%M:%S')}` — **{expr}** = `{res}`")

st.markdown("</div>", unsafe_allow_html=True)
st.caption("© 2025 Casio fx-991EX Style Scientific Calculator | Built with Streamlit")
