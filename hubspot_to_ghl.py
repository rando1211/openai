import os
import requests

HUBSPOT_API_TOKEN = os.getenv("HUBSPOT_API_TOKEN")
GHL_API_TOKEN = os.getenv("GHL_API_TOKEN")

HUBSPOT_BASE_URL = "https://api.hubapi.com"
GHL_BASE_URL = "https://rest.gohighlevel.com"

def fetch_hubspot_contacts():
    """Fetch contacts from Hubspot CRM."""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts"
    headers = {"Authorization": f"Bearer {HUBSPOT_API_TOKEN}"}
    params = {"limit": 100}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

def create_ghl_contact(contact):
    """Create a contact in GHL."""
    url = f"{GHL_BASE_URL}/v1/contacts/"
    headers = {
        "Authorization": f"Bearer {GHL_API_TOKEN}",
        "Content-Type": "application/json",
    }
    properties = contact.get("properties", {})
    data = {
        "firstName": properties.get("firstname", ""),
        "lastName": properties.get("lastname", ""),
        "email": properties.get("email", ""),
        "phone": properties.get("phone", ""),
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def migrate_contacts():
    contacts = fetch_hubspot_contacts()
    for contact in contacts:
        create_ghl_contact(contact)
    print(f"Migrated {len(contacts)} contacts")

if __name__ == "__main__":
    migrate_contacts()
