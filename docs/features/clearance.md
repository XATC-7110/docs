# Clearance Delivery

Your first call of an IFR flight.

## The IFR clearance

Call with your callsign, your destination and the ATIS letter. Clearance Delivery reads the clearance in the usual order:

- the **clearance limit** (your destination),
- the **route**: a SID or radar vectors, "then as filed",
- the **altitude**: the initial altitude and the one to expect,
- the **departure frequency**,
- the **squawk**, different for each flight.

> "November five four seven Golf Alpha, cleared to Portland via the Summa Two departure, then as filed. Maintain five thousand, expect one six thousand one zero minutes after departure. Departure frequency one one niner point two, squawk four five two one."

Read all of it back. A correct readback gets "readback correct"; a wrong item is [corrected](readbacks.md).

| You say | What happens |
|---|---|
| "Say again the clearance" | It is repeated word for word |
| You filed no cruise altitude | ATC asks "say requested altitude" before it clears you |
| You filed a SID that serves the runway in use | You are cleared on it |
| Your filed route cannot be flown as it is | A full route clearance, instead of "then as filed" |

## Amendments

When something changes before you depart, Clearance Delivery amends the clearance and says only the items that changed: a new SID, altitude or squawk. Read those back.

## A clearance by text (PDC)

Instead of copying the clearance by voice, press **Request PDC** in the window. The clearance arrives as text and needs no readback. See [Pre-departure clearance by text](../client/pdc.md).

## By phone, at a field with no radio way

At an airport with no control tower and no radio way to reach Clearance Delivery (no clearance delivery frequency and no ground communication outlet), the **Frequencies** card has a **Clearance Delivery · by phone** row instead of a frequency. You get your clearance by calling.

1. Press **Call**. A call screen opens, already calling, with the facility's name like a saved contact. There is no number to dial.
2. You hear a phone ring. A facility that is busier, such as the approach control of a busy airport, may ring twice before it answers.
3. ATC answers with the facility's name: "Seattle Approach." Ask for your clearance as you would on the radio. The facility is the approach control over the airport, or the Center where no approach control is. It is never Flight Service.
4. Read the clearance back. A correct readback gets "readback correct, have a safe flight", and the call ends. (When the clearance holds for release, see below.)

To talk, hold **Hold to talk** on the call screen or your yoke's push-to-talk button. While a call is open, every press talks on the call, not on a radio. ATC is heard whatever COM1 and COM2 are tuned to, with a telephone's sound. **Mute** stops your side, the keypad is only for looks, and the red button hangs up. (An experimental way to call with no button is in [Settings](../settings.md#phone-calls).)

- **On the ground only.** In the air the row says "No phone in flight: use the departure frequency".
- **The row tells you where the clearance stands**: "Clearance issued · not read back yet", "Clearance received", then **Call back** or **Call again**. If nobody answers, the log says "nobody answered: call again": call again.
- **No text clearance** at these fields: ATC does not offer a [PDC](../client/pdc.md) there.

### Hold for release

At a field like this the clearance ends "hold for release, call back when you are number one for departure". Read it back; the call ends with "readback correct, call back when you are number one". The row then reads **Hold for release**.

When you are number one, press **Call for release** and tell ATC, with the runway: "number one for departure, runway one six". The release comes on that call, not on the readback of the clearance, and a promise to call does not count as the call. It says when the clearance is void:

> "November five four seven Golf Alpha, released for departure, clearance void if not off by one seven four three, ... upon entering controlled airspace, proceed direct Helns."

Read it back. The row shows **Released for departure · void at 17:43Z**. The void time is three minutes after the release. If you are not off by then, the row says **Release ran out · call back for a new one**.

## One frequency, one controller

At many smaller towered airports, one controller works Clearance Delivery and Ground on the same frequency. There the clearance and the taxi come from the same voice, and you are never told to "contact Ground" on the frequency you are already on. Read back your clearance and add "ready to taxi", and you get "readback correct" and your taxi instructions in one reply.
