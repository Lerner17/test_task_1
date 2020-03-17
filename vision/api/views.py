from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .serializers import VisionSerializer
from ..services import localize_objects_uri


class VisionAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        image = request.data['image']
        if image:
            objects_on_image = [
                obj.name for obj in localize_objects_uri(image)]
            if len(objects_on_image) is 0:
                return Response({'message': 'No objects were found in the picture'}, status=HTTP_404_NOT_FOUND)
            return Response({'objects': objects_on_image})
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
