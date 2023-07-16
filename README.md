# Python ModLookup Client

This repository contains the Python client for the ModLookup service. The client provides an interface to interact with the ModLookup API, allowing you to retrieve Twitch streamer data and statistics.

## Deprecation Notice

**This project is now deprecated.** Due to changes in Twitch's API in February 2023, it is no longer possible to keep the ModLookup service operational. This repository is kept for historical purposes and reference, but it will not receive further updates or maintenance.

## Usage

The `ModLookupClient` class provides the following methods:

- `get_user(user: str, limit: int = 100, cursor: str = '')`: Retrieves data for a specific user. You can specify a limit for the number of results and a cursor for pagination.
- `get_user_total(user: str)`: Retrieves the total data for a specific user.
- `get_top()`: Retrieves data for the top users.
- `get_stats()`: Retrieves statistics data.

Here's a basic example of how to use the client:

```python
from modlookup_client import ModLookupClient

client = ModLookupClient()

# Get data for a specific user
user_data = client.get_user('username')

# Get total data for a specific user
user_total = client.get_user_total('username')

# Get data for top users
top_users = client.get_top()

# Get statistics data
stats = client.get_stats()
```

## Installation

You can clone this repository using git:

```bash
git clone https://github.com/johnsosoka/python-modlookup-client.git
cd python-modlookup-client
```

Then, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Contributing

As this project is deprecated, we are not accepting contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.