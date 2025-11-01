"""
Beautiful Streamlit Scientific Calculator (Casio fx-991EX Inspired)
File: streamlit_scientific_calculator.py

Run:
    pip install streamlit numpy
    streamlit run streamlit_scientific_calculator.py
"""

import streamlit as st
import math
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .calculator {
            background-color: #1e1e1e;
            border-radius: 25px;
            padding: 25px;
            width: 360px;
            margin: auto;
            box-shadow: 0 6px 20px rgba(0,0,0,0.5);
        }
        .lcd {
            background: #c7ffc2;
            border-radius: 8px;
            padding: 15px;
            text-align: right;
            font-size: 1.5rem;
            font-family: 'Consolas', monospace;
            color: #000;
            margin-bottom: 20px;
            box-shadow: inset 0 0 6px rgba(0,0,0,0.4);
        }
        .btn-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }
        .stButton>button {
            height: 50px !important;
            border-radius: 10px !important;
            border: none;
            font-size: 1.2rem;
            font-weight: 600;
            transition: 0.2s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
        }
        .num { background-color: #303030 !important; color: white !important; }
        .func { background-color: #0078ff !important; color: white !important; }
        .spec { background-color: #ff8c00 !important; color: white !important; }
        .op   { background-color: #505050 !important; color: white !important; }
        .eq   { background-color: #4caf50 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- Session state ---
if "expr" not in st.session_state: st.session_state.expr = ""
if "result" not in st.session_state: st.session_state.result = ""
if "history" not in st.session_state: st.session_state.history = []
if "memory" not in st.session_state: st.session_state.memory = 0.0

st.markdown("<div class='calculator'>", unsafe_allow_html=True)
st.markdown(f"<div class='lcd'>{st.session_state.expr or '0'}</div>", unsafe_allow_html=True)

# --- Button grid layout ---
layout = [
    ["7","8","9","/","sin"],
    ["4","5","6","*","cos"],
    ["1","2","3","-","tan"],
    ["0",".","(",")","+"],
    ["π","e","^","√","log"],
    ["ln","exp","!","%","C"]
]

# --- Button rendering ---
for row in layout:
    cols = st.columns(5)
    for i, key in enumerate(row):
        cls = "num"
        if key in ["sin","cos","tan","√","log","ln","exp"]: cls = "func"
        if key in ["C","!","π","e"]: cls = "spec"
        if key in ["+","-","*","/","^","%"]: cls = "op"

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

# --- Calculate ---
eq_col = st.columns(1)[0]
if eq_col.button("=", use_container_width=True):
    try:
        st.session_state.result = eval(st.session_state.expr)
        st.session_state.history.append((st.session_state.expr, st.session_state.result, datetime.now()))
        st.session_state.expr = str(st.sess_
