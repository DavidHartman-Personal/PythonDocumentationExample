"""Create Challenges

"""

__version__ = '2019.09'
__author__ = 'David Hartman - PTC Cloud Security'

import sys
import os
import datetime

# This effectively defines the root of the project and so adding ..\, etc is not needed
# in config files,etc
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Add script directory to the path to allow searching for modules
sys.path.insert(0, PROJECT_ROOT_DIR)

from challengetaker.Challenge import Challenge


def create_challenge(challenge_name, challenge_description=""):
    """Creates a challenge object

    Args:
        challenge_name: The name of the challenge
        challenge_description: The description of the challenge. If not
            provided, uses the name (default is "")
    """
    new_challenge = Challenge(challenge_name=challenge_name)


if __name__ == "__main__":
    create_challenge("one", "challenge one")
    create_challenge("two", "challenge two")
