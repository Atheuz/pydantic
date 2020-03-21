from pydantic import BaseModel, SecretStr, SecretBytes, ValidationError

class SimpleModel(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes
    password_idempotent: SecretStr

sm = SimpleModel(password='IAmSensitive', 
                 password_bytes=b'IAmSensitiveBytes', 
                 password_idempotent=SecretStr('IAmIdempotent'))

# Standard access methods will not display the secret
print(sm)
print(sm.password)
print(sm.dict())
print(sm.json())

# Use get_secret_value method to see the secret's content.
print(sm.password.get_secret_value())
print(sm.password_bytes.get_secret_value())
print(sm.password_idempotent.get_secret_value())

# Validation works.
try:
    SimpleModel(password=[1, 2, 3], 
                password_bytes=[1, 2, 3], 
                password_idempotent=[1, 2, 3])
except ValidationError as e:
    print(e)
