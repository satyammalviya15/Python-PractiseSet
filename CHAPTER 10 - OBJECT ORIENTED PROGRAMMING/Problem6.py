# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class call:
    def __init__(self):
        self.name="harry"

user=call()
user.name="satyam"
print(user.name)