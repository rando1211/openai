# openai

This repository includes a script for migrating contact data from Hubspot to the Go High Level (GHL) CRM using their respective APIs.

## Prerequisites

- Python 3.8+
- The `requests` library (`pip install requests`)
- Hubspot and GHL API tokens exported as environment variables:
  - `HUBSPOT_API_TOKEN`
  - `GHL_API_TOKEN`

## Usage

Run the migration script from the command line:

```bash
python hubspot_to_ghl.py
```

The script fetches contacts from Hubspot and creates corresponding contacts in GHL.
