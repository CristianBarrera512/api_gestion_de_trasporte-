from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from openpyxl import Workbook


class BaseViewSet(viewsets.ModelViewSet):

    def success_response(self, message, data=None, status_code=status.HTTP_200_OK):
        return Response(
            {
                "success": True,
                "message": message,
                "data": data
            },
            status=status_code
        )

    def error_response(self, message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(
            {
                "success": False,
                "message": message,
                "errors": errors
            },
            status=status_code
        )
    def get_queryset(self):
        return super().get_queryset().filter(activo=True,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return self.success_response(
            "Consulta realizada correctamente",
            serializer.data
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return self.success_response(
            "Registro encontrado",
            serializer.data
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)

        return self.success_response(
            "Registro creado correctamente",
            serializer.data,
            status.HTTP_201_CREATED
        )

        return self.error_response(
            "Error de validación",
            serializer.errors
    )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )

        if serializer.is_valid():
            serializer.save()

            return self.success_response(
                "Registro actualizado correctamente",
                serializer.data
            )

        return self.error_response(
            "Error de validación",
            serializer.errors
        )

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.activo = False
        instance.save()

        serializer = self.get_serializer(instance)

        return self.success_response(
            "Registro desactivado correctamente",
            serializer.data
     )
    
    @action(detail=False, methods=['get'])
    def exportar_excel(self, request):

        queryset = self.get_queryset()

        wb = Workbook()
        ws = wb.active
        ws.title = self.queryset.model.__name__

        fields = [
            field.name
            for field in self.queryset.model._meta.fields
        ]

        # Encabezados
        ws.append(fields)

        # Datos
        for obj in queryset:
            ws.append([
                str(getattr(obj, field, ''))
                for field in fields
            ])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = (
            f'attachment; filename={self.queryset.model.__name__}.xlsx'
        )

        wb.save(response)

        return response
    @action(detail=False, methods=['get'])
    def inactivos(self, request):
        queryset = self.queryset.filter(activo=False)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)