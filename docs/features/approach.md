# Approach

Approach brings you from the arrival to the final approach course and clears you for the approach.

## Check-in: what to expect

On your first call, Approach gives you the altimeter, your descent, and the approach to expect:

> "November five four seven Golf Alpha, Portland Approach, radar contact, Portland altimeter three zero zero two, descend and maintain four thousand, expect ILS runway one zero right."

Approach also checks, once, that you have the destination's current ATIS where it has one you can tune: "verify you have information Kilo" if you gave no letter, "information Kilo is current, altimeter three zero zero two" if you gave an old one.

## Which approach

Approach picks from what the airport publishes for the runway in use: the ILS first, then RNAV (GPS), then a localizer approach. At most airports, in good weather (ceiling 3,000 ft or more and visibility 5 miles or more), it is a visual approach. At a busy airport such as Seattle, the instrument approach stays the plan in good weather: the check-in says "expect the ILS runway one six center", Approach asks once, within 15 nm, "field is at your two o'clock, one two miles, report field in sight", and you get the visual approach when you report the field or the runway in sight. An approach you ask for by name is never replaced.

**You can ask** for the one you want: "request the RNAV runway one zero right", "request vectors for the ILS". You can also ask for another runway and be vectored for it.

## Vectors to final

Approach vectors you on a downwind, a base and an intercept heading, as a real controller does for a vectored ILS. You do not need to ask for the next turn: ATC calls each one.

- **The first vector says why you are being vectored**: "turn left heading two eight zero, descend and maintain four thousand, vectors for the ILS runway one zero right". ATC does not announce the pattern it plans: the [Approach card](../client/approach-card.md) draws it.
- Altitudes step down as the minimum altitudes allow.
- Every heading allows for the wind.
- Where vectors are not the plan (so far Teterboro, and some RNAV approaches and STARs that end at an initial approach fix), Approach gives you a direct to a fix instead: "after Solberg proceed direct Skuby, descend and maintain three thousand, expect the ILS runway one niner approach", then, before the fix, "maintain three thousand until Skuby, cleared straight-in ILS runway one niner approach". You can ask "request direct Skuby" for a fix of the approach: you get the direct, or one plain reason. Say "unable" and Approach gives you vectors at once, with "cancel approach clearance" first if you were cleared.
- Coming off a STAR: "depart Battle Ground heading one one zero, descend and maintain five thousand, vectors for the ILS runway one zero right". A STAR that ends on the approach's own fix is cleared at that fix, at least 3 nm before it: "at Shafr, cleared ILS runway two eight right approach".

The window shows this as it happens: the [Approach card](../client/approach-card.md) draws ATC's plan with your aircraft on it, and the top line of the window says **ATC is vectoring you**.

## The approach clearance

The last turn comes with the clearance:

> "November five four seven Golf Alpha, turn left heading two five five, maintain three thousand until established, cleared ILS runway one zero right approach."

Read back the heading, the altitude and the approach with its runway. The altitude and the approach are required; a wrong heading is still corrected. The intercept is 30 degrees or less, at or below the glideslope. At a busy airport a jet is asked to keep 170 knots to the final approach fix.

Approach then hands you to [Tower](tower.md) before the final approach fix.

## Visual approaches

> "November five four seven Golf Alpha, field is at your two o'clock, one two miles, report field in sight."

Report the field in sight and you are cleared for the visual approach. If you have not reported it by about 10 nm, Approach gives you the ILS instead. When you report traffic in sight, it may be "number two, follow the Boeing seven thirty seven on a five mile final, cleared visual approach runway one zero right"; when you have not, Approach tells you where you stand: "number two, following a Boeing seven thirty seven on a five mile final". Behind a heavy or a super it adds "caution wake turbulence". Number one says nothing.

## Sequencing and the missed approach

- **Behind other traffic** on final, Approach slows you ("reduce speed to one eight zero"), extends your downwind, or holds you.
- **After a go-around**, Approach gives you a heading, an altitude and vectors for another approach. You can ask to divert instead.
- **Parking.** At an airport with a large number of airline gates (Seattle, for one) Approach may ask you to "say parking", once, on the check-in or with the approach clearance. The window's [Parking card](../client/parking.md) shows what you can say.
- **Cancel IFR** near the field: "IFR cancellation received, contact Portland Tower".

## Arriving at a field with no control tower

There is no plan and no runway until you name an approach. The check-in gives a descent to the lowest usable altitude and ends "advise you have weather and NOTAMs at the field and advise approach requested". The clearance ends "change to advisory frequency approved, cancel with me, this frequency or on the ground", with nothing to read back, and there is no handoff to Tower. If the approach you ask for is not available, Approach says what is: "unable ILS runway two seven, RNAV runway two seven available, advise approach requested".
