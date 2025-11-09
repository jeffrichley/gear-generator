import sys

import pytest

from generators.core.environment import checks


@pytest.mark.unit
def test_collect_environment_profile_reports_python_version_and_status():
    profile = checks.collect_environment_profile()

    assert profile.python_version.startswith(
        f"{sys.version_info.major}.{sys.version_info.minor}"
    )
    assert profile.status in {"ready", "missing-deps", "incompatible"}
    assert isinstance(profile.uv_active, bool)
    assert profile.packages, "Expected dependency list to be populated"


@pytest.mark.unit
def test_required_packages_reported_as_installed():
    profile = checks.collect_environment_profile()
    packages = {record.name: record.status for record in profile.packages}

    for dependency in checks.REQUIRED_PACKAGES:
        assert dependency in packages, f"Missing package record for {dependency}"
        assert packages[dependency] == "installed"


@pytest.mark.unit
def test_environment_profile_serializes_to_dict_and_back():
    profile = checks.collect_environment_profile()
    data = profile.to_dict()

    restored = checks.EnvironmentProfile.from_dict(data)
    assert restored == profile
