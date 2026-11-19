
import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="HomeMind AI | Smart Energy",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# ENERGY ASSUMPTIONS
# =====================================================

LIGHT_MAX_WATTS = 10
FAN_MAX_WATTS = 50

HOURS_PER_DAY = 5
DAYS_PER_MONTH = 30
ELECTRICITY_RATE = 8

# =====================================================
# PREMIUM UI DESIGN
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #202b5c 0%, transparent 35%),
        radial-gradient(ellipse at 90% 10%, #25205b 0%, transparent 35%),
        #090e1d;
    color: #f4f6ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HERO */

.hero {
    background: linear-gradient(115deg, #202e60, #192448 55%, #35265f);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 25px;
    padding: 30px 32px;
    margin-bottom: 28px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.22);
}

.hero-tag {
    color: #a9bbff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
}

.hero-title {
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin: 9px 0;
}

.hero-subtitle {
    color: #c3cdec;
    font-size: 14px;
    line-height: 1.7;
}

/* SECTION HEADINGS */

.section-heading {
    font-size: 21px;
    font-weight: 800;
    color: #ffffff;
    margin: 25px 0 15px;
}

.section-description {
    color: #9eaccd;
    font-size: 12px;
    margin-top: -9px;
    margin-bottom: 18px;
}

/* DEVICE CARDS */

.device-card {
    background: linear-gradient(145deg, #192443, #11192e);
    border: 1px solid rgba(255,255,255,0.11);
    border-radius: 23px;
    padding: 22px 22px 10px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    min-height: 140px;
}

.device-title {
    color: white;
    font-size: 19px;
    font-weight: 800;
}

.device-subtitle {
    color: #9eaccd;
    font-size: 12px;
    margin-top: 5px;
}

.curve {
    height: 23px;
    width: 75%;
    margin: 18px auto 0;
    border-top: 4px solid #8296ff;
    border-radius: 100% 100% 0 0;
    filter: drop-shadow(0 0 8px #748aff);
}

/* SLIDERS */

div[data-testid="stSlider"] {
    padding: 5px 12px 0;
}

div[data-testid="stSlider"] label {
    color: #cbd5f0 !important;
    font-weight: 600;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    height: 35px;
}

div[data-testid="stSlider"] [role="slider"] {
    width: 24px !important;
    height: 24px !important;
    border: 4px solid #ffffff !important;
    box-shadow: 0 0 13px #8398ff !important;
}

div[data-testid="stSlider"] [data-testid="stTickBar"] {
    display: none;
}

/* DEVICE ILLUSTRATIONS */

.illustration-card {
    background: linear-gradient(145deg, #192443, #11192e);
    border: 1px solid rgba(255,255,255,0.11);
    border-radius: 22px;
    text-align: center;
    padding: 15px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
}

.device-percentage {
    color: #a9baff;
    font-size: 25px;
    font-weight: 900;
    margin-top: 0;
}

.device-status {
    color: #a9b8d9;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-top: 2px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(145deg, #1a2747, #121a30);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 20px;
    min-height: 115px;
}

.metric-label {
    color: #aab8d6;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
}

.metric-value {
    color: white;
    font-size: 27px;
    font-weight: 900;
    margin-top: 9px;
}

.metric-caption {
    color: #8496bb;
    font-size: 11px;
    margin-top: 4px;
}

/* MONTHLY BILL */

.bill-card {
    background: linear-gradient(110deg, #304b9a, #57378e);
    border: 1px solid rgba(255,255,255,0.17);
    border-radius: 23px;
    padding: 26px;
    margin-top: 12px;
    box-shadow: 0 12px 35px rgba(39,49,119,0.25);
}

.bill-label {
    color: #d2dcff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.bill-value {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin: 7px 0;
}

.bill-note {
    color: #d0d9ff;
    font-size: 12px;
}

/* BREAKDOWN */

.breakdown-card {
    background: #151f39;
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 10px;
}

.breakdown-title {
    font-size: 17px;
    color: white;
    font-weight: 800;
}

.breakdown-text {
    color: #b3c0dd;
    font-size: 13px;
    line-height: 2;
}

/* INFO AND FOOTER */

.info-box {
    background: #131e35;
    border: 1px solid #2b3d65;
    border-radius: 16px;
    padding: 18px;
    color: #b9c7e6;
    font-size: 12px;
    line-height: 1.8;
}

.footer {
    text-align: center;
    color: #7788ae;
    font-size: 11px;
    letter-spacing: 1.5px;
    padding-top: 30px;
}

div[data-testid="stMarkdownContainer"] p {
    color: #dce5ff;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">INTELLIGENT LIVING • ENERGY INSIGHTS</div>
    <div class="hero-title">🏠 HomeMind AI</div>
    <div class="hero-subtitle">
        Your smart home energy companion.<br>
        Adjust appliances, monitor electricity consumption
        and predict your monthly electricity bill.
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# CONTROLS
# =====================================================

st.markdown(
    '<div class="section-heading">🎛️ Smart Room Controls</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Move the sliders and watch your virtual room respond.</div>',
    unsafe_allow_html=True
)

light_column, fan_column = st.columns(2, gap="large")

with light_column:

    st.markdown("""
    <div class="device-card">
        <div class="device-title">💡 Smart Lighting</div>
        <div class="device-subtitle">Adjust your room's light intensity</div>
        <div class="curve"></div>
    </div>
    """, unsafe_allow_html=True)

    light = st.slider(
        "LIGHT INTENSITY",
        min_value=0,
        max_value=100,
        value=75,
        step=1,
        format="%d",
        key="light_control"
    )

    st.markdown(
        f'<div class="device-percentage">{light}%</div>',
        unsafe_allow_html=True
    )

    light_power = LIGHT_MAX_WATTS * light / 100

    brightness = 0.08 + (light / 100) * 0.92
    glow = 4 + light * 0.40

    light_status = "LIGHT ON" if light > 0 else "LIGHT OFF"

    bulb_html = f"""
    <div class="illustration-card">
        <svg width="190" height="170" viewBox="0 0 190 170">
            <defs>
                <radialGradient id="bulbGlow">
                    <stop offset="0%" stop-color="#fff4a8"
                        stop-opacity="{brightness}"/>
                    <stop offset="100%" stop-color="#ffc94d"
                        stop-opacity="0"/>
                </radialGradient>
            </defs>

            <circle cx="95" cy="75" r="72"
                fill="url(#bulbGlow)"
                style="filter:blur(7px)"/>

            <g opacity="{brightness}">
                <path d="M95 22
                    C65 22 48 44 53 73
                    C56 90 72 99 75 116
                    L115 116
                    C118 99 134 90 137 73
                    C142 44 125 22 95 22Z"
                    fill="#ffe69a"
                    stroke="#fff3c4"
                    stroke-width="3"
                    style="filter:drop-shadow(0 0 {glow}px #ffdb68)"/>

                <path d="M79 117 H111
                    M81 126 H109
                    M85 135 H105"
                    stroke="#d5dced"
                    stroke-width="5"
                    stroke-linecap="round"/>
            </g>

            <path d="M95 22
                C65 22 48 44 53 73
                C56 90 72 99 75 116
                L115 116
                C118 99 134 90 137 73
                C142 44 125 22 95 22Z"
                fill="none"
                stroke="#8999bc"
                stroke-width="2"/>

            <path d="M87 145 H103"
                stroke="#9caccb"
                stroke-width="5"
                stroke-linecap="round"/>
        </svg>

        <div class="device-status">{light_status}</div>
        <div style="color:#91a4cb;font-size:11px;margin-top:7px">
            Estimated power: {light_power:.2f} W
        </div>
    </div>
    """

    components.html(bulb_html, height=225)

with fan_column:

    st.markdown("""
    <div class="device-card">
        <div class="device-title">🌀 Smart Fan</div>
        <div class="device-subtitle">Adjust the speed of your ceiling fan</div>
        <div class="curve"></div>
    </div>
    """, unsafe_allow_html=True)

    fan = st.slider(
        "FAN SPEED",
        min_value=0,
        max_value=100,
        value=60,
        step=1,
        format="%d",
        key="fan_control"
    )

    st.markdown(
        f'<div class="device-percentage">{fan}%</div>',
        unsafe_allow_html=True
    )

    fan_power = FAN_MAX_WATTS * fan / 100

    # Higher slider value = faster rotation
    duration = 3.5 - (fan / 100) * 3.35
    duration = max(0.15, duration)

    fan_status = "FAN RUNNING" if fan > 0 else "FAN STOPPED"

    fan_html = f"""
    <div class="illustration-card">
        <svg width="190" height="170" viewBox="0 0 190 170">
            <g style="
                transform-origin:95px 78px;
                animation:spin {duration:.3f}s linear infinite;
                animation-play-state:{'running' if fan > 0 else 'paused'};
            ">
                <path d="M95 78
                    C72 66 53 32 69 23
                    C86 13 105 47 95 78Z"
                    fill="#78aaff"
                    stroke="#c1ddff"
                    stroke-width="2"/>

                <path d="M95 78
                    C120 66 153 47 160 65
                    C167 84 127 98 95 78Z"
                    fill="#78aaff"
                    stroke="#c1ddff"
                    stroke-width="2"/>

                <path d="M95 78
                    C107 105 115 137 96 146
                    C77 153 76 109 95 78Z"
                    fill="#78aaff"
                    stroke="#c1ddff"
                    stroke-width="2"/>
            </g>

            <circle cx="95" cy="78" r="11"
                fill="#e2efff"
                stroke="#8ebaff"
                stroke-width="3"/>

            <path d="M95 90 V111"
                stroke="#8497bb"
                stroke-width="6"
                stroke-linecap="round"/>

            <path d="M67 111 H123"
                stroke="#a8b8d9"
                stroke-width="7"
                stroke-linecap="round"/>
        </svg>

        <style>
            @keyframes spin {{
                from {{ transform: rotate(0deg); }}
                to {{ transform: rotate(360deg); }}
            }}
        </style>

        <div class="device-status">{fan_status}</div>
        <div style="color:#91a4cb;font-size:11px;margin-top:7px">
            Estimated power: {fan_power:.2f} W
        </div>
    </div>
    """

    components.html(fan_html, height=225)

# =====================================================
# ENERGY CALCULATIONS
# =====================================================

total_power = light_power + fan_power

daily_energy = (
    total_power * HOURS_PER_DAY
) / 1000

monthly_energy = daily_energy * DAYS_PER_MONTH

daily_cost = daily_energy * ELECTRICITY_RATE

monthly_cost = monthly_energy * ELECTRICITY_RATE

light_monthly = (
    light_power * HOURS_PER_DAY * DAYS_PER_MONTH
) / 1000

fan_monthly = (
    fan_power * HOURS_PER_DAY * DAYS_PER_MONTH
) / 1000

# =====================================================
# LIVE ENERGY DASHBOARD
# =====================================================

st.markdown(
    '<div class="section-heading">⚡ Live Energy Overview</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">CURRENT POWER LOAD</div>
        <div class="metric-value">{total_power:.2f} W</div>
        <div class="metric-caption">Combined appliance load</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">DAILY CONSUMPTION</div>
        <div class="metric-value">{daily_energy:.3f}</div>
        <div class="metric-caption">Units per day (kWh)</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">DAILY ELECTRICITY COST</div>
        <div class="metric-value">₹{daily_cost:.2f}</div>
        <div class="metric-caption">At ₹{ELECTRICITY_RATE}/unit</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# MONTHLY PREDICTION
# =====================================================

st.markdown(
    '<div class="section-heading">📊 Monthly Cost Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="bill-card">
    <div class="bill-label">PREDICTED MONTHLY ELECTRICITY BILL</div>
    <div class="bill-value">₹{monthly_cost:.2f}</div>
    <div class="bill-note">
        Estimated monthly consumption: {monthly_energy:.2f} kWh
        &nbsp; • &nbsp; 30-day projection
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# APPLIANCE BREAKDOWN
# =====================================================

st.markdown(
    '<div class="section-heading">🔍 Appliance Breakdown</div>',
    unsafe_allow_html=True
)

a, b = st.columns(2, gap="large")

with a:
    st.markdown(f"""
    <div class="breakdown-card">
        <div class="breakdown-title">💡 Lighting</div>
        <div class="breakdown-text">
            Intensity: <b>{light}%</b><br>
            Current power: <b>{light_power:.2f} W</b><br>
            Monthly consumption: <b>{light_monthly:.2f} kWh</b><br>
            Monthly cost: <b>₹{light_monthly * ELECTRICITY_RATE:.2f}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(light / 100, text="Light intensity")

with b:
    st.markdown(f"""
    <div class="breakdown-card">
        <div class="breakdown-title">🌀 Fan</div>
        <div class="breakdown-text">
            Speed: <b>{fan}%</b><br>
            Current power: <b>{fan_power:.2f} W</b><br>
            Monthly consumption: <b>{fan_monthly:.2f} kWh</b><br>
            Monthly cost: <b>₹{fan_monthly * ELECTRICITY_RATE:.2f}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(fan / 100, text="Fan speed")

# =====================================================
# ENERGY CHART
# =====================================================

st.markdown(
    '<div class="section-heading">📈 Monthly Energy Distribution</div>',
    unsafe_allow_html=True
)

st.bar_chart({
    "Light (kWh)": [light_monthly],
    "Fan (kWh)": [fan_monthly]
})

# =====================================================
# INFORMATION
# =====================================================

st.markdown(f"""
<div class="info-box">
    <b>ℹ️ About this prediction</b><br><br>
    • Light rating: {LIGHT_MAX_WATTS} W at 100% intensity.<br>
    • Fan rating: {FAN_MAX_WATTS} W at 100% speed.<br>
    • Assumed daily operation: {HOURS_PER_DAY} hours.<br>
    • Monthly period: {DAYS_PER_MONTH} days.<br>
    • Electricity tariff: ₹{ELECTRICITY_RATE} per unit.<br><br>
    These are illustrative estimates using a simplified linear
    power model. Real fan power does not necessarily change
    linearly with its speed. Actual electricity consumption
    depends on the appliance and its operating conditions.
    The sliders and illustrations are simulations and do not
    control or measure the physical Arduino model.
</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    HOMEMIND AI &nbsp; • &nbsp; SMARTER ENERGY &nbsp; • &nbsp; SMARTER LIVING
</div>
""", unsafe_allow_html=True)
