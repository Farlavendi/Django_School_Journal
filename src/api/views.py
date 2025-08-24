from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly


class ProtectedViewSet(ModelViewSet):
    permission_classes = (
        # IsAdminOrReadOnly,
    )
    pagination_class = LimitOffsetPagination
    page_size_query_param = "page"
    page_size = 1


class IsSuperUserViewSet(ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,)
    pagination_class = LimitOffsetPagination


class IsOwnerViewSet(ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination
