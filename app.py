
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HomeMind AI | Smart Energy",
    page_icon="🏠",
    layout="wide"
)

# -------------------- CALCULATIONS --------------------

LIGHT_MAX = 10
FAN_MAX = 50
HOURS_PER_DAY = 5
DAYS_PER_MONTH = 30
RATE = 8

# -------------------- PREMIUM DESIGN --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #20245a 0%, transparent 35%),
        radial-gradient(ellipse at 90% 10%, #142e50 0%, transparent 35%),
        #090d1b;
    color: #f5f7ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3, p, label {
    color: #f5f7ff;
}

.hero {
    padding: 30px;
    border-radius: 25px;
    background: linear-gradient(120deg, #202b55, #17213e 60%, #29205a);
    border: 1px solid rgba(255,255,255,0.10);
    margin-bottom: 25px;
}

.hero-tag {
    color: #9cafff;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}

.hero-title {
    font-size: 38px;
    font-weight: 800;
    margin: 8px 0;
    color: white;
}

.hero-sub {
    color: #b9c4e3;
    font-size: 15px;
}

.section-title {
    font-size: 21px;
    font-weight: 750;
    margin: 25px 0 14px;
}

.device-card {
    background: linear-gradient(145deg, #171f39, #11182c);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 23px;
    padding: 22px;
    min-height: 420px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.20);
}

.device-heading {
    font-size: 20px;
    font-weight: 750;
    color: white;
}

.device-caption {
    color: #9daacb;
    font-size: 12px;
    margin-top: 3px;
}

.device-value {
    color: #9db6ff;
    font-size: 25px;
    font-weight: 800;
    text-align: center;
    margin-top: 5px;
}

.arc {
    height: 24px;
    width: 75%;
    margin: 12px auto -2px;
    border-top: 4px solid #788cff;
    border-radius: 100% 100% 0 0;
    filter: drop-shadow(0 0 8px #687aff);
}

.stSlider {
    padding-left: 5px;
    padding-right: 5px;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    height: 32px;
}

div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    width: 23px !important;
    height: 23px !important;
    border: 4px solid white !important;
    box-shadow: 0 0 12px #879cff !important;
}

div[data-testid="stSlider"] [data-testid="stTickBar"] {
    display: none;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div {
    border-radius: 20px;
}

div[data-testid="stSlider"] [data-baseweb="slider"] div[data-testid="stThumbValue"] {
    color: white;
}

.metric-card {
    background: linear-gradient(145deg, #192442, #111a30);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 20px;
    min-height: 115px;
}

.metric-label {
    font-size: 12px;
    color: #9baaca;
    font-weight: 600;
}

.metric-number {
    font-size: 27px;
    font-weight: 800;
    color: white;
    margin-top: 8px;
}

.metric-note {
    font-size: 11px;
    color: #7f92ba;
    margin-top: 4px;
}

.bill-card {
    background: linear-gradient(120deg, #293d82, #49318a);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 22px;
    padding: 25px;
    margin-top: 15px;
}

.bill-number {
    font-size: 38px;
    font-weight: 800;
    color: white;
}

.bill-caption {
    color: #d0d8ff;
    font-size: 13px;
}

.info-box {
    background: #121d34;
    border: 1px solid #26385f;
    border-radius: 15px;
    padding: 16px;
    color: #b9c7e8;
    font-size: 12px;
}

div[data-testid="stMetric"] {
    background: transparent;
}

.stMarkdown, .stCaption {
    color: #dce5ff;
}

div[data-testid="stSlider"] p {
    color: #c5d1ee;
}

.stProgress > div > div > div {
    background: linear-gradient(90deg, #4f8cff, #a36bff);
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">INTELLIGENT LIVING • ENERGY INSIGHTS</div>
    <div class="hero-title">🏠 HomeMind AI</div>
    <div class="hero-sub">
        Your smart home energy companion. Control, monitor and predict
        your household electricity consumption.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🎛️ Smart Room Controls</div>',
            unsafe_allow_html=True)

# -------------------- DEVICE CONTROLS --------------------

left, right = st.columns(2, gap="large")

with left:
    st.markdown("""
    <div class="device-card">
        <div class="device-heading">💡 Smart Lighting</div>
        <div class="device-caption">Adjust your room's light intensity</div>
        <div class="arc"></div>
    </div>
    """, unsafe_allow_html=True)

    light = st.slider(
        "Light intensity",
        min_value=0,
        max_value=100,
        value=75,
        format="%d%%",
        key="light_control"
    )

    st.markdown(f"""
    <div class="device-value">{light}%</div>
    """, unsafe_allow_html=True)

    # Animated bulb illustration
    brightness = 0.15 + (light / 100) * 0.85
    glow = 5 + light * 0.35

    components.html(f"""
    <div style="
        background:linear-gradient(145deg,#171f39,#11182c);
        border:1px solid rgba(255,255,255,.1);
        border-radius:0 0 23px 23px;
        margin-top:-5px;
        padding:20px;
        text-align:center;
        height:220px;
        box-sizing:border-box;
    ">
      <svg width="180" height="165" viewBox="0 0 180 165">
        <defs>
          <radialGradient id="bulbGlow">
            <stop offset="0%" stop-color="#fff8bb"
              stop-opacity="{brightness}"/>
            <stop offset="100%" stop-color="#ffc857"
              stop-opacity="0"/>
          </radialGradient>
        </defs>
        <circle cx="90" cy="69" r="66"
          fill="url(#bulbGlow)"
          style="filter:blur(5px)"/>
        <g opacity="{brightness}">
          <path d="M90 20 C61 20 45 43 50 69
            C53 86 67 92 70 110 L110 110
            C113 92 127 86 130 69
            C135 43 119 20 90 20Z"
            fill="#ffe69a"
            stroke="#fff1c1"
            stroke-width="3"
            style="filter:drop-shadow(0 0 {glow}px #ffdc73)"/>
          <path d="M73 111 H107 M75 120 H105 M79 129 H101"
            stroke="#c2cbe0" stroke-width="5"
            stroke-linecap="round"/>
        </g>
        <path d="M90 20 C61 20 45 43 50 69
          C53 86 67 92 70 110 L110 110
          C113 92 127 86 130 69
          C135 43 119 20 90 20Z"
          fill="none" stroke="#7d8bab" stroke-width="2"/>
        <path d="M81 140 H99" stroke="#aab8d8"
          stroke-width="4" stroke-linecap="round"/>
      </svg>
      <div style="color:#aab8d8;font-size:12px">
        {"LIGHT ON" if light > 0 else "LIGHT OFF"}
      </div>
    </div>
    """, height=230)

with right:
    st.markdown("""
    <div class="device-card">
        <div class="device-heading">🌀 Smart Fan</div>
        <div class="device-caption">Control the speed of your ceiling fan</div>
        <div class="arc"></div>
    </div>
    """, unsafe_allow_html=True)

    fan = st.slider(
        "Fan speed",
        min_value=0,
        max_value=100,
        value=60,
        format="%d%",
        key="fan_control"
    )

    st.markdown(f"""
    <div class="device-value">{fan}%</div>
    """, unsafe_allow_html=True)

    # Fan animation speed
    duration = max(0.15, 3.5 - (fan / 100) * 3.35)

    components.html(f"""
    <div style="
        background:linear-gradient(145deg,#171f39,#11182c);
        border:1px solid rgba(255,255,255,.1);
        border-radius:0 0 23px 23px;
        margin-top:-5px;
        padding:15px;
        text-align:center;
        height:220px;
        box-sizing:border-box;
    ">
      <svg width="190" height="165" viewBox="0 0 190 165">
        <g style="
          transform-origin:95px 75px;
          animation:spin {duration}s linear infinite;
          animation-play-state:{'running' if fan > 0 else 'paused'};
        ">
          <path d="M95 75 C70 65 48 30 65 20
            C83 10 103 45 95 75Z"
            fill="#76aaff" stroke="#b5d4ff" stroke-width="2"/>
          <path d="M95 75 C120 65 150 45 158 62
            C166 80 125 94 95 75Z"
            fill="#76aaff" stroke="#b5d4ff" stroke-width="2"/>
          <path d="M95 75 C105 100 115 135 96 143
            C77 151 76 105 95 75Z"
            fill="#76aaff" stroke="#b5d4ff" stroke-width="2"/>
        </g>
        <circle cx="95" cy="75" r="10"
          fill="#d9e8ff" stroke="#82aaff" stroke-width="3"/>
        <path d="M95 86 V105 M65 105 H125"
          stroke="#7185aa" stroke-width="5"
          stroke-linecap="round"/>
        <path d="M75 105 H115"
          stroke="#9baed0" stroke-width="5"
          stroke-linecap="round"/>
      </svg>
      <style>
        @keyframes spin {
          from { transform:rotate(0deg); }
          to { transform:rotate(360deg); }
        }
      </style>
      <div style="color:#aab8d8;font-size:12px">
        {"FAN RUNNING" if fan > 0 else "FAN STOPPED"}
      </div>
    </div>
    """, height=230)

# -------------------- ENERGY CALCULATIONS --------------------

light_power = LIGHT_MAX * light / 100
fan_power = FAN_MAX * fan / 100
total_power = light_power + fan_power

daily_energy = total_power * HOURS_PER_DAY / 1000
monthly_energy = daily_energy * DAYS_PER_MONTH
daily_cost = daily_energy * RATE
monthly_cost = monthly_energy * RATE

st.markdown('<div class="section-title">⚡ Live Energy Overview</div>',
            unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

def metric_card(label, value, note):
    return f"""
    <div class="metric-card">
      <div class="metric-label">{label}</div>
      <div class="metric-number">{value}</div>
      <div class="metric-note">{note}</div>
    </div>
    """

with c1:
    st.markdown(metric_card(
        "CURRENT POWER LOAD",
        f"{total_power:.1f} W",
        "Combined appliance power"
    ), unsafe_allow_html=True)

with c2:
    st.markdown(metric_card(
        "DAILY CONSUMPTION",
        f"{daily_energy:.3f} kWh",
        "Estimated units per day"
    ), unsafe_allow_html=True)

with c3:
    st.markdown(metric_card(
        "DAILY ELECTRICITY COST",
        f"₹{daily_cost:.2f}",
        "Based on assumed tariff"
    ), unsafe_allow_html=True)

# -------------------- MONTHLY BILL --------------------

st.markdown('<div class="section-title">📊 Monthly Cost Prediction</div>',
            unsafe_allow_html=True)

st.markdown(f"""
<div class="bill-card">
    <div class="bill-caption">PREDICTED MONTHLY ELECTRICITY BILL</div>
    <div class="bill-number">₹{monthly_cost:.2f}</div>
    <div class="bill-caption">
        Estimated consumption: {monthly_energy:.2f} kWh
        &nbsp; • &nbsp; 30-day projection
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🔍 Appliance Breakdown</div>',
            unsafe_allow_html=True)

a, b = st.columns(2)

light_monthly = light_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000
fan_monthly = fan_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000

with a:
    st.markdown("### 💡 Lighting")
    st.write(f"Intensity: **{light}%**")
    st.write(f"Current power: **{light_power:.2f} W**")
    st.write(f"Monthly usage: **{light_monthly:.2f} units**")
    st.write(f"Monthly cost: **₹{light_monthly * RATE:.2f}**")
    st.progress(light / 100)

with b:
    st.markdown("### 🌀 Fan")
    st.write(f"Speed: **{fan}%**")
    st.write(f"Current power: **{fan_power:.2f} W**")
    st.write(f"Monthly usage: **{fan_monthly:.2f} units**")
    st.write(f"Monthly cost: **₹{fan_monthly * RATE:.2f}**")
    st.progress(fan / 100)

# -------------------- CHART --------------------

st.markdown('<div class="section-title">📈 Energy Distribution</div>',
            unsafe_allow_html=True)

st.bar_chart({
    "Monthly Consumption (kWh)": {
        "Light": light_monthly,
        "Fan": fan_monthly
    }
})

# -------------------- FOOTER --------------------

st.markdown("""
<div class="info-box">
    <b>ℹ️ About this prediction</b><br><br>
    This dashboard uses estimated appliance ratings of 10 W for the
    light and 50 W for the fan at 100% settings. It assumes 5 hours
    of daily operation, 30 days per month and an electricity tariff
    of ₹8 per kWh. Actual energy consumption can differ from these
    illustrative estimates. The controls and appliance illustrations
    are simulated and do not operate physical appliances.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;color:#7181a6;font-size:11px;margin-top:30px">
    HOMEMIND AI • SMARTER ENERGY • SMARTER LIVING
</p>
""", unsafe_allow_html=True)
