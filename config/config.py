"""Central configuration for the test suite.

All settings are read once, here, from environment variables (optionally loaded
from a local ``.env`` file). Tests and fixtures import ``settings`` from this
module instead of hard-coding values such as the base URL or timeouts.

Why do it this way?
    * One single source of truth -> change the URL in one place.
    * The same tests can run against different environments just by changing
      environment variables (great for CI/CD later on).
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load variables from a local ".env" file if it exists.
load_dotenv()


def _get_int(name: str, default: int) -> int:
    """Read an environment variable and interpret it as an integer."""
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return int(value)


@dataclass(frozen=True)
class Settings:
    """Immutable bundle of all configuration values.

    Note: browser choice, headed mode and slow-mo are controlled with the
    native ``pytest-playwright`` command-line flags (``--browser``, ``--headed``,
    ``--slowmo``) -- see the README. We only keep here the settings that do not
    have a convenient built-in flag.
    """

    # OrangeHRM's open-source demo. Every URL in the app lives under this path
    # (e.g. <base>/auth/login, <base>/pim/addEmployee).
    base_url: str = os.getenv(
        "BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php"
    )
    default_timeout: int = _get_int("DEFAULT_TIMEOUT", 30_000)

    # The administrator account that ships with the OrangeHRM demo. It always
    # exists and has full access, which makes it the reliable way to test the
    # logged-in features.
    # (Prefixed with ORANGEHRM_ because a plain USERNAME is a reserved
    #  environment variable on Windows and would resolve to your OS login name.)
    username: str = os.getenv("ORANGEHRM_USERNAME", "Admin")
    password: str = os.getenv("ORANGEHRM_PASSWORD", "admin123")

    @property
    def login_url(self) -> str:
        """Full URL of the login page."""
        return f"{self.base_url}/auth/login"


# A ready-to-use, shared instance. Import this everywhere:
#     from config.config import settings
settings = Settings()
