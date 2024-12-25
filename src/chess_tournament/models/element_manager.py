def find_element_by_id(elements_data, user_choice):
    return next(
        (element for element in elements_data if element["id"] == int(user_choice)),
        None,
    )
