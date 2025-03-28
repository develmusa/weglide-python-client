# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.airspace_violation import AirspaceViolation

class TestAirspaceViolation(unittest.TestCase):
    """AirspaceViolation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AirspaceViolation:
        """Test AirspaceViolation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AirspaceViolation`
        """
        model = AirspaceViolation()
        if include_optional:
            return AirspaceViolation(
                id = 56,
                violation = True,
                airspace_openaip_id = '',
                airspace_style = '',
                airspace_name = '',
                airspace_max_alt = 56,
                airspace_min_alt = 56,
                intervals = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                display_intervals = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                total_seconds = 1.337
            )
        else:
            return AirspaceViolation(
                id = 56,
                violation = True,
                airspace_openaip_id = '',
                airspace_style = '',
                airspace_name = '',
                airspace_max_alt = 56,
                airspace_min_alt = 56,
                intervals = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                display_intervals = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                total_seconds = 1.337,
        )
        """

    def testAirspaceViolation(self):
        """Test AirspaceViolation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
