# Next excersize:
# Simulate controlled flight of F-16 (trying barrel roll), read flight data and make graphs accordnigly

import jsbsim
import matplotlib.pyplot as plt
import math

# This excersize requires loading in aircraft, turning the engine and adjusting the conditions to my liking
# Path to JSBSim files, location of the folders "aircraft", "engines" and "systems"
PATH_TO_JSBSIM_FILES="C:\\Users\marcz\AppData\Local\JSBSim"

fdm = jsbsim.FGFDMExec(PATH_TO_JSBSIM_FILES)  

# Load the F16 aircraft model
fdm.load_model('f16') 

# Set engine running
fdm['propulsion/engine[0]/set-running'] = 1

# Results
results = []

# Initial conditions
fdm['ic/h-sl-ft'] = 40000
fdm['ic/vc-kts'] = 800


# Initialize aircraft with initial conditions
fdm.run_ic()

# I copied these lines 33-37 from github disscusion becacause i had no clue how to trim the aircraft so it would stablize it's flight after
# doing the barrel roll
# Attempt to trim the aircraft
# try:
#     fdm['simulation/do_simple_trim'] = 1
# except RuntimeError as e:
#     if e.args[0] != 'Trim Failed':
#         raise

# Simulation settings
results = []
sim_duration = 100  # Total simulation time in seconds
time_step = 0.01  # Simulation steps in seconds

# Main simulation loop
while fdm.get_sim_time() < sim_duration:
    sim_time = fdm.get_sim_time()
    
    # Perform a barrel roll between 10s and 20s
    if 10 < sim_time < 30:
        progress = (sim_time - 10) / 10  # Normalized progress (0 to 1) during the maneuver

        # ok that was counterintuituve, in orderto pitch up we need to pull the stick not push it (facepalm)
        fdm["fcs/elevator-cmd-norm"] = -0.9

        
    else:
        # that does nothing it just kills the controls, but the aircraft can still be going up or down
        fdm["fcs/elevator-cmd-norm"] = 0
    
   
    # Run simulation step
    fdm.run()

    # Extract flight data
    time = fdm.get_sim_time()
    alt = fdm['position/h-sl-ft']          # Altitude in feet
    pitch = fdm['attitude/pitch-rad'] * 57.29578      # Pitch angle in degrees
    roll = fdm['attitude/roll-rad'] * 57.29578  # Roll angle in degrees

    # Save results
    results.append((time, alt, pitch))

# Extract the results
time, alt, pitch = zip(*results)

# Altitude plot
plt.subplot(2, 1, 1)
plt.plot(time, alt, label='Altitude (ft)', color='purple')
plt.title("F-16 Barrel Roll")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (ft)")
plt.grid(True)
plt.legend()

# Roll angle plot
plt.subplot(2, 1, 2)
plt.plot(time, pitch, label='pitch Angle (deg)', color='red')
plt.xlabel("Time (s)")
plt.ylabel("pitch Angle (deg)")
plt.grid(True)
plt.legend()

# Plot height adjustment
plt.subplots_adjust(hspace=0.5)

plt.legend()
plt.show()