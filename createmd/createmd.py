#!/usr/bin/env python

import os
import click
# import secrender
# from yaml import load, FullLoader
# from yamlinclude import YamlIncludeConstructor

@click.command()
@click.option('--in', '-i', 'in_',
              required=True,
              type=click.Path(exists=True, dir_okay=False, readable=True),
              help='values (YAML)')
@click.option('--out', '-o', 'out_',
              type=click.Path(exists=True, dir_okay=True, readable=True),
              required=True,
              help='Output directory')
@click.option('--template', '-t', 'template_dir',
              type=click.Path(exists=True, dir_okay=True, readable=True),
              required=True,
              help='Template directory')
def main(in_, template_dir, out_):
    # Ideally, this would live in secrender.
    # YamlIncludeConstructor.add_to_loader_class(loader_class=FullLoader)

    # with open(in_, "r") as stream:
    #     yaml = load(stream, Loader=FullLoader)
    # print(yaml)
    # do secrender.get_template_args()

    all_templates = get_template_list(template_dir)
    for template in all_templates:
        out = template.replace(template_dir, out_ + '/')
        if not os.path.exists(os.path.dirname(out)):
            os.makedirs(os.path.dirname(out))
        # do secrendering

def get_template_list(template_dir):
    file_list = list()
    for (dirpath, dirname, filenames) in os.walk(template_dir):
        file_list += [os.path.join(dirpath, file) for file in filenames]
    return file_list

if __name__ == '__main__':
    main()