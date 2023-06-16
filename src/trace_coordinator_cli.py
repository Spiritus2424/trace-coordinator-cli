from click import group, version_option
from generate_config import commands

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@group(context_settings=CONTEXT_SETTINGS)
@version_option(version='1.0.0')
def main():
    pass

main.add_command(commands.generate_config)
main.add_command(commands.add_experiment)

if __name__ == '__main__':
    main()