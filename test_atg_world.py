import requests

def test_atg_world_availability():
    """
    Test if atg.world website is available.
    """
    url = "https://www.atg.world/"
    timeout = 5  # seconds

    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            assert True, "atg.world website is available."
        else:
            raise AssertionError(f"Unexpected response code: {response.status_code}")
    except requests.exceptions.Timeout:
        raise AssertionError("Connection timed out. atg.world might be unavailable.")
    except Exception as e:
        raise AssertionError(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_atg_world_availability()
