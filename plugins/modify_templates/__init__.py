from pelican import signals
from jinja2 import ChoiceLoader, DictLoader, PrefixLoader


def modify_template(generator):
    """
    Modify the template of the pelican site.
    """
    default_script_path = 'scripts.html'  # TODO: fix the path
    default_template_to_modify = ['base.html']

    script_path = generator.settings.get('SCRIPTS_PATH',
                                         default_script_path)
    template_to_modify = generator.settings.get('TEMPLATES_TO_MODIFY',
                                                default_template_to_modify)

    with open(script_path) as f:
        new_template = f.read()

    loader_new = DictLoader({t: "{% extends '!old/" + t + "' %}" + new_template
                             for t in template_to_modify})
    loader_old = generator.env.loader
    generator.env.loader = ChoiceLoader([loader_new,
                                         PrefixLoader({"!old": loader_old}),
                                         loader_old])


def register():
    signals.generator_init.connect(modify_template)
