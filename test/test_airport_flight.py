# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.airport_flight import AirportFlight

class TestAirportFlight(unittest.TestCase):
    """AirportFlight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AirportFlight:
        """Test AirportFlight
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AirportFlight`
        """
        model = AirportFlight()
        if include_optional:
            return AirportFlight(
                id = 56,
                name = ''
            )
        else:
            return AirportFlight(
                id = 56,
                name = '',
        )
        """

    def testAirportFlight(self):
        """Test AirportFlight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
