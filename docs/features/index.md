# What ATC can do

SeventyOneTen staffs every position of an IFR flight. Each controller is on its real frequency, hands you to the next one at the right place, and uses the phraseology of the FAA's controller handbook (JO 7110.65).

| Position | What it does for you |
|---|---|
| [Clearance Delivery](clearance.md) | Your IFR clearance (from Ground or Tower where an airport has no Clearance Delivery), amendments, a pre-departure clearance by text, and a clearance by phone where there is no radio way |
| [Ground](ground.md) | Pushback, taxi to the runway, runway crossings, progressive taxi, taxi-in to your parking |
| [Tower](tower.md) | Line up and wait, takeoff and landing clearances, go-arounds, the runway exit |
| [Departure and Center](departure-center.md) | Radar contact, climbs, turns on course, direct routings, descents, holds, diversions, and cancelling IFR (by phone after landing at a field without a tower) |
| [Approach](approach.md) | The approach to expect, vectors to final (or a direct to a fix at some airports), ILS, RNAV and visual approach clearances |

And at every position:

- [Readbacks](readbacks.md) are checked, and reminded when you forget one.
- [ATIS and weather](atis-weather.md) come from the weather in your X-Plane.
- [Common requests](everywhere.md) work everywhere: say again, radio checks, questions, emergencies.

## The rules it plays by

**IFR only, for now.** VFR departures, pattern work and flight following are not built yet.

**Any US airport.** Positions, frequencies, procedures, airspace and minimum altitudes come from the FAA's published data. Taxiways and parking stands come from [your own X-Plane scenery](../client/xplane-data.md). Outside the US, ATC asks your X-Plane for the airport's procedures and frequencies too.

**Nobody on a frequency, no reply.** Tune a frequency no controller uses and you hear nothing. Tune an ATIS frequency and you hear the broadcast.

**It will not make things up.** Every clearance is checked against the airport's data and your flight before it is spoken. When you ask for something ATC has not been taught, the answer is fixed:

> "November five four seven Golf Alpha, unable, I have not completed that training."

When the answer is no, ATC says why: "unable, runway one niner not available", "continue holding short, traffic".

**ATC calls you first** when a real controller would: handoffs, a readback you owe, traffic, drifting off your altitude or your taxi route, a go-around.

**One reply per call.** Ask for two things in one transmission and you get one reply that covers both.

**Silent while paused.** While X-Plane is paused or in a replay, ATC says nothing and does not hear you.

**Your radio has to be on.** You hear a controller only on a radio that is tuned to the frequency, switched on and selected to listen on your audio panel.

## Not built yet

- VFR: departures, pattern work, flight following.
- A sidestep to a parallel runway (for now: a go-around).
- Block altitudes and other less common requests. ATC answers "unable, I have not completed that training".
- Full emergency handling: vectors to the nearest airport, lost-communication routings. The [first steps](everywhere.md#emergencies) are there.
