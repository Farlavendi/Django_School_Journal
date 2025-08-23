from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class StudentsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    # https://www.django-rest-framework.org/api-guide/viewsets/#viewsets
    # or break the logic into GenericViewSet + mixins
    # or GenericAPIView + mixins
    pass

