# steelseries

A simple wrapper for the SteelSeries GameSense API in Python.

## Features

- Register games and events with SteelSeries Engine
- Send live event data (0–100) to control RGB devices
- Built-in auto-sanitization of names

## Example

```python
#import steelseries under the name ss for simplicity
import steelseries as ss

# Register your game
ss.register_game("MYGAME", "NeoEmberArts", "Epic App Idea", iconcolorid=1)

# Register event(s)
ss.register_event("MYGAME", "HEALTH")
ss.register_event("MYGAME", "DAMAGE")

# Send basic data to that event
ss.send_event_data("MYGAME", "HEALTH", 88)

# Send animated data smoothly to 100 then bounce to 0
ss.send_event_data_interpolated("MYGAME", "HEALTH", 0, 100, duration=3.0, interval=0.2, easing="ease-out")
ss.send_event_data_interpolated("MYGAME", "HEALTH", 100, 0, duration=2.0, interval=0.01, easing="bounce-out")

# Remove Event
ss.remove_event("MYGAME", "DAMAGE")
          
# Remove app
ss.remove_game("MYGAME")

# full list of commands!
ss.help()
```
