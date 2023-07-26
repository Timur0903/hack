
import pytest
from account.serializers import RegisterSerializer

@pytest.mark.django_db
@pytest.mark.parametrize('password_len', [5, 6, 10, 20, 21])
def test_len(password_len):
    user_data = {
        'email': 'timur@mail.ru',
        'password': 'a' * password_len,
        'password_confirmation': 'a' * password_len,
        'username': 'timur',
        'first_name': 'akusev',
        'last_name': 'timur123',
        'avatar': None,
        'is_staff': False,
    }

    serializer = RegisterSerializer(data=user_data)
    assert serializer.is_valid() == (password_len >= 6 and password_len <= 20)

