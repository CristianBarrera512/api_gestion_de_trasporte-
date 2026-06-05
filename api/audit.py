from rest_framework import serializers

class AuditMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request:
            if request.method == 'POST':
                if 'usuario_modificacion' in self.fields:
                    self.fields['usuario_modificacion'].read_only = True

            elif request.method in ['PUT', 'PATCH']:
                if 'usuario_creacion' in self.fields:
                    self.fields['usuario_creacion'].read_only = True

                if 'usuario_modificacion' in self.fields:
                    self.fields['usuario_modificacion'].required = True