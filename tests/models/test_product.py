import pytest

from blog.factories import ProductFactory


@pytest.fixture
def product_published():
    return ProductFactory(product_name='The Elder Scrolls V: Skyrim')


@pytest.mark.django_db
def test_create_published_product(product_published):
    assert product_published.product_name == 'The Elder Scrolls V: Skyrim'


