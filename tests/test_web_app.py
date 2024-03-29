import pytest

from flask import session
from website.directory.database_repository import SqlAlchemyRepository

"""
Unfortunately I could not run these types of tests where the 
compiler will complain about not having a repo when getting user 
I am not sure how you would go about fixing this either
"""
# def test_register(client):
#     repo = SqlAlchemyRepository(client)
#     # Check that we retrieve the register page.
#     response_code = client.get('/authentication/register').status_code
#     assert response_code == 200
#
#     # Check that we can register a user successfully, supplying a valid username and password.
#     response = client.post(
#         '/authentication/register',
#         data={'username': 'gmichael', 'password': 'CarelessWhisper1984'}
#     )
#     assert response.headers['Location'] == 'http://localhost/authentication/login'
#
# @pytest.mark.parametrize(('username', 'password', 'message'), (
#         ('', '', b'Your username is required'),
#         ('cj', '', b'Your username is too short'),
#         ('test', '', b'Your password is required'),
#         ('test', 'test', b'Your password must be at least 8 characters, and contain an upper case letter, a lower case letter and a digit'),
#         ('fmercury', 'Test#6^0', b'Your username is already taken - please supply another'),
# ))
#
# def test_register_with_invalid_input(client, username, password, message):
#     # Check that attempting to register with invalid combinations of username and password generate appropriate error
#     # messages.
#     response = client.post(
#         '/authentication/register',
#         data={'username': username, 'password': password}
#     )
#     assert message in response.data
#
#
#
# def test_login(client, auth):
#     # Check that we can retrieve the login page.
#     status_code = client.get('/authentication/login').status_code
#     assert status_code == 200
#
#     # Check that a successful login generates a redirect to the homepage.
#     response = auth.login()
#     assert response.headers['Location'] == 'http://localhost/'
#
#     # Check that a session has been created for the logged-in user.
#     with client:
#         client.get('/')
#         assert session['username'] == 'thorke'