""" swaywm config tests"""

import subprocess
from pathlib import Path
import pytest
import ansible_runner


class SwayConfigValidationError(Exception):
    """Exception raised when sway config is invalid."""


def validate_sway_config(config_file):
    """Validate sway config file"""
    try:
        output = subprocess.run(
            ["sway", "--config", config_file, "--validate", "--debug"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("stdout:", output.stdout.decode())
        print("stderr:", output.stderr.decode())
        print("return code:", output.returncode)
    except subprocess.CalledProcessError as exc:
        raise SwayConfigValidationError(
            f"Config file {config_file} is invalid: {exc.stderr.decode()}"
        ) from exc


@pytest.mark.parametrize("playbook_file", ["minimal_example.yml", "full_example.yml"])
def test_valid_config(playbook_file):
    """Test valid config"""
    result = ansible_runner.run(
        private_data_dir="./tests",
        inventory=["localhost"],
        playbook=playbook_file,
    )
    assert result.rc == 0, f"Playbook failed with {result.rc}."
    config_file = Path.home() / ".config" / "sway" / "config"
    validate_sway_config(config_file)


@pytest.mark.parametrize(
    "playbook_file", ["desktop_background_scaling_mode_not_defined.yml"]
)
def test_invalid_config(playbook_file):
    """Test invalid config"""
    result = ansible_runner.run(
        private_data_dir="./tests",
        inventory=["localhost"],
        playbook=playbook_file,
    )
    assert result.rc == 0, f"Playbook failed with {result.rc}."
    config_file = Path.home() / ".config" / "sway" / "config"
    with pytest.raises(SwayConfigValidationError):
        validate_sway_config(config_file)
