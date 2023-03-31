Import('env')
from os.path import join, realpath

# Pass flags to the Global environemnt (project `src` files, frameworks)
global_env = DefaultEnvironment()
global_env.Append(CPPDEFINES=[("UA_ARCHITECTURE_FREERTOSLWIP", 1)])