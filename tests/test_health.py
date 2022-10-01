from tests.context import test_context


def test_health():
    with test_context() as ctx:
        response = ctx.client.get("/healthz")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
