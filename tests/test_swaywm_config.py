""" swaywm config tests"""

import ansible_runner


def test_minimal_examle():
    """Minimal working example"""
    result = ansible_runner.run(
        private_data_dir="./tests",
        inventory=["localhost"],
        playbook="minimal_example.yml",
    )
    assert result.rc == 0, f"Playbook failed with {result.rc}."
