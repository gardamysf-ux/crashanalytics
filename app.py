import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Crash Analytics & Risk Management",
    page_icon="📈",
    layout="wide",
)

st.title("📈 لوحة تحليل ألعاب Crash والمساعد الذكي")
st.markdown("تحليل بيانات الجولات الـ 58 الخاصة بك وإدارة المخاطر.")

# Session State Initialization with your 58 rounds
if "history" not in st.session_state:
    st.session_state.history = [
        1.31,
        2.14,
        5.22,
        5.75,
        2.23,
        1.20,
        3.23,
        1.50,
        1.45,
        1.57,
        1.19,
        2.58,
        2.44,
        5.43,
        1.31,
        1.17,
        1.09,
        3.97,
        1.28,
        3.20,
        1.04,
        1.01,
        1.19,
        4.81,
        1.75,
        9.72,
        1.20,
        1.02,
        1.06,
        6.50,
        5.53,
        1.07,
        3.83,
        1.33,
        1.63,
        1.12,
        2.94,
        26.67,
        4.73,
        1.00,
        2.88,
        1.19,
        1.13,
        1.35,
        1.27,
        1.42,
        1.01,
        3.00,
        2.81,
        16.35,
        3.87,
        29.87,
        1.49,
        22.35,
        1.11,
        3.69,
        2.55,
        6.49,
    ]

if "initial_bankroll" not in st.session_state:
    st.session_state.initial_bankroll = 1000.0

# Sidebar Settings
st.sidebar.header("⚙️ إعدادات رأس المال والحدود")
bankroll = st.sidebar.number_input(
    "رأس المال الحالي (درهم):",
    min_value=10.0,
    value=st.session_state.initial_bankroll,
    step=50.0,
)
stop_loss = st.sidebar.number_input(
    "حد الخسارة الأقصى - Stop Loss (درهم):",
    min_value=0.0,
    value=200.0,
    step=20.0,
)
take_profit = st.sidebar.number_input(
    "هدف الربح - Take Profit (درهم):",
    min_value=0.0,
    value=300.0,
    step=20.0,
)
risk_pct = (
    st.sidebar.slider(
        "نسبة المخاطرة لكل جولة (%):",
        min_value=0.5,
        max_value=10.0,
        value=2.0,
        step=0.5,
    )
    / 100
)

st.sidebar.markdown("---")
st.sidebar.header("➕ إدخال الجولات")
new_val = st.sidebar.number_input(
    "المضاعف (Multiplier):", min_value=1.00, value=1.50, step=0.05
)

if st.sidebar.button("إضافة الجولة"):
    st.session_state.history.append(new_val)
    st.sidebar.success(f"تمت إضافة {new_val}x بنجاح!")

if st.sidebar.button("مسح
