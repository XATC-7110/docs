# AI traffic

A flight can have other aircraft in it. SeventyOneTen can fill your X-Plane with AI aircraft that depart, taxi, cross runways, fly approaches and land at the airports on your route that have traffic, and ATC works with them: it sequences you with them as with any other aircraft. You read their calls in the log, and you can choose to hear them. This page says how to turn the traffic on, what to install, what the start dialog shows and what you can hear.

!!! info "A prerelease, for now"
    The traffic setup shown here is in the client's 0.20 prereleases. The stable client, 0.19.0, does not start AI traffic. The traffic plugin it needs is not on the Download page yet: see [What X-Plane needs](#what-x-plane-needs).

## Turn it on

In the **New flight** dialog, **Traffic** chooses how busy the sky is:

| Choice | What it is |
|---|---|
| **None** | The default: no AI aircraft. The flight is as it always was |
| **Light**, **Typical**, **Busy**, **Peak**, **Saturation** | From a quiet field to a rush. The airports along your route decide what flies: airliners only where airliners really fly, more light aircraft and business jets at smaller fields |
| **Absurd** | Tests your PC's limit, not realism |
| **Custom** | You choose **Aircraft an hour** and **Filler aircraft** |

The line under the choice says what it does: "AI aircraft that ATC works around you, their radio calls shown as text in the log."

## What X-Plane needs

The traffic is drawn inside X-Plane by two things you install once:

- **The SeventyOneTen traffic plugin**, which goes in your X-Plane's `Resources/plugins` folder. Restart X-Plane after you add it. The plugin is not on the Download page yet. Until it is, AI traffic is only for testers who have been given the plugin.
- **Bluebell**, a package of aircraft models for X-Plane, which you download yourself. Unpack it into the `Custom Data/xatc-traffic/CSL` folder of your X-Plane, then start a new flight. When Bluebell is missing, the window shows the folder and a **Download Bluebell** link.

The window tells you when something is missing. A line under the header says so in words:

- **Traffic is off: the SeventyOneTen traffic plugin isn't answering in X-Plane.** The plugin is not installed, or X-Plane was not restarted after you installed it.
- **Bluebell CSL not found: traffic is off.** Bluebell is not in the folder above.
- **No traffic on this flight: ATC doesn't offer traffic yet.** ATC is not offering traffic on this flight, so the flight goes on without any.
- **No traffic on this flight: there is no traffic at these airports yet.** The airports of this flight have no traffic yet, so the flight goes on without any.
- Another plugin holds X-Plane's AI aircraft: the line names it. Only one can have them at a time, so the traffic yields, for example when you connect to an online network.
- **Traffic is paused while X-Plane is in a menu. It comes back when X-Plane runs again.** This is not a fault. It appears when X-Plane is paused or on its Flight Configuration screen.

### X-Plane's own parked aircraft

If X-Plane draws its own parked aircraft, they overlap SeventyOneTen's traffic at the gates. The traffic line then says: "X-Plane's parked aircraft are on; turn off “draw parked aircraft at airports” in Settings › Graphics and restart X-Plane, so they don't overlap SeventyOneTen's traffic." X-Plane saves that setting only when it quits, so the warning goes after the restart. It needs the newest traffic plugin: with an older one there is no warning.

## Starting a flight with traffic

When **Traffic** is not **None**, the start dialog stays open after ATC is ready and shows its progress, so you do not look at an empty sky:

1. **Connecting**
2. **Loading airport data**
3. **Building traffic**, with a line such as "Placing 116 aircraft around KSEA"
4. **Traffic visible**

Each step shows its state in words: Done, In progress, Waiting or Skipped. The dialog closes when the aircraft are drawn in X-Plane. It never holds you for good: **Fly now** closes it at any time, and after 60 seconds it says "Traffic is still starting; you can fly now." With **Traffic** set to **None** the dialog closes as soon as ATC is ready.

## What ATC does with the traffic

ATC works the AI aircraft as it works you, with the same rules:

- **Tower** keeps the runway for one aircraft at a time. It cancels an AI takeoff if you enter the runway without a clearance (you are told to "hold in position", then "possible pilot deviation, advise you contact the airport's Tower after landing"; every runway entry without a clearance is recorded as a deviation, except during a declared emergency), clears AI aircraft across runways, and tells you where you stand: you may hear **"expect departure delay"** when the wait for your runway is unusually long (over about ten minutes).
- **Traffic calls** name what matters to you, with the distance: "traffic, Boeing seven thirty seven, two mile final". Tower may add **"report traffic in sight"**.
- **Approach** puts you in one landing order with the AI arrivals. You are not given priority: the slower or later aircraft takes the delay, and that can be you, with a slow-down, a longer vector or a "follow". An aircraft closing on a slower one on final is told to cancel its approach, and Tower sends a pair around when the spacing is lost.
- The AI pilots read back only what is required. Their calls and ATC's replies to them show as text in the log.

## Hearing the other traffic

By default you read the traffic's calls in the log. You can also hear them. **Settings > How ATC sounds** has a checkbox, **Hear other traffic on the frequency**, off by default. It shows only when ATC offers it for your flights, and only matters when your flight has traffic.

- **What you hear:** other aircraft's calls, and ATC's replies to them, on a frequency that one of your radios is tuned to **and** set to listen to. Each AI aircraft has its own voice, and the controller keeps one voice for the position.
- **Never over you:** a traffic voice is dropped if you are transmitting, if ATC is talking to you, or if a phone call is ringing or open. One that is playing stops within a tenth of a second when any of those starts.
- **One at a time:** traffic voices play one after another, through your radio effect, and an ATIS pauses for them.
- **A limit per flight:** when a flight reaches it, the log says "Other traffic's voices stopped for this flight (limit reached); their words still show." and the text goes on.
- Saving the setting reconnects the flight (the same flight). ATC's words to you keep your **ATC voices** setting.

## Next

[Settings](settings.md#how-atc-sounds) lists the setting. [Tower](features/tower.md) says more about how it clears you with traffic about.
