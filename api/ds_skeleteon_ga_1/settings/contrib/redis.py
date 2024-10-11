from ..environment import env


REDIS_URL = env.str("DS_SKELETEON_GA_1_REDIS_URL", default="redis://redis:6379/2")
