# data_structures_test.py

import io
import sys
from data_structures import get_names, get_spiciest_foods, print_spicy_foods, \
                            create_spicy_food, get_spicy_food_by_cuisine, \
                            print_spiciest_foods, average_heat_level

class TestDataStructures:
    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        }
    ]

    def test_get_names(self):
        assert get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_foods(self):
        for food in get_spiciest_foods(TestDataStructures.SPICY_FOODS):
            assert food["heat_level"] > 5

    def test_print_spicy_foods(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" \
                                         "Buffalo Wings (American) | Heat Level: 🌶🌶🌶\n" \
                                         "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

    def test_get_spicy_food_by_cuisine(self):
        assert get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American") == {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        }

    def test_print_spiciest_foods(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spiciest_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" \
                                         "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

    def test_average_heat_level(self):
        assert average_heat_level(TestDataStructures.SPICY_FOODS) == 6

    def test_create_spicy_food(self):
        new_spicy_foods = create_spicy_food(
            TestDataStructures.SPICY_FOODS,
            {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
        )

        assert new_spicy_foods == [
            {
                "name": "Green Curry",
                "cuisine": "Thai",
                "heat_level": 9,
            },
            {
                "name": "Buffalo Wings",
                "cuisine": "American",
                "heat_level": 3,
            },
            {
                "name": "Mapo Tofu",
                "cuisine": "Sichuan",
                "heat_level": 6,
            },
            {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },
        ]
