import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Simulasi Energi Kinetik dan Rotasi", page_icon="⚙️", layout="wide")

st.markdown(
    """
    <style>
    .block-container {max-width: 1100px; padding-top: 2rem;}
    .hero {background: linear-gradient(135deg, #7c3aed 0%, #1479a8 100%);
           border-radius: 20px; padding: 26px 28px; margin-bottom: 18px;
           color: #ffffff; position: relative; overflow: hidden;}
    .hero h1 {margin: 0; padding: 0; font-size: 2.1rem; line-height: 1.15;
              color: #ffffff; font-weight: 800; letter-spacing: -0.5px;}
    .hero p {margin: 6px 0 0 0; color: #ede9fe; font-size: 1rem;}
    .hero .bubble {position: absolute; border-radius: 50%; background: rgba(255,255,255,0.12);}
    .hero .b1 {width: 120px; height: 120px; right: -20px; top: -30px;}
    .hero .b2 {width: 60px; height: 60px; right: 90px; bottom: -18px;}
    .hero .b3 {width: 28px; height: 28px; right: 160px; top: 18px;}
    </style>
    <div class="hero">
        <span class="bubble b1"></span><span class="bubble b2"></span><span class="bubble b3"></span>
        <h1>⚙️ Simulasi Energi Kinetik dan Rotasi</h1>
        <p>Atur bentuk, massa, sudut, dan tinggi, lalu lihat energinya berubah.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

SIMULASI = r"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Simulasi Energi Kinetik dan Rotasi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#eef1f6; --panel:#ffffff; --ink:#16213a; --muted:#5b6784; --line:#d3d9e6; --grid:#e1e6f0;
  --pe:#3b5bdb; --kt:#0c9c8a; --kr:#e08a00; --ramp:#c9d1e3; --wheel:#fff;
  --font:"Bricolage Grotesque",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  box-sizing:border-box; color-scheme:light;
  padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0f1524; --panel:#182036; --ink:#e8ecf7; --muted:#9aa6c4; --line:#2b3552; --grid:#212a43;
    --pe:#7d96ff; --kt:#3fd2bd; --kr:#ffb133; --ramp:#2c3757; --wheel:#182036; color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#0f1524; --panel:#182036; --ink:#e8ecf7; --muted:#9aa6c4; --line:#2b3552; --grid:#212a43;
  --pe:#7d96ff; --kt:#3fd2bd; --kr:#ffb133; --ramp:#2c3757; --wheel:#182036; color-scheme:dark;
}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);line-height:1.5}
.wrap{max-width:1040px;margin:0 auto;padding:20px 16px 40px}
h1{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:800;letter-spacing:-.02em;margin:0 0 4px;line-height:1.15}
.lead{color:var(--muted);margin:0 0 20px;max-width:62ch}
.grid{display:grid;grid-template-columns:1fr 280px;gap:16px}
@media(max-width:820px){.grid{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px}
canvas{display:block;width:100%;border-radius:6px}
#stage{height:300px;background:
  linear-gradient(var(--grid) 1px,transparent 1px) 0 0/28px 28px,
  linear-gradient(90deg,var(--grid) 1px,transparent 1px) 0 0/28px 28px}
#plot{height:190px}
label{display:block;font-size:.9rem;font-weight:600;margin-top:12px}
label:first-child{margin-top:0}
label output{float:right;font-weight:400;color:var(--muted);font-variant-numeric:tabular-nums}
input[type=range]{width:100%;accent-color:var(--pe)}
select{width:100%;padding:8px;border-radius:6px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:inherit}
.btns{display:flex;gap:8px;margin-top:16px}
button{flex:1;padding:10px;border-radius:6px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:inherit;font-weight:600;cursor:pointer}
button.primary{background:var(--pe);border-color:var(--pe);color:#fff}
:root[data-theme="dark"] button.primary{color:#0f1524}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) button.primary{color:#0f1524}}
button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid var(--kr);outline-offset:2px}
h2{font-size:1.05rem;margin:0 0 10px}
.bar{display:flex;height:34px;border-radius:6px;overflow:hidden;background:var(--grid);border:1px solid var(--line)}
.bar span{height:100%;transition:width .05s linear}
#bPE{background:var(--pe)} #bKT{background:var(--kt)} #bKR{background:var(--kr)}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.85rem;margin:8px 0 0;color:var(--muted)}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px}
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:14px}
.vals div{border-left:3px solid var(--line);padding-left:8px}
.vals small{display:block;color:var(--muted);font-size:.8rem}
.vals b{font-size:1.15rem;font-variant-numeric:tabular-nums}
.note{margin:14px 0 0;color:var(--muted);font-size:.92rem}
.below{margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:820px){.below{grid-template-columns:1fr}}
.rumus{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.85rem;line-height:1.8}
</style>
</head>
<body>
<div class="wrap">
  <h1>Energi kinetik translasi dan rotasi</h1>
  <p class="lead">Benda menggelinding tanpa selip menuruni bidang miring. Energi potensial berubah menjadi energi kinetik translasi dan rotasi, dan jumlahnya tetap.</p>

  <div class="grid">
    <div class="card">
      <canvas id="stage" aria-label="Animasi benda menggelinding di bidang miring"></canvas>
      <div class="vals" style="margin-top:12px">
        <div><small>Kecepatan v</small><b id="vV">0</b></div>
        <div><small>Kecepatan sudut ω</small><b id="vW">0</b></div>
        <div><small>Percepatan a</small><b id="vA">0</b></div>
        <div><small>Waktu t</small><b id="vT">0</b></div>
      </div>
    </div>

    <div class="card">
      <label for="shape">Bentuk benda</label>
      <select id="shape">
        <option value="silinder">Silinder pejal (k = 1/2)</option>
        <option value="cincin">Cincin tipis (k = 1)</option>
        <option value="bola">Bola pejal (k = 2/5)</option>
        <option value="bolaB">Bola berongga (k = 2/3)</option>
      </select>
      <label for="m">Massa <output id="oM"></output></label>
      <input id="m" type="range" min="0.5" max="10" step="0.5" value="2">
      <label for="r">Jari-jari <output id="oR"></output></label>
      <input id="r" type="range" min="0.1" max="0.5" step="0.05" value="0.3">
      <label for="th">Sudut bidang miring <output id="oTh"></output></label>
      <input id="th" type="range" min="5" max="45" step="1" value="25">
      <label for="h">Tinggi awal <output id="oH"></output></label>
      <input id="h" type="range" min="0.5" max="5" step="0.5" value="2">
      <label for="sp">Kecepatan animasi <output id="oSp"></output></label>
      <input id="sp" type="range" min="0.25" max="2" step="0.25" value="1">
      <div class="btns">
        <button id="go" class="primary">Mulai</button>
        <button id="rs">Ulangi</button>
      </div>
    </div>
  </div>

  <div class="below">
    <div class="card">
      <h2>Pembagian energi saat ini</h2>
      <div class="bar" role="img" aria-label="Diagram batang energi"><span id="bPE"></span><span id="bKT"></span><span id="bKR"></span></div>
      <div class="legend">
        <span><i class="dot" style="background:var(--pe)"></i>Potensial <b id="lPE"></b></span>
        <span><i class="dot" style="background:var(--kt)"></i>Kinetik translasi <b id="lKT"></b></span>
        <span><i class="dot" style="background:var(--kr)"></i>Kinetik rotasi <b id="lKR"></b></span>
      </div>
      <p class="note" id="insight"></p>
      <div class="rumus" style="margin-top:10px">
        Ek translasi = ½ m v²<br>
        Ek rotasi = ½ I ω², I = k m r²<br>
        Ek rotasi / Ek translasi = k<br>
        a = g sin θ / (1 + k)
      </div>
    </div>
    <div class="card">
      <h2>Grafik energi terhadap waktu</h2>
      <canvas id="plot" aria-label="Grafik energi terhadap waktu"></canvas>
    </div>
  </div>
</div>

<script>
const G = 9.8;
const K = {cincin:1, silinder:.5, bola:.4, bolaB:2/3};
const $ = id => document.getElementById(id);
const stage = $('stage'), plot = $('plot');
let run = false, t = 0, hist = [], last = 0;

function P(){
  return {k:K[$('shape').value], m:+$('m').value, r:+$('r').value,
          th:+$('th').value*Math.PI/180, h:+$('h').value, sp:+$('sp').value};
}
function S(p, time){
  const sin = Math.sin(p.th), a = G*sin/(1+p.k), L = p.h/sin, tEnd = Math.sqrt(2*L/a);
  const tt = Math.min(time, tEnd), s = .5*a*tt*tt, v = a*tt, w = v/p.r;
  return {a, L, tEnd, tt, s, v, w, done: time >= tEnd,
    PE: p.m*G*(p.h - s*sin), KT: .5*p.m*v*v, KR: .5*p.k*p.m*p.r*p.r*w*w, E: p.m*G*p.h};
}
const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const f = (x,d=2) => x.toFixed(d).replace('.',',');

function fit(c){
  const d = window.devicePixelRatio||1, r = c.getBoundingClientRect();
  c.width = Math.round(r.width*d); c.height = Math.round(r.height*d);
  const x = c.getContext('2d'); x.setTransform(d,0,0,d,0,0);
  return {x, W:r.width, H:r.height};
}

function drawStage(p, s){
  const {x, W, H} = fit(stage);
  const B = {x:W-24, y:H-24}, sin = Math.sin(p.th), cos = Math.cos(p.th);
  const Lv = Math.min((W-48)/cos, (H-60)/sin);
  const A = {x:B.x-Lv*cos, y:B.y-Lv*sin};
  x.fillStyle = css('--ramp');
  x.beginPath(); x.moveTo(A.x,A.y); x.lineTo(B.x,B.y); x.lineTo(A.x,B.y); x.closePath(); x.fill();
  x.strokeStyle = css('--ink'); x.lineWidth = 2;
  x.beginPath(); x.moveTo(A.x,A.y); x.lineTo(B.x,B.y); x.stroke();
  x.fillStyle = css('--muted'); x.font = '12px sans-serif';
  x.fillText('θ = '+Math.round(p.th*180/Math.PI)+'°', B.x-62, B.y-6);
  x.fillText('h = '+f(p.h,1)+' m', A.x+6, (A.y+B.y)/2+14);
  const rv = 12 + p.r*55, fr = s.s/s.L;
  const Px = A.x + fr*Lv*cos, Py = A.y + fr*Lv*sin;
  const cx = Px + sin*rv, cy = Py - cos*rv, phi = s.s/p.r;
  x.save(); x.translate(cx,cy); x.rotate(phi);
  const hollow = p.k === 1;
  x.beginPath(); x.arc(0,0,rv,0,Math.PI*2);
  x.fillStyle = css('--wheel'); if(!hollow) x.fill();
  x.lineWidth = hollow ? 6 : 3; x.strokeStyle = css('--pe'); x.stroke();
  x.lineWidth = 2; x.strokeStyle = css('--kr');
  for(let i=0;i<4;i++){ x.rotate(Math.PI/2); x.beginPath(); x.moveTo(0,0); x.lineTo(rv-2,0); x.stroke(); }
  x.fillStyle = css('--kr'); x.beginPath(); x.arc(rv*.6,0,4,0,Math.PI*2); x.fill();
  x.restore();
  if(s.v > 0.05){ // panah kecepatan
    const len = Math.min(70, 10 + s.v*10), ax = cx, ay = cy - rv - 10;
    x.strokeStyle = css('--kt'); x.fillStyle = css('--kt'); x.lineWidth = 3;
    const ex = ax + cos*len, ey = ay + sin*len;
    x.beginPath(); x.moveTo(ax,ay); x.lineTo(ex,ey); x.stroke();
    x.beginPath(); x.moveTo(ex,ey); x.lineTo(ex-cos*9-sin*5, ey-sin*9+cos*5); x.lineTo(ex-cos*9+sin*5, ey-sin*9-cos*5); x.fill();
  }
}

function drawPlot(p, s0){
  const {x, W, H} = fit(plot);
  const m = {l:44, r:10, t:10, b:24}, w = W-m.l-m.r, h = H-m.t-m.b;
  const tMax = s0.tEnd, E = s0.E;
  x.strokeStyle = css('--line'); x.fillStyle = css('--muted'); x.font = '11px sans-serif'; x.lineWidth = 1;
  for(let i=0;i<=4;i++){
    const yy = m.t + h - h*i/4;
    x.beginPath(); x.moveTo(m.l,yy); x.lineTo(W-m.r,yy); x.stroke();
    x.fillText(f(E*i/4,0), 4, yy+4);
  }
  x.fillText('0', m.l, H-8); x.fillText(f(tMax,1)+' s', W-m.r-34, H-8);
  x.fillText('J', 4, m.t+2);
  const line = (key, col) => {
    x.strokeStyle = css(col); x.lineWidth = 2.5; x.beginPath();
    hist.forEach((q,i)=>{
      const px = m.l + w*q.t/tMax, py = m.t + h - h*q[key]/E;
      i ? x.lineTo(px,py) : x.moveTo(px,py);
    });
    x.stroke();
  };
  line('PE','--pe'); line('KT','--kt'); line('KR','--kr');
}

function update(){
  const p = P(), s = S(p, t), s0 = S(p, 1e9);
  drawStage(p, s); drawPlot(p, s0);
  const pct = k => (100*k/s.E).toFixed(2)+'%';
  $('bPE').style.width = pct(s.PE); $('bKT').style.width = pct(s.KT); $('bKR').style.width = pct(s.KR);
  $('lPE').textContent = f(s.PE,1)+' J'; $('lKT').textContent = f(s.KT,1)+' J'; $('lKR').textContent = f(s.KR,1)+' J';
  $('vV').textContent = f(s.v)+' m/s'; $('vW').textContent = f(s.w)+' rad/s';
  $('vA').textContent = f(s.a)+' m/s²'; $('vT').textContent = f(s.tt)+' s';
  const frac = p.k/(1+p.k)*100;
  $('insight').textContent = 'Setelah bergulir, '+f(100-frac,0)+'% energi kinetik menjadi translasi dan '+f(frac,0)+'% menjadi rotasi. Semakin besar k, semakin banyak energi tersimpan sebagai putaran, sehingga benda melaju lebih lambat. Massa dan jari-jari tidak mengubah percepatan.';
  $('oM').textContent = p.m+' kg'; $('oR').textContent = f(p.r)+' m';
  $('oTh').textContent = Math.round(p.th*180/Math.PI)+'°'; $('oH').textContent = f(p.h,1)+' m';
  $('oSp').textContent = p.sp+'×';
  return s;
}

function reset(){ t = 0; hist = []; run = false; $('go').textContent = 'Mulai'; record(); update(); }
function record(){ const s = S(P(), t); hist.push({t:s.tt, PE:s.PE, KT:s.KT, KR:s.KR}); }

function tick(now){
  const dt = Math.min(.05, (now-last)/1000); last = now;
  if(run){
    t += dt*P().sp; record();
    const s = update();
    if(s.done){ run = false; $('go').textContent = 'Mulai lagi'; t = s.tEnd; }
  }
  requestAnimationFrame(tick);
}

$('go').onclick = () => {
  if(S(P(), t).done) reset();
  run = !run; $('go').textContent = run ? 'Jeda' : 'Lanjut';
};
$('rs').onclick = reset;
['shape','m','r','th','h'].forEach(id => $(id).addEventListener('input', reset));
$('sp').addEventListener('input', update);
window.addEventListener('resize', update);
reset();
requestAnimationFrame(n => { last = n; tick(n); });
</script>
</body>
</html>
"""

components.html(SIMULASI, height=1500, scrolling=True)
