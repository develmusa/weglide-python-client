# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.ranking import Ranking

class TestRanking(unittest.TestCase):
    """Ranking unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ranking:
        """Test Ranking
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Ranking`
        """
        model = Ranking()
        if include_optional:
            return Ranking(
                contest = None,
                category = 'pilot',
                sc_class = 'ALL',
                user = 'ALL',
                count = 56,
                season = 56,
                country = '',
                region = '',
                multi_region = '',
                continent = '',
                club = '',
                airport = '',
                month = '',
                keyword = '',
                travel_min_days = 56,
                travel_max_days = 56,
                order_by = 'points'
            )
        else:
            return Ranking(
        )
        """

    def testRanking(self):
        """Test Ranking"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
