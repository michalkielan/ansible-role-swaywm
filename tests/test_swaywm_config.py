""" swaywm config tests"""

import pytest
import subprocess
from pathlib import Path
import ansible_runner


class SwayConfigValidationError(Exception):
    """Exception raised when sway config is invalid."""


def validate_sway_config(config_file):
    """Validate sway config file"""
    try:
        subprocess.run(
            ["sway", "--config", config_file, "--validate", "--debug"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        raise SwayConfigValidationError(
            f"Config file {config_file} is invalid: {exc.stderr.decode()}"
        ) from exc


@pytest.mark.parametrize("playbook_file", ["minimal_example.yml", "full_example.yml"])
def test_minimal_examle(playbook_file):
    """Minimal working example"""
    result = ansible_runner.run(
        private_data_dir="./tests",
        inventory=["localhost"],
        playbook=playbook_file,
    )
    assert result.rc == 0, f"Playbook failed with {result.rc}."
    config_file = Path.home() / ".config" / "sway" / "config"
    validate_sway_config(config_file)
