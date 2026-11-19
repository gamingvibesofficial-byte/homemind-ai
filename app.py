
import streamlit as st
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HomeMind AI | Smart Home",
    page_icon="🏠",
    layout="wide"
)

# ---------------- DESIGN ----------------
st.markdown("""
<style>
.stApp {background: #f4f7fb;}
.block-container {padding-top: 2rem; max-width: 1200px;}
h1, h2, h3 {color: #192a41;}
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e4eaf2;
    padding: 16px;
    border-radius: 14px;
}
div.stButton > button {
    border-radius: 10px;
    border: 1px solid #dce5ef;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "light" not in st.session_state:
    st.session_state.light = False

if "fan" not in st.session_state:
    st.session_state.fan = False

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I'm HomeMind, your AI smart-home assistant. "
                "Ask me about energy saving, smart-home automation, "
                "or the current simulated room."
            )
        }
    ]

# ---------------- AI CLIENT ----------------
def get_ai_client():
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        return OpenAI(api_key=api_key)
    except Exception:
        return None

def ask_ai(question):
    client = get_ai_client()

    if client is None:
        return (
            "The AI connection is not configured yet. "
            "Add your OpenAI API key in Streamlit Secrets."
        )

    room_state = {
        "Light": "ON" if st.session_state.light else "OFF",
        "Fan": "ON" if st.session_state.fan else "OFF",
        "Estimated load (W)": (
            (10 if st.session_state.light else 0)
            + (50 if st.session_state.fan else 0)
        )
    }

    instructions = """
    You are HomeMind, an intelligent assistant for a college smart-home
    exhibition. Explain smart-home automation, comfort, safety and energy
    awareness in simple, helpful language.

    You receive simulated room states, not real sensor readings.
    Never claim to measure actual electricity, temperature or occupancy.
    Energy calculations are illustrative estimates only.
    You cannot control physical appliances, Arduino or external hardware.
    If a visitor asks to control something, explain that the dashboard
    buttons change only the simulated room.
    Keep answers concise and engaging for exhibition visitors.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=(
            f"Current simulated room state: {room_state}\n"
            f"Visitor question: {question}"
        ),
        max_output_tokens=350
    )

    return response.output_text

# ---------------- HEADER ----------------
st.title("🏠 HomeMind AI")
st.caption("INTELLIGENT LIVING • AI SMART HOME ASSISTANT")

st.success("AI Smart Home Simulation | Independent of Arduino")

st.divider()

# ---------------- MAIN DASHBOARD ----------------
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.subheader("🏡 My Smart Room")
    st.caption("Control your simulated room appliances.")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 💡 Room Light")
        st.write("Status:", "🟢 ON" if st.session_state.light else "⚪ OFF")
        if st.button(
            "Turn Light OFF" if st.session_state.light else "Turn Light ON",
            key="light_button",
            use_container_width=True
        ):
            st.session_state.light = not st.session_state.light
            st.rerun()

    with c2:
        st.markdown("### 🌀 Ceiling Fan")
        st.write("Status:", "🟢 ON" if st.session_state.fan else "⚪ OFF")
        if st.button(
            "Turn Fan OFF" if st.session_state.fan else "Turn Fan ON",
            key="fan_button",
            use_container_width=True
        ):
            st.session_state.fan = not st.session_state.fan
            st.rerun()

    light_watts = 10 if st.session_state.light else 0
    fan_watts = 50 if st.session_state.fan else 0
    total_watts = light_watts + fan_watts
    daily_cost = total_watts / 1000 * 5 * 8

    st.divider()
    st.subheader("📊 Room Analytics")

    m1, m2, m3 = st.columns(3)
    m1.metric("Devices ON", f"{int(st.session_state.light) + int(st.session_state.fan)}/2")
    m2.metric("Estimated Load", f"{total_watts} W")
    m3.metric("Daily Cost*", f"₹{daily_cost:.2f}")

    st.caption(
        "*Illustrative estimate: light 10 W, fan 50 W, "
        "5 hours/day and ₹8 per kWh. Not actual meter readings."
    )

with right:
    st.subheader("🤖 Ask HomeMind")
    st.caption("Your AI-powered smart-home assistant.")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if question := st.chat_input("Ask HomeMind anything..."):
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("HomeMind is thinking..."):
                try:
                    answer = ask_ai(question)
                except Exception:
                    answer = (
                        "I couldn't connect to the AI service. "
                        "Please check your API key, internet connection "
                        "and API account access."
                    )
                st.write(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

# ---------------- SMART MODES ----------------
st.divider()
st.subheader("⚡ Smart Modes")
st.caption("Choose a routine to update the simulated room.")

a, b, c, d = st.columns(4)

with a:
    if st.button("📚 Study Mode", use_container_width=True):
        st.session_state.light = True
        st.session_state.fan = False
        st.rerun()

with b:
    if st.button("🌙 Sleep Mode", use_container_width=True):
        st.session_state.light = False
        st.session_state.fan = True
        st.rerun()

with c:
    if st.button("🚪 Away Mode", use_container_width=True):
        st.session_state.light = False
        st.session_state.fan = False
        st.rerun()

with d:
    if st.button("☀️ Comfort Mode", use_container_width=True):
        st.session_state.light = True
        st.session_state.fan = True
        st.rerun()

# ---------------- ENERGY INTELLIGENCE ----------------
st.divider()
st.subheader("🌱 Energy Intelligence")

st.progress(min(total_watts / 60, 1.0))
st.write(f"Current illustrative room load: **{total_watts} W**")

if total_watts == 0:
    st.info("All simulated appliances are OFF. No appliance load is currently simulated.")
else:
    st.info(
        "HomeMind can help explain how switching off unused appliances "
        "can reduce unnecessary electricity consumption."
    )

st.divider()
st.caption(
    "HOMEMIND AI • COLLEGE EXHIBITION PROJECT • "
    "SIMULATION ONLY — NO ARDUINO OR PHYSICAL HARDWARE CONNECTION"
)
