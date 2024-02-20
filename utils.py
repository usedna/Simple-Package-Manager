def print_output(result, test=False):
    if test:
        print("Test is on\n")
    print(result.stdout)
    print("stderr: ", result.stderr)

    if result.returncode == 0:
        print("Command ran successfully")
    else:
        print("Command failed: exitcode", result.returncode)
