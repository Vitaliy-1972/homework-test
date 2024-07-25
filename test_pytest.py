import pytest
import requests


class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorisation': 'OAuth token'
        }

    @pytest.mark.parametrize(
        'key,value,status_code',
        (
                ['pat', 'Image', 400],
                ['path', 'Image', 201],
                ['path', 'Image', 409],
                ['path', 'Image', 507],
        )
    )
    def test_create_folder(self, key, value, status_code):
        params = {key: value}
        respons = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                               headers=self.headers,
                               params=params)
        assert respons.status_code == status_code
