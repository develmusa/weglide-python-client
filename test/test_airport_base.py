# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.airport_base import AirportBase

class TestAirportBase(unittest.TestCase):
    """AirportBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AirportBase:
        """Test AirportBase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AirportBase`
        """
        model = AirportBase()
        if include_optional:
            return AirportBase(
                id = 56,
                name = '',
                region = ''
            )
        else:
            return AirportBase(
                id = 56,
                name = '',
                region = '',
        )
        """

    def testAirportBase(self):
        """Test AirportBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
