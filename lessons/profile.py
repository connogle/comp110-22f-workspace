"""Examples of a class and objects."""

class Profile:
    handle: str
    followers: int
    is_private: bool
    follower_list: list[str]

    def __init__(self, handle: str):
        """Constructor, initializes attributes."""
        self.handle = handle
        self.followers = 0
        self.is_private = False
        self.follower_list = []
    
    def tweet(self, msg: str) -> None:
        """An example of a method."""
        print(f"@{ self.handle } tweets \"{ msg }\"")

    def follow(self, acct: str) -> None:
        """What happens when someone follows."""
        self.follower_list.append(acct)
        self.followers += 1


my_profile: Profile = Profile('KrisJordan')
another: Profile = Profile('Billy')

print(f"Profile: { my_profile.handle }\nFollowers: { my_profile.followers }")

my_profile.follow(another.handle)

print(f"Profile: { my_profile.handle }\nFollowers: { my_profile.followers }")

print(my_profile.follower_list)