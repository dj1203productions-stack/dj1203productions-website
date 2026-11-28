#!/usr/bin/env python3
"""Builds the DJ1203 Productions site: python3 build.py"""
import html

PHONE = "(219) 608-4119"; TEL = "2196084119"
EMAIL = "chris@dj1203productions.com"; EMAIL2 = "dj1203productions@gmail.com"
YELP = "https://www.yelp.com/biz/oTMMmo0TyqCyp_4M7_vQAA"
SOCIAL = [("Facebook", "https://www.facebook.com/DJ1203Productions"), ("Instagram", "https://www.instagram.com/DJ1203Productions"),
          ("TikTok", "https://www.tiktok.com/@DJ1203Productions"), ("YouTube", "https://www.youtube.com/@DJ1203Productions"),
          ("X", "https://www.x.com/DJ1203PRODUCTIONS"), ("Yelp", YELP)]
LABS = '<a href="https://dj1203labs.com" target="_blank" rel="noopener">DJ1203 Labs &#8599;</a>'
PAGES = [("index.html", "Home"), ("packages.html", "Packages & Pricing"), ("gallery.html", "Gallery"),
         ("about.html", "About"), ("book.html", "Book Now"), ("shop.html", "Shop")]

def ticks(items): return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def socials(): return '<div class="socials">' + "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL) + "</div>"

def shell(page, title, desc, body):
    top = "".join(f'<a class="tl{" on" if f==page else ""}" href="{f}">{n}</a>' for f, n in PAGES[1:4]+PAGES[5:6])
    drawer = "".join(f'<a href="{f}"{" class=on" if f==page else ""}>{n}</a>' for f, n in PAGES)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://dj1203productions.com/assets/photos/henderson-djing-wide.jpg"><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v=2"></head>
<body class="nojs">
<div class="promo" id="promo">Get the glow &#10024; <b>FREE uplighting ($400 value)</b> with any package booked by Dec 31st! <a href="book.html" style="color:#fff">Book now &rarr;</a></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="index.html" aria-label="DJ1203 Productions home"><img src="assets/logo-headphones.png" alt="DJ1203 Productions"></a>
<nav class="top">{top}<a class="btn sm tl" href="book.html">Book Now</a><button class="menu-btn" id="menuBtn" aria-label="Open menu"><i></i>Menu</button></nav>
</div></header>
<div class="scrim" id="scrim"></div>
<aside class="drawer" aria-label="Menu"><button class="x" id="closeBtn" aria-label="Close menu">&times;</button>
<img src="assets/logo-headphones.png" alt="" style="height:54px;margin-bottom:6px">
<h4>Explore</h4>{drawer}{LABS}
<h4>Info</h4><a href="packages.html#policies">Travel &amp; policies</a><a href="book.html#agreement">Service agreement</a><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms &amp; conditions</a>
<a class="btn" href="book.html">Check my date</a>
<p class="call">Call or text <a href="tel:{TEL}">{PHONE}</a></p></aside>
<main>{body}</main>
<footer><div class="wrap"><div class="cols">
<div><img src="assets/logo-headphones.png" alt="DJ1203 Productions" style="height:62px;margin-bottom:12px"><p>South Bend's hometown DJ. Pro sound, lighting and energy for weddings, school dances, parties and corporate events across Michiana.</p>{socials()}</div>
<div><h5>Explore</h5>{"".join(f'<a href="{f}">{n}</a>' for f, n in PAGES)}{LABS}</div>
<div><h5>Info</h5><a href="packages.html#policies">Travel &amp; policies</a><a href="book.html#agreement">Service agreement</a><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms &amp; conditions</a></div>
<div class="contact"><h5>Contact</h5><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="mailto:{EMAIL2}">{EMAIL2}</a><p style="margin:8px 0 0">South Bend, Indiana<br>Mon&ndash;Fri, 9 am &ndash; 5 pm</p></div>
</div><div class="legal">&copy; 2026 DJ 1203 Productions, LLC. All rights reserved. Fully insured.</div></div></footer>
<div class="lb" id="lb"><button aria-label="Close">&times;</button><img alt=""></div>
<script>
document.body.classList.remove('nojs');
var b=document.body;function nav(o){{b.classList.toggle('nav',o)}}
document.getElementById('menuBtn').onclick=function(){{nav(true)}};document.getElementById('closeBtn').onclick=function(){{nav(false)}};document.getElementById('scrim').onclick=function(){{nav(false)}};
document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{nav(false);lb.classList.remove('on')}}}});
if(new Date()>new Date('2027-01-01T00:00:00'))document.getElementById('promo').style.display='none';
var tabs=document.querySelectorAll('.tabs button');function show(id){{tabs.forEach(function(t){{t.classList.toggle('on',t.dataset.t===id);if(t.dataset.t===id)t.scrollIntoView({{block:'nearest',inline:'center'}})}});document.querySelectorAll('.panel').forEach(function(p){{p.classList.toggle('on',p.id===id)}})}}
tabs.forEach(function(t){{t.onclick=function(){{show(t.dataset.t);history.replaceState(null,'','#'+t.dataset.t);window.scrollTo({{top:document.querySelector('.tabs').offsetTop-70,behavior:'smooth'}})}}}});
if(tabs.length){{var h=location.hash.slice(1);show(document.getElementById(h)&&document.getElementById(h).classList.contains('panel')?h:tabs[0].dataset.t)}}
var lb=document.getElementById('lb');document.querySelectorAll('.gal a').forEach(function(a){{a.onclick=function(e){{e.preventDefault();lb.querySelector('img').src=a.href;lb.classList.add('on')}}}});lb.onclick=function(){{lb.classList.remove('on')}};
</script></body></html>"""

# ---------- HOME ----------
cards = [("Weddings", "From the first dance to last call. Packages from $1,200, or the whole day for one flat price.", "packages.html#weddings", "&#128141;"),
         ("School &amp; Youth", "Clean, radio-friendly dances for elementary through prom, church and youth events.", "packages.html#school", "&#127891;"),
         ("Parties &amp; Events", "Birthdays, holiday parties and get-togethers. Full DJ, sound and lighting from $600.", "packages.html#events", "&#127881;"),
         ("College", "Campus events, Greek life and formals with full production lighting.", "packages.html#college", "&#127979;"),
         ("Quincea&ntilde;eras", "Grand entrances, special dances and a party your family won't forget.", "packages.html#quince", "&#128081;"),
         ("Corporate", "Conferences, galas and company parties. Custom quotes based on your event.", "packages.html#quince", "&#127970;")]
home = f"""
<section class="hero"><div class="reel" aria-hidden="true"><video class="bg on" autoplay muted playsinline preload="auto" poster="assets/video/henderson-castle.jpg"><source src="assets/video/henderson-castle.mp4" type="video/mp4"></video><video class="bg" muted playsinline preload="none" poster="assets/video/laser-show.jpg"><source src="assets/video/laser-show.mp4" type="video/mp4"></video><video class="bg" muted playsinline preload="none" poster="assets/video/beams-booth.jpg"><source src="assets/video/beams-booth.mp4" type="video/mp4"></video></div>
<div class="wrap"><p class="eyebrow">South Bend &middot; Michiana &middot; SW Michigan</p>
<h1>Where great music meets<br>unforgettable memories</h1>
<p>Pro-level sound, lighting and energy for weddings, school dances, parties and corporate events. Your hometown DJ, treating every client like a neighbor.</p>
<div class="cta"><a class="btn" href="book.html">Check my date</a><a class="btn ghost" href="packages.html">See packages</a></div>
<div class="hero-track"><span class="ht-label"><span class="eq" aria-hidden="true"><i></i><i></i><i></i></span>Hear the vibe: <b>Circuitry of the Night</b></span><iframe title="Circuitry of the Night by DJ1203 on SoundCloud" width="100%" height="20" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/dj1203pro/circuitry-of-the-night&color=%232bb3c9&inverse=true&auto_play=false&show_user=true"></iframe></div></div></section>

<section><div class="wrap"><p class="eyebrow">What we do</p><h2>Every kind of event</h2>
<div class="grid svc" style="margin-top:26px">{"".join(f'<a class="card" href="{u}"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p><span class="more">See pricing &rarr;</span></a>' for t,d,u,i in cards)}</div></div></section>

<section class="alt"><div class="wrap split">
<div class="photo"><img src="assets/photos/chris-henderson-smile.jpg" alt="Chris of DJ1203 Productions smiling behind his DJ booth at Henderson Castle" style="aspect-ratio:4/5"></div>
<div><p class="eyebrow">Why DJ1203</p><h2>The full production, not just a playlist</h2>
<p class="muted">Every package comes with a live DJ/MC, two PA speakers, two subwoofers and a wireless mic. Step up to uplighting, lighting totems and moving heads that turn any room into a dance floor.</p>
{ticks(["Pro sound and lighting at every event", "Clean, radio-friendly music for school and youth events", "Fully insured. Certificates of insurance for your venue on request", "Hometown Heroes: 10% off for military, first responders, nurses, teachers and truck drivers"])}
<div class="cta"><a class="btn" href="packages.html">Compare packages</a></div></div></div></section>

<section><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap"><div><p class="eyebrow">Recent events</p><h2 style="margin:0">From the booth</h2></div><a class="btn ghost sm" href="gallery.html">View gallery</a></div>
<div class="strip" style="margin-top:24px"><img src="assets/photos/halloween-dancefloor.jpg" alt="Dance floor at a Halloween party"><img src="assets/photos/banquet-hall-rig.jpg" alt="Full DJ and lighting setup in a banquet hall"><img src="assets/photos/moving-head-beam.jpg" alt="DJ1203 mixing with a moving head light beam"><img src="assets/photos/henderson-castle-night.jpg" alt="Henderson Castle at night"></div></div></section>

<section class="alt"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap"><div><p class="eyebrow">Reviews</p><h2 style="margin:0">What our clients say</h2><p class="muted" style="margin:6px 0 0">5.0 on Google &amp; Thumbtack</p></div><div class="cta" style="margin:0"><a class="btn ghost sm" href="https://www.google.com/maps/search/DJ1203+Productions+LLC" target="_blank" rel="noopener">Read all reviews</a></div></div><div class="grid g2 reviews" style="margin-top:24px"><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;Up and coming but not for long&hellip; He&rsquo;s got a great setup with an awesome light show and is very receptive to what the hosts of the event and party goers want. We have used him a few times now and he easily matches the vibe we are going for. I would highly recommend DJ 1203 if you want to put on an epic event that everyone will surely remember!&rdquo;</blockquote><figcaption>Cecelia J. &middot; Google review</figcaption></figure><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;Chris is an excellent DJ and really fits his style into your needs. I needed a clean playlist for several teen events, and he not only accommodated but nailed it. He is punctual, passionate, and a great communicator. Would not hesitate to hire again.&rdquo;</blockquote><figcaption>Cynthia O. &middot; Google review</figcaption></figure><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;Played our store on 4 separate occasions now. Amazing. Customers love it.&rdquo;</blockquote><figcaption>Matt &middot; Google review</figcaption></figure><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;Super energetic and fun. Good song choices and everyone loved it!&rdquo;</blockquote><figcaption>Addie &middot; Google review</figcaption></figure><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;Chris and Kelli were so awesome to work with. Right from the start the communication was great. They brought great energy to the whole evening. The students thought they were great and fun. Highly recommend.&rdquo;</blockquote><figcaption>Laura H. &middot; Thumbtack review</figcaption></figure><figure class="card review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;I hired DJ1203 for a backyard party. He kept up with communication throughout and made the event so fun. We danced all night. Would recommend to anyone.&rdquo;</blockquote><figcaption>Kerri M. &middot; Thumbtack review</figcaption></figure></div><p class="muted" style="margin-top:18px;font-size:15px">Also rated 5.0 on <a href="https://www.thumbtack.com/in/south-bend/djs/dj1203-productions-llc/service/581611524776960008" target="_blank" rel="noopener">Thumbtack</a> and <a href="{YELP}" target="_blank" rel="noopener">Yelp</a>.</p></div></section>

<section class="band"><div class="wrap"><h2>Ready to lock in your date?</h2><p class="lead" style="margin:0 auto 24px">Tell us when, where and what kind of event, and we'll get back to you with availability and pricing.</p>
<a class="btn" href="book.html">Check my date</a> &nbsp; <a class="btn ghost" href="tel:{TEL}">Call {PHONE}</a></div></section>"""

# ---------- PACKAGES ----------
base = ["DJ/MC", "2 PA speakers", "2 subwoofers", "Wireless mic"]
simple = base + ["Simple lighting"]
full = base + ["Full production lighting", "Wireless uplighting", "Totem towers", "2 moving head lights"]
choice = simple + ["Your choice of wireless uplighting <b>or</b> totem towers with 2 moving heads"]
def pkg(name, price, hrs, items, tag=None):
    return f'<div class="card pkg{" feat" if tag else ""}">{f"<span class=tag>{tag}</span>" if tag else ""}<h3>{name}</h3><div class="price">{price}</div><div class="hrs">{hrs}</div>{ticks(items) if items else ""}</div>'
def rates(rows): return '<table class="rates">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</table>"
heroes = '<div class="note"><b>Hometown Heroes:</b> 10% off for military, first responders, nurses, teachers and truck drivers. <a href="about.html#heroes">Details</a></div>'
panels = [
 ("events", "Events", "Standard events", "Birthdays, holiday parties, family gatherings and more.",
  '<div class="grid g3">' + pkg("Standard Event", "$600", "Up to 3 hours", simple, "Starting point") + '</div>'),
 ("school", "School &amp; Youth", "School, church &amp; youth", "All school and youth events use clean, radio&#8209;friendly music.",
  '<div class="grid g3">' + pkg("Elementary", "$700", "Up to 3 hours", choice) + pkg("Church Dance", "$700", "Up to 3 hours", choice)
  + pkg("Middle School", "$1,000", "3 hours", full) + pkg("High School", "$1,300", "3 hours", full)
  + pkg("Prom / Homecoming", "$1,250", "2 hours", full) + pkg("Prom / Homecoming", "$1,500", "4 hours", full, "Most popular") + '</div>'),
 ("college", "College", "College events", "Every college package includes DJ/MC, 2 PA speakers, 2 subwoofers, wireless mic, full production lighting, wireless uplighting, totem towers and 2 moving head lights.",
  '<div class="grid g2">' + pkg("Small Campus &amp; Greek Life", "$1,300", "3 hours", [])
  + pkg("Campus Events &amp; Formals", "$1,500", "4 hours", [], "Most popular") + '</div>'),
 ("weddings", "Weddings", "Wedding packages", "From an intimate reception to the whole day, one flat price.",
  '<div class="grid g3">' + pkg("Value", "$1,200", "4 hours", simple) + pkg("Standard", "$1,500", "6 hours", simple)
  + pkg("Gold", "$1,800", "6 hours", simple + ["Wireless uplighting"]) + pkg("Platinum", "$2,000", "6 hours", full, "Most popular")
  + pkg("All-Day Wedding", "$2,500", "Up to 10 hours, ceremony through last dance", base + ["Ceremony audio"] + full[4:], "Best value") + '</div>'),
 ("quince", "Quincea&ntilde;eras &amp; Corporate", "Quincea&ntilde;eras &amp; corporate", "",
  '<div class="grid g2">' + pkg("Quincea&ntilde;era", "$1,300", "4 hours", ["Full DJ service", "2 PA speakers", "2 subwoofers", "Wireless mic", "Grand entrance music", "Special dances (father&ndash;daughter, court and more)"])
  + pkg("Corporate Events", "Custom quote", "Based on your event", ["Custom quotes based on scope", "Conference sound &amp; mics", "Event lighting &amp; staging"]) + '</div>'),
 ("addons", "Add-ons", "Add-ons &amp; upgrades", "Add to any package.",
  '<div class="grid g2"><div class="card"><h3>Upgrades</h3>' + rates([("Ceremony audio", "$400"), ("Uplighting package", "$400"), ("Additional PA speaker", "$60 each / $100 pair"),
   ("Additional subwoofer", "$75 each / $125 pair"), ("Moving head light", "$75 each"), ("Outdoor tent rental", "$150")])
  + '</div><div class="card"><h3>Totems &amp; lighting columns</h3><p>Clean, modern aluminum truss totems that frame your DJ booth and dance floor, with professional setup and teardown.</p>'
  + rates([("Single totem (static or color-changing wash)", "$150"), ("Pair of matching totems", "$275"), ("Moving head upgrade (beams, gobos, motion)", "+$75 per fixture")]) + '</div></div>'),
 ("policies", "Travel &amp; Policies", "Travel, time &amp; policies", "",
  '<div class="grid g2"><div class="card"><h3>&#128663; Travel &amp; mileage</h3>' + rates([("First 25 miles from ZIP 46628", "Free"), ("Each additional 25 miles", "$150"), ("Overnight travel", "Please call")])
  + '</div><div class="card"><h3>&#9201;&#65039; Overtime</h3>' + rates([("Extra hours before midnight", "$250/hr"), ("After midnight", "$450/hr")]) + '<p style="margin-top:10px">Billed in 30-minute increments. Must be approved by the client or day-of contact.</p></div>'
  + '<div class="card"><h3>&#129523; Load-in (stairs &amp; long carries)</h3>' + rates([("Stairs without elevator", "$50 per flight"), ("Carry 100&ndash;250 ft", "$75"), ("Carry 250&ndash;500 ft", "$150"), ("Carry 500+ ft", "$250 or quoted")]) + '<p style="margin-top:10px">Please tell us about stairs, elevators and the distance from unloading to setup when you book.</p></div>'
  + '<div class="card"><h3>&#127881; Holiday rates</h3>' + rates([("New Year&rsquo;s Eve, Christmas Day", "Double rate"), ("Christmas Eve, Thanksgiving, Fourth of July, Halloween", "+50%"), ("Memorial Day, Labor Day, St. Patrick&rsquo;s Day", "+25%")]) + '</div>'
  + '<div class="card"><h3>&#128179; Payment policy</h3><p>We don&rsquo;t accept any payment until your invoice is approved and the service agreement is signed by both parties. Please pay only the exact invoiced amount. Any overpayment is applied as a credit toward your event balance. We never refund overpayments by check, wire or gift card, and never send funds to a third party.</p></div>'
  + '<div class="card"><h3>&#128737;&#65039; Fully insured</h3><p>DJ1203 Productions, LLC carries general liability insurance. We&rsquo;re happy to send a Certificate of Insurance to you or your venue. Just ask at least 14 days before your event.</p></div></div>'),
]
packages = (f"""<div class="page-hero"><div class="wrap"><p class="eyebrow">Packages &amp; pricing</p><h1>Pick your party</h1><p class="lead">Clear, upfront pricing for every kind of event. Every package includes a live DJ/MC and pro sound. Tap a category to jump to it.</p></div></div>
<div class="tabs"><div class="wrap">""" + "".join(f'<button data-t="{i}">{t}</button>' for i, t, *_ in panels) + "</div></div><div class=wrap>"
 + "".join(f'<div class="panel" id="{i}"><h2>{h}</h2>{f"<p class=lead>{d}</p>" if d else ""}<div style="margin-top:22px">{heroes if i in ("events","weddings","school") else ""}{c}</div>'
           f'<p class="muted" style="margin-top:26px">Want a quote for your date? <a href="book.html">Send your event details</a> or call <a href="tel:{TEL}">{PHONE}</a>.</p></div>' for i, t, h, d, c in panels)
 + "</div>")

# ---------- GALLERY ----------
photos = [("henderson-djing-wide", "Henderson Castle, Kalamazoo"), ("halloween-dancefloor", "Halloween Bash"), ("booth-totems-moving-heads", "Totems and moving heads"),
          ("henderson-full-setup", "Full setup at Henderson Castle"), ("moving-head-beam", "Beams and fog"), ("banquet-hall-rig", "Banquet hall reception rig"),
          ("halloween-masked-dj", "Halloween behind the decks"), ("culver-dance-floor", "Culver dance floor"), ("culver-auditorium-night", "Culver auditorium at night"), ("chris-djing-bubbles", "Bubbles on the decks"),
          ("henderson-djing-pink", "Mixing at Henderson Castle"), ("case-lights-bw", "The DJ1203 road case"), ("booth-setup", "Pop-up booth setup"), ("henderson-castle-night", "Henderson Castle at night")]
gallery = f"""<div class="page-hero"><div class="wrap"><p class="eyebrow">Gallery</p><h1>Live from the booth</h1><p class="lead">Real setups from real events across South Bend and Michiana. Tap any photo to see it full size.</p></div></div>
<section style="padding-top:44px;padding-bottom:20px"><div class="wrap"><p class="eyebrow">In motion</p><h2>See the show</h2><div class="grid g2 vids" style="margin-top:20px"><figure><video autoplay muted loop playsinline preload="metadata" poster="assets/video/henderson-castle.jpg"><source src="assets/video/henderson-castle.mp4" type="video/mp4"></video><figcaption>Henderson Castle, Kalamazoo</figcaption></figure><figure><video autoplay muted loop playsinline preload="metadata" poster="assets/video/beams-booth.jpg"><source src="assets/video/beams-booth.mp4" type="video/mp4"></video><figcaption>Moving heads and lasers</figcaption></figure><figure><video autoplay muted loop playsinline preload="metadata" poster="assets/video/culver-night.jpg"><source src="assets/video/culver-night.mp4" type="video/mp4"></video><figcaption>Lighting up Culver</figcaption></figure><figure><video autoplay muted loop playsinline preload="metadata" poster="assets/video/halloween-booth.jpg"><source src="assets/video/halloween-booth.mp4" type="video/mp4"></video><figcaption>Halloween Bash</figcaption></figure></div></div></section>
<section style="padding-top:30px"><div class="wrap"><p class="eyebrow">Photos</p><div class="gal">{"".join(f'<a href="assets/photos/{f}.jpg"><img src="assets/photos/{f}.jpg" alt="{c}" loading="lazy"><span>{c}</span></a>' for f, c in photos)}</div></div></section>
<section class="alt"><div class="wrap"><p class="eyebrow">Event highlights</p><h2>Recent nights</h2><div class="grid g3" style="margin-top:22px">
<div class="card"><h3>Hunter Ice Fest 2026</h3><p>Dropped a quick set at Rumor Records during Hunter Ice Fest on January 17. Freezing outside, heat on the decks inside. Smooth mix, fun vibe, and a little mid-festival chaos to keep it interesting.</p></div>
<div class="card"><h3>Halloween Bash 2025</h3><p>Lights flashing, costumes everywhere, and the energy locked in all night. DJ1203 ran the soundtrack and kept the party moving from start to finish.</p></div>
<div class="card"><h3>Rumor Records, May 30, 2026</h3><p>Another clean session inside Rumor Records: tight mix, crisp timing and a solid atmosphere, with the sound dialed in and the flow kept right.</p></div>
</div><p class="muted" style="margin-top:22px">More clips on <a href="https://www.tiktok.com/@DJ1203Productions" target="_blank" rel="noopener">TikTok</a>, <a href="https://www.instagram.com/DJ1203Productions" target="_blank" rel="noopener">Instagram</a> and <a href="https://www.youtube.com/@DJ1203Productions" target="_blank" rel="noopener">YouTube</a>.</p></div></section>"""

# ---------- ABOUT ----------
about = f"""<div class="page-hero"><div class="wrap"><p class="eyebrow">About DJ1203</p><h1>South Bend&rsquo;s hometown DJ</h1><p class="lead">Built on hard work and honoring the people who keep our community running.</p></div></div>
<section><div class="wrap split"><div><h2>Our mission</h2><p class="muted">From weddings to school dances, our mission is to give every client pro-level sound, lighting and energy, and to treat them like neighbors, not invoices.</p>
<p class="muted">We read the room, play the right song at the right moment, and bring a lighting rig that makes the night feel bigger. You get a DJ who shows up early, communicates clearly and gives every event 110%.</p>
<p class="muted">Behind the scenes at DJ1203 Productions, Kelli helps coordinate the details so everything runs smoothly on the big day.</p>
{ticks(["Weddings, quincea&ntilde;eras, school and church dances, college, corporate and private parties", "Clean, radio-friendly sets for school and youth events", "DJ1203 Productions, LLC: fully insured, with COIs for your venue"])}</div>
<div class="photo"><img src="assets/photos/chris-kelli-booth.jpg" alt="Chris and Kelli of DJ1203 Productions in front of their lit booth and totems" style="aspect-ratio:4/5"></div></div></section>
<section class="alt"><div class="wrap split"><div class="photo"><img src="assets/photos/booth-setup.jpg" alt="DJ1203 booth with the neon placard banner" style="aspect-ratio:4/5"></div>
<div><p class="eyebrow" id="heroes">Hometown Heroes</p><h2>Thank you for what you do</h2><p class="muted">We proudly offer 10% off any base package to the people who keep our communities running:</p>
{ticks(["Active-duty and retired military, Guard and Reserve", "First responders: police, fire and EMS", "Nurses", "Teachers", "Truck drivers"])}
<p class="muted" style="margin-top:14px">Just show a valid ID or proof of service when you book, such as a Military ID, DD&#8209;214, department or employer ID, school ID or CDL. Applies to personal events.</p>
<div class="cta"><a class="btn" href="book.html">Book with your discount</a></div></div></div></section>"""

# ---------- BOOK ----------
agreement = [
 ("&#128204; Client responsibilities", ["Provide all final event details at least 30 days before the event.", "Maintain a safe, secure and suitable venue.", "Minimum setup space: 8 ft &times; 6 ft.", "Guests and vendors may not touch DJ equipment.", "Let us know about any venue restrictions.", "Start/end time changes must be requested in writing at least 14 days before the event. Later changes depend on availability and may incur fees.", "If the event starts late for reasons outside our control, the end time stays the same unless overtime is approved."]),
 ("&#127911; Services provided", ["Professional DJ &amp; MC services, sound, lighting and any selected add-ons. Setup and teardown are included."]),
 ("&#128176; Payments &amp; retainer", ["A 50% non-refundable retainer is due at signing to book your date.", "The remaining balance is due 14 days before the event.", "Late payments incur a $25/day fee.", "Accepted payment methods: PayPal and credit/debit card."]),
 ("&#9200; Extra time &amp; overtime", ["Extra hours: $250/hr until midnight, $450/hr after midnight, billed in 30-minute increments.", "Overtime must be approved by the Client or the named Day-of Contact before the scheduled end time. Requests from guests or other vendors are not accepted without that approval.", "Overtime is due the night of the event and depends on venue rules and DJ availability."]),
 ("&#128663; Travel &amp; mileage", ["0&ndash;25 miles: included", "26&ndash;50 miles: +$150", "51&ndash;75 miles: +$300", "76&ndash;100 miles: +$450", "100+ miles: +$600", "Overnight/long-distance events: client provides hotel (3-star minimum), parking and transportation; travel day fee $300/day; DJ meals up to $75/day; equipment transport fee $150 if flying."]),
 ("&#9889; Setup, power &amp; venue", ["Typical setup: 90 minutes (standard events); 2 hours (weddings and full-production events). Teardown: 60 minutes.", "The setup area must be cleared, clean and on a flat, stable surface before we arrive. Delays over 15 minutes may reduce performance time.", "Power: two dedicated 15-amp circuits within 25 feet of the DJ area, not shared with other vendors.", "Outdoor events: full overhead shelter, sidewalls if needed, dry level ground and a backup indoor plan (or add our Outdoor Tent Rental, $150).", "Load-in fees: stairs without elevator $50/flight; carries of 100&ndash;250 ft $75, 250&ndash;500 ft $150, 500+ ft $250. Please disclose stairs and carry distance at booking."]),
 ("&#127782;&#65039; Weather &amp; emergencies", ["We may pause, stop or move equipment if rain, high wind, lightning, extreme heat/cold or power loss puts people or equipment at risk.", "If the event is shortened or stopped for reasons outside our control, the full contracted fee is still due.", "If you move the event to a new date for these reasons, we&rsquo;ll try to accommodate it, subject to availability."]),
 ("&#9749; Breaks, food &amp; beverage", ["The DJ may take brief restroom/hydration breaks; music continues at all times.", "For events of 4+ hours, longer breaks may occur during natural pauses.", "Client provides water and non-alcoholic beverages.", "For events of 5+ hours, client provides a meal or allows the DJ to bring food.", "The DJ will not consume alcohol."]),
 ("&#127925; Music requests", ["Requests must be submitted 14 days before the event.", "The DJ may refuse explicit or unsafe music."]),
 ("&#128683; Cancellation &amp; rescheduling", ["The retainer is non-refundable.", "Cancellations within 30 days require full payment of the balance.", "Rescheduling must be in writing and is subject to availability.", "Rescheduling within 30 days: $100 fee.", "If the DJ cancels, all payments are refunded."]),
 ("&#128737;&#65039; Liability &amp; insurance", ["Client holds DJ1203 Productions harmless for claims arising from guests, venue issues, weather or circumstances beyond our control.", "DJ1203 Productions carries general liability insurance and will provide a Certificate of Insurance on request. Please request it at least 14 days before the event."]),
 ("&#128274; Safety, security &amp; conduct", ["Client must maintain adequate security before, during and after the event.", "Client is responsible for theft, vandalism or damage caused by guests, attendees or venue staff, including dropped microphones.", "If threats, violence or unsafe conditions occur, the DJ may stop immediately and will allow up to 30 minutes for resolution before deciding whether to resume.", "Client remains responsible for full payment and any damages."]),
 ("&#128084; DJ dress code", ["Weddings &amp; formal: dress pants, dress shoes, button-down shirt; optional tie/blazer.", "Corporate: business-casual or business-professional.", "School / youth / casual: clean, professional casual; branded apparel allowed.", "Outdoor: weather-appropriate clothing."]),
 ("&#127894;&#65039; Hometown Heroes discount", ["10% off any base package for active or retired military, police, fire, EMS, nurses, teachers and truck drivers. Proof may be requested."]),
 ("&#128248; Media release", ["Clients choose whether DJ1203 Productions may use photos or video clips from the event for promotional purposes."]),
 ("&#128394;&#65039; Full contract &amp; signatures", ["The full contract will be provided after booking. It must be signed along with the retainer to officially secure your event date.", "If the client is under 18, a parent or legal guardian must also sign and accepts responsibility for payment and all obligations."]),
]
acc = "".join(f'<details class="acc"><summary>{t}</summary><div class="b"><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div></details>' for t, items in agreement)
book = f"""<div class="page-hero"><div class="wrap"><p class="eyebrow">Book now</p><h1>Let&rsquo;s check your date</h1><p class="lead">Tell us when, where, what kind of event and how long it runs, and we&rsquo;ll get back to you with availability and pricing.</p></div></div>
<section style="padding-top:44px"><div class="wrap split" style="align-items:start">
<div><h2 style="font-size:28px">Event details &amp; booking request</h2><div class="embed"><script src="https://empdj.com/embed.js" defer></script><div data-empdj-form="18a31e40-cfb5-49a4-8c3c-1fb376161943"></div></div></div>
<div><div class="card contact"><h3>Prefer to talk?</h3><p style="margin-bottom:12px">Call or text anytime. We answer Monday through Friday, 9 am to 5 pm.</p>
<p style="font-size:22px;font-family:Oswald,sans-serif;margin:0"><a href="tel:{TEL}">{PHONE}</a></p><p style="margin:8px 0 0"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL2}">{EMAIL2}</a></p>{socials()}</div>
<div class="card" style="margin-top:16px"><h3>How booking works</h3>{ticks(["Send your event details", "Get your quote and service agreement", "Sign and pay a 50% retainer to lock your date", "Balance due 14 days before the event"])}</div></div></div></section>
<section class="alt" id="agreement"><div class="wrap" style="max-width:900px"><p class="eyebrow">Before you book</p><h2>Service agreement summary</h2><p class="muted">This is a summary of the DJ1203 Productions, LLC service agreement. A full contract is provided after booking and must be signed to confirm your event. Tap a section to open it.</p>{acc}</div></section>"""

# ---------- SHOP ----------
shop = """<div class="page-hero"><div class="wrap"><p class="eyebrow">Merch</p><h1>Rep DJ1203</h1><p class="lead">Hoodies, hats, tees and beanies. Wear the brand to the next party.</p></div></div>
<section style="padding-top:44px"><div class="wrap"><div class="embed"><div id="my-store-137282256"></div>
<script data-cfasync="false" type="text/javascript" src="https://app.ecwid.com/script.js?137282256&data_platform=code" charset="utf-8"></script>
<script type="text/javascript">xProductBrowser("categoriesPerRow=3","views=grid(20,3) list(60) table(60)","categoryView=grid","searchView=list","id=my-store-137282256");</script></div></div></section>"""

# ---------- PRIVACY / TERMS ----------
privacy = """<div class="page-hero"><div class="wrap"><h1>Privacy policy</h1><p class="muted">Last updated: November 2026</p></div></div><section><div class="wrap prose">
<p>DJ1203 Productions, LLC respects your privacy. This policy explains what information we collect through this website and how we use it.</p>
<h2>Information we collect</h2><p>When you fill out our booking request form, we collect your name, email, phone number, event details and any files you choose to attach. This website loads fonts from Google Fonts, and our booking form and store are provided by EMP DJ and Ecwid, which may collect basic visit data such as your IP address and browser type.</p>
<h2>How we use it</h2><p>We use your information only to answer your inquiry, plan and book your event, send quotes, invoices and agreements, and stay in touch about your event.</p>
<h2>Payments</h2><p>Payments are handled by secure third-party processors such as PayPal. We never see or store your full card or bank details.</p>
<h2>Sharing</h2><p>We do not sell, rent or trade your information. We only share what&rsquo;s needed with trusted partners helping with your event (for example, a backup DJ or your venue), or when required by law.</p>
<h2>Text messages</h2><p>If you give us your phone number, we may text you about your event. Reply STOP at any time to opt out.</p>
<h2>Keeping it safe</h2><p>We take reasonable steps to protect your information and keep it only as long as needed for your event and our business records.</p>
<h2>Questions</h2><p>Contact us at <a href="mailto:dj1203productions@gmail.com">dj1203productions@gmail.com</a> with any questions or to ask that we update or delete your information.</p></div></section>"""
terms = """<div class="page-hero"><div class="wrap"><h1>Terms &amp; conditions</h1><p class="muted">Last updated: November 2026</p></div></div><section><div class="wrap prose">
<h2>Service agreement</h2><p>Approving an estimate means you agree to the services, details and payment terms it lists. Every booking is confirmed by a signed service agreement; see the <a href="book.html#agreement">service agreement summary</a> for the key terms.</p>
<h2>Payments</h2><p>Please review your invoice before approving it. Payment is accepted by PayPal or other approved methods. Retainers are non-refundable, and the final balance is due before your event begins (14 days before, per the service agreement). We don&rsquo;t accept any payment until the invoice is approved and the agreement is signed by both parties.</p>
<h2>Event requirements</h2><p>The client provides a safe setup area and adequate electrical power, and the venue must support professional audio and lighting.</p>
<h2>Liability</h2><p>DJ1203 Productions is not responsible for damage caused by venue conditions, guest behavior or outside factors.</p>
<h2>Cancellations &amp; changes</h2><p>Please communicate changes promptly. Rescheduling depends on availability, and payments and retainers may be non-refundable depending on the situation.</p>
<h2>Media &amp; content</h2><p>Mixes, videos, photos and branded content created by DJ1203 Productions belong to DJ 1203 Productions, LLC.</p>
<h2>Website</h2><p>Prices and packages on this website may change. Your signed agreement sets the price for your event.</p>
<h2>Contact</h2><p>Reach us by phone at <a href="tel:2196084119">(219) 608-4119</a>, by email at <a href="mailto:chris@dj1203productions.com">chris@dj1203productions.com</a>, or through this website.</p></div></section>"""

D = "DJ1203 Productions: South Bend DJ for weddings, school dances, parties and corporate events. Pro sound, lighting and upfront pricing."
ALL = [("index.html", "DJ1203 Productions | South Bend DJ, Sound & Lighting", home), ("packages.html", "Packages & Pricing | DJ1203 Productions", packages),
                   ("gallery.html", "Gallery | DJ1203 Productions", gallery), ("about.html", "About | DJ1203 Productions", about),
                   ("book.html", "Book Now | DJ1203 Productions", book), ("shop.html", "Shop Merch | DJ1203 Productions", shop),
                   ("privacy.html", "Privacy Policy | DJ1203 Productions", privacy), ("terms.html", "Terms & Conditions | DJ1203 Productions", terms)]
# ---------- EDM preview (served at /preview/, not indexed) ----------
import os, re
import shutil; shutil.rmtree("preview", ignore_errors=True)
import math
_pts = " ".join(f"L{x/2:.1f} {23 + 16*math.sin(x*0.045)*(0.35+0.65*abs(math.sin(x*0.004))):.1f}" for x in range(0, 2401, 6))
WAVE = '<svg class="wave" viewBox="0 0 1200 46" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="wg" x1="0" x2="1"><stop offset="0" stop-color="#2bb3c9"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient></defs><path d="M0 23 ' + _pts + '" fill="none" stroke="url(#wg)" stroke-width="1.6"/></svg>'
TICK = "".join(f"<span>{w}</span><b>&#9670;</b>" for w in ["Weddings", "School dances", "Quincea&ntilde;eras", "Proms &amp; homecoming", "College events", "Corporate", "Birthdays", "Holiday parties"])
REEL = """<script>(function(){var v=document.querySelectorAll('.reel video');if(v.length<2)return;var i=0;function next(){var cur=v[i];i=(i+1)%v.length;var n=v[i];n.preload='auto';n.currentTime=0;var p=n.play();if(p&&p.catch)p.catch(function(){});n.classList.add('on');cur.classList.remove('on');setTimeout(function(){cur.pause()},1200)}v.forEach(function(x){x.addEventListener('ended',next)});})();</script>"""
REVEAL = """<script>(function(){var els=document.querySelectorAll('main h2,main .card,main .photo,main .strip img,main .gal a,main .vids figure,main details.acc,main .embed');if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});els.forEach(function(el,i){el.classList.add('rv');el.style.transitionDelay=(i%4)*70+'ms';io.observe(el)})})();</script>"""
for f, t, body in ALL:
    if f == "index.html":
        body = body.replace('<div class="wrap"><p class="eyebrow">South Bend', '<div class="wrap"><div class="eq" aria-hidden="true">' + "<i></i>" * 7 + '</div><p class="eyebrow">South Bend', 1)
        body = body.replace('<h1>Where great music meets<br>unforgettable memories</h1>', '<h1>Where great music meets<br><span class="grad">unforgettable memories</span></h1>')
        body = body.replace('</section>\n\n<section><div class="wrap"><p class="eyebrow">What we do', '</section>\n<div class="ticker" aria-label="Events we cover"><div>' + TICK * 2 + '</div></div>\n\n<section><div class="wrap"><p class="eyebrow">What we do', 1)
    body = body.replace('<section class="alt"', WAVE + '<section class="alt"')
    page = shell(f, t, D, body)
    page = page.replace('<link rel="stylesheet" href="assets/site.css?v=2">', '<link rel="stylesheet" href="assets/site.css?v=2"><link rel="stylesheet" href="assets/site-edm.css">')
    page = page.replace('family=Oswald:wght@400;500;600', 'family=Oswald:wght@400;500;600;700')
    page = page.replace("</body>", REVEAL + (REEL if f == "index.html" else "") + "</body>")
    open(f, "w").write(page)
print("built")
