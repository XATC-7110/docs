# Your plan in X-Plane's avionics

When you start a flight, SeventyOneTen writes your flight plan as a file X-Plane can read, so you can load it into the GNS 530, the G1000 or the FMS without typing the route again.

## Where it goes

The file is `SeventyOneTen.fms`, in the `Output/FMS plans` folder of your X-Plane folder. The client creates the folder if it is missing.

- It is written each time you press **Start flight**, whether you typed the plan in or loaded it from SimBrief.
- The name never changes. Each new flight **replaces** the file, so it always holds your current plan and nothing piles up in X-Plane's list. If you want to keep a plan, save your own copy under another name.
- ATC changing your route during the flight does not rewrite it.
- It is always on. There is no setting to turn it off.

## Loading it

Load it from the aircraft's own GPS, G1000 or FMS, in the cockpit. If the plan does not appear, reopen the flight plan list, or restart X-Plane.

## What is in it

The file holds your departure and destination airports, your cruise altitude and the route: every fix along each airway, in order. The fixes and their positions come from your own X-Plane's navigation data, so the file matches what your avionics load.

**Runways, SIDs, STARs and approaches are not in the file.** Choose them in the avionics. A SID or STAR you named in the route is left out too, and the log says so; a plain fix in the route is kept.

## When something is left out

- **A fix X-Plane does not know.** If a fix in your route is not in your X-Plane's navigation data, it is left out of the file, and the log says which one, for example "ZZYZX is not in your X-Plane navdata, so it is left out." The client never guesses a position.
- **A very long route.** X-Plane's flight plans hold at most 100 waypoints. On a long route the client leaves out some of the fixes along an airway, and the airway still carries the route. If it is still too long, no file is written and the log says why.
- **An airport your X-Plane does not have.** The plan starts or ends at the first or last fix X-Plane does know, and the log says so.
- **No X-Plane folder found.** No file is written, and the log says so (set the folder in **Settings > X-Plane data**). **Your flight starts anyway.**

The log is the one at the bottom of the window, and the line "Your flight plan is in X-Plane as SeventyOneTen.fms" tells you the file was written.

!!! note "Not checked yet"
    Whether the G1000 picks up an updated `SeventyOneTen.fms` without restarting X-Plane has not been checked. If it shows an old plan, reopen the flight plan list, or restart X-Plane.
