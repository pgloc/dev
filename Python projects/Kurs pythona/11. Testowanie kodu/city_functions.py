def get_formatted_text(city, country, population=''):
    """Generuje elegancko sformatowane miasto i państwo."""
    if population:
        full_name = f"{city.title()}, {country.title()} - populacja {population}"
    else:
        full_name = f"{city.title()}, {country.title()}"
    return full_name