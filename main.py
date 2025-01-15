import requests, csv, sys

frequencies = [
    27.2584, 44.3475, 65.574, 91.6164, 123.122, 160.746, 205.164, 257.068,
    317.168, 386.189, 464.863, 553.931, 654.134, 766.209, 890.88, 1028.86,
    1180.84, 1347.49, 1529.42, 1727.23, 1941.47, 2172.62, 2421.12, 2687.33,
    2971.55, 3274.01, 3594.84, 3934.11, 4291.77, 4667.69, 5061.66, 5473.35,
    5902.32, 6348.04, 6809.87, 7287.07, 7778.78, 8284.06, 8801.83, 9330.94,
    9870.15, 10418.1, 10973.3, 11534.4, 12099.6, 12667.3, 13235.9, 13803.4,
    14368.2, 14928.3, 15481.8, 16026.8, 16561.4, 17083.7, 17591.8, 18083.7,
    18557.8, 19012, 19444.8, 19854.4
]

print("Head to the GSMArena specs page for your phone, and look at the end of the URL to find your phone's ID (usually four or five digits).")
print("For example, for the S23 Ultra, https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php yeilds an ID of 12024.")
phone_id = input("\nEnter the phone ID: ")

response = requests.get(f'https://www.gsmarena.com/speakertest-js.php3?idPhone={phone_id}')
try:
    if response.status_code == 200: 
        data = response.json()
        amplitudes = data[-1]
        filename = f"{data[1].lower()}-{data[2].lower().replace(' ', '-')}_gsm-raw-response.csv"
    else:
        print(f"Failed to retrieve data from https://www.gsmarena.com/speakertest-js.php3?idPhone={phone_id}.")
        print("Does your phone have testing data available in the new format?")
        sys.exit()
except:
    print(f"Failed to retrieve data from https://www.gsmarena.com/speakertest-js.php3?idPhone={phone_id}.")
    print("Does your phone have testing data available in the new format?")
    sys.exit()


if len(amplitudes) != len(frequencies):
    print(f"Error: amplitude/frequency count mismatch. Expected {str(len(frequencies))} amplitudes, got {str(len(amplitudes))}.")
    sys.exit()

with open(filename, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Frequency (Hz)", "Amplitude (dB)"]) 
    for freq, amplitude in zip(frequencies, amplitudes):
        writer.writerow([freq, amplitude])

print(f"file successfully created: {filename}")

