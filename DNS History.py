import subprocess
import re
from datetime import datetime

def check_dns_history(domain):
    """
    Check DNS history for a specific domain and display details.

    Args:
        domain (str): The domain to search for in the DNS cache.
    """
    try:
        # Get the current date and time
        execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nExecution Date and Time: {execution_date}")
        print(f"Checking DNS history for domain: {domain}")
        print("-" * 50)

        # Run the ipconfig /displaydns command to fetch DNS cache
        process = subprocess.run(["ipconfig", "/displaydns"], capture_output=True, text=True, shell=True)
        
        if process.returncode != 0:
            print("Error: Unable to retrieve DNS cache. Ensure 'ipconfig /displaydns' works on this system.")
            return

        # Get the DNS cache output
        dns_output = process.stdout

        # Define a regex pattern to match records for the given domain
        domain_pattern = rf"{re.escape(domain)}.*?(\n\s+.*)+"
        matches = re.findall(domain_pattern, dns_output, re.IGNORECASE)

        if matches:
            print(f"\nDNS history for domain '{domain}':\n")
            for match in matches:
                # Display the DNS record details
                print(match.strip())
                print("-" * 50)

                # Attempt to extract and display TTL (Time To Live) values
                ttl_match = re.search(r"Time To Live\s*:\s*(\d+)", match)
                if ttl_match:
                    ttl_seconds = int(ttl_match.group(1))
                    ttl_expiry = datetime.now() + timedelta(seconds=ttl_seconds)
                    print(f"Record will expire approximately on: {ttl_expiry}")
                    print("-" * 50)
        else:
            print(f"No DNS history found for domain: {domain}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the domain to check
    print("DNS History Checker")
    print("-" * 50)
    domain_to_check = input("Enter the domain to check: ").strip()

    if domain_to_check:
        check_dns_history(domain_to_check)
    else:
        print("Error: Invalid input. Please enter a valid domain name.")
