# Install on a Mac

The Mac app is a **disk image**: you download it, drag the app to your Applications folder and open it. There is nothing else to install and no terminal is needed. It is for **Apple silicon Macs (M1 or later)** running **macOS 14 or newer**.

!!! info "A prerelease, for now"
    The Mac app came with client 0.20 (since 0.20.0-rc.10), which is a **prerelease**: a build for testing, not yet a stable release. The Download page shows it under **Prerelease** (with a warning that it can have faults). Install it if you have been asked to, or if you are happy to test. When a stable release carries it, this note goes.

The Mac app is new and has been run by fewer pilots than the Windows one. If something does not work, [report it](troubleshooting.md#reporting-a-problem).

## What you need

| | |
|---|---|
| Simulator | X-Plane 12.1.4 or newer, as on [every platform](getting-started.md#what-you-need), running on the same Mac |
| Mac | An Apple silicon Mac (M1 or later) with macOS 14 or newer. There is no build for Intel Macs |
| Audio | A microphone, and speakers or a headset |
| Account | A SeventyOneTen account, created for you by the project owner |
| Phone | An authenticator app, for the sign-in's second step |

## Install (one time)

1. Go to the pilot site, [app.7110atc.com](https://app.7110atc.com), and sign in with your SeventyOneTen account. Open **Download**, choose **Mac (Apple silicon)**, then press **Download for Mac** under **Prerelease**. The file is `xatc-agent-<version>-arm64.dmg`.
2. Open the downloaded `.dmg` file. A disk image named *SeventyOneTen* and the version opens, with the app and your Applications folder side by side.
3. Drag **xatc-agent** to your **Applications** folder. Finder shows the app by its file name, `xatc-agent`; the window it opens is called **SeventyOneTen client**.
4. Eject the disk image.
5. Open **xatc-agent** from Applications, not from the disk image.
6. The first time, macOS asks whether SeventyOneTen may use the microphone. Allow it, so the app can hear you.

If you said no by mistake, open *System Settings > Privacy & Security > Microphone* and switch on **xatc-agent** (it may be listed as SeventyOneTen).

From here, [sign in and choose your audio](getting-started.md#sign-in) exactly as on Windows.

## Is this the right file?

The app is signed with the project's Apple developer certificate and notarized by Apple, so macOS can check it. (The Windows installer and the Linux AppImage are not signed.) The Download page also shows the file's **SHA-256**. To check that your copy is the one the page describes, run this in Terminal and compare the result with the page:

```
shasum -a 256 xatc-agent-<version>-arm64.dmg
```

Download the file only from the Download page while signed in.

## Staying signed in

You stay signed in for 30 days, across restarts. The app keeps your sign-in in your Mac's **Keychain**, under `xatc-agent-client`. It is never written to a file. **Sign out** in the window removes it.

## Updates

The app asks the pilot site for the newest version when it starts, and once a day while it is open. A newer version shows a banner: **What changed**, **Update now** and **Later**. The banner waits until your flight has ended, and nothing is installed during a flight.

**Update now** downloads the new version, checks that it is the release that was offered and that it is this app, replaces the app and opens it again by itself. If anything is wrong, your old app is left as it was and the banner says why.

Because it replaces the app, the app must be in **Applications** (or another folder you can write to). An app opened straight from the disk image, or left in Downloads, is not updated: move it to Applications first. Until the Mac app is in a stable release, newer Mac builds are prereleases, and the app offers a prerelease only when **Receive prereleases** is on in **Settings > Your account > Updates**: see [Updates](settings.md#updates).

## Where things are kept

| What | Where |
|---|---|
| Settings | `~/Library/Application Support/xatc-agent-client/settings.json` |
| The log file | `~/Library/Application Support/xatc-agent-client/logs/xatc-agent-client.log` (**Settings**, at the bottom, has **Open log folder**, which opens it in Finder) |
| The current flight, for **Rejoin last flight** | `~/.xatc-agent/session.json` |
| Your sign-in | Your Keychain, under `xatc-agent-client`. Never in a file |

None of these is inside the app.

## Remove the app

Drag **xatc-agent** from Applications to the Trash. Your settings, log and session file stay until you delete them. Your sign-in stays in your Keychain until you press **Sign out** in the window, so do that first if you want it gone.

## Next

[Sign in](getting-started.md#sign-in), then [your first flight](first-flight.md).
