from unittest.mock import patch

from monobank.api_wrapper import MonobankApiWrapper


def test_api_wrapper_fetch_user_info_and_statements(
    monobank_api_client_info_stub,
    monobank_api_client_statements_stub,
    test_api_token,
    expected_user_info,
    expected_user_transactions,
):
    with patch("monobank.api_wrapper.MonobankApiWrapper.fetch_user_info", lambda _: monobank_api_client_info_stub):
        api_wrapper = MonobankApiWrapper(api_token=test_api_token)
    assert api_wrapper.user_info == expected_user_info

    with patch("requests.Response.json", lambda _: monobank_api_client_statements_stub):
        jar_transactions = api_wrapper.fetch_jar_transactions_by_id("kKGVoZuHWzqVoZuH")
    assert jar_transactions == expected_user_transactions
