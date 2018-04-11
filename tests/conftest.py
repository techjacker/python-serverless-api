import os
import pytest


@pytest.fixture(autouse=True)
def config_setting():
    """An application for the tests."""
    fallback_config = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '../config/testing.py'
        )
    )
    os.environ['APP_CONFIG_FILE'] = \
        os.environ.get('TEST_APP_CONFIG_FILE', fallback_config)
