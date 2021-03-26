import os

this_root = os.path.abspath(os.path.join(__file__, '../..'))

def make_dir(dir_name):
    os.mkdir(dir_name)

def make_dirs(dir_names):
    for dir_name in dir_names:
        make_dir(dir_name)

def touch(fname):
    try:
        os.utime(fname, None)
    except OSError:
        open(fname, 'a').close()

def touch_files(files):
    for file in files:
        touch(file)

def read_file(file):
    if not os.path.exists(file):
        raise ValueError(f"This file doesn't exist! {file}")

    with open(file, 'r') as f:
        lines = f.readlines()

    return lines

def write_file(data, file):
    with open(file, 'w') as f:
        if isinstance(data, list):
            for line in data:
                f.write(line)
        elif isinstance(data, str):
            f.write(data)
        else:
            raise ValueError(f"Cannot write data type {type(data)}")

def init_git():
    os.system('git init')

def init_env(python_version='3.7'):
    os.system(f'pipenv --python {python_version}')

def repo_exists(dir_name):
    return os.path.exists(dir_name)

def create_repo(repo_name):
    cwd = os.getcwd()

    if os.path.exists(repo_name):
        assert 'Repo already exists'

    make_dir(repo_name)

    root = os.path.join(cwd, repo_name)
    os.chdir(root)

    msg = 'Do you want to create an environment? (y/n) '
    environment = input(msg)
    if environment == 'y':
        version = input('Which python version? ')
        init_env(version)
        print(f'Python {version} created.')
    else:
        print('No environment created.')

    git = input('Do you want to init git? (y/n) ')
    if git == 'y':
        init_git()
        print('Git initialize.')
    else:
        print('No Git Init.')

    # Create Files
    files = ['README.md', '.gitignore']
    touch_files(files)
    sample_gitignore_lines = read_file(os.path.join(this_root, '.gitignore'))
    write_file(sample_gitignore_lines, '.gitignore')

    # Initialize all directories
    root_dirs = ['dev', repo_name, 'tests', 'data']
    make_dirs(root_dirs)

    files = ['__init__.py']
    files = [os.path.join(repo_name, file) for file in files]
    touch_files(files)

    file = os.path.join(repo_name, 'utils.py')
    file_lines = '''import os\n\nDATA_DIR = os.path.abspath(os.path.join(__file__, '../../data'))\n'''
    write_file(file_lines, file)

    os.chdir(os.path.join(root, 'dev'))
    dev_dirs = ['notebooks', 'workspace']
    make_dirs(dev_dirs)
