# The window

The client runs in its own window, titled **xatc-agent client**, beside X-Plane. It has two views, **Radio** and **Settings**. This page is a tour of the Radio view, from the top. [Settings](settings.md) has its own page.

## The header

The top bar has two rows.

- **The name and versions.** **xatc-agent**, then the client's version, then X-Plane's version while X-Plane is connected, then the ATC service's version once ATC has welcomed your flight (the window labels that one **Gateway**, and shows **Gateway —** until then).
- **The theme button**, at the top right: **Night** and **Paper**. Its tooltip says which one it switches to.
- **Your flight**: callsign (a tail number, or an airline callsign such as "Walker 1745"), aircraft type, departure → destination, and its state (starting, ready, ended). With no flight it says "No flight: press New flight". When a flight ended, the line says why, and the **New flight** button is highlighted.
- **The approach confirmation**: while ATC has you on an approach, a pill beside your callsign shows the kind of approach (**ILS**, **RNAV**, **Visual**), the runway, and **ATC is vectoring you**. It turns green and says **cleared for the approach** once ATC clears you. See [The approach plan](client/approach-card.md).
- **End flight** (only while a flight runs, with a confirmation) and **New flight**.

Click an airport in the header ("KSEA → KPDX") to open its [details](#airport-details).

## The services row

Three pills show what the client is connected to, beside **Radio** and **Settings**, which switch the view:

| Pill | What it shows |
|---|---|
| **Gateway** | The connection to the ATC service. It reads **Gateway: connected**, **connecting**, **reconnecting**, **needs setup**, **stopped** or **no flight**. Click it for the reason of the last change and **Reconnect**, which reopens the connection on the same flight |
| **X-Plane** | **X-Plane: connected** with its version, or **not connected**. It turns amber and reads **X-Plane: paused** (or **in replay**) while the sim is paused: ATC is silent then and does not hear you. **X-Plane: too old** means it is older than the minimum: see [X-Plane too old](troubleshooting.md#x-plane-too-old) |
| **Sign-in** | **Signed in · your name** (green) with **Sign out**, **Not signed in** (red) with **Sign in**, or **Signed in · offline** (amber) when the sign-in service cannot be reached |

When your sign-in is within 24 hours of running out, a line beside the pills says so, with **Sign in again**. During a flight it asks you to sign in as the same account, or the flight will end.

Under the row, a banner may appear:

- **Lost the connection to the client. Retrying…** when the window loses its own client.
- A setup banner, with **Open Settings**, when ATC needs something set up or has stopped.
- The update banner: see [Updates](settings.md#updates).
- On the Linux AppImage, the offer to [add xatc-agent to your app menu](install-linux.md#add-xatc-agent-to-your-app-menu).

## The radios

**COM1** and **COM2**, active and standby, exactly as X-Plane has them, with the name of the facility on each frequency when ATC knows it ("Seattle Ground").

- **TX** marks the radio selected to transmit on your aircraft's audio panel. It turns red while you transmit.
- **⇄** swaps active and standby, like the flip-flop key on a real radio.
- A radio tuned to an ATIS says so: "KSEA ATIS Charlie · looping". An airport's automated weather station (AWOS or ASOS) says its name, and an airport with no tower says "Monmouth CTAF · no ATC": nobody answers on the advisory frequency.

The client changes X-Plane's radios and nothing else, so the window always shows what X-Plane really has.

**A radio you hear needs to be on.** You hear ATC on a radio only when it is tuned to the frequency, the radio's own switch is on, the avionics are on, and the radio is selected to listen on your aircraft's audio panel. A radio that is off, or not selected to listen, is silent in the window too, and you cannot transmit on it: see [Cannot transmit](troubleshooting.md#cannot-transmit).

## Push-to-talk

The big button, **PUSH TO TALK**. Press and hold to transmit (it reads **TRANSMITTING**), release to stop. Its hint, "Hold, or hold Space", adds the facility you are transmitting to. It works with a mouse or a touch screen, and holding **Space** does the same while the window has focus. If the window loses focus the button releases, so the radio cannot get stuck keyed.

For a button on your yoke or joystick, see [Settings](settings.md#push-to-talk).

## Read back, and Next

Under push-to-talk:

- **Read back**: what ATC is still waiting for you to read back, with how long it has waited. It empties when your readback is accepted.
- **Next**: after a handoff ("contact Portland Approach one two four point three five") it shows **Next: Portland Approach 124.350** with **COM1** and **COM2** buttons. They put the frequency in that radio's standby; then press **⇄**. The line goes once COM1 is on it.

## Last ATC

Who spoke last and what they said, with the verdict on your last readback: **✓ Readback accepted** or **✗ Corrected**. Numbers are shown as you would write them ("119.2"), while the audio says them as a controller does ("one one niner point two"). Under it, a grey line begins "cloud has:" and says what ATC currently knows about your aircraft, for example its stand, whether it is on the ground and the age of the data. It is there so you can see that ATC sees you.

## The card slot

One card at a time, picked with the chips above it. The slot keeps its height, so the log below never jumps.

| Chip | When it shows |
|---|---|
| **Frequencies** | Always available: the ATC stations for your flight |
| **[Approach](client/approach-card.md)** | When ATC starts vectoring you for an approach |
| **[Parking](client/parking.md)** (with the airport, such as "Parking KPDX") | When ATC asks you to say your parking |
| **[PDC](client/pdc.md)** | After you request a pre-departure clearance by text. **Request PDC** is a chip too, while one is possible |
| **⚠ Deviation** | When ATC flags a pilot deviation, such as taking off without a clearance. It stays until you dismiss it, and the chip stays so that you can bring it back |
| **⚠ No data** | **Unable to access data, check connection**: when ATC cannot read its airport data. The client pauses X-Plane; see [Troubleshooting](troubleshooting.md#unable-to-access-data-check-connection) |
| **⚠ Flight refused** | When ATC refuses the flight, for example "This flight belongs to another pilot. Start a new flight." It has **New flight** and **Dismiss** |

An alert takes the front and its chip turns amber. **Hide** folds the slot down to its chips.

### Frequencies

The stations ATC has for your flight, grouped by airport, your departure and destination first. **C1** and **C2** mark what COM1 and COM2 are tuned to, **TX** the one you transmit on, and each ATIS shows its current letter.

Each station has two small buttons, **1** and **2**: they put its frequency into COM1's or COM2's standby. Then press that radio's **⇄**. The list follows the flight: when a clearance or a handoff names another frequency, the card changes with it.

Some rows are special:

- A tower that is not open around the clock says **part-time**.
- An airport with no tower lists its advisory frequency, tagged **advisory · no ATC**. A call on it is logged as "no reply expected: no controller is on the CTAF", not as a fault.
- An airport's weather station is a row of its own, tagged **automated weather**.
- An airport with no tower and no radio way to Clearance Delivery has a **by phone** row with a **Call** button instead of a frequency: see [Clearance by phone](features/clearance.md#by-phone-at-a-field-with-no-radio-way).

### Airport details

Click an airport name in the header, on the Frequencies card or on the Parking card, and a full-window **Airport** dialog opens with the airport's facts (towered, or part-time with the hours), its **Runways** with a diagram, its **Frequencies** with the same **1** and **2** buttons, and its **Procedures**: **Departures**, **Arrivals** and **Approaches**. The footer says where each part came from, and **Not for navigation**.

## The log

Everything that happened, newest at the bottom:

- **You**: what the speech recognition heard, in grey while it is still working. A correct readback gets silence on the radio, so the verdict appears here: a green **✓ Readback accepted** or an amber **✗ Corrected**.
- **▶ transmitting on COM1 121.700**: the frequency you keyed. On a phone call it says "talking on the phone".
- **ATC**: the station, what it said and the frequency. If you were not tuned to it, or its radio was off, the next line says "not played" and why.
- **An ATIS** appears in full, once when you tune it and once for each new letter while you stay tuned.
- **No reply**: why ATC did not answer. See [Troubleshooting](troubleshooting.md#atc-does-not-answer).
- **Timing**: how long each step of the reply took: "transcript … · agent … · first audio … · total … ms".
- **Flight ended**, with the reason.
- **Error**, for something the client refused or could not do, such as "can't transmit: COM1 is off".

Scroll up to read something and the log stays where you left it; scroll back to the bottom and it follows again. **Clear** empties it.

## Dialogs you will meet

- **The startup dialog**, each time the client starts: your sign-in, the **ATC service** and X-Plane. It closes by itself when the first two are ready. After a client restart mid-flight it offers **Rejoin last flight**.
- **New flight**: the flight plan, by hand or from SimBrief. It opens by itself when a flight ends, with a line saying why.
- **The recording question**, the first time you connect: see [Your data](privacy.md#recordings-of-your-voice).
- **The call screen**, when you press **Call** on a phone row: see [Clearance by phone](features/clearance.md#by-phone-at-a-field-with-no-radio-way).
- **The approach diagram** and **the parking map**, full size, with **Bigger**.
- **Airport details**, above.
