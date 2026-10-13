# Your first flight

An IFR flight from Seattle to Portland, gate to gate. The frequencies and names are examples: the window's **Frequencies** card lists the real ones for your flight.

## Before you call anyone

1. **Start X-Plane 12** and put your aircraft on a stand at the departure airport.
2. **Start the client** and wait for the startup dialog to close (signed in, gateway ready).
3. Press **New flight**.
    - **Enter manually**: callsign, aircraft type, departure, destination, cruise altitude and route. The dialog remembers your last plan.
    - **From SimBrief**: enter your SimBrief username or pilot ID and press **Load**. It fills in your latest flight plan and tells you which one it loaded and how old it is. No password or key is needed.
4. Press **Start flight**. The dialog says **Starting new flight…** and closes when ATC is ready.

!!! tip "The first flight after installing takes longer"
    The first time, the client reads the headers of your X-Plane scenery once, so it can answer ATC's questions about taxiways and parking. The dialog shows a progress bar. On a slow disk this can take a minute or more. After that, only new or updated scenery is read.

## How to talk

- **Push-to-talk**: hold the big button in the window, hold **Space** while the window has focus, or use a yoke or joystick button ([Settings](settings.md#push-to-talk)).
- You transmit on the COM radio selected on your aircraft's audio panel, on its active frequency. The push-to-talk button names who is listening there.
- Say **who you are calling, your callsign, and what you want**, as on a real radio. Read back clearances and instructions.
- You hear ATC only if COM1 or COM2 is tuned to the frequency ATC transmits on.
- While X-Plane is **paused**, ATC is silent and does not hear you.

## Gate to gate

### 1. ATIS

Tune the ATIS frequency on either radio. The recording loops, starting mid-broadcast like the real thing. Note the information letter and the altimeter.

### 2. Clearance Delivery

> **You:** Seattle Clearance, November five four seven Golf Alpha, IFR to Portland with information Charlie.
>
> **ATC:** November five four seven Golf Alpha, cleared to Portland via the Summa Two departure, then as filed. Maintain five thousand, expect one six thousand one zero minutes after departure. Departure frequency one one niner point two, squawk four five two one.
>
> **You:** Cleared to Portland, Summa Two then as filed, five thousand expect one six thousand, one one niner point two, squawk four five two one, five four seven Golf Alpha.
>
> **ATC:** November five four seven Golf Alpha, readback correct.

Prefer not to copy a clearance by voice? [Request a PDC](client/pdc.md) and it arrives as text.

### 3. Ground

> **You:** Seattle Ground, November five four seven Golf Alpha, at alpha eleven, ready to taxi with Charlie.

Ground gives you a route along your scenery's real taxiways, with a hold short for each runway on the way. Read back the runway and every hold short. Ask for a pushback first if you need one. If you get lost, say **"request progressive taxi"** and Ground calls each turn as you come up to it.

### 4. Tower

At the hold line, the window shows **Next: Seattle Tower** with buttons that put the frequency in a radio's standby. Call ready. Tower may line you up and wait, hold you for traffic or wake turbulence, or clear you for takeoff with the wind and your initial heading or RNAV fix.

### 5. Departure and Center

About 1,000 ft above the ground, Tower hands you to Departure. Check in with your altitude:

> **You:** Seattle Departure, November five four seven Golf Alpha, one thousand two hundred climbing five thousand.

Departure says "radar contact", climbs you and turns you on course. Center takes over on the way up and, later, starts your descent: "descend via the Helns Six arrival", or a crossing restriction. Along the way you can ask for another altitude, direct to a fix on your route, or a deviation around weather.

### 6. Approach

Approach tells you which approach to expect and vectors you to final. The first vector says why: "..., vectors for the ILS runway one zero right". ATC does not say the pattern it plans: the window's [Approach card](client/approach-card.md) draws it, and the top line of the window confirms that ATC is vectoring you.

> **ATC:** November five four seven Golf Alpha, turn left heading one three zero, maintain three thousand until established, cleared ILS runway one zero right approach.

Read back the heading, the altitude and the approach with its runway. Approach then hands you to Tower.

### 7. Tower, landing and taxi-in

Tower clears you to land with the wind. Read back "cleared to land" with the runway. On the rollout Tower tells you where to turn off, then hands you to Ground. Tell Ground where you are parking: a gate, an FBO, or "general aviation". If ATC asks **"say parking"**, the window's [Parking card](client/parking.md) lists the names you can say and shows them on a map.

### 8. The end of the flight

Park at your stand and shut down the engines. The flight ends by itself within about a minute. You can also press **End flight**, and closing X-Plane ends the flight after 30 seconds.

## If something goes wrong

- **Silence after you transmit?** The log's **No reply** line says why. See [Troubleshooting](troubleshooting.md).
- **Missed what ATC said?** Say "say again". The words are also in the log.
- **Closed the client mid-flight by accident?** Start it again within about ten minutes and choose **Rejoin last flight**.
