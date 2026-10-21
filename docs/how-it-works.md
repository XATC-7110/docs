---
hide:
  - navigation
---

# How it works

Two parts: a thin **client** on your sim PC, and the **controller** in the cloud. One encrypted connection joins them for the whole flight.

<figure class="xa-diagram">
<svg viewBox="0 0 1060 590" role="img" aria-labelledby="xa-d-title xa-d-desc" xmlns="http://www.w3.org/2000/svg">
<title id="xa-d-title">How the parts of SeventyOneTen work together</title>
<desc id="xa-d-desc">On your PC, X-Plane 12 gives the SeventyOneTen client the aircraft's state, and the client tunes X-Plane's radios; your microphone and headset carry your voice in and ATC's audio out. The client signs in through your browser with the sign-in service, then keeps one encrypted connection per flight to the ATC service in the cloud. It sends the aircraft's state, your voice and answers about your scenery, and receives ATC's audio and text, the approach plan and parking. In the ATC service, speech recognition hears the call, an AI model understands it, the controller agent (an AI model) decides which ATC tool to use, the tool checks the request and writes the phraseology, and text to speech speaks it. Monitors watch every frame and start ATC's own calls through the same tools. The tools read the FAA's data. Each flight is written to a flight log that is reviewed afterwards.</desc>
<defs>
<marker id="xa-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="ah" d="M0,0 L10,5 L0,10 Z"/></marker>
<marker id="xa-ah2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path class="ah2" d="M0,0 L10,5 L0,10 Z"/></marker>
</defs>
<rect class="g" x="20" y="60" width="270" height="420" rx="14"/>
<text class="gt" x="36" y="84">Your PC</text>
<rect class="g" x="470" y="60" width="570" height="510" rx="14"/>
<text class="gt" x="486" y="84">The cloud</text>
<rect class="b" x="40" y="110" width="230" height="70" rx="9"/>
<text class="t" x="155" y="140" text-anchor="middle">X-Plane 12</text>
<text class="u" x="155" y="160" text-anchor="middle">your aircraft, weather, traffic, scenery</text>
<rect class="b hl" x="40" y="240" width="230" height="110" rx="9"/>
<text class="t" x="155" y="278" text-anchor="middle">SeventyOneTen client</text>
<text class="u" x="155" y="300" text-anchor="middle">push-to-talk, radios, the cards</text>
<text class="u" x="155" y="316" text-anchor="middle">plays ATC through a radio effect</text>
<rect class="b" x="40" y="404" width="230" height="56" rx="9"/>
<text class="t" x="155" y="437" text-anchor="middle">Microphone and headset</text>
<path class="a" d="M120,180 V238" marker-end="url(#xa-ah)"/>
<text class="l" x="112" y="206" text-anchor="end">aircraft</text>
<text class="l" x="112" y="220" text-anchor="end">state</text>
<path class="a" d="M190,240 V182" marker-end="url(#xa-ah)"/>
<text class="l" x="198" y="206">radio</text>
<text class="l" x="198" y="220">tuning</text>
<path class="a" d="M120,404 V352" marker-end="url(#xa-ah)"/>
<text class="l" x="112" y="374" text-anchor="end">your</text>
<text class="l" x="112" y="388" text-anchor="end">voice</text>
<path class="a" d="M190,350 V402" marker-end="url(#xa-ah)"/>
<text class="l" x="198" y="374">ATC</text>
<text class="l" x="198" y="388">audio</text>
<rect class="b" x="490" y="95" width="210" height="50" rx="9"/>
<text class="t" x="595" y="117" text-anchor="middle">Sign-in service</text>
<text class="u" x="595" y="134" text-anchor="middle">knows which pilot is flying</text>
<path class="a" d="M270,252 H305 V120 H488" marker-end="url(#xa-ah)"/>
<text class="l" x="318" y="112">sign in, in your browser</text>
<path class="a2" d="M270,275 H488" marker-end="url(#xa-ah2)"/>
<text class="l" x="318" y="180">aircraft state</text>
<text class="l" x="318" y="196">your voice, while you</text>
<text class="l" x="318" y="210">hold push-to-talk</text>
<text class="l" x="318" y="226">answers about your</text>
<text class="l" x="318" y="240">scenery, when asked</text>
<text class="lk" x="380" y="299" text-anchor="middle">one encrypted connection per flight</text>
<path class="a2" d="M490,320 H272" marker-end="url(#xa-ah2)"/>
<text class="l" x="318" y="342">ATC's audio and text</text>
<text class="l" x="318" y="358">the approach plan</text>
<text class="l" x="318" y="374">parking, frequencies</text>
<rect class="gw" x="490" y="175" width="530" height="270" rx="12"/>
<text class="t" x="506" y="200">ATC service</text>
<text class="u" x="596" y="200">one isolated session per flight</text>
<rect class="b" x="505" y="215" width="92" height="64" rx="8"/>
<text class="t" x="551" y="243" text-anchor="middle">Hear</text>
<text class="u" x="551" y="261" text-anchor="middle">speech to text</text>
<rect class="m" x="607" y="215" width="92" height="64" rx="8"/>
<text class="t" x="653" y="243" text-anchor="middle">Understand</text>
<text class="u" x="653" y="261" text-anchor="middle">reads the call</text>
<rect class="m" x="709" y="215" width="92" height="64" rx="8"/>
<text class="t" x="755" y="243" text-anchor="middle">Decide</text>
<text class="u" x="755" y="261" text-anchor="middle">picks a tool</text>
<rect class="b" x="811" y="215" width="92" height="64" rx="8"/>
<text class="t" x="857" y="243" text-anchor="middle">ATC tools</text>
<text class="u" x="857" y="261" text-anchor="middle">check, phrase</text>
<rect class="b" x="913" y="215" width="92" height="64" rx="8"/>
<text class="t" x="959" y="243" text-anchor="middle">Speak</text>
<text class="u" x="959" y="261" text-anchor="middle">text to speech</text>
<path class="a" d="M597,247 H605" marker-end="url(#xa-ah)"/>
<path class="a" d="M699,247 H707" marker-end="url(#xa-ah)"/>
<path class="a" d="M801,247 H809" marker-end="url(#xa-ah)"/>
<path class="a" d="M903,247 H911" marker-end="url(#xa-ah)"/>
<rect class="b" x="505" y="335" width="194" height="60" rx="8"/>
<text class="t" x="602" y="361" text-anchor="middle">Monitors</text>
<text class="u" x="602" y="379" text-anchor="middle">watch every frame, call you first</text>
<path class="a" d="M699,365 H835 V281" marker-end="url(#xa-ah)"/>
<text class="u" x="712" y="357">ATC's own calls</text>
<text class="u" x="507" y="417">A readback is judged by the AI model, item by item;</text>
<text class="u" x="507" y="431">code checks every quote against what you said.</text>
<rect class="s" x="640" y="475" width="250" height="70" rx="9"/>
<text class="t" x="765" y="504" text-anchor="middle">The FAA's data</text>
<text class="u" x="765" y="524" text-anchor="middle">procedures, frequencies, airspace, altitudes</text>
<path class="a" d="M875,475 V281" marker-end="url(#xa-ah)"/>
<rect class="s" x="910" y="475" width="110" height="70" rx="9"/>
<text class="t" x="965" y="504" text-anchor="middle">Flight log</text>
<text class="u" x="965" y="524" text-anchor="middle">reviewed after</text>
<path class="a" d="M965,445 V473" marker-end="url(#xa-ah)"/>
<rect class="m" x="24" y="508" width="26" height="16" rx="4"/>
<text class="u" x="58" y="520">an AI model</text>
<rect class="b" x="24" y="532" width="26" height="16" rx="4"/>
<text class="u" x="58" y="544">plain code: it checks, and it writes ATC's words</text>
<rect class="s" x="24" y="556" width="26" height="16" rx="4"/>
<text class="u" x="58" y="568">data</text>
</svg>
<figcaption>How the parts work together. The AI model understands and chooses; plain code checks the request and writes what ATC says.</figcaption>
</figure>

## One radio call

1. **You key the mic.** The client streams your audio while push-to-talk is held, beside a frame of aircraft state about once a second.
2. **Speech recognition** turns the audio into text. It is tuned for aviation phraseology, and with the **Scribe** choice in Settings it is also given the names from your flight (callsign, cities, procedures, route fixes).
3. **Plain code checks the basics**: is a controller on that frequency, and did your callsign come through.
4. **An AI model reads the call.** Is it a readback of what ATC just said, a request, or both?
5. **A readback is judged** item by item, quoting your own words. Code refuses any quote that is not in the transcript, then decides: accept in silence, correct one item, or ask once for a safety item.
6. **A request goes to the controller agent**, an AI model that plays the position you called. Its job is to pick the right **tool** for what you asked: issue a taxi clearance, assign an altitude, clear an approach.
7. **The tool does the controlling.** It checks the request against the FAA's data, your scenery and the state of your flight, writes the exact phraseology, and refuses in fixed words when the data says no.
8. **Text to speech** speaks it, the client adds the radio effect (the optional radio voices already sound like a radio, so they get only the key-up click), and you hear it if a radio that is on and selected to listen is tuned to that frequency. A call you could not hear is said again once when the radio can hear it, within about a minute.

Meanwhile **monitors** watch every frame of your aircraft's state and start ATC's own calls: handoffs, readback reminders, an altitude that drifted, traffic.

## Where the AI is, and where it is not

The AI model understands what you said and chooses what kind of thing a controller would do next. It does not invent the clearance.

| The model does | Code does |
|---|---|
| Classifies your transmission | Decides whether a controller is listening on that frequency |
| Judges a readback against what was said | Checks that every quoted word was really in your transmission |
| Picks the tool for your request | Checks the request against the data: runways, procedures, minimum altitudes, traffic |
| | Writes the words ATC speaks, in standard phraseology |
| | Watches your flight and starts ATC's own calls |

A model can still pick the wrong tool. When it does, the tool refuses rather than issue something the data does not support, and the cost is a retry or an "unable", not a wrong clearance. When no tool fits, ATC says "unable, I have not completed that training".

## The data

- **The FAA's published data**, updated every 28-day cycle: procedures (SIDs, STARs, approaches), fixes and airways, facility frequencies and hours, airspace boundaries, minimum vectoring and minimum IFR altitudes.
- **Your X-Plane**, asked when needed: taxiways, stands and runway use. The weather and traffic around you are sent continuously. See [Your X-Plane's data](client/xplane-data.md).

## One session per flight

Each flight gets its own isolated session in the cloud, which keeps the flight's state: your clearance, where you are in the flight, what you still owe a readback for. It survives a reconnect (a transmission lost in a dropped connection is sent again once), and it stops when the flight ends.

## Why it takes a moment to answer

Each reply involves speech recognition, two or three model calls (a router for every call, a judge for a readback, the controller agent for a request), and speech synthesis. Expect a few seconds from releasing push-to-talk to the first word. The log's **Timing** line shows each step.
