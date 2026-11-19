
import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="HomeMind AI | Smart Home Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# POWER AND BILLING ASSUMPTIONS
# --------------------------------------------------

LIGHT_MAX_WATTS = 10
FAN_MAX_WATTS = 50
HOURS_PER_DAY = 5
DAYS_PER_MONTH = 30
RATE_PER_UNIT = 8

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #5278F5;
    --purple: #8A63F6;
    --ink: #17213B;
    --muted: #77819A;
    --surface: #FFFFFF;
    --background: #F5F7FC;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--background);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header, footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: var(--ink);
}

.hero {
    background: linear-gradient(120deg, #233B79 0%, #526FE0 58%, #8462E9 100%);
    border-radius: 26px;
    padding: 32px 36px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 15px 40px rgba(57, 78, 160, 0.16);
}

.hero h1 {
    color: white !important;
    font-size: 36px;
    margin: 0;
    font-weight: 800;
}

.hero p {
    color: rgba(255,255,255,.82);
    margin-top: 8px;
    font-size: 15px;
}

.hero-tag {
    display: inline-block;
    padding: 7px 13px;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.22);
    border-radius: 30px;
    font-size: 12px;
    margin-bottom: 14px;
}

.section-heading {
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--ink);
    margin: 22px 0 14px 0;
}

.panel {
    background: white;
    border: 1px solid #E9ECF5;
    border-radius: 22px;
    padding: 23px;
    box-shadow: 0 7px 25px rgba(31, 48, 92, .045);
    margin-bottom: 16px;
}

.metric-label {
    color: #77819A;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 7px;
}

.metric-value {
    font-family: 'Outfit', sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: #17213B;
}

.metric-note {
    color: #8A93A8;
    font-size: 12px;
    margin-top: 5px;
}

.device-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 18px;
    color: #17213B;
}

.device-subtitle {
    font-size: 12px;
    color: #8A93A8;
}

.power-pill {
    display: inline-block;
    background: #EEF2FF;
    color: #4F6FE8;
    padding: 7px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}

.note {
    color: #7D879D;
    font-size: 12px;
    line-height: 1.6;
}

hr {
    border-color: #E9ECF5 !important;
}

/* Larger native Streamlit slider track and handle */
div[data-testid="stSlider"] {
    padding-top: 8px;
    padding-bottom: 8px;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    min-height: 48px !important;
    padding: 10px 0 !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
    height: 12px !important;
    border-radius: 20px !important;
}

div[data-testid="stSlider"] [role="slider"] {
    width: 29px !important;
    height: 29px !important;
    border: 4px solid white !important;
    box-shadow: 0 2px 10px rgba(50,70,130,.25) !important;
}

div[data-testid="stSlider"] label {
    font-weight: 700 !important;
    color: #35415E !important;
    font-size: 14px !important;
}

/* Large toggle switches */
div[data-testid="stToggle"] {
    padding: 8px 0 12px 0;
}

div[data-testid="stToggle"] label {
    font-size: 16px !important;
    font-weight: 800 !important;
    color: #253251 !important;
    gap: 13px !important;
}

div[data-testid="stToggle"] [role="switch"] {
    transform: scale(1.35);
    transform-origin: left center;
    margin-right: 10px;
}

div[data-testid="stToggle"] [role="switch"] > div {
    border-radius: 30px !important;
}

div[data-testid="stToggle"] [role="switch"][aria-checked="true"] {
    background: #5578F4 !important;
    border-color: #5578F4 !important;
}

div[data-testid="stToggle"] [role="switch"][aria-checked="false"] {
    background: #C7CDDA !important;
    border-color: #C7CDDA !important;
}

@media(max-width: 640px) {
    .block-container {
        padding: 1rem 0.8rem 2rem 0.8rem;
    }

    .hero {
        padding: 24px 20px;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .panel {
        padding: 18px;
        border-radius: 18px;
    }

    .metric-value {
        font-size: 25px;
    }

    div[data-testid="stSlider"] [data-baseweb="slider"] {
        min-height: 56px !important;
    }

    div[data-testid="stSlider"] [role="slider"] {
        width: 33px !important;
        height: 33px !important;
    }

    div[data-testid="stToggle"] [role="switch"] {
        transform: scale(1.5);
    }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "light_on" not in st.session_state:
    st.session_state.light_on = True

if "fan_on" not in st.session_state:
    st.session_state.fan_on = True

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ SMART LIVING SIMULATOR</div>
    <h1>HomeMind AI</h1>
    <p>Control your home environment and understand your electricity consumption in real time.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DEVICE CONTROL SECTION
# --------------------------------------------------

st.markdown('<div class="section-heading">Your Home Controls</div>',
            unsafe_allow_html=True)

col_light, col_fan = st.columns(2, gap="large")

with col_light:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("""
    <div class="device-title">💡 Smart Lighting</div>
    <div class="device-subtitle">Brightness and power management</div>
    """, unsafe_allow_html=True)

    light_on = st.toggle(
        "LIGHT POWER",
        key="light_on"
    )

    light = st.slider(
        "Brightness",
        min_value=0,
        max_value=100,
        value=70,
        step=1,
        format="%d",
        disabled=not light_on,
        key="light_brightness"
    )

    st.markdown(
        f'<div class="power-pill">{"● LIGHT ON" if light_on else "○ LIGHT OFF"}</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col_fan:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("""
    <div class="device-title">🌀 Smart Ceiling Fan</div>
    <div class="device-subtitle">Fan speed and power management</div>
    """, unsafe_allow_html=True)

    fan_on = st.toggle(
        "FAN POWER",
        key="fan_on"
    )

    fan = st.slider(
        "Fan speed",
        min_value=0,
        max_value=100,
        value=60,
        step=1,
        format="%d",
        disabled=not fan_on,
        key="fan_speed"
    )

    st.markdown(
        f'<div class="power-pill">{"● FAN ON" if fan_on else "○ FAN OFF"}</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# LIVE POWER CALCULATIONS
# --------------------------------------------------

light_power = LIGHT_MAX_WATTS * light / 100 if light_on else 0
fan_power = FAN_MAX_WATTS * fan / 100 if fan_on else 0

total_power = light_power + fan_power

daily_energy = total_power * HOURS_PER_DAY / 1000
monthly_energy = daily_energy * DAYS_PER_MONTH
monthly_cost = monthly_energy * RATE_PER_UNIT

# --------------------------------------------------
# ANIMATED APPLIANCE PREVIEW
# --------------------------------------------------

st.markdown('<div class="section-heading">Live Appliance Preview</div>',
            unsafe_allow_html=True)

visual_col1, visual_col2 = st.columns(2, gap="large")

# Bulb preview
with visual_col1:
    bulb_glow = light / 100 if light_on else 0
    bulb_opacity = 0.12 + 0.88 * bulb_glow

    bulb_html = f"""
    <div style="
        background:white;
        border:1px solid #E9ECF5;
        border-radius:22px;
        padding:22px;
        text-align:center;
        box-shadow:0 7px 25px rgba(31,48,92,.045);
    ">
        <div style="font-family:Outfit,sans-serif;font-size:17px;
        font-weight:700;color:#17213B;">Lighting Preview</div>

        <div style="height:190px;display:flex;align-items:center;
        justify-content:center;position:relative;">
            <div style="
                position:absolute;
                width:130px;height:130px;border-radius:50%;
                background:radial-gradient(circle,
                rgba(255,193,65,{bulb_glow * 0.55}),
                rgba(255,193,65,0));
                filter:blur(12px);
            "></div>

            <svg width="125" height="155" viewBox="0 0 125 155">
                <path d="M62 15 C28 15 16 40 24 66
                C28 82 43 91 45 108 L79 108
                C81 91 96 82 100 66
                C108 40 96 15 62 15Z"
                fill="#FFD46A"
                fill-opacity="{bulb_opacity}"
                stroke="#D59B35"
                stroke-width="3"/>

                <path d="M45 110 L79 110 M46 119 L78 119
                M49 128 L75 128"
                stroke="#8791A6" stroke-width="5"
                stroke-linecap="round"/>

                <path d="M53 135 L71 135"
                stroke="#8791A6" stroke-width="5"
                stroke-linecap="round"/>
            </svg>
        </div>

        <div style="font-size:14px;font-weight:700;
        color:{'#278A62' if light_on else '#9AA3B5'};">
            {"● ON" if light_on else "○ OFF"}
        </div>
        <div style="font-size:12px;color:#8791A6;margin-top:5px;">
            {light if light_on else 0}% brightness
        </div>
    </div>
    """

    components.html(bulb_html, height=290)

# Fan preview
with visual_col2:
    fan_duration = max(0.35, 4 - (fan / 100 * 3.5)) if fan_on else 0
    fan_animation = (
        f"animation: fanSpin {fan_duration}s linear infinite;"
        if fan_on and fan > 0 else ""
    )

    fan_html = f"""
    <div style="
        background:white;
        border:1px solid #E9ECF5;
        border-radius:22px;
        padding:22px;
        text-align:center;
        box-shadow:0 7px 25px rgba(31,48,92,.045);
    ">
        <div style="font-family:Outfit,sans-serif;font-size:17px;
        font-weight:700;color:#17213B;">Fan Preview</div>

        <div style="height:190px;display:flex;align-items:center;
        justify-content:center;">
            <svg width="190" height="170" viewBox="0 0 190 170">
                <defs>
                    <linearGradient id="blade" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#91A8FF"/>
                        <stop offset="100%" stop-color="#526FE0"/>
                    </linearGradient>
                </defs>

                <g style="{fan_animation}transform-origin:95px 85px;">
                    <g fill="url(#blade)" opacity="{1 if fan_on else 0.35}">
                        <path d="M95 85 C82 65 73 35 91 10
                        C103 -2 116 12 112 34
                        C108 56 102 73 95 85Z"/>
                        <path d="M95 85 C82 65 73 35 91 10
                        C103 -2 116 12 112 34
                        C108 56 102 73 95 85Z"
                        transform="rotate(120 95 85)"/>
                        <path d="M95 85 C82 65 73 35 91 10
                        C103 -2 116 12 112 34
                        C108 56 102 73 95 85Z"
                        transform="rotate(240 95 85)"/>
                    </g>
                    <circle cx="95" cy="85" r="12"
                    fill="#344D9D" stroke="white" stroke-width="3"/>
                </g>
            </svg>
        </div>

        <style>
            @keyframes fanSpin {{
                from {{ transform: rotate(0deg); }}
                to {{ transform: rotate(360deg); }}
            }}
        </style>

        <div style="font-size:14px;font-weight:700;
        color:{'#278A62' if fan_on else '#9AA3B5'};">
            {"● ON" if fan_on else "○ OFF"}
        </div>
        <div style="font-size:12px;color:#8791A6;margin-top:5px;">
            {fan if fan_on else 0}% speed
        </div>
    </div>
    """

    components.html(fan_html, height=290)

# --------------------------------------------------
# ENERGY DASHBOARD
# --------------------------------------------------

st.markdown('<div class="section-heading">Energy & Cost Dashboard</div>',
            unsafe_allow_html=True)

m1, m2, m3 = st.columns(3, gap="medium")

with m1:
    st.markdown(f"""
    <div class="panel">
        <div class="metric-label">LIVE POWER</div>
        <div class="metric-value">{total_power:.1f} W</div>
        <div class="metric-note">Current estimated load</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="panel">
        <div class="metric-label">MONTHLY ENERGY</div>
        <div class="metric-value">{monthly_energy:.2f}</div>
        <div class="metric-note">Kilowatt-hours (units)</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="panel">
        <div class="metric-label">PREDICTED MONTHLY BILL</div>
        <div class="metric-value">₹{monthly_cost:.2f}</div>
        <div class="metric-note">Estimated electricity cost</div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# APPLIANCE BREAKDOWN
# --------------------------------------------------

st.markdown('<div class="section-heading">Appliance Breakdown</div>',
            unsafe_allow_html=True)

breakdown_col1, breakdown_col2 = st.columns(2, gap="large")

with breakdown_col1:
    light_monthly = light_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000
    light_cost = light_monthly * RATE_PER_UNIT

    st.markdown(f"""
    <div class="panel">
        <div class="device-title">💡 Lighting</div>
        <hr>
        <div class="metric-label">Current power</div>
        <div class="metric-value">{light_power:.2f} W</div>
        <br>
        <div class="metric-label">Monthly consumption</div>
        <div style="font-size:19px;font-weight:700;color:#526FE0;">
            {light_monthly:.2f} kWh
        </div>
        <br>
        <div class="metric-label">Estimated monthly cost</div>
        <div style="font-size:19px;font-weight:700;color:#17213B;">
            ₹{light_cost:.2f}
        </div>
    </div>
    """, unsafe_allow_html=True)

with breakdown_col2:
    fan_monthly = fan_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000
    fan_cost = fan_monthly * RATE_PER_UNIT

    st.markdown(f"""
    <div class="panel">
        <div class="device-title">🌀 Ceiling Fan</div>
        <hr>
        <div class="metric-label">Current power</div>
        <div class="metric-value">{fan_power:.2f} W</div>
        <br>
        <div class="metric-label">Monthly consumption</div>
        <div style="font-size:19px;font-weight:700;color:#526FE0;">
            {fan_monthly:.2f} kWh
        </div>
        <br>
        <div class="metric-label">Estimated monthly cost</div>
        <div style="font-size:19px;font-weight:700;color:#17213B;">
            ₹{fan_cost:.2f}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# ASSUMPTIONS AND FOOTER
# --------------------------------------------------

st.markdown('<div class="section-heading">Calculation Assumptions</div>',
            unsafe_allow_html=True)

st.markdown(f"""
<div class="panel">
    <div style="display:flex;flex-wrap:wrap;gap:12px;">
        <div class="power-pill">Light: {LIGHT_MAX_WATTS} W at 100%</div>
        <div class="power-pill">Fan: {FAN_MAX_WATTS} W at 100%</div>
        <div class="power-pill">Daily use: {HOURS_PER_DAY} hours</div>
        <div class="power-pill">Billing period: {DAYS_PER_MONTH} days</div>
        <div class="power-pill">Tariff: ₹{RATE_PER_UNIT}/kWh</div>
    </div>
    <br>
    <div class="note">
        These figures are illustrative estimates for demonstration.
        Actual electricity consumption depends on the appliance,
        its efficiency, operating conditions and local electricity tariff.
        Fan power does not necessarily vary linearly with its speed.
        This dashboard is a simulation and does not control physical appliances.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:20px 0;color:#9AA3B5;font-size:12px;">
    HOMEMIND AI · SMART HOME ENERGY SIMULATOR
    <br>
    Designed for an interactive smart home demonstration
</div>
""", unsafe_allow_html=True)
