def test_create_status(app, logged_user):
    input_text = 'Welcome to the Hell'
    # Locate existed text statuses
    old_status_list = app.status_text_elements()
    # Create new status
    app.create_new_text_status(input_text)
    app.wait_new_status_appear(old_status_list)
    # Verification
    new_status_element = app.status_text_elements()[0]
    assert new_status_element.text == input_text
    assert app.user_of_new_status_elements()[0].text == logged_user.real_name
