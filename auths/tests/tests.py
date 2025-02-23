import pytest

from auths.models import CusUser

from django.contrib.auth import get_user_model

from django.urls import reverse

User = get_user_model()


@pytest.fixture
def create_user(db):
    user1 = CusUser.objects.create_user(
        email="luiyunish1@gmai.com",
        username="yunish1",
        password="aaa123aaa",
        role="USER_ROLE_ADMIN",
    )
    user2 = CusUser.objects.create_user(
        email="luiyunish2@gmai.com",
        username="yunish2",
        password="aaa123aaa",
        role="USER_ROLE_REGULAR",
    )
    return user1, user2


@pytest.mark.django_db
def test_user_role(create_user):
    user1, user2 = create_user

    assert user1.role == "USER_ROLE_ADMIN"
    assert user2.role == "USER_ROLE_REGULAR"


@pytest.mark.django_db
def test_user_login_code(client, create_user):

    res = client.post(
        reverse("login"), {"username": "yunish1", "password": "aaa123aaa"}
    )
    assert res.status_code == 302

    res = client.post(
        reverse("login"), {"username": "yunish2", "password": "aaa123aaa"}
    )

    assert res.status_code == 200


@pytest.mark.django_db
def test_user_register(client, create_user):
    res = client.post(
        reverse("register"),
        {"username": "yunish2", "password1": "aaa123aaa", "password2": "aaa123aaa"},
    )
    assert "A user with that username already exists" in str(res.content)


@pytest.mark.django_db
def test_user_login_response(client, create_user):
    res = client.post(
        reverse("login"), {"username": "yunish2", "password": "aaa123aaa"}
    )
    assert "is not a Admin user" in str(res.content)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "username,password,result",
    [
        ("yunish1", "aaa123aaa", 302),
    ],
)
def test_parameter_login(client, create_user, username, password, result):

    res = client.post(reverse("login"), {"username": username, "password": password})
    assert res.status_code == result


@pytest.mark.django_db
@pytest.mark.parametrize(
    "username,password1,password2,role,result,msg",
    [
        ("yunish3", "aaa123aaa", "aaa123aaa", "USER_ROLE_ADMIN", 302, None),
        ("yunish4", "aaa123aaa", "aaa123aaa", "USER_ROLE_ADMIN", 302, None),
        (
            "yunish1",
            "aaa123aaa",
            "aaa123aaa",
            "role1",
            200,
            "A user with that username already exists",
        ),
    ],
)
def test_parameter_register(
    client, create_user, username, password1, password2, role, result, msg
):

    res = client.post(
        reverse("register"),
        {
            "username": username,
            "password1": password1,
            "password2": password2,
            "role": role,
        },
    )

    if result:
        assert res.status_code == result

    if msg:

        assert msg in res.content.decode()
