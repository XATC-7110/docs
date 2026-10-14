# Your data

What the client sends, what is kept, and what stays on your PC. This page describes how the software works. It is not a legal agreement. xatc-agent is an invitation-only experiment; ask the project owner about anything this page does not answer.

## Your account

You sign in with an xatc-agent account that the owner creates for you: your email address, a password you choose, and an authenticator app or a passkey.

- The client never sees your password. You type it into the sign-in page in your own browser.
- The client keeps your sign-in in Windows Credential Manager, for up to 30 days. It is never written to a file.
- ATC knows which account is flying. A flight belongs to the pilot who started it, and nobody else can rejoin it.
- **Sign out** removes the sign-in from your PC and cancels it with the sign-in service.

## What the client sends during a flight

Over one encrypted connection to ATC, for as long as a flight is running:

| What | When |
|---|---|
| Your flight plan: callsign, aircraft type, departure, destination, cruise altitude, route | When the flight starts |
| Your aircraft's state: position, altitude, speed, heading, radios, on the ground or not | About once a second |
| The weather at your aircraft and X-Plane's clock | Every few seconds |
| The other aircraft in your X-Plane (the nearest 32) | About once a second |
| **Your microphone** | **Only while you hold push-to-talk** |
| Answers to ATC's questions about your scenery: an airport's taxiways and stands | When ATC asks. See [Your X-Plane's data](client/xplane-data.md) |

No connection to ATC is open when no flight is running, and your microphone is never sent outside push-to-talk.

## What happens to your voice

While you hold push-to-talk, your audio is streamed to a speech recognition service and turned into text. The text is what ATC works from.

### Recordings of your voice

By default **nothing you say is kept as audio**. The first time you connect, the window asks:

> **Keep your radio audio to improve xatc?** xatc can keep recordings of what you say on the radio, to train it to understand pilots better. Only your own transmissions are kept, in private storage, for 180 days. The owner and the ATC expert can listen to them. You can change this at any time in Settings. Nothing is kept unless you allow it.

- You must choose **Allow** or **Don't allow** before you can transmit.
- The choice is stored with your account, so you are asked once, not once per PC.
- Change it at any time in **Settings > Audio**.

## What is kept about a flight

Each flight is logged so that it can be reviewed and the controller improved:

- what you said, as text, and what ATC answered,
- what ATC decided,
- your aircraft's track,
- which account flew it.

The project owner and an air traffic control expert who advises the project review flights in a private tool. They can see the items above, and they can listen to your recordings only if you allowed them.

## Other services

- **The AI model.** The text of your transmissions, with the facts of your flight, is processed by an AI model to work out what you asked for and to judge readbacks. See [How it works](how-it-works.md).
- **SimBrief.** If you load a flight plan from SimBrief, the client fetches your latest plan from SimBrief with the username or pilot ID you typed. No SimBrief password or key is involved.

## What stays on your PC

- **Settings**: ATC's address (written from your account's answer, never shown in the window, and recorded in the log file), your SimBrief username or pilot ID, your X-Plane folder, your last flight plan. No password and no key.
- **The log file**: connections, ATC's address, what ATC asked of your X-Plane, warnings and errors. Never your sign-in and never audio.
- **The window** answers only to your own PC. No website can press your push-to-talk, sign you in or sign you out.
- **Your X-Plane files** are read, never uploaded as files. The only writes are the optional [FAA procedures](client/xplane-data.md#faa-procedures-for-your-x-plane), which you install and remove yourself.
