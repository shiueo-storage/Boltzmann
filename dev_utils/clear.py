from dev_utils import prettier, requirements_txt


def code_foromat_and_make_requirements_txt(path):
    prettier.code_format(path)
    requirements_txt.make_requirements_txt(path)
