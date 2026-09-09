#!/usr/bin/env python3
"""Advanced IP Lookup Tool"""

import requests
import sys
import json

def ipinfo_lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    r = requests.get(url)
    return r.json()

def ipapi_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    r = requests.get(url)
    return r.json()

def ipwhois_lookup(ip):
    url = f"https://ipwho.is/{ip}"
    r = requests.get(url)
    return r.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: python ip_lookup.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]
    print(f"\n[+] Scanning IP: {ip}\n")

    print("[1] ipinfo.io")
    try:
        data = ipinfo_lookup(ip)
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"[-] Error: {e}")

    print("\n[2] ip-api.com")
    try:
        data = ipapi_lookup(ip)
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"[-] Error: {e}")

    print("\n[3] ipwho.is")
    try:
        data = ipwhois_lookup(ip)
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()
