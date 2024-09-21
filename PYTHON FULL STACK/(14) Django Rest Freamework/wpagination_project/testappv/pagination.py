from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'mypage'     # default value is 'page'
    page_size_query_param = 'num'
    max_page_size = 10
    last_page_strings = ('endpage',)   # default value is ('last',)

class MyPagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'     # default value is 'limit'
    offset_query_param = 'myoffset'   # default value is 'offset'
    max_limit = 20

class MyPagination3(CursorPagination):   # can you provide all records according to ascending order of esal but per page 5 only
    ordering = '-esal'                    # default value is '-created'
    page_size = 5

    """
    ordering = 'esal'   # Ascending order
    ordering = '-esal'  # Descending order

    """