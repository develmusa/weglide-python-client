# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.body_reset_password_v1_auth_reset_password_post import BodyResetPasswordV1AuthResetPasswordPost

class TestBodyResetPasswordV1AuthResetPasswordPost(unittest.TestCase):
    """BodyResetPasswordV1AuthResetPasswordPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BodyResetPasswordV1AuthResetPasswordPost:
        """Test BodyResetPasswordV1AuthResetPasswordPost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BodyResetPasswordV1AuthResetPasswordPost`
        """
        model = BodyResetPasswordV1AuthResetPasswordPost()
        if include_optional:
            return BodyResetPasswordV1AuthResetPasswordPost(
                token = '',
                new_password = ''
            )
        else:
            return BodyResetPasswordV1AuthResetPasswordPost(
                token = '',
                new_password = '',
        )
        """

    def testBodyResetPasswordV1AuthResetPasswordPost(self):
        """Test BodyResetPasswordV1AuthResetPasswordPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
