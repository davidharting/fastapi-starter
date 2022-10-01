import typing
from contextlib import contextmanager

from attr import dataclass
from fastapi.testclient import TestClient

from fastapi_starter.main import app


@dataclass
class FeatureTestContext:
    client: TestClient


@contextmanager
def test_context() -> typing.Generator[FeatureTestContext, None, None]:
    """
    Setup the environment for a feature test and yield a test context to the caller.
    It is expected to need to use this feature test context for most, if not all, feature tests.
    If this test context does not suit your needs, we can add parameters to it to allow for customization. Or perhaps additional test context managers need to be created.
    """
    context = FeatureTestContext(client=TestClient(app))
    yield context
