class Challenge:
    """Update 12/30/2021 This class describes a Challenge that someone can take or a challenge - updated by dave
    that someone can define to be taken by others.

    This is the more detailed description of the Challenge class

    Args:
        challenge_name: The name of the challenge (all other attributes can be
            blank)
    """

    # static Array of header columns that can be used to generate a report of defined challenges
    header_columns = ["CHALLENGE_ID",
                      "CHALLENGE_NAME",
                      "CHALLENGE_DESCRIPTION"]

    def __init__(self,
                 challenge_name,
                 challenge_description="",
                 challenge_type="",
                 challenge_author="",
                 challenge_create_date="",
                 tags=[]):
        """Initializes a Challenge object. Only a name is required.

        Args:
            challenge_name:
            challenge_description:
            challenge_type:
            challenge_author:
            challenge_create_date:
            tags:
        """
        self.challenge_name = challenge_name
        self.challenge_description = challenge_description
        self.challenge_type = challenge_type
        self.challenge_author = challenge_author
        self.challenge_create_date = challenge_create_date
        self.tags = tags

    def __repr__(self):
        return repr((self.challenge_name, self.challenge_description))


    def add_tag(self,tag):
        """Adds a tag to the array of tags if it doesn't already exist

        Args:
            tag: tag to add
        """
        self.tags.append(tag)


    def get_tags(self):
        """returns an array of all of the tabs

        Returns:
            tag_array: an array of all of the tags
        """
        return self.tags

    def print_tabs(self):
        """prints all of the tabs"""
        for tag in self.tags:
            print(str(tag))