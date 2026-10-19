# At every position

Things you can say to any controller, and things any controller may say to you.

## Common requests

| You say | You get |
|---|---|
| "Say again" | The last transmission again |
| "Radio check" | "November five four seven Golf Alpha, Seattle Ground, read you five" |
| A question | The answer, for: the wind, the weather, the altimeter, the runway to expect, the ATIS, your position, your assigned heading, altitude or squawk, any facility's frequency, the time, a distance, traffic |
| "Thanks for the help", "good day" | One short reply, or a "good day" after a handoff |

A remark that needs no answer gets none.

## A call you could not hear

Silence is not the end of it. If ATC called you while your radio was off, not selected to listen, or not tuned to the frequency, ATC says its latest call on that frequency again, once, when a radio can hear it again within about a minute, as long as you have not transmitted to that position since. A call lost in a dropped connection is sent again once after the reconnect. The log says "not played" for the call you missed. An ATIS or weather broadcast is not repeated: it loops.

## Frequency changes

> "November five four seven Golf Alpha, contact Seattle Ground one two one point seven."

Reading it back is optional. The window shows **Next: Seattle Ground 121.700** with buttons to put it in a radio's standby.

## Squawk and altimeter

Any controller may give you a squawk, "squawk and ident", "ident", or the local altimeter.

## Traffic and safety alerts

- **Traffic advisories**: "traffic, two o'clock, five miles, southbound, Boeing seven thirty seven, altitude indicates one thousand feet above you". The traffic is the other aircraft in your X-Plane.
- **Safety alerts**: a low altitude alert, or a traffic alert with a suggested escape.
- **A TCAS resolution advisory**: tell ATC, and it answers "roger" and issues nothing until you report "clear of conflict".

## Emergencies

The first steps are built:

- **"Mayday", "Pan-Pan" or squawking 7700**: "roger, say fuel remaining and souls on board", and you get priority.
- **Lost communications (7600)**, or no answer after "are you with me?": "if you hear this transmission, ident". After a handoff, if you are still on the old frequency a minute later, the old controller says "are you with me? contact Seattle Departure one one niner point two". If you are on the new frequency and silent, the new controller says "how do you hear?", and 30 seconds later "if you hear this transmission, ident".

Vectors to the nearest airport and lost-communication routings are not built yet.

## Pilot deviations

When you do something a real controller would report, such as landing or taking off without a clearance, or entering the departure runway without one, ATC tells you on the radio and the window shows a red **Pilot deviation** alert until you dismiss it. It is there so you notice, and so the flight can be reviewed afterwards. Nobody will ask you to copy a phone number.

## When the flight ends

ATC ends the flight by itself when:

- you are parked at your destination stand (stopped within about 60 m of it, with the brake set or the engines off) for a minute, or you have flown and then sit with every engine off for 30 seconds,
- the aircraft crashed,
- X-Plane has been closed for 30 seconds,
- or you press **End flight**.

After that nothing reconnects until you press **New flight**.

## What ATC says when it cannot

- **Not possible**: "unable", with the reason.
- **Not taught yet**: "unable, I have not completed that training". Each of these is logged, so the gaps get filled in the order pilots hit them.
