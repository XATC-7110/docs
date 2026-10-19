# Clearance Delivery

Your first call of an IFR flight.

## The IFR clearance

Call with your callsign, your destination and the ATIS letter. Clearance Delivery reads the clearance in the usual order:

- the **clearance limit** (your destination),
- the **route**: a SID or radar vectors, "then as filed",
- the **altitude**: the initial altitude and the one to expect,
- the **departure frequency**,
- the **squawk**, different for each flight.

> "November five four seven Golf Alpha, cleared to Portland International airport via the Summa Two departure, then as filed, climb and maintain five thousand, expect one six thousand ten minutes after departure, departure frequency one one niner point two, squawk four five two one."

With a SID that has altitude restrictions, the altitude part may instead be "climb via SID", with the expect clause kept. Ask for a SID by name, or for radar vectors ("via radar vectors, Seattle, then as filed"). A SID that does not serve your runway gets "unable, the Summa Two departure is not available from runway one six left".
Read all of it back. A correct readback gets "readback correct"; a wrong item is [corrected](readbacks.md).

| You say | What happens |
|---|---|
| "Say again the clearance" | It is repeated word for word |
| You filed no cruise altitude | ATC asks "say requested altitude" before it clears you |
| You filed only your destination as the route ("clearance to Easton") | The same as no route: ATC clears you via radar vectors. A destination name at the end of a route is dropped ("PLOOP Easton" is cleared via PLOOP) |
| You filed a SID that serves the runway in use | You are cleared on it |
| Your filed route cannot be flown as it is | A full route clearance, instead of "then as filed" |

## Where there is no Clearance Delivery

At an airport with a Ground frequency but no Clearance Delivery, Ground gives your IFR clearance, in Ground's name, with the same readback. Ask for pushback or taxi first and you get the clearance first; the taxi comes on your next call after you read it back. Where there is only a Tower, the Tower gives it. Call Tower at an airport that has a Ground and no Clearance Delivery and Tower tells you where the clearance is: "clearance on one two one point seven". Where Clearance Delivery exists, Ground sends you there the same way.

## Amendments

When something changes before you depart, Clearance Delivery amends the clearance and says only the items that changed: a new SID, altitude or squawk. Read those back.

## A clearance by text (PDC)

Instead of copying the clearance by voice, press **Request PDC** in the window. The clearance arrives as text and needs no readback. See [Pre-departure clearance by text](../client/pdc.md). There is no PDC at an airport with no control tower.

## By phone, at a field with no radio way

At an airport with no control tower and no radio way to reach Clearance Delivery (no clearance delivery frequency and no ground communication outlet), the **Frequencies** card has a **Clearance Delivery · by phone** row instead of a frequency. You get your clearance by calling.

1. Press **Call**. A call screen opens, already calling, with the facility's name like a saved contact. There is no number to dial.
2. You hear a phone ring, made by the client, from the dial until ATC answers. A normal facility rings once; a busier one, such as the approach control of a busy airport, rings once or twice. ATC answers in the pause after a ring, never in the middle of one, and never after a third ring. If nobody has answered 14 seconds after the dial, the call ends and the log says so.
3. ATC answers with the facility's name: "Seattle Approach." Ask for your clearance as you would on the radio. The facility is the approach control over the airport, or the Center where no approach control is. It is never Flight Service.
4. Read the clearance back. A correct readback gets "readback correct, have a safe flight", and the call ends. (When the clearance holds for release, see below.)

To talk, hold **Hold to talk** on the call screen or your yoke's push-to-talk button. While a call is open, every press talks on the call, not on a radio. ATC is heard whatever COM1 and COM2 are tuned to, with a telephone's sound. **Mute** stops your side, the keypad is only for looks, and the red button hangs up. (An experimental way to call with no button, offered only on some accounts, is in [Settings](../settings.md#phone-calls).)

- **On the ground only.** In the air the row says "No phone in flight: use the departure frequency".
- **The row tells you where the clearance stands**: "Clearance issued · not read back yet", "Clearance received", then **Call back** or **Call again**. If nobody answers, the log says "nobody answered: call again": call again.
- **No text clearance** at these fields: ATC does not offer a [PDC](../client/pdc.md) there.

### Hold for release

At an airport with no control tower the clearance ends "hold for release, call back when you are number one for departure". This holds at every such airport, whether you reach Clearance by phone or on a radio frequency or ground outlet (then you call back on the radio). Read it back; the call ends with "readback correct, call back when you are number one". The row then reads **Hold for release**.

When you are number one, press **Call for release** and tell ATC, with the runway: "number one for departure, runway one six". The release comes on that call, not on the readback of the clearance, and a promise to call does not count as the call. If you do not name your runway, ATC asks "say departure runway". It says when the clearance is void:

> "November five four seven Golf Alpha, released for departure, clearance void if not off by one seven four three, ... upon entering controlled airspace, proceed direct Helns."

Read it back, with the void time (leave it out and ATC asks once, "read back clearance void time"). The row shows **Released for departure · void at 17:43Z**. The void time is three minutes after the release. If you are not off by then, the row says **Release ran out · call back for a new one**.

## One frequency, one controller

At many smaller towered airports, one controller works Clearance Delivery and Ground on the same frequency. There the clearance and the taxi come from the same voice, and you are never told to "contact Ground" on the frequency you are already on. Read back your clearance and add "ready to taxi", and you get "readback correct" and your taxi instructions in one reply.
