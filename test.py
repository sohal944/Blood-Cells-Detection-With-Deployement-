import pkg_resources

# Path to your requirements.txt
requirements_file = 'requirements.txt'

# Read the requirements.txt file
with open(requirements_file, 'r') as file:
    packages = file.readlines()

# Strip any extra spaces or newlines and check the version of each package
for package in packages:
    package_name = package.strip().split('==')[0]
    try:
        version = pkg_resources.get_distribution(package_name).version
        print(f"{package_name}: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{package_name} is not installed.")
