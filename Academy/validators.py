from django.core.exceptions import ValidationError


def number_on_tshirt(value):
    if 1 > value > 99:
        raise ValidationError("Numer na koszulce niepoprawny")


def test_result(value):
    if 1 > value > 10:
        raise ValidationError("Wynik testu niepoprawny (1-10)")
