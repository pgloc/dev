def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='fizyka')
print(user_profile)

user_profile = build_profile('przemysław', 'gloc',
                             city='sosnowiec',
                             work='maspex',
                             wife='monika')
print(user_profile)