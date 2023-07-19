#!/bin/bash
set -o pipefail

# Run the Flask server, using the pact_provider.py as the app to be able to
# inject the provider_states endpoint
FLASK_APP=tests/pact_provider.py python -m flask run -p 5001 &
FLASK_PID=$!

function teardown {
  echo "Tearing down Flask server: ${FLASK_PID}"
  kill -9 $FLASK_PID
}
trap teardown EXIT

sleep 1

echo $@
pytest tests $@
