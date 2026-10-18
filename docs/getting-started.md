# Install and sign in

xatc-agent has two parts. The controller runs in the cloud. On your sim PC you run a small program, the **client**, in its own window beside X-Plane. It reads your aircraft's state from X-Plane, sends your voice while you hold push-to-talk, and plays ATC's replies through a radio effect.

## What you need

| | |
|---|---|
| Simulator | X-Plane 12.1.4 or newer. The client uses X-Plane's own Web API, and needs the version of it that arrived in 12.1.4. Tested on 12.4.3. Use the current X-Plane 12 release |
| PC | Windows 10 or 11. The window uses Edge WebView2, which ships with both |
| Audio | A microphone, and speakers or a headset |
| Account | An xatc-agent account, created for you by the project owner |
| The client | The installer, from the pilot site once you are signed in (below) |
| Phone | An authenticator app, for the sign-in's second step |

!!! note "Invitation only"
    xatc-agent is an experiment and is not open for sign-up. If you were invited, the owner has sent you an email with a temporary password.

## Install (one time)

1. Go to the pilot site, [xatc.bandd.cloud](https://xatc.bandd.cloud), and sign in with your xatc-agent account. Open **Download** and press **Download for Windows**. The file is `xatc-agent-setup-<version>.exe`.
2. Run it. It installs for your Windows account only and does not ask for an administrator password.
3. The installer is not signed yet, so Windows may say "Windows protected your PC". Choose **More info**, then **Run anyway**. Do this only for a file you downloaded from the Download page while signed in.
4. Open **xatc-agent** from the Start menu (or from the last page of the installer).
5. Allow the microphone: *Windows Settings > Privacy & security > Microphone > Let desktop apps access your microphone*.

There is nothing else to install and no keys to copy. You sign in from the window.

The installed app updates itself: see [Updates](settings.md#updates). To remove it, use *Windows Settings > Apps > xatc-agent > Uninstall*. Your settings and log stay in `%LOCALAPPDATA%\xatc-agent-client` until you delete that folder. Your sign-in stays in Windows Credential Manager until you press **Sign out** in the window; do that before uninstalling if you want it gone.

## Start the client

Open **xatc-agent** from the Start menu. The **xatc-agent** window opens with the startup dialog: one row each for your sign-in, the ATC gateway and X-Plane. There is no console window; the [log file](settings.md#where-things-are-kept) holds what a console would show.

- X-Plane is shown but not required yet. Start it whenever you like; the client keeps looking for it.
- Only one client runs at a time. Starting it again brings the window that is already open to the front.

## Sign in

1. Press **Sign in** in the startup dialog. Your browser opens the xatc-agent sign-in page.
2. The first time, enter your email and the temporary password from your invitation, choose your own password, and set up your authenticator app. After that it is your email, your password and the authenticator's code (or a passkey, if you add one).
3. The browser says **Signed in** and you can close the tab. The window's sign-in pill turns green.

You stay signed in for 30 days, across restarts. In the last 24 hours the window offers **Sign in again**, which never interrupts a flight. The client keeps your sign-in in Windows Credential Manager, never in a file.

## Choose your audio

ATC's address comes with your account. When you sign in, the client gets it. The **ATC** section of Settings has one line about it: **From your account.** once the client has it.

1. Open the **Settings** view (the startup dialog closes by itself once you are signed in).
2. Under **Audio**, pick your microphone and your speakers or headset.
3. Press **Save**.

If the line says the address could not be fetched, press **Try again**.

That is all the setup. [Settings](settings.md) describes everything else you can change, such as push-to-talk on a yoke button and how the controllers sound.

## The recording question

The first time you connect, the window asks one thing before you can transmit:

> **Keep your radio audio to improve xatc?** xatc can keep recordings of what you say on the radio, to help it understand pilots better. Only your own transmissions are kept, in private storage, for 180 days. The owner and the ATC expert can listen to them. You can change this at any time in Settings. Nothing is kept unless you allow it.

Choose **Allow** or **Don't allow**. Your choice is remembered with your account, and you can change it in **Settings > Audio**. [Your data](privacy.md) says what else is sent and kept.

## Next

[Your first flight](first-flight.md).
