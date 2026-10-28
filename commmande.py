import subprocess
import sys

def wifi_scan():
    try:
        result=subprocess.run(
                    ["netsh","wlan","show","networks","mode=bssid"],
                       capture_output=True,
                       text=True,
                       check=True
                       )
        print(f"Nearby Wifi Networks..")
        print(result.stdout)
    except FileNotFoundError:
        sys.exit("File not found")
    except subprocess.CalledProcessError:
        sys.exit('Cant find wifi networks check your wifi adapter')

wifi_scan()

