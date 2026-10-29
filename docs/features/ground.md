# Ground

Ground moves you between your parking and the runway, on the taxiways of your own X-Plane scenery.

## Before you taxi

**Pushback.** Ask for it and Ground approves it, with the direction your tail points: "push back approved, tail south". No readback is needed. If you are IFR and have no clearance yet, Ground sends you for it first ("clearance on one two seven point eight"), or gives it itself where there is no Clearance Delivery: see [Clearance Delivery](clearance.md#where-there-is-no-clearance-delivery).

**Where you are.** Ground starts your taxi from where X-Plane says your aircraft is, so a "ready to taxi" call in any words is enough. You can say your position by its name in your scenery ("at alpha eleven", "at the FBO"); if the place you name is far from where your aircraft is, Ground checks: "verify at gate bravo twelve?"

## Taxi to the runway

> "November five four seven Golf Alpha, runway one six left, taxi via Bravo, hold short of runway one six center."

- The route follows your scenery's real taxiways and names.
- The taxi instruction ends at the first runway on the way: a hold short of the runway to cross, or of your departure runway. Each later crossing is its own clearance. A hold short for a crossing must be read back; a plain hold short of your departure runway is said, and a wrong runway is still corrected.
- If you did not report the ATIS, Ground gives you the wind and the altimeter.
- If X-Plane gives ATC no ground layout for your **departure** airport, the flight ends at the start and the window says why: see [Troubleshooting](../troubleshooting.md#flight-ended-no-ground-data-from-x-plane-for-the-departure-airport). At your destination (or a diversion airport) with no taxiway data, Ground says "taxi to parking at your own discretion". While the airport's layout is still being fetched from your X-Plane, Ground says "stand by" and calls back.

**Runway crossings** are cleared one runway at a time, once the runway is clear: "cross runway one six left at Charlie, hold short of runway one six center". Ground clears each one as you come up to the hold line, without being asked, and you do not need to stop first. While the runway is busy you hear "continue holding short of runway one six center, traffic". A second crossing waits until you have crossed the first, and one asked for from far back is held until you are close.

## Requests while you taxi

| You ask for | What happens |
|---|---|
| Another runway | A new route to it |
| A route "via Alpha" | The route goes that way when it can |
| An intersection departure | Approved, with the runway distance left |
| Full length | A route to the full-length hold line |
| Progressive taxi | Ground calls each turn as you come up to it, across the crossings, to the hold line or your parking |

## Ground calls you

- **A readback you owe**: about 30 seconds after ATC stops talking, "read back hold instructions".
- **Traffic**: "hold position, traffic" and the aircraft, "hold for traffic", "follow the Boeing", and "continue taxiing" once the traffic has passed.
- **Off your route**: "you are off your cleared taxi route", with a new route from where you are.
- **Moving without a clearance**: "hold position" ("hold in position" if you are on a runway).
- **A runway change** forced by the wind: a new route and the new ATIS letter.
- **At the runway**: "contact Tower" or "monitor Tower".

## Taxi-in after landing

After Tower sends you to Ground, say where you are parking: a gate, an FBO by name, or "general aviation".

- Name nothing and Ground asks **"say parking"** once per taxi-in. If you still name nothing, or name something it cannot find, it taxis you to a general parking and says which. In an emergency it does not ask. The window's [Parking card](../client/parking.md) lists the stands you can say, and comes up on its own when you land and when you switch to Ground.
- A parking Ground cannot find: "unable to find the <what you said>, taxi to ..." with a general parking, named.
- A gate that another aircraft is on: you are held on a taxiway until it is free.
