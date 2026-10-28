# Send a plan to your account

If you plan your flights in ForeFlight or another planning app, you do not have to type the plan into the client. Send the plan file to your SeventyOneTen account, from your iPhone or from the pilot site, then load it in the client with **New flight > From my account**.

!!! info "A prerelease, for now"
    **From my account** is in the client's 0.20 prereleases (since 0.20.0-rc.10). The stable client, 0.19.0, does not have it. Sending a plan from the pilot site works for everyone with an account. The iPhone app is a test version for invited testers.

## What a plan file is

SeventyOneTen reads three kinds of file:

- `.fpl`, the flight plan file that ForeFlight exports;
- `.gfp`, a plain text plan;
- `.gpx`, a GPX route file.

From the file it takes the **departure**, the **destination**, the **route**, the **cruise altitude** and the **tail number**. A flight of two airports with no fixes in between is a direct flight, and its route stays empty with no "missing" mark. The file must be no larger than 256 KB.

## Send a plan from your iPhone

The iPhone app is called **SeventyOneTen**. It is available through TestFlight, Apple's test program, to testers the owner has invited.

1. Open the app once and press **Sign in**. You sign in with your SeventyOneTen account, as in the client.
2. In ForeFlight, open the flight, tap **Share**, and choose **SeventyOneTen** from the Share menu.
3. A card shows the file. Nothing is sent until you tap **Send**. If the file is not a flight plan the card says so, and nothing is sent.

The app's home screen lists the plans you sent recently, and has **Sign out**.

## Send a plan from the pilot site

1. Sign in to the pilot site, [app.7110atc.com](https://app.7110atc.com), and open **Send a plan** (beside **Download**).
2. In ForeFlight, open the flight, tap **Share**, then **Save to Files**. Then choose the file on the page. It is sent as soon as you choose it.
3. The page shows what it found in the file, and says what is not in it. Anything the file lacks, you fill in when you start the flight.

**Your recent plans** on that page lists what you sent.

## Load the plan in the client

1. Press **New flight**, and choose the **From my account** tab.
2. The tab shows your newest plan: the two airports, the route, the cruise altitude and the tail number, and when and from where it was sent, such as "Sent from your iPhone, 2 min ago".
3. Press **Use this plan**. It fills in the flight plan for you to check. Anything the plan lacks is left empty and marked.
4. Check the fields, then press **Start flight**.

The tail number from the plan fills only an empty **Tail number** field, so it never replaces a callsign you already entered. Starting the flight marks the plan as used.

If you are not signed in, the tab has a **Sign in** button. If the plan could not be fetched, it has **Try again**.

## What is kept

SeventyOneTen keeps your **five most recent plans**: the airports, route, altitude and tail number in each, and the file's name. The file itself is not stored. Older plans are removed as new ones arrive, and all of them are deleted with your account. See [Your data](privacy.md#plans-you-send-to-your-account).

## Next

[Your first flight](first-flight.md).
