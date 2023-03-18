import pytest


@pytest.fixture
def test_api_token():
    return "aaaaaaaaaa"


@pytest.fixture
def expected_user_info():
    return {
        "clientId": "3MSaMMtczs",
        "name": "Мазепа Іван",
        "webHookUrl": "https://example.com/some_random_data_for_security",
        "permissions": "psfj",
        "accounts": [
            {
                "id": "kKGVoZuHWzqVoZuH",
                "sendId": "uHWzqVoZuH",
                "balance": 10000000,
                "creditLimit": 10000000,
                "type": "black",
                "currencyCode": 980,
                "cashbackType": "UAH",
                "maskedPan": [],
                "iban": "UA733220010000026201234567890",
            }
        ],
        "jars": [
            {
                "id": "kKGVoZuHWzqVoZuH",
                "sendId": "uHWzqVoZuH",
                "title": "На тепловізор",
                "description": "На тепловізор",
                "currencyCode": 980,
                "balance": 1000000,
                "goal": 10000000,
            }
        ],
    }


@pytest.fixture
def expected_user_transactions():
    return [
        {
            "id": "ZuHWzqkKGVo=",
            "time": 1554466347,
            "description": "Покупка щастя",
            "mcc": 7997,
            "originalMcc": 7997,
            "hold": False,
            "amount": -95000,
            "operationAmount": -95000,
            "currencyCode": 980,
            "commissionRate": 0,
            "cashbackAmount": 19000,
            "balance": 10050000,
            "comment": "За каву",
            "receiptId": "XXXX-XXXX-XXXX-XXXX",
            "invoiceId": "2103.в.27",
            "counterEdrpou": "3096889974",
            "counterIban": "UA898999980000355639201001404",
            "counterName": "ТОВАРИСТВО З ОБМЕЖЕНОЮ ВІДПОВІДАЛЬНІСТЮ «ВОРОНА»",
        }
    ]
