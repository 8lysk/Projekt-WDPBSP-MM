import jsbsim
import os

# uruchomienie jsbsim do pobrania danych
fdm = jsbsim.FGFDMExec(None) 
fdm.load_script('scripts/f16_test.xml')  # mozna wybrac obojetnie jaki skrpyt a program bedzie dzialal
fdm.run_ic()  # uruchomienie symulacji

# wykorzystalem tutaj z uruchomienei programu z thread'a na githubie (nie do konca wiedzialem jak uruchomic program w pythonie)




# zapis danych w pliku 
output_file = os.path.join(os.getcwd(), "f16_simulation_data.txt")

# otowrzenie pliku i wpsianie kolumn
with open(output_file, 'w') as file:
    file.write("Time, Altitude, Velocity, Roll, Pitch, Yaw, Ailerons, Flaps, Elevator, Rudder,fcs/left-aileron-control,fcs/right-aileron-control,fcs/flaps-control,fcs/rudder-control\n")
    
    # uruchomienie symulacji 
    while fdm.run():
        # pobranie czasu
        time = fdm.get_sim_time()
        
        # pobranie danych
        altitude = fdm.get_property_value("position/h-sl-ft")  # Altitude in feet
        velocity = fdm.get_property_value("velocities/vt-fps")  # Velocity in ft/s
        roll = fdm.get_property_value("attitude/phi-rad")  # Roll angle in radians
        pitch = fdm.get_property_value("attitude/theta-rad")  # Pitch angle in radians
        yaw = fdm.get_property_value("attitude/psi-rad")  # Yaw angle in radians
        
        left_aileron = fdm.get_property_value("fcs/left-aileron-control")
        right_aileron = fdm.get_property_value("fcs/right-aileron-control")
        flaps = fdm.get_property_value("fcs/flaps-control")
        rudder = fdm.get_property_value("fcs/rudder-control")
        
        # zapisanie pobranych danych do pliku
        file.write(f"{time}, {altitude}, {velocity}, {roll}, {pitch}, {yaw}, {left_aileron},{right_aileron},{flaps},{rudder}\n")

print("gotowe")