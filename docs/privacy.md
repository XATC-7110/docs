# Your data

What the client sends, what is kept, and what stays on your PC. This page describes how the software works. It is not a legal agreement. SeventyOneTen is an invitation-only experiment; ask the project owner about anything this page does not answer.

## Your account

You sign in with a SeventyOneTen account that the owner creates for you: your email address, a password you choose, and an authenticator app or a passkey.

- The client never sees your password. You type it into the sign-in page in your own browser.
- The client keeps your sign-in in Windows Credential Manager (on a Mac, in your Keychain; on Linux, in your keyring), for up to 30 days. It is never written to a file.
- ATC knows which account is flying. A flight belongs to the pilot who started it, and nobody else can rejoin it.
- **Sign out** removes the sign-in from your PC and cancels it with the sign-in service.

## What the client sends during a flight

Over one encrypted connection to ATC, for as long as a flight is running:

| What | When |
|---|---|
| Your flight plan: callsign, aircraft type, departure, destination, cruise altitude, route | When the flight starts |
| Your aircraft's state: position, altitude, speed, heading, radios (frequencies, and whether each is on and selected to listen), transponder code, on the ground or not | About once a second |
| The weather at your aircraft and X-Plane's clock | Every few seconds |
| The other aircraft in your X-Plane (the nearest 32), including [AI traffic](traffic.md) if you turned it on | About once a second |
| **Your microphone** | **Only while you hold push-to-talk.** The exception is an experimental [two-way phone call](#two-way-phone-calls-experimental), where it is open for the whole call |
| Answers to ATC's questions about your scenery: an airport's taxiways and stands | When ATC asks. See [Your X-Plane's data](client/xplane-data.md) |

No connection to ATC is open when no flight is running, and your microphone is never sent outside push-to-talk, except on a two-way phone call you chose.

## What happens to your voice

While you hold push-to-talk, your audio is streamed to a speech recognition service and turned into text. The text is what ATC works from.

When the client's **Speech recognition** setting is **Scribe**, the audio of your transmissions goes to a third-party speech service outside SeventyOneTen's own systems, to be written down. When it is **Standard**, or if that service cannot be reached, SeventyOneTen's own speech recognition writes it down within SeventyOneTen's systems.

The full statement, which names the services, is the [Privacy page on the pilot site](https://app.7110atc.com/#/privacy).

### Two-way phone calls (experimental)

On a [clearance call](features/clearance.md#by-phone-at-a-field-with-no-radio-way) you can choose a **Two-way** call in Settings ([Phone calls](settings.md#phone-calls)). It is experimental and offered only on some accounts. On a two-way call there is no push-to-talk button: **your microphone is open for the whole call**, and the call's audio goes to a live voice service that carries the conversation. With **Two-way B** that is a third-party service outside SeventyOneTen's own systems; the [Privacy page on the pilot site](https://app.7110atc.com/#/privacy) names the services. SeventyOneTen does not keep the audio of a two-way call, whatever you chose in the recording question below. On **Push to talk**, the default, a call is like the radio: the microphone is open only while you hold the key.

### Recordings of your voice

By default **nothing you say is kept as audio**. The first time you connect, the window asks:

> **Keep your radio audio to improve SeventyOneTen?** SeventyOneTen can keep recordings of what you say on the radio, to help it understand pilots better. Only your own transmissions are kept, in private storage, for 180 days. The owner and the ATC expert can listen to them. SeventyOneTen also keeps the text its speech recognizer wrote down for what you said, with your flight's record, for as long as that flight is kept: only the audio is deleted after 180 days. You can change this at any time in Settings. Your flight's transcript is always kept with the flight. The recording and the recognizer's own text are kept only if you allow it.

- You must choose **Allow** or **Don't allow** before you can transmit.
- The choice is stored with your account, so you are asked once, not once per PC.
- Change it at any time in **Settings > Your account > Recording**.
- When the wording of the question changes, every pilot is asked again. The wording above (version 3) first ships with the next client release (it reaches you first as a prerelease if you have opted in; see [Settings](settings.md) for how prereleases are offered), so you will see the question once more after you update to a client that carries it; client 0.19.0 still shows the earlier wording.

## What is kept about a flight

Each flight is logged so that it can be reviewed and the controller improved:

- what you said, as text, and what ATC answered,
- what ATC decided,
- your aircraft's track,
- which account flew it.

The project owner, an air traffic control expert who advises the project, and the project's testers review flights in a private tool. They can see the items above. Only the owner and the expert can listen to your recordings, and only if you allowed them.

If you allowed recordings, the flight's record also keeps the text the speech recognizer wrote down for what you said, exactly as it wrote it, for as long as the flight is kept. That is longer than the audio: **only the audio is deleted after 180 days**; the text stays with the flight. If you chose **Don't allow**, that text is not kept (the transcript of what you said, listed above, always is). Text already kept with earlier flights stays with them.

A flight log is kept until it is deleted: there is no automatic expiry today. The pilot site's [Privacy page](https://app.7110atc.com/#/privacy) says how to ask for a copy of what is held about you, or for your account, flights or recordings to be deleted.

## Plans you send to your account

If you [send a flight plan to your account](send-a-plan.md), SeventyOneTen keeps your five most recent plans (the airports, route, altitude and tail number in each, and the file's name) so you can load one in the client. The file itself is not stored. Older plans are removed as new ones arrive, and all of them are deleted with your account. The iPhone app keeps its sign-in in the iPhone's Keychain and sends a file only when you tap **Send**.

## Other services

- **The radio voices.** ATC's voice is made by SeventyOneTen's own text to speech. Only when **ATC voices** is set to **Radio voices** do the words ATC says on the radio go instead, as text, to a third-party speech service outside SeventyOneTen's own systems, to give each controller a distinct voice and accent. Only ATC's words are sent, never your voice. The setting is off by default. Push-to-talk phone calls, the ATIS and AWOS are always spoken by SeventyOneTen's own text to speech; on a two-way call the live voice service speaks ATC's words too (see [Two-way phone calls](#two-way-phone-calls-experimental)). So is any radio transmission that the third-party service cannot speak in time.
- **The AI model.** The text of your transmissions, with the facts of your flight, is processed by an AI model to work out what you asked for and to judge readbacks. See [How it works](how-it-works.md).
- **SimBrief.** If you load a flight plan from SimBrief, the client fetches your latest plan from SimBrief with the username or pilot ID you typed. No SimBrief password or key is involved.

## What stays on your PC

- **Settings**: ATC's address (written from your account's answer, never shown in the window, and recorded in the log file), your SimBrief username or pilot ID, your X-Plane folder, your last flight plan. No password and no key.
- **The log file**: connections, ATC's address, what ATC asked of your X-Plane, warnings and errors. Never your sign-in and never audio.
- **The window** answers only to your own PC. No website can press your push-to-talk, sign you in or sign you out.
- **Your X-Plane files** are read, never uploaded as files. The client writes to your X-Plane folder in two places only: the optional [FAA procedures](client/xplane-data.md#faa-procedures-for-your-x-plane), which you install and remove yourself, and [your flight plan](client/flight-plan-file.md), the one file `Output/FMS plans/SeventyOneTen.fms`, which is written when you start a flight and never sent anywhere.
