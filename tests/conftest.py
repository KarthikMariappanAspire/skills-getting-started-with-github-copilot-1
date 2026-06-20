from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_activities_state():
    """Reset in-memory activities state between tests."""
    # Arrange
    baseline = deepcopy(activities)

    yield

    # Assert isolation for the next test by restoring shared state.
    activities.clear()
    activities.update(deepcopy(baseline))
