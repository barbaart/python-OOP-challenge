from models import PortableGhettoblaster, HomeStereo

def create_portable_ghettoblaster():
    """Creates the portable ghettoblaster"""
    ghettoblaster = PortableGhettoblaster()
    print(ghettoblaster.__str__() + " created by flask CLI.")

def create_homestereo():
    """Creates the home stereo"""
    stereo = HomeStereo()
    print(stereo.__str__() + " created by flask CLI.")

def register_commands(app):
    for command in [create_portable_ghettoblaster, create_homestereo]:
        app.cli.add_command(app.cli.command()(command))