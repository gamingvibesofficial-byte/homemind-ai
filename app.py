
import streamlit as st

st.set_page_config(
    page_title="HomeMind AI",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 HomeMind AI")
st.caption("Smart Home Energy Monitoring & Prediction System")

st.markdown("""
Adjust the light intensity and fan speed to see how your
electricity consumption and monthly bill change instantly.
""")

# Assumptions
LIGHT_MAX = 10       # Watts
FAN_MAX = 50         # Watts
HOURS_PER_DAY = 5
DAYS_PER_MONTH = 30
RATE = 8             # Rupees per kWh

st.divider()

# Controls
st.subheader("🎛️ Smart Room Controls")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💡 Light Intensity")
    light = st.slider(
        "Adjust light intensity",
        min_value=0,
        max_value=100,
        value=75,
        format="%d%%"
    )

with col2:
    st.markdown("### 🌀 Fan Speed")
    fan = st.slider(
        "Adjust fan speed",
        min_value=0,
        max_value=100,
        value=60,
        format="%d%%"
    )

# Simulated power calculation
light_power = LIGHT_MAX * light / 100
fan_power = FAN_MAX * fan / 100

total_power = light_power + fan_power

# Energy calculations
daily_energy = (total_power * HOURS_PER_DAY) / 1000
monthly_energy = daily_energy * DAYS_PER_MONTH
monthly_cost = monthly_energy * RATE

daily_cost = daily_energy * RATE

st.divider()

# Live dashboard
st.subheader("⚡ Live Energy Dashboard")

c1, c2, c3 = st.columns(3)

c1.metric("Current Power Load", f"{total_power:.2f} W")
c2.metric("Daily Energy", f"{daily_energy:.3f} kWh")
c3.metric("Daily Cost", f"₹{daily_cost:.2f}")

st.divider()

# Monthly prediction
st.subheader("📊 Monthly Usage Prediction")

m1, m2, m3 = st.columns(3)

m1.metric("Monthly Consumption", f"{monthly_energy:.2f} Units")
m2.metric("Estimated Monthly Bill", f"₹{monthly_cost:.2f}")
m3.metric("Monthly Power Usage", f"{monthly_energy * 1000:.0f} Wh")

st.divider()

# Device breakdown
st.subheader("🔍 Device-wise Consumption")

light_monthly = (light_power * HOURS_PER_DAY * DAYS_PER_MONTH) / 1000
fan_monthly = (fan_power * HOURS_PER_DAY * DAYS_PER_MONTH) / 1000

col1, col2 = st.columns(2)

with col1:
    st.markdown("**💡 Light**")
    st.write(f"Intensity: {light}%")
    st.write(f"Power: {light_power:.2f} W")
    st.write(f"Monthly consumption: {light_monthly:.2f} Units")
    st.write(f"Monthly cost: ₹{light_monthly * RATE:.2f}")

with col2:
    st.markdown("**🌀 Fan**")
    st.write(f"Speed: {fan}%")
    st.write(f"Power: {fan_power:.2f} W")
    st.write(f"Monthly consumption: {fan_monthly:.2f} Units")
    st.write(f"Monthly cost: ₹{fan_monthly * RATE:.2f}")

st.divider()

# Energy visualization
st.subheader("📈 Monthly Energy Distribution")

st.bar_chart({
    "Energy Consumption (kWh)": {
        "Light": light_monthly,
        "Fan": fan_monthly
    }
})

st.info(
    "Prediction assumptions: 5 hours of daily usage, "
    "30 days per month and ₹8 per kWh. "
    "Actual consumption may vary depending on the appliances, "
    "operating conditions and electricity tariff."
)

st.caption(
    "HomeMind AI | Educational Smart Home Energy Simulation"
)
