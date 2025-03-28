# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.achievement_with_badge_no_user import AchievementWithBadgeNoUser

class TestAchievementWithBadgeNoUser(unittest.TestCase):
    """AchievementWithBadgeNoUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AchievementWithBadgeNoUser:
        """Test AchievementWithBadgeNoUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AchievementWithBadgeNoUser`
        """
        model = AchievementWithBadgeNoUser()
        if include_optional:
            return AchievementWithBadgeNoUser(
                id = 56,
                badge_id = '',
                points = 56,
                flight_id = 56,
                value = 1.337,
                user_id = 56,
                badge = weglide_client.models.badge.Badge(
                    id = '', 
                    name = '', 
                    logo = '', 
                    description = weglide_client.models.description.Description(), 
                    points = [
                        56
                        ], 
                    values = [
                        1.337
                        ], )
            )
        else:
            return AchievementWithBadgeNoUser(
                id = 56,
                badge_id = '',
                points = 56,
                user_id = 56,
                badge = weglide_client.models.badge.Badge(
                    id = '', 
                    name = '', 
                    logo = '', 
                    description = weglide_client.models.description.Description(), 
                    points = [
                        56
                        ], 
                    values = [
                        1.337
                        ], ),
        )
        """

    def testAchievementWithBadgeNoUser(self):
        """Test AchievementWithBadgeNoUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
