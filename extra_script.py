Import('env')
from os.path import join, realpath

global_env = DefaultEnvironment()
global_env.Append(
    CPPDEFINES=[
        ("UA_ARCHITECTURE_FREERTOSLWIP", 1), ("UA_ENABLE_AMALGAMATION", 1), ("UA_ARCHITECTURE_FREERTOSLWIP_POSIX_CLOCK", 1)
    ]
)