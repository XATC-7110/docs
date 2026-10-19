# Departure and Center

The radar controllers: Departure takes you from the runway into the climb, Center takes you to cruise and back down, and each hands you to the next at the edge of its airspace.

## Departure

**Check in** with your altitude. Departure answers "radar contact" with the altimeter and your climb:

> "November five four seven Golf Alpha, Seattle Departure, radar contact, Seattle altimeter three zero zero two, climb and maintain one five thousand."

Departure climbs you to your filed cruise, up to the top of its own airspace, and Center gives the rest. If your transponder is not on the squawk you were given: "radar contact, reset transponder, squawk zero one seven four", and once more 30 seconds later if it is still wrong.

On a SID with altitude restrictions it is "climb via the Summa Two departure", sometimes "except maintain" an altitude.

**On course.** After a heading off the runway, Departure turns you toward your route: "turn left heading two niner zero, vectors to Mapel", then "proceed direct Mapel" on its own. A SID that ends on a heading is followed by "proceed direct" its next fix. You can also ask: "request on course".

**A route with no fix in it.** If your route has no fix ATC knows (none filed, or just your destination's name), the destination stands in for it. Departure says "proceed direct Easton" when it is ahead of you, or "turn left heading one three zero, vectors to Easton" and then "proceed direct Easton" once you have come round. "Request direct Easton" is granted. It is not used within 5 nm of the destination. At a field with no tower the release still says "fly runway heading", and Departure's radar contact adds the direct or the turn.

**Still on the wrong frequency?** If you call Tower when you should be with Departure: "you're on Seattle Tower, contact Seattle Departure". If you stay on the old frequency, the old controller says "are you with me? contact Seattle Departure one one niner point two", and if you switch but never check in, the new one asks "how do you hear?" The same happens at every handoff.

## Center

The handoff to Center comes on its own: climbing through a thousand feet below the top of Departure's airspace when your cruise is at or above that top, otherwise at the edge of its airspace, sideways, to whoever owns the airspace there (on a short flight, to the destination's Approach). Check in and Center clears you to your cruise altitude, in steps around traffic if it has to.

## What you can ask for

| You ask for | What you get |
|---|---|
| Higher or lower | Your altitude, or "unable" with the reason. With no altitude named: "say requested altitude" |
| Direct to a fix | "proceed direct Helns", for a fix ahead on your route |
| A heading or a speed | Approved when it is safe |
| A deviation around weather | "deviation twenty degrees left approved, advise when able to proceed direct Helns" |
| A hold | "hold west of Battle Ground as published, expect further clearance two one three five" |
| A diversion | "cleared to the Olympia airport via direct, maintain ..." |
| To return to your departure airport | Radar vectors back, and what to expect |
| To cancel IFR | "IFR cancellation received, squawk VFR, frequency change approved". Not in Class A airspace: "unable, IFR cannot be cancelled in Class Alpha airspace". Near a towered destination it ends "contact Portland Tower" and the frequency; inbound to a field with no tower, "change to advisory frequency approved". Words that do not say what is cancelled get "confirm cancelling IFR?" |

Cancelling IFR in the air is on the radio, as above. After you land at an airport with no control tower, you cancel on the ground: see [Cancelling IFR after landing](#cancelling-ifr-after-landing).

ATC never clears you below the minimum altitude for where you are. The FAA's minimum vectoring and minimum IFR altitude charts for the whole US are in its data.

## The descent

At the top of descent Center starts you down without being asked:

> "November five four seven Golf Alpha, descend via the Helns Six arrival, Portland altimeter three zero zero two."

or a crossing restriction: "cross Battle Ground at and maintain one one thousand". Asking "request lower" or "request descend via" starts the same descent.

The top of descent allows for speed, so a descent that starts early at high speed is normal. Center then hands you to the next sector, and finally to [Approach](approach.md): at the first of these, once you are inside the destination's approach airspace, 40 nm from the field, or within 2 nm of the arrival's last fix.

## Cancelling IFR after landing

At an airport with a control tower, your IFR flight plan closes when you land. At one without, you cancel it yourself. Once you have landed at your destination:

- **With no radio way to Clearance Delivery** (no clearance delivery frequency, no ground communication outlet), the **Frequencies** card shows **Cancel IFR · by phone** under that airport, with **Call to cancel** and the text "IFR flight plan open · call to cancel". Press it, say "cancel IFR" when ATC answers with the facility's name, and ATC says "IFR cancellation received". The row then reads **IFR cancelled**. The call works like the [clearance call](clearance.md#by-phone-at-a-field-with-no-radio-way).
- **With a radio way**, there is no phone row: cancel on that frequency.
- **If you already cancelled in the air**, there is nothing left to cancel and no row.

ATC ends the flight about 30 seconds after the engines are off, call or no call. If that cuts the call before the cancellation is in, the log says the flight ended before it was confirmed. Call before you shut down.

## The radar controller calls you

- **Altitude**: 300 ft off your assigned altitude and not correcting, "verify altitude".
- **Course**: "verify on course", "verify you are proceeding direct Helns", or a heading back to your route.
- **A missed restriction** on a SID or STAR: "verify you are descending via the Helns Six arrival".
- **Low altitude alert**: "low altitude alert, check your altitude immediately, the minimum altitude in your area is ...".
- **Traffic**: converging aircraft are called in the climb and en route, once each, with the clock position, distance, direction and altitude. A climb held for traffic is answered "unable higher, traffic".
- **Speed**: above 250 knots below 10,000 ft, "reduce speed to two five zero knots".
- **A readback you owe** for an altitude, a crossing or a procedure, about 30 seconds after ATC stops talking.
