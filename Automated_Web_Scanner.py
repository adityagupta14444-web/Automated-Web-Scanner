"""
Automated Web Scanner - beginner project
Checks visible response headers on a website you own or have permission to assess.
This is a basic configuration checker, not a penetration-testing tool.
"""
from urllib.parse import urlparse
import sys
import requests

HEADERS_TO_CHECK = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def validate_url(value):
    value = value.strip()
    if not value:
        raise ValueError("URL cannot be empty.")
    if "://" not in value:
        value = "https://" + value
    parts = urlparse(value)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError("Enter a valid http:// or https:// URL.")
    if parts.username or parts.password:
        raise ValueError("Do not include usernames or passwords in the URL.")
    return value

def scan(url):
    try:
        response = requests.get(
            url, timeout=10, allow_redirects=True,
            headers={"User-Agent": "Beginner-Automated-Web-Scanner/1.0"}
        )
    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        return

    print("\n--- SCAN SUMMARY ---")
    print("HTTP status:", response.status_code)
    print("Final URL:", response.url)
    print("HTTPS used:", urlparse(response.url).scheme == "https")
    print("\n--- SECURITY HEADER OBSERVATIONS ---")
    for header in HEADERS_TO_CHECK:
        value = response.headers.get(header)
        if value:
            print("[PRESENT]", header, ":", value)
        else:
            print("[NOT OBSERVED]", header)

    print("\n--- CORS OBSERVATION ---")
    cors = response.headers.get("Access-Control-Allow-Origin")
    credentials = response.headers.get("Access-Control-Allow-Credentials")
    if cors:
        print("Access-Control-Allow-Origin:", cors)
        if cors == "*" and credentials and credentials.lower() == "true":
            print("NOTICE: Review this configuration and actual CORS behavior.")
        else:
            print("Header observed; this alone does not prove a CORS flaw.")
    else:
        print("Access-Control-Allow-Origin was not observed in this response.")
        print("This alone does not prove a CORS problem.")

    print("\nLimitations: Checks only visible response headers.")
    print("Missing headers or CORS observations are not automatically vulnerabilities.")

def main():
    print("AUTOMATED WEB SCANNER")
    print("Only scan a site you own or have permission to check.")
    try:
        url = validate_url(input("Enter website URL: "))
    except ValueError as error:
        print("Input error:", error)
        sys.exit(1)

    permission = input("Do you own this site or have permission? (yes/no): ")
    if permission.strip().lower() != "yes":
        print("Stopped. Permission is required.")
        return
    scan(url)

if __name__ == "__main__":
    main()
