# leash.io
Documentation for final project.

Problem

As hinted in the Context section, the problem is that of providing users in the Greater Seattle Area with a means to track a simple walking streak metric in a device that also stores their dog’s leash, as well as making a better outdoors preparedness strategy through weather data placed in the dog leash’s storage proximity.

Approach

Our approaches primarily revolved around understanding the confluence of the following parameters:

  Tracking walks
  
  A weather interface
  
  Small enough to be placed near the exit of one’s home

With these in mind, we started exploring various form factors and sensing modalities. We chose to have a visual output to present the user with the live weather data, as well as sensing a leash’s presence on the device. We narrowed down on a physical sensor capable of sensing the simple gravitational acceleration experienced by a dog leash. A micro-switch sufficed for the application, and we kept it as an integral design decision till the very end of the process.

We also considered using traditional sensors such as a photo-resistor or an ultrasound sensor behind a transparent, acrylic surface to sense the presence of a dog leash. Using a threshold value on the photo-resistor introduces sensing errors in a dark room. However, possible implementations of ultrasound sensors may prove useful for future design explorations for a similar problem space.

We envisioned the micro-switch being placed underneath a physical surface left free to move vertically under the weight of a dog leash. Mechanical actuation proved precise since it allowed for a binary ‘on’ or ‘off’ input into the central computer (a Raspberry Pi, in this case.) A dual-spring loaded mechanism is used to keep the press-able region under an outward directed tension.

Further experimentation with different types of buttons may reveal varying weight sensing thresholds and click feels. We did not do so for this project given the tight time constraints. However, we leave that as an unexplored avenue worthy of further investigation in the project’s future iterations.
