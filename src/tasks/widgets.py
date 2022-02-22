from django import forms


class DateTimeInput(forms.widgets.TextInput):
    """
    Subclass TextInput since there's no direct way to override its type attribute,
    We need to override date_of_birth input type from text to date.
    This way the Bootstrap calendar widget will work
    """

    input_type = "date"
