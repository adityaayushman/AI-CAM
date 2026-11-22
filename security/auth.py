import hmac
import os

# Demo-grade guard. Set CLASSROOM_API_KEY to use your own key. The built-in
# default is public (it is in this repository), so do not rely on it beyond local use.
API_KEY = os.environ.get("CLASSROOM_API_KEY", "classroom_secure_key")


def verify(key):
    if not key:
        return False
    return hmac.compare_digest(str(key), API_KEY)
