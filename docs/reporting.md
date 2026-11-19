# Reporting a problem

If ATC mishears you, says something wrong or does not answer, tell us from inside the client. There is no other website to go to.

!!! note "Coming in the next client release"
    This page describes a client version that is not released yet. Your client does not have the Flag button, the flags in the Log or the Feedback view until it is updated.

You can report in three ways. A report about a flight is attached to that flight, so the call is seen in its place by the owner, the ATC expert and the testers, who already review flights. Ideas and bugs that are not about a flight are listed in one place for the owner and the ATC expert only.

## Flag a moment while you fly

Nothing is sent while you fly, so there is nothing to type at the wrong time.

- Press the **Flag** button in the flight row, beside **End flight**. It only shows while a flight is on.
- Or set a joystick button: in **Settings > Controls > Flag a moment**, press **Learn button** and then the button within 10 seconds. X-Plane must be running, because the client reads the button through X-Plane. A button that is already your push-to-talk button is refused.

Either way the client notes the time and the latest call, and shows "Flagged at 14:21:07" with **Undo** for 10 seconds. A second press within 5 seconds is ignored, so a bouncing button does not flag twice.

Describe your flags afterwards, when you end the flight (below) or later in the Feedback view, where they wait under **Not sent yet**. A flag you have not described is dropped after 30 days.

## Report a call from the Log

Each radio call in the Log has a small flag button (it shows when you point at the line or focus it, and always on a touch screen). Press it, pick what went wrong, add a note if you like, and press **Send**. The line then shows a filled flag.

The choices are:

| You pick | It means |
|---|---|
| ATC misheard me | The words written down are not what you said |
| Wrong instruction | ATC gave a heading, altitude, frequency or route that is wrong |
| Not what a controller would say | The instruction is allowed, but a real controller would not put it that way |
| Hard to understand | The spoken reply is hard to follow |
| No answer | You called and nothing came back, or ATC missed something it should have called |
| The client did something wrong / Something else | Anything that does not fit above |

## The Feedback view

The **Feedback** view sits beside Radio and Settings. Use it at any time:

- Choose **Something's broken** or **An idea** and write in the one text box.
- **About** says what it concerns: your last flight, your last 5 flights or **Not about a flight**.
- **Attach the client's log file** is ticked by default on a bug. Untick it if you would rather not send it.

**Not sent yet** lists your flags that you have not described. **Your reports** lists what you have sent, with each one's status. The Feedback tab shows a count while you have flags to describe or a report's status has changed since you last looked.

## When you end a flight with flags

**End flight** lists your flags. Each shows its time, your altitude and the nearest call, with the same choices, a note and **Skip**. Then:

- **Send and end flight** sends the ones you described.
- **End without sending** ends the flight and keeps your flags under **Not sent yet** in the Feedback view. A flag you **Skip** also stays there.
- **Cancel** goes back to the flight.

If a flight ends another way (ATC ends it, X-Plane closes, the client stops), your flags are kept under **Not sent yet** too.

## What a report sends

A report sends:

- what you wrote, and the choice you made
- the call or moment it is about, and the flight it belongs to
- the client's version, and, for feedback that is not about a flight, your computer's system
- the newest part of the client's log file, only if **Attach the client's log file** is ticked

The log file holds your callsign, airports and times. It never holds your audio or your sign-in. A log file is kept for 180 days. The owner and the ATC expert read reports; a report about a flight is also seen by the testers, like the flight itself. Only the owner and the ATC expert see feedback that is not about a flight, and log files. Reports and their log files are deleted with your account. [Your data](privacy.md#reports-you-send) says the rest.

A report adds nothing to what is recorded: if you allowed recording, the call's audio is already kept as described in [Your data](privacy.md#recordings-of-your-voice), and if you did not, a report does not change that.

## What the statuses mean

| Status | Meaning |
|---|---|
| **Received** | It reached us and nobody has started on it |
| **Looking into it** | Someone is working out the cause |
| **Fixed** | A fix is made. It reaches you in a later update of the client or of ATC, so you may not see it yet |
| **Closed** | We decided not to change anything for this one. The reason is not shown to you |

## The limit

You can send up to 30 reports a day. Past that the client says "You've sent a lot today. Try again tomorrow." Each flag you send when you end a flight counts as one report; flags you have not described are not counted until you send them. A note can be up to 2,000 characters.
