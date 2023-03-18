import datetime
from unittest.mock import patch

import pytest

from lots.models import Lot
from monobank.models import MonobankJar


@pytest.mark.django_db
def test_get_empty_lot_view(client, admin_client):
    response = admin_client.get("/lots")

    assert response.json() == {
        "pagination": {
            "current": 1,
            "next": None,
            "previous": None,
            "total": 0,
        },
        "results": [],
    }


@patch("monobank.models.MonobankJar.update_data")
@patch("monobank.api_wrapper.MonobankApiWrapper.fetch_user_info", lambda: {})
@pytest.mark.django_db
def test_create_list_lot(client, admin_client_with_jwt, test_lot_data):
    # check there is no lots and jars before test
    assert MonobankJar.objects.count() == 0
    assert Lot.objects.count() == 0

    # create lot (and associated jar)
    admin_client_with_jwt.post(
        "/lots",
        data=test_lot_data,
        content_type="application/json",
    )

    # check created lot and jar exists
    assert MonobankJar.objects.count() == 1
    assert Lot.objects.count() == 1

    # get lots list
    response = admin_client_with_jwt.get("/lots")
    assert response.status_code == 200

    created_lot_data = response.json()["results"][0]

    # check first lot has corresponding data
    assert created_lot_data["name"] == test_lot_data["name"]
    assert created_lot_data["description"] == test_lot_data["description"]
    assert created_lot_data["monobank_jar"]["link"].endswith(test_lot_data["monobank_jar_link"])
