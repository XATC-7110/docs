# Troubleshooting

Start with the **log** at the bottom of the window. It says why something did not happen.

If something is simply not built yet, it is on the [known limitations](known-limitations.md) page.

## ATC does not answer

After a transmission with no reply, the log has a **No reply** line with the reason, in words:

| Reason | What it means | What to do |
|---|---|---|
| no controller on frequency | Nobody works the frequency you transmitted on | Check which radio is selected to transmit (**TX**), and its active frequency. The Frequencies card lists the right ones. On an airport's advisory frequency (**advisory · no ATC**) silence is normal: the log says "no reply expected" |
| sim paused | X-Plane is paused | Unpause. ATC is silent and deaf while paused |
| sim in replay | X-Plane is in a replay | Leave the replay |
| empty transcript | The speech recognition heard nothing | Check your microphone (below) |
| agent chose silence, readback accepted | ATC judged that no reply was needed | Normal after a correct readback or a remark. Look for the **✓ Readback accepted** |
| busy | ATC was still handling your previous call | Wait a moment and say it again |
| error | Something failed | Say it again. If it repeats, send the log file |

If ATC answers "Aircraft calling, say again", it did not catch your callsign. Say your full callsign clearly. If you fly under an airline callsign, say it as ATC says it ("Walker seventeen forty-five").

## I cannot hear ATC

- **You hear ATC only on a radio that is tuned to the frequency, switched on, and selected to listen on your audio panel.** If the log says a reply was "not played", the line says why: "isn't on COM1/COM2 active" (neither radio was tuned to it), or "COM1 is off", "COM1 isn't selected to listen", "the avionics are off".
- **A call you missed is said again.** When the radio can hear it again within about a minute, and you have not transmitted since, ATC repeats its latest call on that frequency once.
- ATC's audio waits while you are transmitting. Release push-to-talk.
- Check **Settings > Your setup > Audio > Speakers / headset**. A headset you switched on after the client started appears after **Refresh devices**.

## Cannot transmit

Pressing push-to-talk does nothing, and the log shows an **Error** line that begins "can't transmit":

| The line says | What to do |
|---|---|
| the avionics are off | Switch the avionics on in X-Plane |
| COM1 is off (or COM2) | Switch that radio on. It is the radio selected to transmit, marked **TX** |
| COM1 isn't selected to listen | Select it to listen on your audio panel, or select the other radio to transmit |
| no aircraft state yet (is X-Plane connected?) | Start X-Plane: see [X-Plane: not connected](#x-plane-not-connected) |
| answer the recording question in the SeventyOneTen window first | Choose **Allow** or **Don't allow** in the [recording question](privacy.md#recordings-of-your-voice) |
| your recording choice is still being saved | Wait for the **Saving settings** box to finish, or choose **Try again** or **Close** if it says it could not save |

Nothing is sent to ATC when a press is refused.

## The log shows nothing after "You:"

Your microphone is not reaching the client.

- *Windows Settings > Privacy & security > Microphone*: allow desktop apps. On a Mac, open *System Settings > Privacy & Security > Microphone* and switch SeventyOneTen on. On Linux, check your desktop's sound settings and that the microphone is not muted.
- **Settings > Your setup > Audio > Microphone**: pick the right device.
- Push-to-talk releases when the window loses focus. To transmit while X-Plane has focus, use a [yoke or joystick button](settings.md#push-to-talk).

## X-Plane: not connected

- The client and X-Plane must run on the same PC. X-Plane's Web API listens only on `127.0.0.1:8086`.
- Check **Settings > Your setup > X-Plane**: host `127.0.0.1`, port `8086`. (Under **Advanced**, **Aircraft state from** must be *X-Plane 12 (Web API)*; that is how it ships.)
- The client keeps looking every few seconds. You do not need to restart it after starting X-Plane.

## X-Plane too old

The client needs **X-Plane 12.1.4 or newer**. It uses X-Plane's own Web API, and needs the version of it that arrived in 12.1.4.

The X-Plane pill reads **X-Plane: too old**, with "X-Plane 12.1.4 or newer is needed; this is 12.1.2" (the version your X-Plane reports), or "X-Plane 12.1.4 or newer is needed; this one is older" when your X-Plane is too old to say which version it is. When X-Plane is connected, the window's header shows its version after the client's.

What to do: update X-Plane 12 to the current release.

## Tower will not clear me

- **Traffic.** Tower waits for a departure ahead to be clear, and for an arrival on short final. It tells you why.
- **Wake turbulence.** Behind a heavy aircraft or a Boeing 757 the wait is two minutes, behind a super three, and longer from an intersection or an offset parallel runway. Tower says "hold for wake turbulence" and clears you once the time is up.
- **No traffic data.** If the client loses X-Plane's traffic feed, Tower holds every takeoff and landing clearance until it is back, because it cannot see the runway. A multiplayer plugin, or another plugin that takes over X-Plane's AI aircraft, can cause this. If the cause is SeventyOneTen's own [AI traffic](traffic.md), the traffic line under the window's header says what is wrong.

## Unable to access data, check connection

A red alert, and **X-Plane is paused for you**. ATC could not read its airport and procedure data, so it cannot control safely.

- Check your internet connection.
- When the data is back, the alert clears by itself and the log says "Data access restored". X-Plane stays paused until **you** unpause it.

## Update required

The window shows a banner, **Update required.**: "This is SeventyOneTen 0.19.0, and 0.20.0 or newer is needed to fly." ATC needs a newer client than yours and has stopped connecting. Press **Update now** in the banner (it has no **Later**), or download the newest installer from the pilot site ([app.7110atc.com](https://app.7110atc.com), **Download**) and run it over your copy. If it says "No update was found yet", press **Check again**. Then start the client again.

!!! note "Older than 0.20.0-rc.11: it cannot find updates"
    The pilot site moved to [app.7110atc.com](https://app.7110atc.com) on 2026-10-20. A client older than **0.20.0-rc.11** still asks the old address for updates, so **Update now** and **Check again** find nothing. Install the newest version once by hand from [app.7110atc.com/#/download](https://app.7110atc.com/#/download); it updates itself from then on.

## Sign-in

| You see | What to do |
|---|---|
| **Not signed in** | Press **Sign in**. A sign-in lasts 30 days |
| **Signed in · offline** | The sign-in service cannot be reached. Your flight keeps going and the client keeps trying |
| "Your sign-in expires in ..." | Press **Sign in again** whenever it suits you. During a flight, sign in as the same account or the flight will end |
| "Your sign-in has run out. Sign in again to keep flying." | Press **Sign in again** |
| Your passkey is not offered, or is refused | Passkeys belong to the sign-in address, which changed on 2026-10-20: add the passkey again. Sign in with your email, password and the authenticator's code, then add the passkey again |
| "This flight belongs to another pilot" | You tried to rejoin a flight another account started. Press **New flight** |
| "Your account isn't allowed to fly" | Ask the owner |
| "Can't confirm this flight's pilot right now. Retrying." | Nothing to do. The client reconnects by itself and your flight is kept |

## The window

- **It opened in my browser instead.** On Windows the window needs Edge WebView2, which ships with Windows 10 and 11; on Linux it needs WebKit2GTK; on a Mac it uses the web view that is built into macOS. Without it the same page opens in your default browser and works the same.
- **On Linux I have to sign in every time.** Staying signed in needs a keyring (GNOME Keyring or KWallet). Without one, the sign-in lasts only while the app runs.
- **"SeventyOneTen is already running".** Only one client runs at a time. Starting it again brings the window that is already open to the front. If the line adds that the window could not be brought forward, look for it in the taskbar.
- **I closed the client mid-flight.** Start it again within about ten minutes and choose **Rejoin last flight**.

## Flight ended: no ground data from X-Plane for the departure airport

The flight ended at the start. ATC could not get the airport's ground layout (its taxiways, hold lines and stands) from your X-Plane for the **departure** airport, so it cannot serve the flight. The window's header says **Flight ended: no ground data from X-Plane for the departure airport**, and the **New flight** dialog shows what to check:

- X-Plane has the departure airport's scenery installed and enabled.
- The client has your X-Plane folder: **Settings > X-Plane data > X-Plane folder**.
- X-Plane is running and connected (the **X-Plane** pill is green), then start a new flight.

An older client (before 0.20.0-rc.17) shows only a general error line for the same end.

## ATC got stuck on that call

A card appears in the window: **ATC got stuck on that call. It has been reported.** ATC could not make sense of your last call and said nothing. The card has a **Reference** line, such as "Reference: t-1234", and **Close**.

- The flight goes on, and nothing is retried by itself. Close the card and say the call again, in other words if you can.
- The problem has already been reported. If it keeps happening, send the reference and the time with your [report](#reporting-a-problem).
- The technical cause is in the log file, not in the window.

## The radios will not tune from the window

The **1**, **2** and **⇄** buttons write to X-Plane. They are greyed out while X-Plane is not connected; hover over them for the reason. Only real VHF COM frequencies are accepted (118.000 to 136.990 MHz).

## Reporting a problem

Check the [known limitations](known-limitations.md) first. Then send the owner:

1. What you said and what you expected, with the time.
2. The log file: **Settings**, at the bottom, **Open log folder**. It never contains your sign-in or any audio.
