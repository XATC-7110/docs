# Install on Linux

The Linux client is an **AppImage**: one file that you download, make executable and run. There is nothing to install and no terminal is needed. It is for 64-bit Intel and AMD PCs (x86_64) only.

!!! info "A prerelease, for now"
    The Linux app first came with client 0.20, which is a **prerelease**: a build for testing, not yet a stable release. The Download page shows it under **Prerelease** (with a warning that it can have faults), and when no Linux version has been published it says **No Linux release yet**. Install it if you have been asked to, or if you are happy to test. When a stable release carries it, this note goes.

The Linux app is new and has been run by fewer pilots than the Windows one. If something does not work, [report it](troubleshooting.md#reporting-a-problem).

## What you need

| | |
|---|---|
| Simulator | X-Plane 12.1.4 or newer, as on [every platform](getting-started.md#what-you-need) |
| PC | A 64-bit (x86_64) Linux desktop. The app is built on Ubuntu 22.04, so it also runs on Ubuntu 24.04, Debian 12, Fedora 38 and later, and Linux Mint 21 and later |
| Window | WebKit2GTK 4.1, from your system, so the app opens in its own window. Ubuntu 24.04 and most desktop distributions have it. Without it, the same panel opens in your web browser and works the same |
| Staying signed in | A keyring: GNOME Keyring or KWallet. Without one you sign in each time you start the app |
| Audio | A microphone, and speakers or a headset |
| Account | An xatc-agent account, created for you by the project owner |
| Phone | An authenticator app, for the sign-in's second step |

## Install (one time)

1. Go to the pilot site, [xatc.bandd.cloud](https://xatc.bandd.cloud), and sign in with your xatc-agent account. Open **Download**, choose **Linux (x86_64 AppImage)**, then press **Download for Linux**. The file is `xatc-agent-<version>-x86_64.AppImage`.
2. Make it executable. Either:
    - in your file manager, open the file's **Properties** and tick **Allow executing as program**; or
    - in a terminal, run `chmod +x xatc-agent-<version>-x86_64.AppImage`.
3. Run it by double-clicking it (or `./xatc-agent-<version>-x86_64.AppImage` in a terminal). The **xatc-agent** window opens.
4. Allow the microphone if your desktop asks.

If the file will not start and the message mentions FUSE, run it in a terminal as `APPIMAGE_EXTRACT_AND_RUN=1 ./xatc-agent-<version>-x86_64.AppImage`.

The file is not signed. The Download page shows the file's **SHA-256**; to check that your copy is the one the page describes, run `sha256sum xatc-agent-<version>-x86_64.AppImage` and compare the result with the page. Download the file only from the Download page while signed in.

From here, [sign in and choose your audio](getting-started.md#sign-in) exactly as on Windows.

## Add xatc-agent to your app menu

The first time you run the AppImage, the window offers to add xatc-agent to your app menu: **Add** or **Not now**. **Add** gives you a menu entry and an icon, so you can start it like any other app. **Settings > Your setup** has the same thing, under **App menu**: **Add to app menu**, and **Remove from app menu** to undo it.

The menu entry points at the AppImage file where it is now. If you move the file, add the entry again from **Settings > Your setup > App menu**.

## Staying signed in

You stay signed in for 30 days, across restarts, when your desktop has a keyring (GNOME Keyring or KWallet), which the app uses to keep your sign-in. The sign-in is never written to a file. Most desktop distributions set a keyring up for you. Without one, the app still works, but you sign in each time you start it.

## Updates

The app asks the pilot site for the newest version when it starts, and once a day while it is open. A newer version shows a banner: **What changed**, **Update now** and **Later**. The banner waits until your flight has ended, and nothing is installed during a flight.

**Update now** replaces the AppImage file with the new version, checks it first, and opens the app again by itself. Because it replaces the file, the AppImage must be somewhere you can write to, such as your home folder. Until Linux is in a stable release, newer Linux builds are prereleases, and the app offers a prerelease only when **Receive prereleases** is on in **Settings > Your account > Updates**: see [Updates](settings.md#updates). If an update fails, your old file is left as it was and the banner says why.

## Where things are kept

| What | Where |
|---|---|
| Settings | `~/.config/xatc-agent-client/settings.json` |
| The log file | `~/.config/xatc-agent-client/logs/xatc-agent-client.log` |
| Your sign-in | Your keyring, under `xatc-agent-client`. Never in a file |

To remove the app, delete the AppImage file and, if you added it, use **Remove from app menu** first. The settings folder stays until you delete it.

## Next

[Sign in](getting-started.md#sign-in), then [your first flight](first-flight.md).
