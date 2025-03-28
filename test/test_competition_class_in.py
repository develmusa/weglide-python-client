# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.competition_class_in import CompetitionClassIn

class TestCompetitionClassIn(unittest.TestCase):
    """CompetitionClassIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompetitionClassIn:
        """Test CompetitionClassIn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompetitionClassIn`
        """
        model = CompetitionClassIn()
        if include_optional:
            return CompetitionClassIn(
                name = '',
                device = [
                    weglide_client.models.competition_device_in.CompetitionDeviceIn(
                        id = '', 
                        index = 1.337, )
                    ]
            )
        else:
            return CompetitionClassIn(
                name = '',
                device = [
                    weglide_client.models.competition_device_in.CompetitionDeviceIn(
                        id = '', 
                        index = 1.337, )
                    ],
        )
        """

    def testCompetitionClassIn(self):
        """Test CompetitionClassIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
