"""
Streamlit Calculator App
File: streamlit_calculator.py

How to use:
1. Install Streamlit: pip install streamlit
2. Run: streamlit run streamlit_calculator.py

This single-file app provides:
- Basic arithmetic: + - * /
- Modulo, power, sqrt
- Memory (M+, M-, MR, MC)
- Calculation history stored in session state
- Keyboard-friendly input and a clean layout

Add to GitHub: create a new repo and push this file. Optionally add requirements.txt with `streamlit`.

"""

import streamlit as st
import math
from datetime import datetime

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# --- Helpers ---

def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b
        if op == "%":
            return a % b
        if op == "^":
            return a ** b
    except Exception as e:
        return f"Error: {e}"

    return "Unknown operation"


# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "memory" not in st.session_state:
    st.session_state.memory = 0.0
if "last_result" not in st.session_state:
    st.session_state.last_result = 0.0

# --- UI ---
st.title("🧮 Simple Streamlit Calculator")
st.write("A clean, single-file calculator you can drop into a GitHub repository and run with `streamlit run`.")

col1, col2 = st.columns([2, 1])

with col1:
    with st.form(key="calc_form"):
        num1 = st.text_input("First number", value=str(st.session_state.get("last_input1", "")))
        op = st.selectbox("Operation", ["+", "-", "*", "/", "%", "^"])
        num2 = st.text_input("Second number", value=str(st.session_state.get("last_input2", "")))
        submitted = st.form_submit_button("Calculate")

    # quick unary operations
    st.markdown("**Unary operations (apply to first number)**")
    ucol1, ucol2, ucol3 = st.columns(3)
    if ucol1.button("√ (sqrt)"):
        try:
            val = float(num1)
            result = math.sqrt(val)
            op_str = f"√({val})"
            st.session_state.history.append((op_str, result, datetime.now()))
            st.session_state.last_result = result
        except Exception as e:
            st.error(f"Error: {e}")
    if ucol2.button("1/x (reciprocal)"):
        try:
            val = float(num1)
            result = 1.0 / val
            op_str = f"1/({val})"
            st.session_state.history.append((op_str, result, datetime.now()))
            st.session_state.last_result = result
        except Exception as e:
            st.error(f"Error: {e}")
    if ucol3.button("± (negate)"):
        try:
            val = float(num1)
            result = -val
            op_str = f"negate({val})"
            st.session_state.history.append((op_str, result, datetime.now()))
            st.session_state.last_result = result
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    st.subheader("Memory")
    st.write(f"**Stored:** {st.session_state.memory}")
    mcol1, mcol2 = st.columns(2)
    if mcol1.button("M+"):
        try:
            st.session_state.memory += float(st.session_state.last_result)
        except Exception:
            st.error("No numeric last result to add to memory")
    if mcol2.button("M-"):
        try:
            st.session_state.memory -= float(st.session_state.last_result)
        except Exception:
            st.error("No numeric last result to subtract from memory")

    mcol3, mcol4 = st.columns(2)
    if mcol3.button("MR"):
        st.info(f"Memory recall: {st.session_state.memory}")
    if mcol4.button("MC"):
        st.session_state.memory = 0.0
        st.success("Memory cleared")


# Perform calculation when form submitted
if 'submitted' in locals() and submitted:
    try:
        a = float(num1)
    except Exception:
        st.error("First number is not a valid number")
        a = None
    try:
        b = float(num2)
    except Exception:
        st.error("Second number is not a valid number")
        b = None

    if a is not None and b is not None:
        result = calculate(a, b, op)
        st.session_state.history.append((f"{a} {op} {b}", result, datetime.now()))
        st.session_state.last_result = result
        st.session_state.last_input1 = num1
        st.session_state.last_input2 = num2
        st.success(f"Result: {result}")

# Show last result prominently
if st.session_state.last_result is not None:
    st.markdown("---")
    st.subheader("Last result")
    st.write(st.session_state.last_result)

# History
with st.expander("Calculation history"):
    if len(st.session_state.history) == 0:
        st.write("No calculations yet.")
    else:
        for item, res, ts in reversed(st.session_state.history[-20:]):
            st.write(f"`{ts.strftime('%Y-%m-%d %H:%M:%S')}` — **{item}** = `{res}`")

# Small footer with GitHub instructions
st.markdown("---")
st.write("To add to GitHub: create a repo, add this file (`streamlit_calculator.py`) and push. Add a `requirements.txt` containing `streamlit`.")

# Helpful keyboard tip (can't capture keyboard globally without extra JS)
st.info("Tip: use the inputs and press Calculate. For advanced keyboard shortcuts you can extend this app with Streamlit's components.")

# End of file
