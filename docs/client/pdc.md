# Pre-departure clearance by text

At a busy airport, airline crews often get their IFR clearance as text instead of copying it by voice. You can do the same.

## How to use it

1. Start your flight. Once ATC is connected, a **Request PDC** chip shows above the card slot.
2. Press it. The clearance arrives as the **PDC** card and in the log:

    ```text
    N547GA CLRD TO KPDX VIA SUMMA2 THEN AS FILED. MAINT 5000, EXP 16000 10 MIN AFT DEP.
    DEP FREQ 119.2. SQUAWK 4521. ATIS K.
    ```

3. Set the squawk and note the departure frequency. There is **no voice readback**.
4. When you are ready to taxi, call Ground with the ATIS. You do not need to say "with the PDC".

## If you cannot get one

The card says why, and you call for your clearance by voice (or by phone) instead. Where the airport has no Clearance Delivery, the card names the position that gives it, Ground or Tower. Reasons include: the airport has no control tower (there is never a PDC there), you were already cleared by voice, you are airborne, your flight has no cruise altitude, or a voice amendment is waiting for your readback.

## Good to know

- The card is titled "PDC" and the station, such as "PDC · Seattle Clearance", and says "No readback needed. Call Ground with the ATIS when ready to taxi."
- Press **Request PDC** again and the clearance is repeated as it now stands, for example after an amendment.
- **Close** takes the card out of the slot. The clearance stays in the log.
- **New flight** clears it.
- The chip shows only while a PDC is possible: ATC connected, and no PDC answer already showing.
