# Your X-Plane's data

ATC uses the FAA's published data for everything in the air over the US: procedures, fixes, airways, frequencies, tower hours, airspace and minimum altitudes. On the ground, it uses **your** X-Plane, so that the taxiways and stands ATC names are the ones you see.

## ATC asks, the client answers

Nothing is uploaded in advance. When ATC needs something only your X-Plane has, it asks, and the client answers over the flight's connection:

| What | When | From |
|---|---|---|
| **The airport's ground layout**: taxiways with their names, hold lines, stands, runways as drawn, runway-use rules | The departure airport at the start, the destination when you are inbound | The scenery pack that wins in your X-Plane, in `scenery_packs.ini` order |
| **Parking stands** | When the Parking card comes up | The same scenery |
| **Outside the US only**: the airport's runways, frequencies and procedures, the fixes and airways along your route | At the start of the flight | Your X-Plane's navigation data. It is assumed to be current |

It is done safely. ATC can ask only for these kinds of data, for an airport identifier that is checked first, and for a few weather values that X-Plane itself reports, read-only. It can never name a file to read, and it can never write or command anything. (The client itself writes in your X-Plane folder in two places only, listed in [Your data](../privacy.md#what-stays-on-your-pc).) The log says what was read: "ATC read KBFI's ground layout from your X-Plane".

If X-Plane gives ATC no ground layout for your **departure** airport, the flight ends at the start, and the window says why (see [Troubleshooting](../troubleshooting.md#flight-ended-no-ground-data-from-x-plane-for-the-departure-airport)). If your scenery has no taxiway data for your destination or a diversion airport, Ground says "taxi to parking at your own discretion". While an answer is still on its way, Ground says "stand by" and calls back.

### The scenery index, once

The first flight after installing reads the header of every airport file in your scenery, once, before it connects to ATC. The New flight dialog shows "Preparing the scenery index (one time)…" with a progress bar. On a slow disk this takes a minute or more. Afterwards only new or changed scenery is read.

## What the client sends during a flight

About once a second, and at once when you change a radio:

- your aircraft's position, altitude, speed, heading and whether it is on the ground,
- your radios: frequencies, which one you transmit on, and whether each is on and selected to listen,
- your transponder code,
- the weather at the aircraft (sampled about every five seconds and sent with the once-a-second state),
- X-Plane's clock, so that ATC judges things like tower opening hours by the sim's time,
- the other aircraft X-Plane knows about (its AI traffic, SeventyOneTen's own [AI traffic](../traffic.md) when you turned it on, and aircraft a multiplayer plugin adds): the nearest 32.

See [Your data](../privacy.md) for the whole picture.

## FAA procedures for your X-Plane

Optional. ATC clears you on the FAA's current procedures. If your X-Plane's navigation data is older, your aircraft's FMS may not have a procedure ATC names. **Settings > X-Plane data** can install the FAA's current procedures into X-Plane, so that the two agree.

- **Check for update** shows the release, its AIRAC cycle and its dates.
- **Install** downloads it, checks every file, backs up anything it replaces, and writes the FAA's procedure file into your X-Plane's `Custom Data` folder.
- **Update** replaces an installed pack with a newer one.
- **Remove** puts your own files back exactly as they were.

You need a flight started to check or install, because the download link comes from ATC. **Restart X-Plane** afterwards: it reads navigation data only when it starts.

!!! warning "It overrides your navigation data for US procedures"
    While the pack is installed, X-Plane uses the FAA's procedures in place of your provider's (Navigraph, for example) for the airports it covers. **Remove** undoes it. Settings warns you when your navigation data is a different AIRAC cycle from the pack: fixes may then not match.

A pack for a cycle that has not started yet can be installed early. Settings marks it **Not valid until** its first day.
