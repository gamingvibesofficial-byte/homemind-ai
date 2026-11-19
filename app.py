
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HomeMind AI | Smart Living",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

dashboard = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
 --bg:#080C16;
 --shell:#111827;
 --screen:#0B1220;
 --panel:#18243A;
 --line:rgba(255,255,255,.09);
 --white:#F7F8FC;
 --muted:#94A0B5;
 --yellow:#FFD66B;
 --green:#62D6A5;
}

* { box-sizing:border-box; }

html,body {
 margin:0;
 background:transparent;
 color:var(--white);
 font-family:'DM Sans',sans-serif;
}

button { font:inherit; }

.stage {
 width:100%;
 display:flex;
 justify-content:center;
 padding:18px 8px 26px;
}

.phone {
 width:100%;
 max-width:430px;
 min-height:830px;
 background:var(--shell);
 border:2px solid #3B465A;
 border-radius:43px;
 padding:9px;
 box-shadow:0 28px 80px rgba(0,0,0,.48);
 overflow:hidden;
 position:relative;
}

.screen {
 min-height:810px;
 background:var(--screen);
 border-radius:34px;
 overflow:hidden;
 position:relative;
 padding-bottom:86px;
}

.notch {
 position:absolute;
 top:8px;
 left:50%;
 transform:translateX(-50%);
 width:88px;
 height:19px;
 border-radius:20px;
 background:#03060B;
 z-index:3;
}

.statusbar {
 height:34px;
 padding:8px 22px 0;
 display:flex;
 align-items:center;
 justify-content:space-between;
 font-size:11px;
 font-weight:800;
}

.status-icons {
 display:flex;
 gap:6px;
 align-items:center;
}

.apphead {
 padding:17px 20px 12px;
 display:flex;
 justify-content:space-between;
 align-items:center;
 gap:10px;
}

.brand {
 display:flex;
 align-items:center;
 gap:10px;
}

.brand-icon {
 width:39px;
 height:39px;
 border-radius:13px;
 display:grid;
 place-items:center;
 background:linear-gradient(140deg,#344B75,#1A2945);
 border:1px solid var(--line);
 font-size:21px;
}

.brand-name {
 font:800 18px Outfit,sans-serif;
}

.brand-sub {
 font-size:8px;
 letter-spacing:1.5px;
 color:var(--muted);
 margin-top:2px;
}

.sim-pill {
 font-size:9px;
 font-weight:800;
 color:var(--green);
 background:rgba(98,214,165,.09);
 border:1px solid rgba(98,214,165,.18);
 padding:7px 9px;
 border-radius:20px;
 white-space:nowrap;
}

.page {
 display:none;
 padding:5px 17px 20px;
 animation:appear .2s ease;
}

.page.active { display:block; }

@keyframes appear {
 from { opacity:.4; transform:translateY(4px); }
 to { opacity:1; transform:translateY(0); }
}

.greeting { padding:10px 3px 17px; }

.eyebrow {
 font-size:9px;
 font-weight:800;
 letter-spacing:1.7px;
 color:var(--yellow);
 margin-bottom:7px;
}

h1 {
 font:700 27px/1.12 Outfit,sans-serif;
 letter-spacing:-.7px;
 margin:0;
}

.subtext {
 font-size:11px;
 line-height:1.55;
 color:var(--muted);
 margin:7px 0 0;
}

.hero {
 border:1px solid var(--line);
 border-radius:20px;
 padding:16px;
 background:
 radial-gradient(circle at 90% 10%,rgba(255,214,107,.12),transparent 38%),
 linear-gradient(130deg,#1B2A46,#121D30);
 margin-bottom:19px;
}

.hero-top {
 display:flex;
 justify-content:space-between;
 align-items:center;
 color:#AEBBD0;
 font-size:10px;
 font-weight:700;
}

.live-dot {
 width:7px;
 height:7px;
 border-radius:50%;
 background:var(--green);
 display:inline-block;
 margin-right:5px;
 box-shadow:0 0 9px var(--green);
}

.hero-number {
 font:800 33px Outfit,sans-serif;
 margin-top:9px;
}

.hero-foot {
 font-size:10px;
 color:var(--yellow);
 margin-top:3px;
}

.section-head {
 display:flex;
 justify-content:space-between;
 align-items:center;
 margin:19px 2px 10px;
}

.section-title {
 font:700 16px Outfit,sans-serif;
}

.section-hint {
 font-size:9px;
 color:var(--muted);
}

.devices {
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:10px;
}

.device {
 background:linear-gradient(145deg,#18243A,#121B2B);
 border:1px solid var(--line);
 border-radius:18px;
 padding:13px;
 min-width:0;
}

.device-top {
 display:flex;
 justify-content:space-between;
 align-items:flex-start;
}

.device-icon { font-size:25px; }

.device-state {
 font-size:8px;
 font-weight:800;
 border-radius:12px;
 padding:5px 7px;
 background:#273247;
 color:#A6B1C4;
}

.device-state.on {
 color:var(--green);
 background:rgba(98,214,165,.1);
}

.device-name {
 font:700 12px Outfit,sans-serif;
 margin-top:9px;
}

.device-watts {
 font-size:9px;
 color:var(--muted);
 margin-top:3px;
}

.toggle {
 border:1px solid var(--line);
 border-radius:11px;
 background:#253149;
 color:#D8DFEB;
 width:100%;
 padding:9px 5px;
 margin-top:11px;
 font-size:9px;
 font-weight:800;
 cursor:pointer;
 min-height:35px;
}

.toggle.on {
 background:rgba(255,214,107,.13);
 border-color:rgba(255,214,107,.32);
 color:var(--yellow);
}

.visual-card {
 background:linear-gradient(145deg,#18243A,#121B2B);
 border:1px solid var(--line);
 border-radius:18px;
 padding:14px;
 margin-top:10px;
}

.visual-head {
 display:flex;
 justify-content:space-between;
 align-items:center;
}

.visual-title {
 font:700 12px Outfit,sans-serif;
}

.visual-meta {
 font-size:9px;
 color:var(--muted);
}

.visual {
 height:105px;
 display:flex;
 align-items:center;
 justify-content:center;
 position:relative;
}

.bulb-glow {
 position:absolute;
 width:100px;
 height:100px;
 border-radius:50%;
 background:radial-gradient(circle,rgba(255,214,107,.35),transparent 70%);
 opacity:.7;
 pointer-events:none;
}

.bulb-svg {
 width:65px;
 height:90px;
 position:relative;
 filter:drop-shadow(0 0 14px rgba(255,214,107,.5));
}

.fan-svg {
 width:125px;
 height:110px;
 overflow:visible;
}

.fan-rotor {
 transform-origin:100px 87px;
 animation:spin 1.5s linear infinite;
 animation-play-state:paused;
}

@keyframes spin {
 to { transform:rotate(360deg); }
}

.range {
 appearance:none;
 width:100%;
 height:9px;
 border-radius:20px;
 outline:none;
 cursor:pointer;
 background:#303A4D;
 touch-action:pan-y;
}

.range::-webkit-slider-thumb {
 appearance:none;
 width:25px;
 height:25px;
 border-radius:50%;
 background:var(--yellow);
 border:4px solid #FFF3D1;
 box-shadow:0 0 0 4px rgba(255,214,107,.12);
 cursor:grab;
}

.range::-moz-range-thumb {
 width:17px;
 height:17px;
 border-radius:50%;
 background:var(--yellow);
 border:4px solid #FFF3D1;
 cursor:grab;
}

.range:disabled {
 opacity:.3;
 cursor:not-allowed;
}

.range-row {
 display:flex;
 justify-content:space-between;
 align-items:center;
 margin:7px 0 8px;
 font-size:10px;
 color:#DCE3EF;
 font-weight:700;
}

.range-row strong {
 color:var(--yellow);
 font:800 12px Outfit,sans-serif;
}

.watt-line {
 display:flex;
 justify-content:space-between;
 border-top:1px solid var(--line);
 padding-top:9px;
 margin-top:10px;
 color:var(--muted);
 font-size:9px;
}

.watt-line strong {
 color:var(--white);
 font-size:10px;
}

.add-card {
 border:1px dashed rgba(255,214,107,.45);
 background:rgba(255,214,107,.035);
 border-radius:17px;
 min-height:106px;
 display:flex;
 flex-direction:column;
 align-items:center;
 justify-content:center;
 gap:6px;
 color:var(--yellow);
 cursor:pointer;
 transition:.2s;
}

.add-card:hover {
 background:rgba(255,214,107,.09);
 transform:translateY(-1px);
}

.add-plus { font-size:25px; line-height:1; }
.add-label { font-size:10px; font-weight:800; }
.add-caption { font-size:8px; color:var(--muted); }

.extra-device {
 background:linear-gradient(145deg,#18243A,#121B2B);
 border:1px solid var(--line);
 border-radius:15px;
 padding:11px;
 display:flex;
 align-items:center;
 gap:9px;
 min-width:0;
}

.extra-icon { font-size:23px; }

.extra-info { min-width:0; flex:1; }

.extra-name {
 font:700 10px Outfit,sans-serif;
 white-space:nowrap;
 overflow:hidden;
 text-overflow:ellipsis;
}

.extra-desc {
 font-size:8px;
 color:var(--muted);
 margin-top:3px;
}

.extra-actions {
 display:flex;
 gap:5px;
 align-items:center;
}

.mini-toggle,.remove {
 border:1px solid var(--line);
 background:#273247;
 color:#DCE3EF;
 border-radius:8px;
 padding:6px 7px;
 font-size:8px;
 font-weight:800;
 cursor:pointer;
}

.mini-toggle.on {
 color:var(--yellow);
 border-color:rgba(255,214,107,.3);
}

.remove {
 color:#FF9B9B;
 padding:6px;
}

.metric-grid {
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:9px;
}

.metric {
 background:linear-gradient(145deg,#18243A,#121B2B);
 border:1px solid var(--line);
 border-radius:16px;
 padding:14px;
}

.metric.wide { grid-column:1/-1; }

.metric-label {
 font-size:8px;
 font-weight:800;
 letter-spacing:.8px;
 color:var(--muted);
}

.metric-value {
 font:800 23px Outfit,sans-serif;
 margin-top:7px;
 overflow-wrap:anywhere;
}

.metric-value.yellow { color:var(--yellow); }

.metric-note {
 font-size:9px;
 color:#7E8AA0;
 margin-top:4px;
}

.break-card,.settings-card {
 background:linear-gradient(145deg,#18243A,#121B2B);
 border:1px solid var(--line);
 border-radius:17px;
 padding:14px;
 margin-top:10px;
}

.break-title {
 font:700 12px Outfit,sans-serif;
}

.break-row {
 display:flex;
 justify-content:space-between;
 gap:10px;
 margin-top:13px;
 font-size:10px;
 color:#AAB5C8;
}

.break-row strong { color:white; }

.bar {
 height:6px;
 background:#303A4D;
 border-radius:10px;
 overflow:hidden;
 margin-top:8px;
}

.bar-fill {
 height:100%;
 border-radius:10px;
 background:linear-gradient(90deg,#E9B84E,#FFE08B);
 width:0%;
 transition:width .1s;
}

.setting-row {
 display:flex;
 justify-content:space-between;
 gap:12px;
 padding:11px 0;
 border-bottom:1px solid var(--line);
 font-size:10px;
}

.setting-row:last-child { border-bottom:0; }
.setting-row span { color:var(--muted); }
.setting-row strong { text-align:right; }

.notice {
 font-size:9px;
 line-height:1.65;
 color:#8B98AD;
 margin-top:13px;
}

.bottom-nav {
 position:absolute;
 bottom:0;
 left:0;
 right:0;
 height:76px;
 background:rgba(14,22,36,.97);
 border-top:1px solid var(--line);
 display:grid;
 grid-template-columns:repeat(3,1fr);
 padding:9px 14px 14px;
 z-index:5;
}

.nav-btn {
 border:0;
 background:transparent;
 color:#78859B;
 display:flex;
 flex-direction:column;
 align-items:center;
 justify-content:center;
 gap:4px;
 font-size:8px;
 font-weight:800;
 cursor:pointer;
 border-radius:12px;
}

.nav-icon { font-size:19px; line-height:1; }

.nav-btn.active {
 color:var(--yellow);
 background:rgba(255,214,107,.07);
}

.home-indicator {
 position:absolute;
 bottom:4px;
 left:50%;
 transform:translateX(-50%);
 width:76px;
 height:4px;
 border-radius:5px;
 background:#CBD1DC;
 opacity:.65;
 z-index:7;
 pointer-events:none;
}

.modal-backdrop {
 position:absolute;
 inset:0;
 background:rgba(0,0,0,.68);
 z-index:10;
 display:none;
 align-items:flex-end;
 padding:10px;
}

.modal-backdrop.open { display:flex; }

.modal {
 width:100%;
 background:#172338;
 border:1px solid rgba(255,255,255,.13);
 border-radius:23px;
 padding:17px;
 box-shadow:0 20px 60px rgba(0,0,0,.45);
 animation:slideup .2s ease;
}

@keyframes slideup {
 from { transform:translateY(20px); opacity:.5; }
 to { transform:translateY(0); opacity:1; }
}

.modal-head {
 display:flex;
 justify-content:space-between;
 align-items:center;
 margin-bottom:5px;
}

.modal-title {
 font:700 17px Outfit,sans-serif;
}

.close-modal {
 border:0;
 background:#2A3850;
 color:#DCE3EF;
 border-radius:9px;
 width:29px;
 height:29px;
 cursor:pointer;
 font-size:16px;
}

.modal-desc {
 font-size:10px;
 color:var(--muted);
 margin-bottom:13px;
}

.option-grid {
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:8px;
}

.option {
 border:1px solid var(--line);
 border-radius:14px;
 background:#202E45;
 color:white;
 padding:12px 9px;
 text-align:left;
 cursor:pointer;
 min-height:76px;
}

.option:hover {
 border-color:rgba(255,214,107,.45);
 background:#293750;
}

.option-emoji { font-size:22px; }
.option-name { font:700 11px Outfit,sans-serif; margin-top:6px; }
.option-power { font-size:8px; color:var(--muted); margin-top:2px; }

.toast {
 position:absolute;
 left:50%;
 bottom:88px;
 transform:translateX(-50%);
 background:#26364E;
 border:1px solid rgba(255,214,107,.25);
 color:#FFF0C2;
 padding:9px 13px;
 border-radius:20px;
 font-size:9px;
 white-space:nowrap;
 z-index:12;
 display:none;
}

.toast.show { display:block; }

.page-footer {
 text-align:center;
 color:#65728A;
 font-size:8px;
 letter-spacing:1px;
 padding:20px 0 4px;
}

@media(max-width:480px) {
 .stage { padding:0; margin:0; }
 .phone {
  max-width:none;
  border:0;
  border-radius:0;
  padding:0;
  min-height:100vh;
  box-shadow:none;
 }
 .screen {
  min-height:100vh;
  border-radius:0;
  padding-bottom:90px;
 }
 .notch { top:7px; }
 .statusbar { padding-top:9px; }
 .bottom-nav { position:fixed; }
 .home-indicator { position:fixed; }
}
</style>
</head>

<body>
<div class="stage">
<div class="phone">
<div class="screen">

<div class="notch"></div>

<div class="statusbar">
 <span id="clock">21:41</span>
 <div class="status-icons">
  <span>▮▮▮</span><span>⌁</span><span>▰</span>
 </div>
</div>

<header class="apphead">
 <div class="brand">
  <div class="brand-icon">⌂</div>
  <div>
   <div class="brand-name">HomeMind <span style="color:#FFD66B">AI</span></div>
   <div class="brand-sub">SMART LIVING SYSTEM</div>
  </div>
 </div>
 <div class="sim-pill">● SIMULATION</div>
</header>

<main>

<!-- HOME PAGE -->
<section class="page active" id="homePage">

 <div class="greeting">
  <div class="eyebrow">✦ YOUR SMART HOME</div>
  <h1>Good evening.<br>Welcome home.</h1>
  <p class="subtext">
   Your space, your comfort. Manage your appliances
   and keep an eye on energy.
  </p>
 </div>

 <div class="hero">
  <div class="hero-top">
   <span>⚡ LIVE POWER USAGE</span>
   <span><i class="live-dot"></i>LIVE ESTIMATE</span>
  </div>
  <div class="hero-number" id="heroPower">68.0 W</div>
  <div class="hero-foot" id="activeCount">2 appliances currently active</div>
 </div>

 <div class="section-head">
  <div class="section-title">Your appliances</div>
  <div class="section-hint" id="deviceCount">2 DEVICES</div>
 </div>

 <div class="devices">

  <div class="device">
   <div class="device-top">
    <span class="device-icon">💡</span>
    <span class="device-state on" id="lightState">ON</span>
   </div>
   <div class="device-name">Smart Light</div>
   <div class="device-watts">Maximum 20 W</div>
   <button class="toggle on" id="lightToggle">TURN OFF</button>
  </div>

  <div class="device">
   <div class="device-top">
    <span class="device-icon">🌀</span>
    <span class="device-state on" id="fanState">ON</span>
   </div>
   <div class="device-name">Ceiling Fan</div>
   <div class="device-watts">Maximum 90 W</div>
   <button class="toggle on" id="fanToggle">TURN OFF</button>
  </div>

  <button class="add-card" id="openAdd">
   <span class="add-plus">＋</span>
   <span class="add-label">Add New Appliance</span>
   <span class="add-caption">CUSTOMISE YOUR SMART HOME</span>
  </button>

 </div>

 <div class="section-head">
  <div class="section-title">Quick controls</div>
  <div class="section-hint">LIVE RESPONSE</div>
 </div>

 <!-- LIGHT CONTROL -->
 <div class="visual-card">

  <div class="visual-head">
   <span class="visual-title">💡 Light brightness</span>
   <span class="visual-meta" id="lightValue">70%</span>
  </div>

  <div class="visual">
   <div class="bulb-glow" id="bulbGlow"></div>

   <svg class="bulb-svg" viewBox="0 0 125 160">
    <defs>
     <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFF1B6"/>
      <stop offset="100%" stop-color="#E6A92F"/>
     </linearGradient>
    </defs>

    <path id="bulbGlass"
     d="M62 12 C29 12 15 38 23 67
     C27 83 42 94 46 112 L78 112
     C82 94 97 83 101 67
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

  <div class="range-row">
   <span>DIM</span><strong id="lightRangeLabel">70%</strong>
  </div>

  <input class="range" id="lightSlider"
   type="range" min="0" max="100" value="70">

  <div class="watt-line">
   <span>Current light power</span>
   <strong id="lightWatts">14.0 W</strong>
  </div>

 </div>

 <!-- FAN CONTROL -->
 <div class="visual-card">

  <div class="visual-head">
   <span class="visual-title">🌀 Fan speed</span>
   <span class="visual-meta" id="fanValue">60%</span>
  </div>

  <div class="visual">

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
      C99 -2 114 3 117 20 C121 44 108 72 100 87Z"/>

      <path d="M100 87 C85 66 76 38 91 12
      C99 -2 114 3 117 20 C121 44 108 72 100 87Z"
      transform="rotate(120 100 87)"/>

      <path d="M100 87 C85 66 76 38 91 12
      C99 -2 114 3 117 20 C121 44 108 72 100 87Z"
      transform="rotate(240 100 87)"/>
     </g>

     <circle cx="100" cy="87" r="13"
      fill="#263A61" stroke="#E7EDFF" stroke-width="3"/>
     <circle cx="100" cy="87" r="4" fill="#FFD66B"/>

    </g>
   </svg>

  </div>

  <div class="range-row">
   <span>SLOW</span><strong id="fanRangeLabel">60%</strong>
  </div>

  <input class="range" id="fanSlider"
   type="range" min="0" max="100" value="60">

  <div class="watt-line">
   <span>Current fan power</span>
   <strong id="fanWatts">54.0 W</strong>
  </div>

 </div>

 <div id="extraDevices"
  style="display:grid;gap:8px;margin-top:10px">
 </div>

 <div class="page-footer">
  HOMEMIND AI · SMARTER EVERYDAY LIVING
 </div>

</section>

<!-- ENERGY PAGE -->
<section class="page" id="energyPage">

 <div class="greeting">
  <div class="eyebrow">⚡ ENERGY INSIGHTS</div>
  <h1>Your energy,<br>made clearer.</h1>
  <p class="subtext">
   A live estimate based on your current appliance settings.
  </p>
 </div>

 <div class="metric-grid">

  <div class="metric">
   <div class="metric-label">LIVE POWER LOAD</div>
   <div class="metric-value" id="totalPower">68.0 W</div>
   <div class="metric-note">Combined appliance power</div>
  </div>

  <div class="metric">
   <div class="metric-label">MONTHLY ENERGY</div>
   <div class="metric-value" id="monthlyEnergy">10.20</div>
   <div class="metric-note">Estimated kWh / units</div>
  </div>

  <div class="metric wide">
   <div class="metric-label">PREDICTED MONTHLY BILL</div>
   <div class="metric-value yellow" id="monthlyCost">₹81.60</div>
   <div class="metric-note">Illustrative electricity cost</div>
  </div>

 </div>

 <div class="section-head">
  <div class="section-title">Appliance breakdown</div>
 </div>

 <div class="break-card">
  <div class="break-title">💡 Smart Lighting</div>
  <div class="break-row">
   <span>Monthly energy</span>
   <strong id="lightEnergy">2.10 kWh</strong>
  </div>
  <div class="bar"><div class="bar-fill" id="lightBar"></div></div>
  <div class="break-row">
   <span>Estimated monthly cost</span>
   <strong id="lightCost">₹16.80</strong>
  </div>
 </div>

 <div class="break-card">
  <div class="break-title">🌀 Ceiling Fan</div>
  <div class="break-row">
   <span>Monthly energy</span>
   <strong id="fanEnergy">8.10 kWh</strong>
  </div>
  <div class="bar"><div class="bar-fill" id="fanBar"></div></div>
  <div class="break-row">
   <span>Estimated monthly cost</span>
   <strong id="fanCost">₹64.80</strong>
  </div>
 </div>

 <div class="break-card">
  <div class="break-title">Added appliances</div>
  <div id="extraBreakdown" class="notice">
   No additional appliances have been added.
  </div>
 </div>

 <div class="page-footer">
  ESTIMATES UPDATE AS YOU CHANGE YOUR CONTROLS
 </div>

</section>

<!-- SETTINGS PAGE -->
<section class="page" id="settingsPage">

 <div class="greeting">
  <div class="eyebrow">⚙ PERSONALISE</div>
  <h1>App settings.</h1>
  <p class="subtext">
   Review the assumptions used by this demonstration.
  </p>
 </div>

 <div class="settings-card">

  <div class="section-title" style="margin:0 0 5px">
   Calculation assumptions
  </div>

  <div class="setting-row">
   <span>Light maximum power</span><strong>20 W</strong>
  </div>

  <div class="setting-row">
   <span>Fan maximum power</span><strong>90 W</strong>
  </div>

  <div class="setting-row">
   <span>Daily usage assumption</span><strong>5 hours</strong>
  </div>

  <div class="setting-row">
   <span>Monthly period</span><strong>30 days</strong>
  </div>

  <div class="setting-row">
   <span>Electricity tariff</span><strong>₹8 / kWh</strong>
  </div>

 </div>

 <div class="settings-card">

  <div class="section-title" style="margin:0 0 5px">
   About HomeMind AI
  </div>

  <p class="notice" style="margin:7px 0 0">
   HomeMind AI is a student smart-home dashboard concept.
   Appliance controls, animations and energy calculations are
   simulated in this browser interface. Adding an appliance
   creates a demonstration card only; it does not connect
   to real devices.
  </p>

 </div>

 <div class="settings-card">

  <div class="section-title" style="margin:0 0 5px">
   Project status
  </div>

  <div class="setting-row">
   <span>Interface</span>
   <strong style="color:var(--green)">Ready</strong>
  </div>

  <div class="setting-row">
   <span>Physical device connection</span>
   <strong>Not connected</strong>
  </div>

  <div class="setting-row">
   <span>External API</span>
   <strong>Not required</strong>
  </div>

 </div>

 <div class="page-footer">
  HOMEMIND AI · SMART LIVING SYSTEM
 </div>

</section>

</main>

<!-- BOTTOM NAVIGATION -->
<nav class="bottom-nav">

 <button class="nav-btn active" data-page="homePage">
  <span class="nav-icon">⌂</span>
  <span>HOME</span>
 </button>

 <button class="nav-btn" data-page="energyPage">
  <span class="nav-icon">ϟ</span>
  <span>ENERGY</span>
 </button>

 <button class="nav-btn" data-page="settingsPage">
  <span class="nav-icon">⚙</span>
  <span>SETTINGS</span>
 </button>

</nav>

<div class="home-indicator"></div>

<!-- ADD APPLIANCE POPUP -->
<div class="modal-backdrop" id="modalBackdrop">

 <div class="modal">

  <div class="modal-head">
   <div class="modal-title">Add an appliance</div>
   <button class="close-modal" id="closeModal">×</button>
  </div>

  <div class="modal-desc">
   Choose a device to add to your simulated smart home.
  </div>

  <div class="option-grid">

   <button class="option" data-type="ac">
    <div class="option-emoji">❄️</div>
    <div class="option-name">Smart AC</div>
    <div class="option-power">1500 W maximum</div>
   </button>

   <button class="option" data-type="tv">
    <div class="option-emoji">📺</div>
    <div class="option-name">Smart TV</div>
    <div class="option-power">100 W maximum</div>
   </button>

   <button class="option" data-type="lock">
    <div class="option-emoji">🔒</div>
    <div class="option-name">Smart Door Lock</div>
    <div class="option-power">5 W maximum</div>
   </button>

   <button class="option" data-type="plug">
    <div class="option-emoji">🔌</div>
    <div class="option-name">Smart Plug</div>
    <div class="option-power">100 W demo load</div>
   </button>

  </div>

  <p class="notice">
   Demo values only. Actual appliance power varies by model.
  </p>

 </div>
</div>

<div class="toast" id="toast"></div>

</div>
</div>
</div>

<script>
(function(){

 const LIGHT_WATTS = 20;
 const FAN_WATTS = 90;
 const HOURS_PER_DAY = 5;
 const DAYS_PER_MONTH = 30;
 const RATE = 8;

 let lightOn = true;
 let fanOn = true;
 let light = 70;
 let fan = 60;

 let extras = [];
 let nextId = 1;

 const $ = id => document.getElementById(id);
 const fmt = n => n.toFixed(2);
 const money = n => "₹" + n.toFixed(2);

 function toast(message) {
  const t = $("toast");
  t.textContent = message;
  t.classList.add("show");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(
   () => t.classList.remove("show"), 1900
  );
 }

 function track(el) {
  const p = Number(el.value);
  el.style.background =
   `linear-gradient(to right,#FFD66B ${p}%,#303A4D ${p}%)`;
 }

 function updateLight() {

  const intensity = lightOn ? light / 100 : 0;

  $("bulbGlow").style.opacity = intensity;

  $("bulbGlass").style.opacity =
   lightOn ? .2 + intensity * .8 : .2;

  $("lightState").textContent = lightOn ? "ON" : "OFF";
  $("lightState").classList.toggle("on", lightOn);

  $("lightToggle").textContent =
   lightOn ? "TURN OFF" : "TURN ON";

  $("lightToggle").classList.toggle("on", lightOn);

  $("lightSlider").disabled = !lightOn;

  $("lightValue").textContent = light + "%";
  $("lightRangeLabel").textContent = light + "%";

  $("lightWatts").textContent =
   (lightOn ? LIGHT_WATTS * light / 100 : 0).toFixed(1) + " W";

  track($("lightSlider"));
 }

 function updateFan() {

  const rotor = $("fanRotor");
  const speed = fanOn ? fan : 0;

  if (speed > 0) {
   const duration = 3.5 - speed / 100 * 3.25;
   rotor.style.animationDuration = duration + "s";
   rotor.style.animationPlayState = "running";
  } else {
   rotor.style.animationPlayState = "paused";
  }

  $("fanState").textContent = fanOn ? "ON" : "OFF";
  $("fanState").classList.toggle("on", fanOn);

  $("fanToggle").textContent =
   fanOn ? "TURN OFF" : "TURN ON";

  $("fanToggle").classList.toggle("on", fanOn);

  $("fanSlider").disabled = !fanOn;

  $("fanValue").textContent = fan + "%";
  $("fanRangeLabel").textContent = fan + "%";

  $("fanWatts").textContent =
   (fanOn ? FAN_WATTS * fan / 100 : 0).toFixed(1) + " W";

  track($("fanSlider"));
 }

 function extraPower(d) {
  return d.on ? d.watts : 0;
 }

 function renderExtras() {

  $("extraDevices").innerHTML = "";

  extras.forEach(d => {

   const card = document.createElement("div");
   card.className = "extra-device";

   const icon = document.createElement("span");
   icon.className = "extra-icon";
   icon.textContent = d.icon;

   const info = document.createElement("div");
   info.className = "extra-info";

   const name = document.createElement("div");
   name.className = "extra-name";
   name.textContent = d.name;

   const desc = document.createElement("div");
   desc.className = "extra-desc";

   desc.textContent = d.on
    ? d.watts + " W · ON"
    : "OFF · " + d.watts + " W max";

   info.append(name, desc);

   const actions = document.createElement("div");
   actions.className = "extra-actions";

   const toggle = document.createElement("button");

   toggle.className = "mini-toggle" + (d.on ? " on" : "");
   toggle.textContent = d.on ? "ON" : "OFF";

   toggle.addEventListener("click", () => {
    d.on = !d.on;
    renderExtras();
    updateAll();
   });

   const remove = document.createElement("button");
   remove.className = "remove";
   remove.textContent = "✕";

   remove.addEventListener("click", () => {
    extras = extras.filter(x => x.id !== d.id);
    renderExtras();
    updateAll();
    toast(d.name + " removed");
   });

   actions.append(toggle, remove);
   card.append(icon, info, actions);

   $("extraDevices").append(card);

  });

  $("deviceCount").textContent =
   (2 + extras.length) + " DEVICES";
 }

 function updateCalculations() {

  const lp = lightOn ? LIGHT_WATTS * light / 100 : 0;
  const fp = fanOn ? FAN_WATTS * fan / 100 : 0;

  const extra = extras.reduce(
   (sum, d) => sum + extraPower(d), 0
  );

  const total = lp + fp + extra;

  const le = lp * HOURS_PER_DAY * DAYS_PER_MONTH / 1000;
  const fe = fp * HOURS_PER_DAY * DAYS_PER_MONTH / 1000;
  const ee = extra * HOURS_PER_DAY * DAYS_PER_MONTH / 1000;

  const me = le + fe + ee;
  const cost = me * RATE;

  $("heroPower").textContent = total.toFixed(1) + " W";

  const active =
   Number(lightOn && lp > 0) +
   Number(fanOn && fp > 0) +
   extras.filter(d => d.on).length;

  $("activeCount").textContent =
   active + " appliances currently active";

  $("totalPower").textContent = total.toFixed(1) + " W";
  $("monthlyEnergy").textContent = fmt(me) + " kWh";
  $("monthlyCost").textContent = money(cost);

  $("lightEnergy").textContent = fmt(le) + " kWh";
  $("fanEnergy").textContent = fmt(fe) + " kWh";

  $("lightCost").textContent = money(le * RATE);
  $("fanCost").textContent = money(fe * RATE);

  $("lightBar").style.width =
   (me ? le / me * 100 : 0) + "%";

  $("fanBar").style.width =
   (me ? fe / me * 100 : 0) + "%";

  $("extraBreakdown").textContent = extras.length
   ? extras.map(d => {
      const e = d.on
       ? d.watts * HOURS_PER_DAY * DAYS_PER_MONTH / 1000
       : 0;
      return d.name + ": " + fmt(e) +
       " kWh · " + money(e * RATE);
     }).join(" | ")
   : "No additional appliances have been added.";
 }

 function updateAll() {
  updateLight();
  updateFan();
  updateCalculations();
 }

 $("lightToggle").addEventListener("click", () => {
  lightOn = !lightOn;
  updateAll();
 });

 $("fanToggle").addEventListener("click", () => {
  fanOn = !fanOn;
  updateAll();
 });

 $("lightSlider").addEventListener("input", e => {
  light = Number(e.target.value);
  updateAll();
 });

 $("fanSlider").addEventListener("input", e => {
  fan = Number(e.target.value);
  updateAll();
 });

 // Add appliance popup

 $("openAdd").addEventListener("click", () => {
  $("modalBackdrop").classList.add("open");
 });

 $("closeModal").addEventListener("click", () => {
  $("modalBackdrop").classList.remove("open");
 });

 $("modalBackdrop").addEventListener("click", e => {
  if (e.target === $("modalBackdrop")) {
   $("modalBackdrop").classList.remove("open");
  }
 });

 const types = {

  ac: {
   name:"Smart AC",
   icon:"❄️",
   watts:1500
  },

  tv: {
   name:"Smart TV",
   icon:"📺",
   watts:100
  },

  lock: {
   name:"Smart Door Lock",
   icon:"🔒",
   watts:5
  },

  plug: {
   name:"Smart Plug",
   icon:"🔌",
   watts:100
  }

 };

 document.querySelectorAll(".option").forEach(btn => {

  btn.addEventListener("click", () => {

   const d = types[btn.dataset.type];

   extras.push({
    id:nextId++,
    name:d.name,
    icon:d.icon,
    watts:d.watts,
    on:true
   });

   renderExtras();
   updateAll();

   $("modalBackdrop").classList.remove("open");

   toast(d.name + " added to your home");

  });

 });

 // Bottom navigation

 document.querySelectorAll(".nav-btn").forEach(btn => {

  btn.addEventListener("click", () => {

   document.querySelectorAll(".nav-btn").forEach(b => {
    b.classList.toggle("active", b === btn);
   });

   document.querySelectorAll(".page").forEach(p => {
    p.classList.toggle(
     "active",
     p.id === btn.dataset.page
    );
   });

  });

 });

 // Smartphone clock

 function clock() {
  const d = new Date();

  $("clock").textContent =
   d.toLocaleTimeString([], {
    hour:"2-digit",
    minute:"2-digit",
    hour12:false
   });
 }

 clock();
 setInterval(clock, 30000);

 renderExtras();
 updateAll();

})();
</script>

</body>
</html>
"""

components.html(
    dashboard,
    height=1150,
    scrolling=True
)
