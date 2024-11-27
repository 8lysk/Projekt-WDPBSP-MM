import pandas as pd
import matplotlib.pyplot as plt

# wczytanie
file_path = "f16_simulation_data.txt" 
data = pd.read_csv(file_path)

# znalazlem problem ze spacjami
# rozwiaznie == usuniecie spacji z kolumn zaczelo dzialac
# na chwile haha

data.columns = data.columns.str.strip()


# skomentowany kod, debbugowawalem kod
# print
#print("kolumny:", data.columns)
#print(data.head())

# zmiana z radinaow na stopnie
data['Roll (deg)'] = data['Roll'] * (180 / 3.14)
data['Pitch (deg)'] = data['Pitch'] * (180 / 3.14)
data['Yaw (deg)'] = data['Yaw'] * (180 / 3.14)

# wysokosc
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Altitude'], label='Altitude (ft)')
plt.title("Altitude vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (ft)")
plt.grid(True)
plt.legend()
plt.show()

# predkosc
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Velocity'], label='Velocity (ft/s)', color='orange')
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (ft/s)")
plt.grid(True)
plt.legend()
plt.show()

# odchylenia pochylenia
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Roll (deg)'], label='Roll (deg)', color='red')
plt.plot(data['Time'], data['Pitch (deg)'], label='Pitch (deg)', color='green')
plt.plot(data['Time'], data['Yaw (deg)'], label='Yaw (deg)', color='blue')
plt.title("Attitude Angles vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)
plt.legend()
plt.show()

# lotki
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['fcs/left-aileron-control'], label='Left Aileron Control', color='blue')
plt.plot(data['Time'], data['fcs/right-aileron-control'], label='Right Aileron Control', color='orange')
plt.title("Aileron Control vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Control Position ")
plt.grid(True)
plt.legend()
plt.show()
#brak danych-------------

# klapy
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['fcs/flaps-control'], label='Flaps Control', color='purple')
plt.title("Flaps Control vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Flap Position")
plt.grid(True)
plt.legend()
plt.show()
#brak danych-------------

# stery
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['fcs/rudder-control'], label='Rudder Control', color='green')
plt.title("Rudder Control vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Rudder Position")
plt.grid(True)
plt.legend()
plt.show()
#brak danych-------------
# w trzech ostatnich wykresach nie doszedlem jeszcze do odczytania danych, bardzo mozliwym bledem jest sposob zapisu w test1.py, albo odczyt danych z pliku CSV
# sprobouje rozwiazac problem i dostarczyc rozwiazanie na kolejny termin

#testowanie srodowiska github


#symulacja w petli ze sterowaniem +obserwacje 