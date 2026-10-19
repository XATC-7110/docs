# ATIS and weather

ATC's weather is the weather in your X-Plane.

## The ATIS

Tune an airport's ATIS frequency on COM1 or COM2 and the recording loops, starting mid-broadcast like the real thing. The radio must be on and selected to listen on your audio panel, or you hear nothing. Tune away, or switch the radio off, and it stops. A new letter takes over at the next loop. ATC's calls and your own transmissions come first; the loop picks up again after them.

It gives the information letter, the time, the wind, visibility, the sky, temperature, the altimeter, and the runways and approach in use.

- **The letter** starts at a random one and advances when the weather changes enough to matter: the wind turns 10 degrees or changes 5 knots, the altimeter moves 0.02, or the ceiling or visibility crosses a limit (500, 1,000 or 3,000 ft, 1 or 3 miles, and the instrument-condition limits). A change has to hold for a minute, and letters come at least two minutes apart. A change of runway or approach in use, and wind shear starting or stopping, advance it at once. It advances while you are on the ground at the airport (or, for your destination, while the weather estimate can change); in the air the destination's letter holds.
- **Approach in use.** At a busy airport in good weather the ATIS names both: "ILS runway one six right approach in use, visual approaches in use."
- **Closing words.** "Read back all runway hold short instructions" and "Advise on initial contact you have information Charlie".
- **The sky** comes from X-Plane's cloud layers: "few", "scattered", "broken" or "overcast" with the height, and the ceiling named ("ceiling niner hundred overcast").
- **Gusts** are reported when the gust is 10 knots or more over the steady wind.
- **Wind shear** in your X-Plane weather becomes "wind shear reported", in the ATIS and in Tower's takeoff and landing clearances, when the shear is 10 degrees or more and the steady wind is over 10 knots.

The window names the ATIS on the radio tuned to it ("KSEA ATIS Charlie · looping"), tags each ATIS in the Frequencies card with its current letter, and puts the full text in the log while you listen.

## The letter on the radio

Say the letter on your first call: "with information Charlie". ATC remembers it for that airport. If you give no letter, the controller says "advise you have information Charlie". If you give an old one: "information Kilo is current, altimeter three zero zero two". "Confirm you have information Kilo, altimeter three zero zero two" is said when the letter changed since another controller had yours. Arriving, Approach checks the destination's letter, once. Departure and Center never ask.

## Weather in clearances

- Ground gives the wind and the altimeter with your taxi if you did not report the ATIS.
- Tower gives the wind with every takeoff and landing clearance.
- Radar controllers give the altimeter when you check in and when you start down.
- The runway in use follows the wind. A wind shift can change the runway while you taxi, and Ground then gives you a new route.

## Weather stations

An airport with no ATIS but an automated weather station (AWOS or ASOS) has a broadcast of its own, with no information letter and a new observation each minute: the station's name, "automated weather observation", the time, wind, visibility, sky, temperature and dew point, and the altimeter. A missing element is said as missing. It plays only while a radio on and selected to listen is tuned to it, and only near the airport. The window's radio card names it, and the Frequencies card tags it **automated weather**.

## Where the weather comes from

The client samples the weather at your aircraft about every five seconds and sends it with its once-a-second state: wind, pressure, temperature, visibility, gusts, wind shear and cloud layers. For an airport you are not at yet, ATC uses X-Plane's regional weather as its estimate. Nothing is fetched from the real world, so ATC always agrees with what you see out of the window.
