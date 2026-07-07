import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "hot sauce", 100.0),
        ("FILLING", "cutlet", 300.0),
        ("SAUCE", "sour cream", 50.0)
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "hot sauce", 100.0),
        ("FILLING", "cutlet", 300.0),
        ("SAUCE", "sour cream", 50.0)
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "hot sauce", 100.0),
        ("FILLING", "cutlet", 300.0),
        ("SAUCE", "sour cream", 50.0)
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type