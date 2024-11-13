# MEMBERS ONLY

## This serves to document the Journey so as to look back and continue to learn from past achievements and mistakes.

## Goal:
`To practice:
1. Create Models
2. Create forms
3. Login and Logout Users
4. Basic Validation
`

## Ecountered:
### Could not login users
1. This happened due to the fact that users password were being created as plain text so when the user tries to log in the the User Model (django's default model) expects a hashed password which now brougt in confict. this was solved by using the UserCreationForm (django's default for creating users) which will handle even the hashing of the passwords.
