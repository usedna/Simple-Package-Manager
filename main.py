import config
import subprocess
import sys
from utils import print_output


def run(install_type='package', pkg_mgr='apt', name=None, state='present', test=False):
    if install_type != "package" and install_type != "software":
        print("Invalid option")
        return 0

    playbook = config.PLAYBOOK[install_type]

    cmd = f"ansible-playbook -i {config.INVENTORY} {playbook} -e 'pkg_name={name} state={state} pkg_mgr={pkg_mgr}'"

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print_output(result, test)


def run_test():
    print("\nTest 1\n")
    run('package', 'pip', 'pandas', 'present', True)

    print("\nTest 2\n")
    run('package', 'pip', 'pandas', 'absent', True)

    print("\nTest 3\n")
    run('software', 'apt', 'pandas', 'present', True)

def main():
    run_test()

    if len(sys.argv) <= 4:
        print("Not enough arguments\nargs: {install_type(package/software)}, "
              "{pkg_mgr(apt/pip)}, {pkg_soft_name}, {state(present/absent}")
        return -1

    if sys.argv[1] != "package" and sys.argv[1] != "software":
        print("Parameter wrong, 1: install_type(package/software)")
        return -1

    if sys.argv[1] == 'software' and sys.argv[2] == 'pip':
        print('Invalid arg, 2: install_type(pkg), pkg_manager(apt)')

    if sys.argv[2] != "apt" and sys.argv[2] != "pip":
        print("Parameter wrong, 3: pkg_manager(apt/pip)")
        return -1

    if sys.argv[4] != "present" and sys.argv != "absent":
        print("Parameter wrong, 4: state(present/absent)")
        return -1

    run(install_type=str(sys.argv[1]), pkg_mgr=str(sys.argv[2]), name=str(sys.argv[3]), state=str(sys.argv[4]))


if __name__ == "__main__":
    main()
