import requests
import pytest

host = 'https://api.pokemonbattle.me'  # хост для покемонов
token = '9fde3c4e897a6cf0351e94fd6de72bed'


def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 227})
    assert response.status_code == 200


def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 227})
    assert response.json()[0]['city'] == 'Москва'


@pytest.mark.parametrize('key, value', [('city', 'Москва'),
                                        ('trainer_name', 'Никита'),
                                        ('battles', 0)])
def test_parts_of_answer(key, value):
    response = requests.get(f'{host}/pokemons', params={'trainer_id': 227})
    assert response.json()[key] == value
