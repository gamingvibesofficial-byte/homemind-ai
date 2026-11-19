
import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="HomeMind | Smart Energy",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# SIMULATION ASSUMPTIONS
# =====================================================

LIGHT_MAX_WATTS = 10
FAN_MAX_WATTS = 50

HOURS_PER_DAY = 5
DAYS_PER_MONTH = 30
RATE_PER_UNIT = 8

# =====================================================
# CUSTOM DESIGN
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #0b1020;
    --card: #151e34;
    --card-light: #1b2945;
    --text: #f5f7ff;
    --muted: #9baac8;
    --blue: #79aaff;
    --violet: #a18bff;
    --green: #71dfb0;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, #1c3158 0%, transparent 33%),
        radial-gradient(ellipse at 95% 5%, #29204c 0%, transparent 32%),
        var(--bg);
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1180px;
    padding: 28px 24px 55px;
}

/* HEADER */

.hero {
    background: linear-gradient(120deg, #20365e, #1b2949 55%, #332858);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 25px;
    padding: 30px;
    margin-bottom: 28px;
    box-shadow: 0 18px 45px rgba(0,0,0,.20);
}

.eyebrow {
    color: #b3c6ff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero h1 {
    color: white;
    font-size: clamp(29px, 4vw, 40px);
    font-weight: 900;
    margin: 9px 0 6px;
}

.hero p {
    color: #c2cce5;
    font-size: 14px;
    line-height: 1.7;
    margin: 0;
}

/* SECTION TITLES */

.section-title {
    color: white;
    font-size: 21px;
    font-weight: 800;
    margin: 26px 0 6px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 17px;
}

/* APPLIANCE CARDS */

.appliance-card {
    background: linear-gradient(150deg, #1a2947, #121c32);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 12px 32px rgba(0,0,0,.18);
}

.appliance-name {
    color: white;
    font-size: 19px;
    font-weight: 800;
}

.appliance-description {
    color: #a6b5d2;
    font-size: 12px;
    margin-top: 5px;
}

/* CURVED ACCENT */

.slider-arc {
    width: 78%;
    height: 17px;
    margin: 23px auto 8px;
    border-top: 4px solid #829cff;
    border-radius: 100% 100% 0 0;
    filter: drop-shadow(0 0 7px rgba(121,151,255,.7));
}

/* LARGE SLIDERS */

div[data-testid="stSlider"] {
    padding: 9px 7px 3px;
}

div[data-testid="stSlider"] label {
    color: #dce5fa !important;
    font-size: 12px !important;
    font-weight: 700 !important;
}

/* Larger touch target */
div[data-testid="stSlider"] [data-baseweb="slider"] {
    min-height: 46px !important;
    padding: 8px 0 !important;
    cursor: pointer;
}

/* Thicker slider track */
div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
    height: 12px !important;
    border-radius: 20px !important;
}

/* Large circular handle */
div[data-testid="stSlider"] [role="slider"] {
    width: 30px !important;
    height: 30px !important;
    border-radius: 50% !important;
    background: #ffffff !important;
    border: 5px solid #8da7ff !important;
    box-shadow: 0 0 0 5px rgba(130,156,255,.16),
                0 2px 12px rgba(0,0,0,.4) !important;
    cursor: grab !important;
}

div[data-testid="stSlider"] [data-testid="stTickBar"] {
    display: none !important;
}

/* VALUE */

.value-display {
    color: #a9beff;
    text-align: center;
    font-size: 27px;
    font-weight: 900;
    margin: 0 0 7px;
}

/* DEVICE VISUALS */

.visual-card {
    background: linear-gradient(145deg, #17243e, #111a2e);
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 21px;
    padding: 15px;
    text-align: center;
    margin-top: 10px;
}

.visual-status {
    color: #c0cde7;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.6px;
    margin-top: 3px;
}

.visual-power {
    color: #91a5cb;
    font-size: 12px;
    margin-top: 6px;
}

/* METRICS */

.metric-card {
    background: linear-gradient(145deg, #1a2946, #121b30);
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 19px;
    padding: 20px;
    min-height: 112px;
}

.metric-label {
    color: #a6b5d2;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.metric-value {
    color: white;
    font-size: 27px;
    font-weight: 900;
    margin-top: 9px;
}

.metric-caption {
    color: #8c9dbd;
    font-size: 11px;
    margin-top: 3px;
}

/* BILL */

.bill-card {
    background: linear-gradient(115deg, #304d91, #543b91);
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 23px;
    padding: 25px;
    margin-top: 14px;
    box-shadow: 0 15px 40px rgba(35,46,116,.2);
}

.bill-label {
    color: #d2ddff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
}

.bill-value {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin: 7px 0;
}

.bill-caption {
    color: #d5ddff;
    font-size: 12px;
}

/* DEVICE BREAKDOWN */

.breakdown-card {
    background: #17233c;
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 19px;
    padding: 20px;
}

.breakdown-heading {
    color: white;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 10px;
}

.breakdown-line {
    color: #b8c5df;
    font-size: 13px;
    line-height: 2;
}

/* INFO */

.info-box {
    background: #131e34;
    border: 1px solid #293b5e;
    border-radius: 17px;
    padding: 18px;
    color: #b8c7e4;
    font-size: 12px;
    line-height: 1.8;
}

.footer {
    text-align: center;
    color: #788bad;
    font-size: 10px;
    letter-spacing: 1.5px;
    padding-top: 30px;
}

/* MOBILE */

@media (max-width: 640px) {
    .block-container {
        padding: 15px 12px 35px;
    }

    .hero {
        padding: 23px 19px;
        border-radius: 20px;
    }

    .appliance-card {
        padding: 18px;
    }

    .section-title {
        font-size: 19px;
    }

    .metric-card {
        padding: 14px;
        min-height: 100px;
    }

    .metric-value {
        font-size: 21px;
    }

    .bill-value {
        font-size: 36px;
    }

    div[data-testid="stSlider"] [data-baseweb="slider"] {
        min-height: 54px !important;
    }

    div[data-testid="stSlider"] [role="slider"] {
        width: 32px !important;
        height: 32px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero">
    <div class="eyebrow">SMART LIVING · ENERGY INTELLIGENCE</div>
    <h1>HomeMind</h1>
    <p>
        A smarter way to understand your home's energy.
        Adjust your virtual appliances and explore your
        estimated electricity consumption.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# CONTROLS
# =====================================================

st.markdown(
    '<div class="section-title">Your smart room</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Adjust the controls to see your room respond in real time.</div>',
    unsafe_allow_html=True
)

light_col, fan_col = st.columns(2, gap="large")

# ---------------- LIGHT ----------------

with light_col:

    st.markdown("""
    <div class="appliance-card">
        <div class="appliance-name">💡 Lighting</div>
        <div class="appliance-description">
            Set the brightness of your room
        </div>
        <div class="slider-arc"></div>
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
        f'<div class="value-display">{light}%</div>',
        unsafe_allow_html=True
    )

    light_power = LIGHT_MAX_WATTS * light / 100

    # Bulb brightness changes with slider
    brightness = 0.08 + (light / 100) * 0.92
    glow = 5 + light * 0.38

    light_status = "LIGHT ON" if light > 0 else "LIGHT OFF"

    bulb_html = f"""
    <div class="visual-card">
        <svg width="100%" height="180" viewBox="0 0 220 180">
            <defs>
                <radialGradient id="glow">
                    <stop offset="0%" stop-color="#fff4a8"
                        stop-opacity="{brightness}"/>
                    <stop offset="100%" stop-color="#ffcb55"
                        stop-opacity="0"/>
                </radialGradient>
            </defs>

            <circle cx="110" cy="76" r="78"
                fill="url(#glow)"
                style="filter:blur(7px)"/>

            <g opacity="{brightness}">
                <path d="
                    M110 20
                    C77 20 58 45 63 77
                    C66 97 84 105 88 124
                    L132 124
                    C136 105 154 97 157 77
                    C162 45 143 20 110 20Z"
                    fill="#ffe69a"
                    stroke="#fff4c6"
                    stroke-width="3"
                    style="filter:drop-shadow(0 0 {glow}px #ffdb73)"/>

                <path d="M91 125 H129 M94 135 H126 M99 144 H121"
                    stroke="#d9e2f3"
                    stroke-width="5"
                    stroke-linecap="round"/>
            </g>

            <path d="
                M110 20
                C77 20 58 45 63 77
                C66 97 84 105 88 124
                L132 124
                C136 105 154 97 157 77
                C162 45 143 20 110 20Z"
                fill="none"
                stroke="#8498bd"
                stroke-width="2"/>

            <path d="M101 154 H119"
                stroke="#9eafd0"
                stroke-width="5"
                stroke-linecap="round"/>
        </svg>

        <div class="visual-status">{light_status}</div>
        <div class="visual-power">Estimated power · {light_power:.2f} W</div>
    </div>
    """

    components.html(bulb_html, height=235)

# ---------------- FAN ----------------

with fan_col:

    st.markdown("""
    <div class="appliance-card">
        <div class="appliance-name">🌀 Ceiling Fan</div>
        <div class="appliance-description">
            Set your preferred fan speed
        </div>
        <div class="slider-arc"></div>
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
        f'<div class="value-display">{fan}%</div>',
        unsafe_allow_html=True
    )

    fan_power = FAN_MAX_WATTS * fan / 100

    # Fan rotates faster as the slider increases
    duration = max(0.15, 3.5 - (fan / 100) * 3.35)

    fan_status = "FAN RUNNING" if fan > 0 else "FAN STOPPED"

    fan_html = f"""
    <div class="visual-card">
        <svg width="100%" height="180" viewBox="0 0 220 180">

            <!-- Three equal blades, spaced exactly 120 degrees -->
            <g style="
                transform-origin:110px 78px;
                animation:fanSpin {duration:.3f}s linear infinite;
                animation-play-state:{'running' if fan > 0 else 'paused'};
            ">

                <g transform="rotate(0 110 78)">
                    <path d="
                        M110 70
                        C98 51 82 27 91 14
                        C99 2 114 12 119 28
                        C125 44 117 59 114 72
                        Z"
                        fill="#77aaff"
                        stroke="#c3ddff"
                        stroke-width="2"/>
                </g>

                <g transform="rotate(120 110 78)">
                    <path d="
                        M110 70
                        C98 51 82 27 91 14
                        C99 2 114 12 119 28
                        C125 44 117 59 114 72
                        Z"
                        fill="#77aaff"
                        stroke="#c3ddff"
                        stroke-width="2"/>
                </g>

                <g transform="rotate(240 110 78)">
                    <path d="
                        M110 70
                        C98 51 82 27 91 14
                        C99 2 114 12 119 28
                        C125 44 117 59 114 72
                        Z"
                        fill="#77aaff"
                        stroke="#c3ddff"
                        stroke-width="2"/>
                </g>

            </g>

            <!-- Central motor hub -->
            <circle cx="110" cy="78" r="12"
                fill="#e5efff"
                stroke="#8db8ff"
                stroke-width="4"/>

            <!-- Fan rod -->
            <path d="M110 91 V115"
                stroke="#91a6cb"
                stroke-width="7"
                stroke-linecap="round"/>

            <!-- Ceiling mount -->
            <path d="M79 116 H141"
                stroke="#aebfe0"
                stroke-width="8"
                stroke-linecap="round"/>

        </svg>

        <style>
            @keyframes fanSpin {{
                from {{ transform: rotate(0deg); }}
                to {{ transform: rotate(360deg); }}
            }}
        </style>

        <div class="visual-status">{fan_status}</div>
        <div class="visual-power">Estimated power · {fan_power:.2f} W</div>
    </div>
    """

    components.html(fan_html, height=235)

# =====================================================
# ENERGY CALCULATIONS
# =====================================================

total_power = light_power + fan_power

daily_energy = total_power * HOURS_PER_DAY / 1000
monthly_energy = daily_energy * DAYS_PER_MONTH

daily_cost = daily_energy * RATE_PER_UNIT
monthly_cost = monthly_energy * RATE_PER_UNIT

light_monthly = light_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000
fan_monthly = fan_power * HOURS_PER_DAY * DAYS_PER_MONTH / 1000

# =====================================================
# LIVE OVERVIEW
# =====================================================

st.markdown(
    '<div class="section-title">Energy overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Your estimated electricity usage based on current settings.</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">CURRENT POWER</div>
        <div class="metric-value">{total_power:.1f} W</div>
        <div class="metric-caption">Combined appliance load</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">DAILY ENERGY</div>
        <div class="metric-value">{daily_energy:.3f}</div>
        <div class="metric-caption">kWh per day</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">DAILY COST</div>
        <div class="metric-value">₹{daily_cost:.2f}</div>
        <div class="metric-caption">Estimated daily expense</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# MONTHLY BILL
# =====================================================

st.markdown(
    '<div class="section-title">Monthly bill prediction</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="bill-card">
    <div class="bill-label">ESTIMATED MONTHLY ELECTRICITY COST</div>
    <div class="bill-value">₹{monthly_cost:.2f}</div>
    <div class="bill-caption">
        {monthly_energy:.2f} kWh monthly consumption
        &nbsp; · &nbsp; 30-day estimate
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# APPLIANCE BREAKDOWN
# =====================================================

st.markdown(
    '<div class="section-title">Appliance breakdown</div>',
    unsafe_allow_html=True
)

a, b = st.columns(2, gap="large")

with a:
    st.markdown(f"""
    <div class="breakdown-card">
        <div class="breakdown-heading">💡 Lighting</div>
        <div class="breakdown-line">
            Intensity: <b>{light}%</b><br>
            Current power: <b>{light_power:.2f} W</b><br>
            Monthly usage: <b>{light_monthly:.2f} kWh</b><br>
            Monthly cost: <b>₹{light_monthly * RATE_PER_UNIT:.2f}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown(f"""
    <div class="breakdown-card">
        <div class="breakdown-heading">🌀 Ceiling Fan</div>
        <div class="breakdown-line">
            Speed: <b>{fan}%</b><br>
            Current power: <b>{fan_power:.2f} W</b><br>
            Monthly usage: <b>{fan_monthly:.2f} kWh</b><br>
            Monthly cost: <b>₹{fan_monthly * RATE_PER_UNIT:.2f}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# ASSUMPTIONS
# =====================================================

st.markdown(
    '<div class="section-title">How we calculate</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="info-box">
    <b>Simulation assumptions</b><br>
    • Light rating: {LIGHT_MAX_WATTS} W at 100% intensity.<br>
    • Fan rating: {FAN_MAX_WATTS} W at 100% speed.<br>
    • Daily usage: {HOURS_PER_DAY} hours.<br>
    • Billing period: {DAYS_PER_MONTH} days.<br>
    • Electricity tariff: ₹{RATE_PER_UNIT} per unit.<br><br>

    <b>Calculation:</b><br>
    Energy (kWh) = Power (W) × Hours ÷ 1000<br>
    Monthly cost = Monthly energy × Electricity tariff<br><br>

    These are illustrative estimates using a simplified
    linear power model. Actual fan power does not necessarily
    change linearly with speed. The sliders and illustrations
    are simulations and do not control or measure your physical
    Arduino model.
</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    HOMEMIND · SMARTER ENERGY · SMARTER LIVING
</div>
""", unsafe_allow_html=True)
