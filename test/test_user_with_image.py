# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.user_with_image import UserWithImage

class TestUserWithImage(unittest.TestCase):
    """UserWithImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserWithImage:
        """Test UserWithImage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserWithImage`
        """
        model = UserWithImage()
        if include_optional:
            return UserWithImage(
                id = 56,
                name = '',
                image = '',
                badge = True
            )
        else:
            return UserWithImage(
                id = 56,
                name = '',
        )
        """

    def testUserWithImage(self):
        """Test UserWithImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
