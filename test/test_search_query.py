# coding: utf-8

"""
    WeGlide

    Quantifying airsports

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from weglide_client.models.search_query import SearchQuery

class TestSearchQuery(unittest.TestCase):
    """SearchQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchQuery:
        """Test SearchQuery
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchQuery`
        """
        model = SearchQuery()
        if include_optional:
            return SearchQuery(
                search_items = [
                    weglide_client.models.query.Query(
                        key = 'language', 
                        value = '', )
                    ],
                documents = [
                    null
                    ],
                limit = 56
            )
        else:
            return SearchQuery(
                search_items = [
                    weglide_client.models.query.Query(
                        key = 'language', 
                        value = '', )
                    ],
                documents = [
                    null
                    ],
        )
        """

    def testSearchQuery(self):
        """Test SearchQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
