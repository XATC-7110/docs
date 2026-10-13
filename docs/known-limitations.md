# Known limitations

xatc is an invitation-only experiment under active development. These are the edges as of 2026-10-13; each will be removed from this page when it is fixed.

- **IFR only.** Every flight is an IFR flight. VFR departures, pattern work, flight following and VFR arrivals are not built.
- **The United States first.** The FAA's data covers the US only. Elsewhere ATC works from your X-Plane's own navigation data for the airport's procedures, fixes and frequencies, and it has no airspace boundaries, Center sectors or minimum vectoring altitudes for the area, so expect less of it there. The project has not flown outside the US. See [Your X-Plane's data](client/xplane-data.md).
- **Windows, and X-Plane 12.1.4 or newer.** The client is a Windows 10 or 11 app and talks to X-Plane through its own Web API. X-Plane has had that API since 12.1.1, and the client needs the version of it that arrived in 12.1.4. Laminar is still extending it release by release, so use the current X-Plane 12. Tested on 12.4.3. There is no macOS or Linux client, and it does not work with X-Plane 11 or other simulators. With an older X-Plane 12 the client shows **X-Plane: not connected**: see [X-Plane too old](troubleshooting.md#x-plane-too-old).
- **The X-Plane data pack replaces the FAA procedure file.** ATC flies the FAA's procedures of the current cycle. **Settings > X-Plane data** can install them into X-Plane's `Custom Data` folder so your aircraft's FMS and ATC agree. While the pack is installed, X-Plane's own GPS shows the FAA's procedures too, and **Remove** puts your files back. See [FAA procedures for your X-Plane](client/xplane-data.md#faa-procedures-for-your-x-plane).
- **Clearances by phone at fields without a tower.** At an airport with no control tower and no radio way to reach Clearance Delivery, the Frequencies card has a **Clearance Delivery · by phone** row instead of a frequency. You call the overlying approach control (or the Center) from the window, on the ground only, never Flight Service. The clearance ends with "hold for release": you call back when you are number one for departure and are given a release with a void time.
- **Some replies are still intermittent.** In a small number of situations the controller answers correctly most of the time, but not every time. The list shrinks with each release.
- **Controller voices.** All the voices are synthetic and speak American English; the radio voices add regional American accents. **Settings > Audio** has four choices for **ATC voices**: the radio voices, which give each controller a distinct voice and already sound like a radio, and three standard voices from the most robotic to the most natural. See [Settings](settings.md#audio).
- **One client per PC.** Starting the client again brings the window that is already open to the front.

## If you hit something that is not here

Say what you said, what you expected and the time, and send the log file: see [Reporting a problem](troubleshooting.md#reporting-a-problem).
