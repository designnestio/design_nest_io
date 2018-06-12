from datetime import date
from jinja2 import Environment, PackageLoader
import pprint
env = Environment(loader=PackageLoader('generator', 'templates'))


def generate_class(obj):
    template = env.get_template('class.py')

    required_fields = []
    for field in obj.fields:
        if "required-field" in field.attributes:
            required_fields.append('"{}"'.format(field.internal_name))

    obj.schema = pprint.pformat(obj.schema)
    context = {}
    context["obj"] = obj
    context["required_fields"] = ", ".join(required_fields)

    return template.render(context)


def generate_group(groupname, sources):
    template = env.get_template('group.py')
    context = {}
    context["sources"] = sources
    context["group"] = groupname
    return template.render(context)
    

if __name__ == '__main__':
    pass