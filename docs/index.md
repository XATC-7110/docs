---
hide:
  - navigation
  - toc
---

<div class="xa-hero" markdown>

<span class="xa-kicker">AI air traffic control · X-Plane 12</span>

# Talk to ATC. It talks back.

<p class="xa-tagline">Hold push-to-talk and speak as you would on a real radio. A controller answers in US FAA phraseology, on the frequency you are tuned to, from the gate at one airport to the gate at the next.</p>

[Get started](getting-started.md){ .md-button .md-button--primary }
[What ATC can do](features/index.md){ .md-button }

<div class="xa-call">
<p class="you"><span class="who">You</span><span class="said">Seattle Clearance, November 547 Golf Alpha, IFR to Portland with Charlie.</span></p>
<p class="atc"><span class="who">Clearance</span><span class="said">N547GA, cleared to Portland via the SUMMA2 departure, then as filed. Maintain 5000, expect 16000 10 minutes after departure. Departure frequency 119.2, squawk 4521.</span></p>
<p class="you"><span class="who">You</span><span class="said">Cleared to Portland, SUMMA2 then as filed, 5000 expect 16000, 119.2, squawk 4521, 547GA. <span class="ok">✓ Readback accepted</span></span></p>
</div>

![The xatc-agent window during an approach: the radios, push-to-talk, ATC's plan for the approach and the log](assets/window-approach.png)

</div>

<ul class="xa-strip">
  <li><b>128.000</b>Clearance</li>
  <li><b>121.700</b>Ground</li>
  <li><b>119.900</b>Tower</li>
  <li><b>119.200</b>Departure</li>
  <li><b>124.200</b>Center</li>
  <li><b>124.350</b>Approach</li>
  <li><b>118.700</b>Tower</li>
  <li><b>121.900</b>Ground</li>
</ul>

## What it does

<div class="grid cards" markdown>

-   :material-radio-tower: **Every position talks to you**

    ---

    Clearance Delivery, Ground, Tower, Departure, Center and Approach, each on its real frequency. Tune a frequency nobody is on and you hear nothing.

    [:octicons-arrow-right-24: What ATC can do](features/index.md)

-   :material-airplane-takeoff: **Real procedures**

    ---

    IFR clearances, taxi routes with hold shorts, SIDs and STARs, climbs and descents, vectors to an ILS, RNAV or visual approach, and handoffs in between.

    [:octicons-arrow-right-24: A flight, gate to gate](first-flight.md)

-   :material-check-decagram: **Readbacks are checked**

    ---

    A correct readback gets silence and a check mark. A wrong one is corrected: "negative, squawk six six six two".

    [:octicons-arrow-right-24: Readbacks](features/readbacks.md)

-   :material-bullhorn: **ATC calls you first**

    ---

    Handoffs, a readback you forgot, an altitude you drifted from, traffic, a go-around: the controller speaks when a real one would.

    [:octicons-arrow-right-24: At every position](features/everywhere.md)

-   :material-map-marker-path: **ATC's plan, drawn**

    ---

    When Approach vectors you, the window draws the whole plan: the downwind, the base turn, where you join the final, and you.

    [:octicons-arrow-right-24: The approach plan](client/approach-card.md)

-   :material-earth: **Any US airport**

    ---

    Procedures, frequencies and airspace from the FAA's own data. Taxiways and parking from your own X-Plane scenery.

    [:octicons-arrow-right-24: Your X-Plane's data](client/xplane-data.md)

</div>

## What a flight is like

1. Start X-Plane 12 and the xatc-agent window. Press **New flight** and enter your flight plan, or load it from SimBrief.
2. Tune the ATIS and listen. Then call Clearance Delivery, get your clearance and read it back.
3. Ground taxis you to the runway. Tower clears you for takeoff. Departure climbs you and puts you on course. Center takes you to cruise and brings you down again.
4. Approach vectors you to final and clears the approach. Tower clears you to land and tells you where to leave the runway. Ground taxis you to the parking you ask for.

[Your first flight](first-flight.md) walks through it step by step.

## What you need

<div class="grid cards" markdown>

-   :material-monitor: **X-Plane 12 on Windows**

    ---

    X-Plane 12.1.4 or newer, Windows 10 or 11, a microphone, and an internet connection during the flight. The controller runs in the cloud; the window beside X-Plane is a thin client.

-   :material-account-key: **An invitation**

    ---

    xatc-agent is an invitation-only experiment. The owner creates your account and gives you the client.

    [:octicons-arrow-right-24: Install and sign in](getting-started.md)

</div>

## Know before you fly

!!! warning "A simulation, and an experiment"
    xatc-agent is for flight simulation only. It is not a training device and must never be used for real-world flying. It is under active development: what a controller says and does changes between releases, and things break.

- **IFR only**, for now. VFR departures, pattern work and flight following are not built.
- **US airports** work best: everything outside the taxiways comes from the FAA's data. Outside the US, ATC asks your X-Plane for the airport's procedures and frequencies instead.
- **English, FAA phraseology.**
- When ATC is asked for something it has not been taught, it says so: *"unable, I have not completed that training."* It does not make something up.
