# Settings

Everything is configured on the window's **Settings** view. There are no command-line options to learn and no files to edit. The view has two tabs: **General** and **X-Plane data**.

**Save** checks every field first. A bad value is highlighted and nothing is saved. With a flight under way, Save reconnects on the same flight with the new settings, waiting for ATC to finish talking first. Save never starts a flight.

## ATC

| Setting | What it is |
|---|---|
| **ATC address** | One line, not a field. ATC's address comes with your account when you sign in. The line says **From your account.** once the client has it, and the window never shows the address itself. If it could not be fetched, the line says so and **Try again** is beside it |
| **Sign-in service** | Two values that come with the client. Change them only when the owner tells you to |

While a flight is up, this section also shows the flight's session id.

## Simulator

| Setting | What it is |
|---|---|
| **Aircraft state from** | **X-Plane 12** is the normal choice. *Replay a recording* and *None* (a fixed aircraft parked at Seattle) are for testing without the sim |
| **X-Plane host** and **Web API port** | Where X-Plane's Web API listens. The default, `127.0.0.1` and `8086`, is right when the client runs on the same PC as X-Plane |
| **Silence X-Plane's own ATIS and AWOS during a flight** | On by default. X-Plane has an ATIS and AWOS of its own on the same frequencies, so with both on you would hear two voices with two sets of weather. During a flight the client switches X-Plane's off and switches it back on when the flight ends. If you had it off already, it stays off |
| **End the flight when X-Plane is closed for** | Seconds. The default is 30. A pause or a stutter never ends a flight. `0` turns it off |

## Push-to-talk

The window's button and the **Space** key always work. **Also transmit with** adds one more:

| Choice | What it does |
|---|---|
| Only this window | The button, or hold Space while the window has focus |
| A yoke or joystick button, through X-Plane | Hold the button to transmit, wherever the focus is |

For a yoke or joystick button, press **Learn button**, then press and release the button you want within 10 seconds. X-Plane must be running. The client reads the button through X-Plane, so anything X-Plane sees as a joystick button works.

## Audio

| Setting | Choices |
|---|---|
| **Use the microphone and speakers** | Off: no microphone and no sound, for testing |
| **Microphone**, **Speakers / headset** | Your devices, or the system default. A headset switched on after the client started appears after **Refresh devices** |
| **Radio effect** | *Clean*, *Realistic* or *Busy day*: how much of a VHF radio you hear on ATC's voice |
| **ATC voices** | The voices ATC speaks with. Four choices, in this order: *Radio voices: distinct controllers with accents*, then under **Standard voices**: *Standard* (the most robotic), *Neural* (the default) and *Generative* (the most natural, and may be slightly slower to start). Saving a change reconnects the flight (the same flight), so ATC switches at once |
| **Speech recognition** | How your transmissions are written down for ATC. Two choices: *Standard* (the default) and *Scribe, which knows your flight's names*. Saving a change reconnects the flight (the same flight); it applies from your next transmission. If Scribe is not available on a flight, Settings says **Scribe is not available on this flight: speech recognition is Standard.** See [Your data](privacy.md#what-happens-to-your-voice) for where the audio goes |
| **ATC delivery** | How briskly controllers talk: *Relaxed*, *Brisk* (the default, about 15% faster) or *Fast* (about 30% faster). The ATIS is always read at the relaxed pace |
| **The recording choice** | Your answer to the recording question, with **Allow** and **Don't allow** to change it. See [Your data](privacy.md#recordings-of-your-voice) |

### The radio voices

The radio voices are off by default. With them on, each controller on the radio gets a distinct voice with an accent. Within a flight, one frequency keeps one voice. They already sound like a radio, so the **Radio effect** only adds its key-up click and tail to them. Phone calls, the ATIS and AWOS keep the Neural voices. If the radio voices are not available on a flight, the flight goes on with the standard voices, and Settings says so under the list.

## Display

| Setting | What it is |
|---|---|
| **Theme** | Dark (the default) or light. The sun/moon button in the header switches it too |
| **Show the Approach card** | On by default. Off, the window never shows [ATC's approach plan](client/approach-card.md) as a card. The confirmation in the header still shows |

## Updates

The installed app asks the pilot site for the newest version when it starts, and once a day while it is open. A newer version shows a banner above the views: **What changed**, **Update now** and **Later**. The banner waits until your flight has ended, and nothing is installed during a flight. **Update now** downloads the installer, checks it, runs it, and the app opens again by itself. **Later** puts that version off until a newer one comes, or until you start the app again.

- **Check now** checks on request, and says if it could not.
- **Receive prereleases** is off unless you turn it on. On, you are offered early versions too. A prerelease is a build for testing; it can have faults, and a later change to the service can stop it working until you update. Turn it on only if you have been asked to.
- If ATC needs a newer client than yours, the banner says **Update required** and has no **Later**.

## X-Plane data

The second tab.

| Setting | What it is |
|---|---|
| **X-Plane folder** | Leave blank to use the folder X-Plane last ran from |
| **FAA procedures and ATC data for X-Plane** | Installs the FAA's current procedures into your X-Plane, and takes them out again. See [Your X-Plane's data](client/xplane-data.md#faa-procedures-for-your-x-plane) |

## Where things are kept

| What | Where (Windows) |
|---|---|
| Settings | `%LOCALAPPDATA%\xatc-agent-client\settings.json` |
| The log file | `%LOCALAPPDATA%\xatc-agent-client\logs\xatc-agent-client.log` |
| Your sign-in | Windows Credential Manager, under `xatc-agent-client`. Never in a file |

The Settings view shows both paths at the bottom, with **Open log folder**.

The settings file never holds a password or a key. It holds ATC's address (written from your account's answer, never by the window, and never shown in it), the sign-in service's two public values, your SimBrief username or pilot ID, your X-Plane folder, and your last flight plan, which pre-fills the New flight dialog.

The log file rotates at 5 MB and keeps five older files. It has every connect and disconnect, ATC's address, what ATC asked of your X-Plane, and every warning and error. It never has your sign-in or any audio. Send it along when you report a problem.
