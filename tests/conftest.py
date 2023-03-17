import pytest

pytest_plugins = "pytest_pulp_cli"


@pytest.fixture
def pulp_cli_vars(pulp_cli_vars):
    result = {}
    result.update(pulp_cli_vars)
    result.update(
        {
            "MAVEN_REMOTE_URL": "https://repo1.maven.org/maven2/",
        }
    )
    return result
