
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HomeMind AI | Smart Living",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# All live controls, animations and calculations run inside
# this HTML/JavaScript dashboard. No paid API is required.

dashboard = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #090D18;
    --panel: #111827;
    --panel2: #151E30;
    --border: rgba(255,255,255,.075);
    --white: #F6F7FB;
    --muted: #8993A8;
    --yellow: #FFD66B;
    --blue: #7895FF;
    --green: #62D6A5;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: var(--bg);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

.dashboard {
    width: 100%;
    max-width: 1250px;
    margin: auto;
    padding: 24px 22px 38px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    margin-bottom: 25px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
}

.brand-icon {
    width: 47px;
    height: 47px;
    border-radius: 15px;
    display: grid;
    place-items: center;
    background: linear-gradient(135deg,#26395E,#18243E);
    border: 1px solid rgba(255,255,255,.1);
    font-size: 23px;
}

.brand-name {
    font-family: Outfit,sans-serif;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -.5px;
}

.brand-sub {
    color: var(--muted);
    font-size: 11px;
    margin-top: 2px;
    letter-spacing: 1.4px;
}

.status {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #121C2C;
    border: 1px solid var(--border);
    border-radius: 30px;
    padding: 10px 15px;
    color: #B9C5D9;
    font-size: 12px;
    font-weight: 700;
}

.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 10px var(--green);
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 30px;
    border-radius: 24px;
    background:
        radial-gradient(circle at 85% 15%,rgba(255,214,107,.12),transparent 30%),
        linear-gradient(115deg,#17233B,#101827 70%);
    border: 1px solid var(--border);
    margin-bottom: 26px;
}

.hero-tag {
    color: var(--yellow);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero h1 {
    font-family: Outfit,sans-serif;
    font-size: clamp(27px,4vw,39px);
    line-height: 1.12;
    margin: 0;
    letter-spacing: -.8px;
}

.hero p {
    color: #A9B4C8;
    font-size: 14px;
    line-height: 1.7;
    max-width: 540px;
    margin: 12px 0 0;
}

.section-title {
    font-family: Outfit,sans-serif;
    font-size: 20px;
    font-weight: 700;
    margin: 28px 0 14px;
}

.section-desc {
    color: var(--muted);
    font-size: 12px;
    margin-top: -8px;
    margin-bottom: 16px;
}

.devices {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 17px;
}

.card {
    background: linear-gradient(145deg,#141D2E,#101725);
    border: 1px solid var(--border);
    border-radius: 23px;
    padding: 23px;
    min-width: 0;
    box-shadow: 0 12px 35px rgba(0,0,0,.12);
}

.device-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
}

.device-title {
    font-family: Outfit,sans-serif;
    font-size: 19px;
    font-weight: 700;
}

.device-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 5px;
}

.state {
    color: #8D98AD;
    background: #202A3C;
    padding: 7px 11px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 800;
    white-space: nowrap;
}

.state.active {
    color: var(--green);
    background: rgba(98,214,165,.1);
}

.visual {
    height: 205px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    margin: 8px 0 3px;
}

.bulb-glow {
    position: absolute;
    width: 160px;
    height: 160px;
    border-radius: 50%;
    background: radial-gradient(circle,rgba(255,214,107,.28),transparent 70%);
    opacity: .7;
    transition: opacity .08s linear;
    pointer-events: none;
}

.bulb-svg {
    position: relative;
    z-index: 1;
    width: 125px;
    height: 160px;
    overflow: visible;
    filter: drop-shadow(0 0 0 transparent);
    transition: filter .08s linear;
}

.fan-svg {
    width: 190px;
    height: 175px;
    overflow: visible;
}

.fan-rotor {
    transform-origin: 100px 87px;
    animation: spin 1.5s linear infinite;
    animation-play-state: paused;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.icon-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
    min-height: 55px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,.12);
    background: #202B3D;
    color: white;
    cursor: pointer;
    font-family: 'DM Sans',sans-serif;
    font-weight: 800;
    font-size: 13px;
    transition: .2s ease;
    margin-top: 8px;
}

.icon-button.on {
    background: linear-gradient(110deg,#554A2D,#3D3627);
    border-color: rgba(255,214,107,.35);
    color: var(--yellow);
}

.icon-button:hover {
    transform: translateY(-1px);
    filter: brightness(1.15);
}

.icon-button:active {
    transform: scale(.985);
}

.switch-symbol {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    border: 1.5px solid currentColor;
    font-size: 13px;
}

.control-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 23px;
    margin-bottom: 11px;
}

.control-label {
    font-size: 13px;
    font-weight: 700;
    color: #DDE3EF;
}

.control-value {
    color: var(--yellow);
    font-family: Outfit,sans-serif;
    font-size: 15px;
    font-weight: 800;
}

.range {
    appearance: none;
    width: 100%;
    height: 11px;
    border-radius: 20px;
    outline: none;
    cursor: pointer;
    margin: 8px 0 4px;
    background: #303A4D;
    touch-action: pan-y;
}

.range::-webkit-slider-thumb {
    appearance: none;
    width: 27px;
    height: 27px;
    border-radius: 50%;
    background: var(--yellow);
    border: 5px solid #FFF3D1;
    box-shadow: 0 0 0 5px rgba(255,214,107,.12),0 2px 12px rgba(0,0,0,.4);
    cursor: grab;
}

.range::-moz-range-thumb {
    width: 19px;
    height: 19px;
    border-radius: 50%;
    background: var(--yellow);
    border: 5px solid #FFF3D1;
    box-shadow: 0 0 0 5px rgba(255,214,107,.12);
    cursor: grab;
}

.range:disabled {
    opacity: .3;
    cursor: not-allowed;
}

.range:disabled::-webkit-slider-thumb {
    cursor: not-allowed;
}

.range-help {
    display: flex;
    justify-content: space-between;
    color: #727F95;
    font-size: 10px;
    margin-top: 8px;
}

.power-line {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border);
    padding-top: 15px;
    margin-top: 17px;
    color: var(--muted);
    font-size: 12px;
}

.power-line strong {
    color: white;
    font-size: 14px;
}

.metrics {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));
    gap: 15px;
}

.metric {
    background: linear-gradient(145deg,#151F30,#101725);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 21px;
    min-width: 0;
}

.metric-label {
    color: #98A3B8;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .7px;
}

.metric-value {
    font-family: Outfit,sans-serif;
    font-size: clamp(22px,3vw,31px);
    font-weight: 800;
    margin-top: 10px;
    letter-spacing: -.5px;
    color: white;
    overflow-wrap: anywhere;
}

.metric-value.yellow {
    color: var(--yellow);
}

.metric-note {
    color: #7E8AA0;
    font-size: 11px;
    margin-top: 6px;
}

.breakdown {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 15px;
}

.break-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin: 15px 0;
    font-size: 12px;
}

.break-row span:first-child {
    color: #A1ACC0;
}

.break-row strong {
    color: white;
}

.bar {
    width: 100%;
    height: 7px;
    background: #2A3447;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 10px;
}

.bar-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(90deg,#E9B84E,#FFE08B);
    width: 0%;
    transition: width .08s linear;
}

.assumption-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-bottom: 15px;
}

.assumption {
    padding: 9px 12px;
    border-radius: 10px;
    background: #202A3C;
    border: 1px solid var(--border);
    color: #DCE3EF;
    font-size: 11px;
    font-weight: 600;
}

.notice {
    color: #8390A6;
    font-size: 11px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    padding: 30px 10px 5px;
    color: #68758B;
    font-size: 10px;
    letter-spacing: 1px;
}

.disabled-visual {
    opacity: .35;
}

@media(max-width:700px) {
    .dashboard {
        padding: 16px 12px 28px;
    }

    .hero {
        padding: 24px 20px;
        border-radius: 19px;
    }

    .devices {
        grid-template-columns: 1fr;
    }

    .metrics {
        grid-template-columns: 1fr;
        gap: 10px;
    }

    .metric {
        padding: 17px;
    }

    .metric-value {
        font-size: 27px;
    }

    .breakdown {
        grid-template-columns: 1fr;
    }

    .card {
        padding: 19px;
    }

    .visual {
        height: 185px;
    }

    .brand-name {
        font-size: 19px;
    }

    .status {
        padding: 9px 10px;
        font-size: 10px;
    }

    .range {
        height: 13px;
        margin: 12px 0 8px;
    }

    .range::-webkit-slider-thumb {
        width: 31px;
        height: 31px;
    }
}
</style>
</head>

<body>
<div class="dashboard">

    <header class="header">
        <div class="brand">
            <div class="brand-icon">⌂</div>
            <div>
                <div class="brand-name">HomeMind <span style="color:#FFD66B">AI</span></div>
                <div class="brand-sub">SMART LIVING SYSTEM</div>
            </div>
        </div>

        <div class="status">
            <span class="status-dot"></span>
            SIMULATION ACTIVE
        </div>
    </header>

    <section class="hero">
        <div class="hero-tag">✦ YOUR SMART HOME</div>
        <h1>Control your space.<br>Understand your energy.</h1>
        <p>
            A smarter way to manage everyday appliances.
            Adjust your settings and watch your energy estimates
            respond instantly.
        </p>
    </section>

    <div class="section-title">Appliance Control</div>
    <div class="section-desc">
        Tap an appliance icon to switch it on or off.
    </div>

    <section class="devices">

        <!-- LIGHT CARD -->

        <div class="card">
            <div class="device-head">
                <div>
                    <div class="device-title">Smart Lighting</div>
                    <div class="device-subtitle">Ambient brightness control</div>
                </div>
                <div class="state active" id="lightState">● ON</div>
            </div>

            <div class="visual" id="bulbVisual">
                <div class="bulb-glow" id="bulbGlow"></div>

                <svg class="bulb-svg" id="bulbSvg" viewBox="0 0 125 160">
                    <defs>
                        <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#FFF1B6"/>
                            <stop offset="100%" stop-color="#E6A92F"/>
                        </linearGradient>
                    </defs>

                    <path id="bulbGlass"
                        d="M62 12 C29 12 15 38 23 67
                        C27 83 42 94 46 112
                        L78 112 C82 94 97 83 101 67
                        C109 38 95 12 62 12Z"
                        fill="url(#glass)"
                        stroke="#FFD66B"
                        stroke-width="3"/>

                    <path d="M47 116 L77 116 M48 124 L76 124
                    M51 132 L73 132 M55 140 L69 140"
                        stroke="#B6C0D1"
                        stroke-width="5"
                        stroke-linecap="round"/>

                    <path d="M53 145 L71 145"
                        stroke="#7C879B"
                        stroke-width="4"
                        stroke-linecap="round"/>
                </svg>
            </div>

            <button class="icon-button on" id="lightToggle" type="button"
                aria-label="Turn light off">
                <span class="switch-symbol" id="lightSymbol">✓</span>
                <span id="lightButtonText">LIGHT IS ON · TAP TO TURN OFF</span>
            </button>

            <div class="control-row">
                <span class="control-label">Brightness</span>
                <span class="control-value" id="lightValue">70%</span>
            </div>

            <input class="range" id="lightSlider" type="range"
                min="0" max="100" value="70">

            <div class="range-help">
                <span>DIM</span>
                <span>BRIGHT</span>
            </div>

            <div class="power-line">
                <span>Current power consumption</span>
                <strong id="lightWatts">7.0 W</strong>
            </div>
        </div>

        <!-- FAN CARD -->

        <div class="card">
            <div class="device-head">
                <div>
                    <div class="device-title">Smart Ceiling Fan</div>
                    <div class="device-subtitle">Adjustable speed control</div>
                </div>
                <div class="state active" id="fanState">● ON</div>
            </div>

            <div class="visual" id="fanVisual">
                <svg class="fan-svg" viewBox="0 0 200 175">
                    <defs>
                        <linearGradient id="bladeGradient" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#FFF0BB"/>
                            <stop offset="100%" stop-color="#B5C8FF"/>
                        </linearGradient>
                    </defs>

                    <g id="fanRotor" class="fan-rotor">
                        <g fill="url(#bladeGradient)">
                            <path d="M100 87 C85 66 76 38 91 12
                            C99 -2 114 3 117 20
                            C121 44 108 72 100 87Z"/>

                            <path d="M100 87 C85 66 76 38 91 12
                            C99 -2 114 3 117 20
                            C121 44 108 72 100 87Z"
                            transform="rotate(120 100 87)"/>

                            <path d="M100 87 C85 66 76 38 91 12
                            C99 -2 114 3 117 20
                            C121 44 108 72 100 87Z"
                            transform="rotate(240 100 87)"/>
                        </g>

                        <circle cx="100" cy="87" r="13"
                            fill="#263A61" stroke="#E7EDFF" stroke-width="3"/>
                        <circle cx="100" cy="87" r="4" fill="#FFD66B"/>
                    </g>
                </svg>
            </div>

            <button class="icon-button on" id="fanToggle" type="button"
                aria-label="Turn fan off">
                <span class="switch-symbol" id="fanSymbol">✓</span>
                <span id="fanButtonText">FAN IS ON · TAP TO TURN OFF</span>
            </button>

            <div class="control-row">
                <span class="control-label">Fan speed</span>
                <span class="control-value" id="fanValue">60%</span>
            </div>

            <input class="range" id="fanSlider" type="range"
                min="0" max="100" value="60">

            <div class="range-help">
                <span>SLOW</span>
                <span>FAST</span>
            </div>

            <div class="power-line">
                <span>Current power consumption</span>
                <strong id="fanWatts">30.0 W</strong>
            </div>
        </div>

    </section>

    <!-- ENERGY METRICS -->

    <div class="section-title">Energy Dashboard</div>
    <div class="section-desc">
        Estimates update instantly as you adjust the appliances.
    </div>

    <section class="metrics">
        <div class="metric">
            <div class="metric-label">LIVE POWER LOAD</div>
            <div class="metric-value" id="totalPower">37.0 W</div>
            <div class="metric-note">Combined appliance power</div>
        </div>

        <div class="metric">
            <div class="metric-label">MONTHLY ENERGY</div>
            <div class="metric-value" id="monthlyEnergy">5.55 kWh</div>
            <div class="metric-note">Estimated electricity units</div>
        </div>

        <div class="metric">
            <div class="metric-label">PREDICTED MONTHLY BILL</div>
            <div class="metric-value yellow" id="monthlyCost">₹44.40</div>
            <div class="metric-note">Estimated electricity cost</div>
        </div>
    </section>

    <!-- BREAKDOWN -->

    <div class="section-title">Appliance Breakdown</div>

    <section class="breakdown">
        <div class="card">
            <div class="device-title">💡 Lighting</div>

            <div class="break-row">
                <span>Monthly energy</span>
                <strong id="lightEnergy">1.05 kWh</strong>
            </div>
            <div class="bar">
                <div class="bar-fill" id="lightBar"></div>
            </div>

            <div class="break-row">
                <span>Monthly estimated cost</span>
                <strong id="lightCost">₹8.40</strong>
            </div>
        </div>

        <div class="card">
            <div class="device-title">🌀 Ceiling Fan</div>

            <div class="break-row">
                <span>Monthly energy</span>
                <strong id="fanEnergy">4.50 kWh</strong>
            </div>
            <div class="bar">
                <div class="bar-fill" id="fanBar"></div>
            </div>

            <div class="break-row">
                <span>Monthly estimated cost</span>
                <strong id="fanCost">₹36.00</strong>
            </div>
        </div>
    </section>

    <!-- ASSUMPTIONS -->

    <div class="section-title">Calculation Assumptions</div>

    <div class="card">
        <div class="assumption-grid">
            <span class="assumption">Light: 10 W maximum</span>
            <span class="assumption">Fan: 50 W maximum</span>
            <span class="assumption">Daily use: 5 hours</span>
            <span class="assumption">30-day month</span>
            <span class="assumption">Tariff: ₹8 / kWh</span>
        </div>

        <div class="notice">
            This dashboard is an interactive simulation.
            Power consumption is estimated using illustrative linear
            appliance models. Actual fan power does not necessarily
            vary linearly with speed. Real consumption and electricity
            bills depend on appliance specifications, usage and local tariffs.
            These controls do not operate physical appliances or the Arduino model.
        </div>
    </div>

    <div class="footer">
        HOMEMIND AI · SMART HOME ENERGY SIMULATOR
        <br><br>
        DESIGNED FOR SMARTER EVERYDAY LIVING
    </div>

</div>

<script>
(function () {
    const LIGHT_WATTS = 20;
    const FAN_WATTS = 90;
    const HOURS_PER_DAY = 5;
    const DAYS_PER_MONTH = 30;
    const RATE = 8;

    let lightOn = true;
    let fanOn = true;

    let light = 70;
    let fan = 60;

    const $ = (id) => document.getElementById(id);

    const lightSlider = $("lightSlider");
    const fanSlider = $("fanSlider");

    function money(value) {
        return "₹" + value.toFixed(2);
    }

    function updateSliderTrack(slider) {
        const min = Number(slider.min);
        const max = Number(slider.max);
        const value = Number(slider.value);
        const percentage = ((value - min) / (max - min)) * 100;

        slider.style.background =
            `linear-gradient(to right, #FFD66B ${percentage}%, #303A4D ${percentage}%)`;
    }

    function updateLightVisual() {
        const intensity = lightOn ? light / 100 : 0;

        $("bulbGlow").style.opacity = intensity;
        $("bulbSvg").style.filter =
            intensity > 0
            ? `drop-shadow(0 0 ${8 + intensity * 25}px rgba(255,214,107,${intensity * .8}))`
            : "none";

        $("bulbGlass").style.opacity = lightOn ? .2 + intensity * .8 : .2;

        $("lightState").textContent = lightOn ? "● ON" : "○ OFF";
        $("lightState").classList.toggle("active", lightOn);

        $("lightButtonText").textContent =
            lightOn ? "LIGHT IS ON · TAP TO TURN OFF" :
                      "LIGHT IS OFF · TAP TO TURN ON";

        $("lightSymbol").textContent = lightOn ? "✓" : "○";
        $("lightToggle").classList.toggle("on", lightOn);
        $("lightToggle").setAttribute(
            "aria-label",
            lightOn ? "Turn light off" : "Turn light on"
        );

        $("lightSlider").disabled = !lightOn;
        $("lightValue").textContent = light + "%";
        $("lightWatts").textContent =
            (lightOn ? LIGHT_WATTS * light / 100 : 0).toFixed(1) + " W";

        $("bulbVisual").classList.toggle("disabled-visual", !lightOn);
        updateSliderTrack(lightSlider);
    }

    function updateFanVisual() {
        const rotor = $("fanRotor");

        const activeSpeed = fanOn ? fan : 0;

        if (activeSpeed > 0) {
            const duration = 3.5 - (activeSpeed / 100) * 3.25;
            rotor.style.animationDuration = duration + "s";
            rotor.style.animationPlayState = "running";
        } else {
            rotor.style.animationPlayState = "paused";
        }

        $("fanState").textContent = fanOn ? "● ON" : "○ OFF";
        $("fanState").classList.toggle("active", fanOn);

        $("fanButtonText").textContent =
            fanOn ? "FAN IS ON · TAP TO TURN OFF" :
                    "FAN IS OFF · TAP TO TURN ON";

        $("fanSymbol").textContent = fanOn ? "✓" : "○";
        $("fanToggle").classList.toggle("on", fanOn);
        $("fanToggle").setAttribute(
            "aria-label",
            fanOn ? "Turn fan off" : "Turn fan on"
        );

        $("fanSlider").disabled = !fanOn;
        $("fanValue").textContent = fan + "%";
        $("fanWatts").textContent =
            (fanOn ? FAN_WATTS * fan / 100 : 0).toFixed(1) + " W";

        $("fanVisual").classList.toggle("disabled-visual", !fanOn);
        updateSliderTrack(fanSlider);
    }

    function updateCalculations() {
        const lightPower = lightOn ? LIGHT_WATTS * light / 100 : 0;
        const fanPower = fanOn ? FAN_WATTS * fan / 100 : 0;

        const totalPower = lightPower + fanPower;

        const lightEnergy =
            lightPower * HOURS_PER_DAY * DAYS_PER_MONTH / 1000;

        const fanEnergy =
            fanPower * HOURS_PER_DAY * DAYS_PER_MONTH / 1000;

        const monthlyEnergy = lightEnergy + fanEnergy;

        const lightCost = lightEnergy * RATE;
        const fanCost = fanEnergy * RATE;

        const totalCost = monthlyEnergy * RATE;

        $("totalPower").textContent = totalPower.toFixed(1) + " W";
        $("monthlyEnergy").textContent = monthlyEnergy.toFixed(2) + " kWh";
        $("monthlyCost").textContent = money(totalCost);

        $("lightEnergy").textContent = lightEnergy.toFixed(2) + " kWh";
        $("fanEnergy").textContent = fanEnergy.toFixed(2) + " kWh";

        $("lightCost").textContent = money(lightCost);
        $("fanCost").textContent = money(fanCost);

        const lightShare = monthlyEnergy > 0
            ? lightEnergy / monthlyEnergy * 100 : 0;

        const fanShare = monthlyEnergy > 0
            ? fanEnergy / monthlyEnergy * 100 : 0;

        $("lightBar").style.width = lightShare + "%";
        $("fanBar").style.width = fanShare + "%";
    }

    function updateAll() {
        updateLightVisual();
        updateFanVisual();
        updateCalculations();
    }

    lightSlider.addEventListener("input", function () {
        light = Number(this.value);
        updateAll();
    });

    fanSlider.addEventListener("input", function () {
        fan = Number(this.value);
        updateAll();
    });

    $("lightToggle").addEventListener("click", function () {
        lightOn = !lightOn;
        updateAll();
    });

    $("fanToggle").addEventListener("click", function () {
        fanOn = !fanOn;
        updateAll();
    });

    updateAll();
})();
</script>

</body>
</html>
"""

components.html(
    dashboard,
    height=1800,
    scrolling=True
)
