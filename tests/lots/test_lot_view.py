from unittest.mock import patch

import pytest
from django.urls import reverse

from lots.constants import LOT_STATUS
from lots.models import Lot
from monobank.models import MonobankJar


@pytest.mark.django_db
def test_get_empty_lot_view(client, admin_client):
    response = client.get("/lots")

    assert response.json() == {
        "pagination": {
            "current": 1,
            "next": None,
            "previous": None,
            "total": 0,
        },
        "results": [],
    }


@pytest.mark.django_db
def test_create_lot(client, client_with_jwt, test_lot_data):
    # check there is no lots and jars before test
    assert MonobankJar.objects.count() == 0
    assert Lot.objects.count() == 0

    with patch("monobank.models.MonobankJar.update_data"):
        # create lot (and associated jar)
        client_with_jwt.post(
            reverse("lots-list"),
            data=test_lot_data,
            content_type="application/json",
        )

    # check created lot and jar exists
    assert MonobankJar.objects.count() == 1
    assert Lot.objects.count() == 1

    # get lots list
    response = client_with_jwt.get(reverse("lots-list"))
    assert response.status_code == 200

    created_lot_data = response.json()["results"][0]

    # check first lot has corresponding data
    assert created_lot_data["name"] == test_lot_data["name"]
    assert created_lot_data["description"] == test_lot_data["description"]
    assert created_lot_data["monobank_jar"]["link"].endswith(test_lot_data["monobank_jar_link"])
    assert created_lot_data["status"] == LOT_STATUS.MODERATION


@pytest.mark.django_db
def test_user_can_change_his_own_lot_data(client_with_jwt, test_lot_data, updated_test_lot_data):
    with patch("monobank.models.MonobankJar.update_data"):
        response = client_with_jwt.post(reverse("lots-list"), data=test_lot_data)
        assert response.status_code == 201

    lot_id = response.json()["id"]

    response = client_with_jwt.patch(
        f"{reverse('lots-list')}/{lot_id}",
        data=updated_test_lot_data,
        content_type="application/json",
    )
    assert response.status_code == 200

    response = client_with_jwt.get(f"{reverse('lots-list')}/{lot_id}")
    assert response.status_code == 200

    assert response.json()["name"] == updated_test_lot_data["name"]
    assert response.json()["description"] == updated_test_lot_data["description"]


@pytest.mark.django_db
def test_user_cant_fetch_others_lot_under_moderation(
    admin_client_with_jwt, client_with_jwt, test_lot_data, updated_test_lot_data
):
    with patch("monobank.models.MonobankJar.update_data"):
        response = admin_client_with_jwt.post(reverse("lots-list"), data=test_lot_data)
        assert response.status_code == 201

    response = client_with_jwt.patch(
        f"{reverse('lots-list')}/{response.json()['id']}",
        data=updated_test_lot_data,
        content_type="application/json",
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_cant_change_lot_status(client_with_jwt, test_lot_data):
    with patch("monobank.models.MonobankJar.update_data"):
        response = client_with_jwt.post(
            reverse("lots-list"),
            data=test_lot_data,
            content_type="application/json",
        )
        assert response.status_code == 201

    response = client_with_jwt.patch(
        f"{reverse('lots-list')}/{response.json()['id']}",
        data={"status": "ACTIVE"},
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.json() == {"user": "Only admin can change status"}
