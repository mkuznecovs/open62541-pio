Import('env')
from os.path import join, realpath

global_env = DefaultEnvironment()
global_env.Append(
    CPPDEFINES=[
        ("UA_ENABLE_AMALGAMATION", 1),
    ]
)