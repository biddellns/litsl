from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/biddellns/litsl.git'

def deploy():
		site_folder = 'home/{0}/sites/{1}'.format(env.user, env.host)  
		source_folder = site_folder + '/source'
		_create_directory_structure(site_folder)
		_get_latest_source(source_folder)
		_update_settings(source_folder, env.host)
		_update_virtualenv(env.user, env_name, source_folder)
		_update_static_files(source_folder)
		_update_database(source_folder)

def _create_directory_structure(site_folder):
    for subfolder in ('static', 'source'):
        run('mkdir -p {0}/{1}'.format(site_folder, subfolder))

def _get_latest_source(source_folder):
    # Has the git repo already been cloned?
    if exists(source_folder + '/.git'):
        # Fetch latest updates
        run ('cd {0} && git fetch'.format(source_folder))
    else:
        # Clone the reop
        run('git clone {0} {1}'.format(REPO_URL, source_folder))
			
    latest_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd {0} && git reset --hard {1}'.format(source_folder, latest_commit))

def _update_virtualenv(env_user, env_name, source_folder):
    virtualenv_folder = '/home/{0}/.virtualenvs/{1}'.format(env_user, env_name)

    # Has the virtual environment been created?
    if not exists(virtualenv_folder + '/bin'):
        # Create the virtual environment
        run('mkvirtualenv {0}'.format(env_name))

    # Install requirements from requirements.txt
    run('{0}/bin/pip3 install -r {1}/requirements.txt'.format(virtualenv_folder, source_folder))

def _update_static_files(source_folder, env_user, env_name):
    run('cd {0} && /home/{1}/.virtualenvs/{2}/bin/python3 managage.py collectstatic --noinput'.format(source_folder, env_user, env_name))


