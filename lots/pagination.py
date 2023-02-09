from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_page_url = self.get_next_link()  # "http://localhost:8000/lots?page=2"
        previous_page_url = self.get_previous_link()

        # TODO: rework this ugly w/a which is used to show just indexes
        if next_page_url is not None:
            next_page_url = int(next_page_url[-1])

        if previous_page_url is not None:
            previous_page_url = int(previous_page_url[-1])

        return Response(
            {
                "pagination": {
                    "current": self.page.number,
                    "next": next_page_url,
                    "previous": previous_page_url,
                    "total": self.page.paginator.count,
                },
                "results": data,
            }
        )
