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
    context["extensible_keys"] = ", ".join(['"{}"'.format(field.internal_name) for field in obj.extensible_fields])

    return template.render(context)


def generate_group(groupname, sources):
    template = env.get_template('group.py')
    context = {}
    context["sources"] = sources
    context["group"] = groupname
    return template.render(context)


def generate_idf(objs):
    source_files = set()
    required_objects = set()
    unique_objects = set()
    for obj in objs:
        source_files.add(obj.file_name)
        if "required-object" in obj.attributes:
            required_objects.add('"{}"'.format(obj.internal_name.lower()))

        if "unique-object" in obj.attributes:
            unique_objects.add('"{}"'.format(obj.internal_name.lower()))

    template = env.get_template('idf.py')
    context = {}
    context["generation_date"] = date.today()
    context["objs"] = objs
    context["file_names"] = list(source_files)
    context["required_objects"] = ", ".join(required_objects)
    context["unique_objects"] = ", ".join(unique_objects)
    return template.render(context)


def generate_helper(objs):

    template = env.get_template('helper.py')
    context = {}
    context["objs"] = objs
    return template.render(context)


def generate_init(version):
    template = env.get_template('__init__.py')
    context = {}
    context['version'] = version
    return template.render(context)
    

if __name__ == '__main__':
    pass