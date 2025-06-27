#import steelseries under the name ss for simplicity
import steelseries as ss

# Register your game
ss.register_game("MYGAME", "Neo", "Cool App", iconcolorid=1)

# Register event
ss.register_event("MYGAME", "HEALTH")
ss.register_event("MYGAME", "DAMAGE")

# Send basic data to that event
ss.send_event_data("MYGAME", "HEALTH", 88)

# Send animated data
ss.send_event_data_interpolated("MYGAME", "HEALTH", 0, 100, duration=3.0, interval=0.2, easing="ease-out", False) # not silent
ss.send_event_data_interpolated("MYGAME", "HEALTH", 0, 100, 2.0, 0.05, easing="bounce-out", True) # silent

          
# Remove app
ss.remove_game("MYGAME")
