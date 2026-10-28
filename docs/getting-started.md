# Install and sign in

SeventyOneTen has two parts. The controller runs in the cloud. On your sim PC you run a small program, the **client**, in its own window beside X-Plane. It reads your aircraft's state from X-Plane, sends your voice while you hold push-to-talk, and plays ATC's replies through a radio effect.

## What you need

| | |
|---|---|
| Simulator | X-Plane 12.1.4 or newer. The client uses X-Plane's own Web API, and needs the version of it that arrived in 12.1.4. Tested on 12.4.3. Use the current X-Plane 12 release |
| PC | Windows 10 or 11. The window uses Edge WebView2, which ships with both. On Linux, see [Install on Linux](install-linux.md). On an Apple silicon Mac with macOS 14 or newer, see [Install on a Mac](install-mac.md) |
| Audio | A microphone, and speakers or a headset |
| Account | A SeventyOneTen account, created for you by the project owner |
| The client | The installer (Windows), the AppImage (Linux) or the disk image (Mac), from the pilot site once you are signed in (below) |
| Phone | An authenticator app, for the sign-in's second step |

!!! note "Invitation only"
    SeventyOneTen is an experiment and is not open for sign-up. If you were invited, the owner has sent you an email with a temporary password.

## Install (one time)

These steps are for Windows. On Linux, follow [Install on Linux](install-linux.md); on a Mac, follow [Install on a Mac](install-mac.md). Then come back here to sign in.

1. Go to the pilot site, [app.7110atc.com](https://app.7110atc.com), and sign in with your SeventyOneTen account. Open **Download** (<https://app.7110atc.com/#/download>) and press **Download for Windows**. The file is `xatc-agent-setup-<version>.exe`.
2. Run it. It installs for your Windows account only and does not ask for an administrator password.
3. The installer is not signed yet, so Windows may say "Windows protected your PC". Choose **More info**, then **Run anyway**. Do this only for a file you downloaded from the Download page while signed in.
4. Open **SeventyOneTen** from the Start menu (or from the last page of the installer).
5. Allow the microphone: *Windows Settings > Privacy & security > Microphone > Let desktop apps access your microphone*.

There is nothing else to install and no keys to copy. You sign in from the window.

!!! note "Installed it before 20 October 2026? Reinstall once, by hand"
    On 2026-10-20 the pilot site moved to [app.7110atc.com](https://app.7110atc.com) (the product's home is [7110atc.com](https://7110atc.com)). A client older than **0.20.0-rc.11** looks for updates at the old address, so it can no longer find them: download the newest installer from [app.7110atc.com/#/download](https://app.7110atc.com/#/download) and run it over your copy. After that, updates arrive by themselves again.

The installed app updates itself: see [Updates](settings.md#updates). To remove it, use *Windows Settings > Apps > SeventyOneTen > Uninstall*. Your settings and log stay in `%LOCALAPPDATA%\xatc-agent-client` until you delete that folder. Your sign-in stays in Windows Credential Manager until you press **Sign out** in the window; do that before uninstalling if you want it gone.

## Start the client

Open **SeventyOneTen** from the Start menu. The **SeventyOneTen client** window opens with the startup dialog: one row each for your sign-in, the ATC service and X-Plane. There is no console window; the [log file](settings.md#where-things-are-kept) holds what a console would show.

- X-Plane is shown but not required yet. Start it whenever you like; the client keeps looking for it.
- Only one client runs at a time. Starting it again brings the window that is already open to the front.

## Sign in

1. Press **Sign in** in the startup dialog. Your browser opens the SeventyOneTen sign-in page.
2. The first time, enter your email and the temporary password from your invitation, choose your own password, and set up your authenticator app. After that it is your email, your password and the authenticator's code (or a passkey, if you add one). **Passkeys must be added again** after the sign-in move of 2026-10-20: a passkey belongs to the sign-in address, so the old ones no longer work. Sign in with your password and the authenticator's code, then add the passkey again.
3. The browser says **Signed in** and you can close the tab. The window's sign-in pill turns green.

You stay signed in for 30 days, across restarts. In the last 24 hours the window offers **Sign in again**, which never interrupts a flight. The client keeps your sign-in in Windows Credential Manager (on a Mac, in your Keychain; on Linux, in your keyring), never in a file.

## Choose your audio

ATC's address comes with your account. When you sign in, the client gets it. Under **Your account**, Settings has an **ATC** part with one line about it: **From your account.** once the client has it.

1. Open the **Settings** view (the startup dialog closes by itself once you are signed in).
2. Under **Your setup > Audio**, pick your microphone and your speakers or headset.
3. Press **Save**, at the bottom of the page.

If the ATC line says the address could not be fetched, press **Try again**.

That is all the setup. [Settings](settings.md) describes everything else you can change, such as push-to-talk on a yoke button (**Your setup**) and how the controllers sound (**How ATC sounds**).

## The recording question

The first time you connect, the window asks one thing before you can transmit:

> **Keep your radio audio to improve SeventyOneTen?** SeventyOneTen can keep recordings of what you say on the radio, to help it understand pilots better. Only your own transmissions are kept, in private storage, for 180 days. The owner and the ATC expert can listen to them. SeventyOneTen also keeps the text its speech recognizer wrote down for what you said, with your flight's record, for as long as that flight is kept: only the audio is deleted after 180 days. You can change this at any time in Settings. Your flight's transcript is always kept with the flight. The recording and the recognizer's own text are kept only if you allow it.

Choose **Allow** or **Don't allow**. Your choice is remembered with your account, and you can change it in **Settings > Your account > Recording**. [Your data](privacy.md) says what else is sent and kept.

## Next

[Your first flight](first-flight.md).
