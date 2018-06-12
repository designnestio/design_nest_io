class {{ obj.class_name }}:
    """ Corresponds to object `{{ obj.internal_name }}`
    {%- if obj.memo  %}
        {{ memo }}
    {%- endif %}
    """
    _schema = {{ obj.schema }}


    {%- for field in obj.fields %}

    @property
    def {{field.field_name}}(self):
        """field `{{ field.internal_name }}`
        |  {{field.comment}}
        """
        return self["{{ field.internal_name }}"]

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}}{% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}):
        """  Corresponds to field `{{field.internal_name}}`
        """
        self["{{ field.internal_name }}"] = value
    {%- endfor %}
        