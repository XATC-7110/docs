# Troubleshooting

Start with the **log** at the bottom of the window. It says why something did not happen.

If something is simply not built yet, it is on the [known limitations](known-limitations.md) page.

## ATC does not answer

After a transmission with no reply, the log has a **No reply** line with the reason:

| Reason | What it means | What to do |
|---|---|---|
| `no_controller_on_frequency` | Nobody works the frequency you transmitted on | Check which radio is selected to transmit (**TX**), and its active frequency. The Frequencies card lists the right ones |
| `sim_paused` | X-Plane is paused | Unpause. ATC is silent and deaf while paused |
| `sim_in_replay` | X-Plane is in a replay | Leave the replay |
| `empty_transcript` | The speech recognition heard nothing | Check your microphone (below) |
| `agent_chose_silence` | ATC judged that no reply was needed | Normal after a correct readback or a remark. Look for the **✓ Readback accepted** |
| `busy` | ATC was still handling your previous call | Wait a moment and say it again |
| `error` | Something failed | Say it again. If it repeats, send the log file |

If ATC answers "Aircraft calling, say again", it did not catch your callsign. Say your full callsign clearly.

## I cannot hear ATC

- **You hear ATC only on a frequency you are tuned to.** If the log says a reply was "not played (not tuned)", COM1 or COM2 was not on that frequency.
- ATC's audio waits while you are transmitting. Release push-to-talk.
- Check **Settings > Audio > Speakers / headset**. A headset you switched on after the client started appears after **Refresh devices**.

## The log shows nothing after "You:"

Your microphone is not reaching the client.

- *Windows Settings > Privacy & security > Microphone*: allow desktop apps.
- **Settings > Audio > Microphone**: pick the right device.
- Push-to-talk releases when the window loses focus. To transmit while X-Plane has focus, use a [yoke or joystick button](settings.md#push-to-talk).

## X-Plane: not connected

- The client and X-Plane must run on the same PC. X-Plane's Web API listens only on `127.0.0.1:8086`.
- Check **Settings > Simulator**: *X-Plane 12*, host `127.0.0.1`, port `8086`.
- The client keeps looking every few seconds. You do not need to restart it after starting X-Plane.

## X-Plane too old

The client needs **X-Plane 12.1.4 or newer**. It uses X-Plane's own Web API, and needs the version of it that arrived in 12.1.4.

- **Client 0.13.0 or newer:** the X-Plane pill reads **X-Plane: too old**, with "X-Plane 12.1.4 or newer is needed; this is 12.1.2" (the version your X-Plane reports), or "X-Plane 12.1.4 or newer is needed; this one is older" when your X-Plane is too old to say which version it is. When X-Plane is connected, the window's header shows its version after the client's.
- **A client older than 0.13.0:** an older X-Plane 12 does not answer the client's first question, so the client treats it as not there. The startup dialog and the window show **X-Plane: not connected**, with "not reachable at 127.0.0.1:8086; retrying", and the console window says "X-Plane not reachable". It does not go away, however long you wait, and it looks like [X-Plane: not connected](#x-plane-not-connected), whose checks do not help.

What to do: update X-Plane 12 to the current release.

## Tower will not clear me

- **Traffic.** Tower waits for a departure ahead to be clear, and for an arrival on short final. It tells you why.
- **Wake turbulence.** Behind a heavy, the wait is two or three minutes: "expect departure in two minutes".
- **No traffic data.** If the client loses X-Plane's traffic feed, Tower holds every takeoff and landing clearance until it is back, because it cannot see the runway. A multiplayer or traffic plugin that takes over X-Plane's traffic can cause this.

## Unable to access data, check connection

A red alert, and **X-Plane is paused for you**. ATC could not read its airport and procedure data, so it cannot control safely.

- Check your internet connection.
- When the data is back, the alert clears by itself and the log says "Data access restored". X-Plane stays paused until **you** unpause it.

## Update the client

"Update the client to x.y.z or newer": ATC needs a newer client than yours and has stopped connecting. Install the newer client package from the owner and start again.

## Sign-in

| You see | What to do |
|---|---|
| **Not signed in** | Press **Sign in**. A sign-in lasts 30 days |
| **Signed in · offline** | The sign-in service cannot be reached. Your flight keeps going and the client keeps trying |
| "Your sign-in expires in ..." | Press **Sign in again** whenever it suits you. It does not interrupt a flight |
| "This flight belongs to another pilot" | You tried to rejoin a flight another account started. Press **New flight** |
| "Your account isn't allowed to fly" | Ask the owner |
| "Can't confirm this flight's pilot right now. Retrying." | Nothing to do. The client reconnects by itself and your flight is kept |

## The window

- **It opened in my browser instead.** The window needs Edge WebView2, which ships with Windows 10 and 11. Without it the same page opens in your default browser and works the same.
- **"Already running".** Only one client runs at a time. Starting it again brings the window that is already open to the front (a client older than 0.13.0 says it cannot start: use the window that is open).
- **I closed the client mid-flight.** Start it again within about ten minutes and choose **Rejoin last flight**.

## The radios will not tune from the window

The **1**, **2** and **⇄** buttons write to X-Plane. They are greyed out while X-Plane is not connected; hover over them for the reason. Only real VHF COM frequencies are accepted (118.000 to 136.990 MHz).

## Reporting a problem

Check the [known limitations](known-limitations.md) first. Then send the owner:

1. What you said and what you expected, with the time.
2. The log file: **Settings**, at the bottom, **Open log folder**. It never contains your sign-in or any audio.
