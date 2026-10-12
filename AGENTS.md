# AGENTS.md: xatc-agent documentation

The public documentation site for xatc-agent, AI air traffic control for X-Plane 12. This repository is **public** so that GitHub Pages can serve it. The product's own repositories (the gateway, the client, the ATC view, the sign-in) are private.

## Requirements

- **A public repository for pilot-facing documentation** (owner, 2026-10-06: "can you create a new public repo that contains documentation about how to use, configure, the features of the agentic ai for xplane? It needs to be public so we can use github pages"). The site covers how to use it, how to configure it, and its features. It follows the older xatc documentation site: MkDocs Material, the `gh-pages` branch, a strict build.
- **The site looks like the product** (owner, 2026-10-06: "Make the theme cooler and match the overall color scheme of the product"). The colours are the client window's own tokens (its `style.css`: dark `#0d1117` / panel `#161b22` / border `#30363d` / accent `#58a6ff` / frequency green `#7ee787` / amber `#e3b341` / ATC blue `#79c0ff`, and its light set), in `docs/stylesheets/xatc.css`. Like the window, the site is **dark by default** with a switch to light, uses the system fonts (no web fonts are fetched), and a quote reads like a line of the window's log. The home page is a landing page: a hero with a radio call and the window, the flight's frequencies, and feature cards. When the client's colours change, change the tokens at the top of `xatc.css` to match. The hero's radar sweep stands still for anyone who asks for reduced motion; keep it that way.
- **A diagram of how the parts work together, and the cloud side kept vague** (owner, 2026-10-06: "also, make a diagram showing how the components interact", then "keep the aws bit vuage"). `docs/how-it-works.md` has the diagram: inline SVG styled by `xatc.css` (classes `g`, `b`, `m`, `s`: a group, plain code, an AI model, data), so it follows the theme switch. On the whole site the cloud is "the cloud": **no cloud provider and none of its services are named**, in text or in a picture. Say what a part does ("speech recognition", "an AI model", "text to speech", "the voice gateway", "the sign-in service"). The one exception is a label the pilot has to find in the client's window, such as Settings' **Runtime ARN**, which is quoted as the window shows it.
- **State the minimum X-Plane version** (owner, 2026-10-12, relayed by the reviewer session, verbatim: "IN the docs, include the minimum version of xplane. I know the websocket and rest api are being implemented slowly over time"). The floor is X-Plane 12.1.4: the client uses X-Plane's own Web API, which arrived in 12.1.1 and gained the commands the client needs in 12.1.4; tested on 12.4.3. It is in the requirements table of `docs/getting-started.md`, on the home page's X-Plane card, and in an "X-Plane too old" entry of `docs/troubleshooting.md`. Never write that 12.1.4 "is best"; it is the minimum. Describe what the client really does below the floor, not a message it does not show yet.
- **Correction to the minimum-version entry** (2026-10-12, from the coordinator, who had the Client Developer read Laminar's own Web API article and the client code again). The first version of the "X-Plane too old" entry said that on X-Plane 12.1.1 to 12.1.3 the client connects, swaps radios by writing frequencies and cannot pause: wrong. The first version of the Web API (datarefs) is 12.1.1 and up; the second is 12.1.4 and up and adds the root endpoint that reports the supported versions and the commands. The client's reachability probe and its X-Plane version both come from that endpoint (client `sim/webapi.py`), so on any X-Plane 12 older than 12.1.4 the request fails and the client shows "X-Plane: not connected" (detail "not reachable at host:port; retrying"). The entry now says only that, with the one fix: update X-Plane 12.
- **Record every requirement the owner states here**, dated, with his words, in the same change that carries it out.

## What must never be in this repository

Everything here is public, including the history. Before every commit, check that none of this is in it:

- cloud account ids, resource names or addresses (the gateway's runtime ARN, bucket names, the sign-in domain, the sign-in app client id, user pool ids);
- anyone's email address or name, including in screenshots (the client's demo data shows a real name: replace it before taking a screenshot);
- flight ids, session ids, recordings, transcripts or tracks of real flights;
- the cloud provider's name or its services' names (above), costs, and anything about the owner's cloud setup beyond what `docs/how-it-works.md` says;
- the private repositories' code, their internal notes, and the owner's or the testers' words from them.

The pilot gets the gateway address and the client package from the owner, privately. The site says so and never prints them.

## Writing

- **For pilots, not developers.** Say what the pilot sees and does. No wave numbers, protocol versions, pull request numbers or module names.
- **Only what is built.** A feature goes on the site when it is in a released client or gateway. What is not built is listed plainly ("Not built yet" in `docs/features/index.md`).
- **Phraseology in examples is illustrative.** Use the product's own example flight (N547GA, Seattle to Portland) and keep examples consistent with what the controller really says.
- **`docs/privacy.md` must stay true.** It describes what is sent and kept. Change it in the same change as any documentation of a feature that changes what is sent or kept, and quote the recording question's wording exactly as the client shows it.
- Screenshots come from the client's demo data, never from a real flight.

## Sources

The site is written from the private repositories, which stay the source of truth: the client's README (the window, settings, sign-in, sessions), the gateway's pilot capability map (what each position does) and its system overview (how it works). When they change, change the site.

## Checks

| What | Command |
|---|---|
| Build, strict | `mkdocs build --strict` |
| Preview | `mkdocs serve` |
| Publish (from a clean `main`) | `scripts/publish-docs.sh` |

## Git

Work goes on a branch and opens as a pull request. Commit messages end with the co-author line the harness gives.
