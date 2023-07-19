import logging

import pytest
from pact import Verifier

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


PROVIDER_URL = "http://localhost:5001"

@pytest.fixture
def broker_opts(request):
    broker_token = request.config.getoption("--broker-token")
    broker_url = request.config.getoption("--broker-url")
    publisher_version = request.config.getoption("--publisher-version")
    published = request.config.getoption("--publish-verification")
    return {
        "broker_token": broker_token,
        "broker_url": broker_url,
        "publish_version": publisher_version,
        "publish_verification_results": published,
    }

def test_user_service_provider_against_broker(broker_opts):
    verifier = Verifier(provider="CDCT-provider", provider_base_url=PROVIDER_URL)

    success, _ = verifier.verify_with_broker(
        **broker_opts,
        verbose=True,
        provider_states_setup_url=f"{PROVIDER_URL}/_pact/provider_states",
        enable_pending=False,
    )
    assert success == 0
