import yaml
import json
from pathlib import Path
from typing import Tuple


def load_test_config(path="config/browser_config.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)


def load_account(path: str = "config/account.json",
                 profile: str = "default",
                 account: str = "itaka",
                 role: str = "administrator") -> Tuple[str, str]:
    """
    Returns (username, password) from the account.json file.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"The file does not exist: {path}")

    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        creds = data[profile]["account"][account][role]
        return creds["username"], creds["password"]
    except KeyError as e:
        raise KeyError(f"No path found in {path}: {e}")


def load_url_value(key: str, env: str = "testing") -> str:
    """
    Returns the URL value for the specified key (e.g. "main_url", "sign_out_url")
    from the config/url.json file for the specified environment.
    """
    path = Path("config/url.json")
    if not path.exists():
        raise FileNotFoundError(f"The file does not exist: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        return data[env][key]
    except KeyError as e:
        raise KeyError(
            f"The key '{key}' is missing in config/url.json for the environment '{env}': {e}"
        )
