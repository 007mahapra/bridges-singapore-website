from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mental Wellness by Bridges — Venue Cost Calculator</title>
<style>
:root{--bg:#f5f7fb;--card:#fff;--text:#172033;--muted:#667085;--line:#e4e7ec;--accent:#315efb;--good:#087443;--warn:#9a6700;--bad:#b42318}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 Arial,sans-serif}
header{background:linear-gradient(135deg,#182b59,#315efb);color:#fff;padding:28px 16px}
.wrap{max-width:1100px;margin:auto;padding:0 14px}.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:12px;opacity:.8}
h1{margin:6px 0;font-size:30px}h2{margin:0 0 14px;font-size:22px}h3{margin:0 0 8px}
nav{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line);overflow:auto;white-space:nowrap}
nav a{display:inline-block;padding:12px 14px;color:#344054;text-decoration:none;font-weight:600}
section{padding:22px 0}.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 2px 8px #1018280a}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.controls input{width:120px;padding:11px;border:1px solid #cfd4dc;border-radius:10px;font-size:16px}
button{border:1px solid #cfd4dc;background:#fff;border-radius:10px;padding:10px 14px;font-weight:700;cursor:pointer}
button:hover{background:#f2f4f7}.quick.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.label{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.big{font-size:27px;font-weight:800;margin-top:3px}.muted{color:var(--muted)}
.results{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:15px}
.result{border:1px solid var(--line);border-radius:14px;padding:15px;background:#fff}
.result h3{font-size:18px}.price{font-size:24px;font-weight:800}.rows{margin:10px 0}.row{display:flex;justify-content:space-between;gap:10px;padding:5px 0;border-bottom:1px dashed #eaecf0}.row:last-child{border:0}
.badge{display:inline-block;border-radius:999px;padding:4px 8px;font-size:12px;font-weight:700;background:#eef2ff;color:#344054}
.warn{color:var(--warn);background:#fffaeb;padding:9px;border-radius:9px}.na{color:var(--muted);background:#f2f4f7;padding:9px;border-radius:9px}
table{width:100%;border-collapse:collapse;background:#fff}th,td{padding:10px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}th{background:#f9fafb}
.table-scroll{overflow:auto;border:1px solid var(--line);border-radius:12px}
details{background:#fff;border:1px solid var(--line);border-radius:12px;margin:10px 0;padding:0 14px}summary{cursor:pointer;font-weight:700;padding:14px}
small{color:var(--muted)}.footer{padding:30px 0;color:var(--muted);font-size:13px}
@media(max-width:720px){h1{font-size:25px}.grid,.results{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}section{padding:17px 0}.card{padding:14px}.controls input{width:100px}.price{font-size:22px}}
@media print{nav{display:none}.card,details{box-shadow:none}.controls{display:none}body{background:#fff}}
</style>
</head>
<body>
<header><div class="wrap">
<div class="eyebrow">Mental Wellness by Bridges</div>
<h1>Singapore Venue Costing — 28 November 2026</h1>
<div>Saturday • Venue comparison with variable pax + food costing</div>
</div></header>

<nav><div class="wrap">
<a href="#calculator">Calculator</a><a href="#scenarios">Scenarios</a><a href="#venues">Venues</a><a href="#planning">Planning Notes</a>
</div></nav>

<main class="wrap">
<section id="calculator">
<div class="card">
<h2>Interactive Cost Calculator</h2>
<p class="muted">Change the total number of attendees. Food is automatically calculated at <b>S$7 per pax</b>. Quick-select the common scenarios or enter any custom number.</p>
<div class="controls">
<label><span class="label">Total pax</span><br><input id="pax" type="number" min="1" max="500" value="120"></label>
<button id="minus">−10</button><button id="plus">+10</button>
<button class="quick" data-pax="100">100</button>
<button class="quick active" data-pax="120">120</button>
<button class="quick" data-pax="150">150</button>
<button class="quick" data-pax="200">200</button>
</div>
<div class="grid" style="margin-top:15px">
<div><div class="label">Food cost</div><div class="big" id="food">S$840.00</div><small>120 × S$7</small></div>
<div><div class="label">Selected pax</div><div class="big" id="paxDisplay">120</div><small>Attendees</small></div>
</div>
</div>
<div class="results" id="results"></div>
</section>

<section id="scenarios">
<div class="card">
<h2>Default Planning Scenarios</h2>
<p class="muted">Food is included in every venue estimate. Deposits are shown separately and are not included in totals.</p>
<div class="table-scroll">
<table>
<thead><tr><th>Venue</th><th>100 pax</th><th>120 pax</th><th>150 pax</th><th>200 pax</th></tr></thead>
<tbody id="scenarioBody"></tbody>
</table>
</div>
</div>
</section>

<section id="venues">
<h2>Venue Details</h2>

<details open><summary>Tanglin Community Club — up to 220 pax</summary>
<div class="card">
<p><b>Availability:</b> Available on 28 Nov (information shared by Amar ji).</p>
<p><b>Rate:</b> S$150/hour, minimum 4 hours. Cleaning S$300. Refundable deposit S$600. Projector included; PA system not included.</p>
<p><b>Location:</b> 245 Whitley Road, Singapore 297829 • <b>MRT:</b> Stevens MRT (DT10), approx. 4–5 min walk.</p>
<p><b>Food assumption:</b> S$7/pax.</p>
</div></details>

<details><summary>Woodleigh Community Club — up to 220 pax</summary>
<div class="card">
<p><b>Rate:</b> S$4,000 minimum 4 hours for non-resident/corporate booking; additional hour S$1,000. Cleaning S$500. Security deposit S$500. Includes 48 chairs and 12 tables.</p>
<p><b>Availability:</b> To confirm for 28 Nov.</p>
<p><b>Location:</b> Woodleigh / Bidadari, Singapore • <b>MRT:</b> Woodleigh MRT (NE11).</p>
<p><b>Food assumption:</b> S$7/pax.</p>
</div></details>

<details><summary>Common Ground Civic Centre, Bedok — quoted setup 126 pax</summary>
<div class="card">
<p><b>Quoted:</b> Level 3 Auditorium S$1,430.63; Common Area S$81.75/hour; mandatory Weekend Assistant S$87.20; mandatory Weekend Cleaning S$114.45. Quotation is for Saturday 10am–5pm.</p>
<p><b>Location:</b> 21 Bedok North Street 1, Singapore 469659 • <b>MRT:</b> Bedok MRT (EW5), approx. 5 min walk.</p>
<p><b>Capacity note:</b> Quoted theatre setup is 126 pax. Dining in the Common Area alone cannot accommodate 120 seated diners at one time. For 150/200 pax, obtain a revised layout/quotation.</p>
<p><b>Food assumption:</b> S$7/pax.</p>
</div></details>

<details><summary>SingPost Auditorium & Foyer — capacity about 242 pax</summary>
<div class="card">
<p><b>Published benchmark rate:</b> Saturday/Sunday/PH S$860 for first 3 hours + S$300 per subsequent hour, exclusive of GST. Refundable deposit S$300. AV system, microphones, surround sound, projector/screen, lighting controls and technical support are listed services.</p>
<p><b>Location:</b> 10 Eunos Road 8, #05-30, Singapore 408600 • <b>MRT:</b> Paya Lebar MRT (EW8/CC9), Exit A.</p>
<p><b>Important:</b> The public rate sheet is an older benchmark; obtain a current 2026 quotation and availability confirmation.</p>
<p><b>Food assumption:</b> S$7/pax.</p>
</div></details>

<details><summary>SPH News Centre Auditorium / SPH Hub — capacity up to about 250</summary>
<div class="card">
<p><b>Location:</b> 1000 Toa Payoh North, Singapore 318994 • <b>MRT:</b> Braddell MRT (NS18), approx. 7 min walk.</p>
<p><b>Pricing / availability:</b> TBC. Obtain an event quotation, including auditorium, AV, staffing, cleaning and food arrangements.</p>
</div></details>
</section>

<section id="planning">
<div class="card">
<h2>Planning Notes</h2>
<ul>
<li><b>Food:</b> calculator assumes S$7 per attendee for every venue. Replace this assumption if a caterer gives a different quote.</li>
<li><b>Deposits:</b> refundable/security deposits are excluded from the estimated totals.</li>
<li><b>GST:</b> SingPost's published benchmark rental is exclusive of GST; the calculator applies 9% GST to the rental benchmark.</li>
<li><b>Duration:</b> Tanglin, Woodleigh and SingPost support 4h/5h/8h estimates because an hourly structure is available. Common Ground uses its specific 10am–5pm quotation; SPH remains TBC.</li>
<li><b>Capacity:</b> the calculator flags Common Ground when pax exceeds the quoted 126-pax setup.</li>
<li><b>Final booking:</b> confirm 28 Nov 2026 availability, setup, AV/PA, cleaning, food rules, GST, deposits and overtime directly with each venue.</li>
</ul>
</div>
</section>
<div class="footer">Prepared as an estimation/planning report for Mental Wellness by Bridges. Costs are estimates based on the information available; final venue quotations govern.</div>
</main>

<script>
const venues = [
 {name:"Tanglin Community Club",cap:220,deposit:600,kind:"hourly",food:7,
  calc:p=>({r4:150*4+300,r5:150*5+300,r8:150*8+300})},
 {name:"Woodleigh Community Club",cap:220,deposit:500,kind:"hourly",food:7,
  calc:p=>({r4:4000+500,r5:5000+500,r8:8000+500})},
 {name:"Common Ground Civic Centre, Bedok",cap:126,deposit:0,kind:"quoted",food:7,
  calc:p=>({quoted:1430.63+81.75*7+87.20+114.45})},
 {name:"SingPost Auditorium & Foyer",cap:242,deposit:300,kind:"hourly",food:7,
  calc:p=>({r4:1160*1.09,r5:1460*1.09,r8:2360*1.09})},
 {name:"SPH News Centre Auditorium / SPH Hub",cap:250,deposit:0,kind:"tbc",food:7,
  calc:p=>({tbc:null})}
];

function money(n){return n==null?"TBC":"S$"+n.toLocaleString("en-SG",{minimumFractionDigits:2,maximumFractionDigits:2});}
function currentPax(){return Math.max(1,Math.min(500,parseInt(document.getElementById("pax").value)||1));}
function render(){
 const p=currentPax(); document.getElementById("pax").value=p;
 document.getElementById("paxDisplay").textContent=p;
 document.getElementById("food").textContent=money(p*7);
 document.querySelectorAll(".quick").forEach(b=>b.classList.toggle("active",+b.dataset.pax===p));
 const out=document.getElementById("results"); out.innerHTML="";
 venues.forEach(v=>{
   const x=v.calc(p), food=p*v.food, box=document.createElement("div"); box.className="result";
   let body="";
   if(v.kind==="tbc") body='<div class="na">Venue pricing/availability: TBC</div>';
   else if(v.kind==="quoted"){
      if(p>v.cap) body='<div class="warn">Quoted setup is limited to 126 pax. Request a revised layout/quotation for this pax.</div>';
      else {let total=x.quoted+food; body=`<div class="rows"><div class="row"><span>Quoted venue/fixed cost</span><b>${money(x.quoted)}</b></div><div class="row"><span>Food (${p} × S$7)</span><b>${money(food)}</b></div><div class="row"><span>Estimated total</span><b>${money(total)}</b></div></div><div class="price">${money(total)}</div><small>${money(total/p)} per pax</small>`;}
   } else {
      body=`<div class="rows">
      <div class="row"><span>4h venue cost</span><b>${money(x.r4)}</b></div>
      <div class="row"><span>5h venue cost</span><b>${money(x.r5)}</b></div>
      <div class="row"><span>8h venue cost</span><b>${money(x.r8)}</b></div>
      <div class="row"><span>Food (${p} × S$7)</span><b>${money(food)}</b></div></div>
      <div class="grid4">
       <div><span class="label">4h total</span><br><b>${money(x.r4+food)}</b></div>
       <div><span class="label">5h total</span><br><b>${money(x.r5+food)}</b></div>
       <div><span class="label">8h total</span><br><b>${money(x.r8+food)}</b></div>
       <div><span class="label">Deposit</span><br><b>${money(v.deposit)}</b></div>
      </div>`;
   }
   box.innerHTML=`<h3>${v.name} <span class="badge">Capacity ${v.cap}</span></h3>${body}`;
   out.appendChild(box);
 });
}
function renderScenarios(){
 const body=document.getElementById("scenarioBody"); body.innerHTML="";
 [100,120,150,200].forEach(p=>{
  venues.forEach((v,i)=>{
   let text;
   if(v.kind==="tbc") text="TBC";
   else if(v.kind==="quoted"){
    text=p>v.cap?"N/A":money(v.calc(p).quoted+p*7);
   }else{
    const x=v.calc(p); text=`4h ${money(x.r4+p*7)}<br><small>5h ${money(x.r5+p*7)} • 8h ${money(x.r8+p*7)}</small>`;
   }
   const row=document.createElement("tr");
   row.innerHTML=i===0?`<td>${v.name}</td><td>${text}</td>`:"";
   if(i===0){[100,120,150,200].forEach((_,j)=>{if(j===0)row.children[1].innerHTML=text});}
   body.appendChild(row);
   if(i>0){
     const cells=body.lastElementChild.children;
   }
  });
 });
 // rebuild properly as one row per venue
 body.innerHTML="";
 venues.forEach(v=>{
  const tr=document.createElement("tr"); let cells=`<td>${v.name}</td>`;
  [100,120,150,200].forEach(p=>{
   let text;
   if(v.kind==="tbc") text="TBC";
   else if(v.kind==="quoted") text=p>v.cap?"N/A":money(v.calc(p).quoted+p*7);
   else {const x=v.calc(p); text=`4h ${money(x.r4+p*7)}<br><small>5h ${money(x.r5+p*7)} • 8h ${money(x.r8+p*7)}</small>`;}
   cells+=`<td>${text}</td>`;
  });
  tr.innerHTML=cells; body.appendChild(tr);
 });
}
document.getElementById("pax").addEventListener("input",render);
document.getElementById("minus").onclick=()=>{document.getElementById("pax").value=currentPax()-10;render()};
document.getElementById("plus").onclick=()=>{document.getElementById("pax").value=currentPax()+10;render()};
document.querySelectorAll(".quick").forEach(b=>b.onclick=()=>{document.getElementById("pax").value=b.dataset.pax;render()});
render();renderScenarios();
</script>
</body>
</html>'''

path = Path("Mental_Wellness_by_Bridges_Venue_Presentation_Interactive_Nov_28_2026.html")
path.write_text(html, encoding="utf-8")
print(path)
