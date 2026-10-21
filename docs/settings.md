# Settings

Everything is configured on the window's **Settings** view. There are no command-line options to learn and no files to edit.

Settings is one page that scrolls, in six sections, in the order a pilot uses them. A row of buttons stays at the top of the page: **Your setup**, **How ATC sounds**, **X-Plane data**, **Your account**, **Appearance** and **Advanced**. A button scrolls to its section, and the section you are looking at is the one marked.

At the bottom, **Save** and **Revert**. **Save** checks every field first. A bad value is highlighted, its section opens, and nothing is saved. With a flight under way, Save reconnects on the same flight with the new settings, waiting for ATC to finish talking first. Save never starts a flight. **Revert** reloads what was last saved.

## Your setup

What you set on day one: your microphone and speakers, your push-to-talk button, and where X-Plane is.

### Audio

| Setting | What it is |
|---|---|
| **Use the microphone and speakers** | Off: no microphone and no sound, for testing |
| **Microphone**, **Speakers / headset** | Your devices, or **System default**. A headset switched on after the client started appears after **Refresh devices** |

### Push-to-talk

The window's button and the **Space** key always work. **Also transmit with** adds one more:

| Choice | What it does |
|---|---|
| Only this window (button, or hold Space) | The button, or hold Space while the window has focus |
| A yoke or joystick button, through X-Plane | Hold the button to transmit, wherever the focus is |

For a yoke or joystick button, press **Learn button**, then press and release the button you want within 10 seconds. X-Plane must be running. The client reads the button through X-Plane, so anything X-Plane sees as a joystick button works. The client says "Learned button 5 and saved it" (with your button's number), and **Button index** shows it.

(When you run the client from a console window, there is a third choice, **Enter in the console window (toggles)**. The installed app has no console, so it does not show it.)

#### Phone calls

The last row of this part is **Phone calls**. **Push to talk** is the default: on a [clearance call](features/clearance.md#by-phone-at-a-field-with-no-radio-way) you hold the key, as on the radio.

The two **Two-way (experimental)** choices, **Two-way A** and **Two-way B** (two versions of the same thing, being compared), open your microphone for the call: there is no button, you just talk, and ATC answers when you have finished. Use a headset. They are experimental and offered only on some accounts for now. When a flight does not offer one, its choice is greyed and calls stay push to talk. If a two-way call has trouble, it goes on as push to talk and the call screen says "Two-way calling stopped. Hold to talk to continue." The choice applies from your next call; saving it never reconnects the flight.

### X-Plane

| Setting | What it is |
|---|---|
| **X-Plane host** and **Web API port** | Where X-Plane's Web API listens. The default, `127.0.0.1` and `8086`, is right when the client runs on the same PC as X-Plane |
| **End the flight when X-Plane is closed for (s, 0 = never)** | Seconds. The default is 30. A pause or a stutter never ends a flight. `0` turns it off |
| **Silence X-Plane's own ATIS and AWOS during a flight** | On by default. X-Plane has an ATIS and AWOS of its own on the same frequencies, so with both on you would hear two voices with two sets of weather. During a flight the client switches X-Plane's off and switches it back on when the flight ends. If you had it off already, it stays off |

### App menu (Linux AppImage)

Only on Linux, and only when you run the AppImage, there is one more part, **App menu**, with **Add to app menu** and **Remove from app menu**. See [Install on Linux](install-linux.md#add-the-app-to-your-app-menu). Nowhere else shows it.

## How ATC sounds

| Setting | Choices |
|---|---|
| **ATC voices** | The voices ATC speaks with. Four choices, in this order: *Radio voices: distinct controllers with accents*, then under **Standard voices**: *Standard: cheapest, most robotic*, *Neural: the default* and *Generative: most natural, about twice neural's cost, may be slightly slower to start*. Saving a change reconnects the flight (the same flight), so ATC switches at once; an ATIS already on the air keeps its voice until its next letter |
| **ATC delivery** | How briskly controllers talk: *Relaxed*, *Brisk* (the default, about 15% faster) or *Fast* (about 30% faster). The ATIS is always read at the relaxed pace. Saving a change reconnects the flight (the same flight) |
| **Radio effect** | *Clean*, *Realistic* (the default) or *Busy day*: how much of a VHF radio you hear on ATC's voice |
| **Speech recognition** | How your transmissions are written down for ATC. Two choices: *Standard (the default)* and *Scribe, which knows your flight's names*. Saving a change reconnects the flight (the same flight); it applies from your next transmission. If Scribe is not available on a flight, Settings says **Scribe is not available on this flight: speech recognition is Standard.** See [Your data](privacy.md#what-happens-to-your-voice) for where the audio goes |

### The radio voices

The radio voices are off by default. With them on, each controller on the radio gets a distinct voice with an accent. Within a flight, one frequency keeps one voice. They already sound like a radio, so the **Radio effect** only adds its key-up click and tail to them. Phone calls, the ATIS and AWOS keep the Neural voices. If the radio voices are not available on a flight, the flight goes on with the standard voices, and Settings says so under the list.

## X-Plane data

| Setting | What it is |
|---|---|
| **X-Plane folder** (optional) | Leave blank to use the folder X-Plane last ran from. The line under it says "Reading" and the folder the client found, or that it found none |
| **FAA procedures and ATC data for X-Plane** | Installs the FAA's current procedures into your X-Plane, and takes them out again, with **Check for update**, **Install**, **Update** and **Remove**. See [Your X-Plane's data](client/xplane-data.md#faa-procedures-for-your-x-plane) |

## Your account

### ATC

| Line | What it is |
|---|---|
| **ATC address** | One line, not a field. ATC's address comes with your account when you sign in. The line says **From your account.** once the client has it, and **It comes from your account when you sign in.** until then. The window never shows the address itself. If it could not be fetched, the line says so and **Try again** is beside it |
| **This flight** | While a flight is up, the flight's session id |

### Recording

**Keep my radio audio to improve SeventyOneTen** shows your answer to the [recording question](privacy.md#recordings-of-your-voice), with **Allow** and **Don't allow** to change it. Your choice is saved with your account and takes effect at once. Recordings already kept stay until they expire. While it saves, a **Saving settings** box keeps you from leaving the page until the choice is saved.

### Updates

The installed app asks the pilot site for the newest version when it starts, and once a day while it is open. A newer version shows a banner above the views: **What changed**, **Update now** and **Later**. The banner waits until your flight has ended, and nothing is installed during a flight. **Update now** downloads the new version, checks it, installs it, and the app opens again by itself. On Windows it runs the installer; on Linux it replaces the AppImage file (see [Install on Linux](install-linux.md#updates)). **Later** puts that version off until a newer one comes, or until you start the app again.

- **Check now** checks on request, and says if it could not.
- **Receive prereleases: early versions, to try before everyone gets them** is off unless you turn it on. On, you are offered early versions too. A prerelease is a build for testing; it can have faults, and a later change to the service can stop it working until you update. Turn it on only if you have been asked to.
- If ATC needs a newer client than yours, the banner says **Update required** and has no **Later**.

## Appearance

| Setting | What it is |
|---|---|
| **Theme** | **Night** (the default) or **Paper**. The button at the top right of the window switches it too |
| **Show the Approach card: ATC's plan for your vectors and approach, as a diagram** | On by default. Off, the window never shows [ATC's approach plan](client/approach-card.md) as a card. The confirmation in the header still shows |

## Advanced

**Advanced, for developers** is folded away unless something in it has been changed. You do not need it to fly. It holds the two sign-in service values that come with the client (change them only when the owner tells you to), **Aircraft state from** (*X-Plane 12 (Web API)* is the normal choice; *Replay a recording* and *None*, a fixed aircraft parked at Seattle, are for testing without the sim) and a manual source for the X-Plane data pack, for testing.

## Where things are kept

At the very bottom of the page the window shows the **Settings file** and the **Log file** paths, with **Open log folder**.

| What | Where (Windows) |
|---|---|
| Settings | `%LOCALAPPDATA%\xatc-agent-client\settings.json` |
| The log file | `%LOCALAPPDATA%\xatc-agent-client\logs\xatc-agent-client.log` |
| Your sign-in | Windows Credential Manager, under `xatc-agent-client`. Never in a file |

On Linux the settings and the log are in `~/.config/xatc-agent-client/` (the log in its `logs` folder), and the sign-in is in your keyring.

The settings file never holds a password or a key. It holds ATC's address (written from your account's answer, never by the window, and never shown in it), the sign-in service's two public values, your SimBrief username or pilot ID, your X-Plane folder, and your last flight plan, which pre-fills the New flight dialog.

The log file rotates at 5 MB and keeps five older files. It has every connect and disconnect, ATC's address, what ATC asked of your X-Plane, and every warning and error. It never has your sign-in or any audio. Send it along when you report a problem.
