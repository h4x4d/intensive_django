import os

os.system('poetry export --without-hashes '
          '--format=requirements.txt > requirements.txt')

with open('requirements.txt', 'r+') as file:
    requirements = [requirement[:requirement.find(';')] for
                    requirement in file.readlines()]

    file.seek(0)
    file.write('\n'.join(requirements))
    file.truncate()


os.system('poetry export --without-hashes '
          '--format=requirements.txt > requirements-dev.txt --with dev')

with open('requirements-dev.txt', 'r+') as file:
    requirements = [requirement[:requirement.find(';')] for
                    requirement in file.readlines()]

    file.seek(0)
    file.write('\n'.join(requirements))
    file.truncate()


print('REQUIREMENTS GENERATED SUCCESSFULLY')
