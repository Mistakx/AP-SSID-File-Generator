file_location: str = "/home/mistakx/Desktop/SSIDs"
ap_ssid: str = "Test"

with open(file_location, "w") as file:
    for i in range(1000):
        file.write(f"{ap_ssid}{i}\n")