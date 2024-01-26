import subprocess

install_env = "{{ cookiecutter.install_enviroment }}"

if install_env.lower() == 'y':
    print(f"installing dependencies...")
    result = subprocess.call(['conda', 'env', 'create','--file','environment.yml'])
    if result == 0:
        print("The dependencies have been installed")
    else:
        print("There was an error during the installation")
else:
    print("User rejected the installation of dependencies")