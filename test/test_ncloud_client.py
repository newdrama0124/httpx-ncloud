import pytest_httpx

from httpx_ncloud import NcloudClient


def test_ncloud_client(httpx_mock: pytest_httpx.HTTPXMock):
    httpx_mock.add_response()

    client = NcloudClient(base_url="https://cloudsearch.apigw.ntruss.com",
                          follow_redirects=True,
                          access_key="a",
                          secret_key="b",
                          )
    res = client.get(url="/v1/domain/rel-20240509")
    print(res.text)
