import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from ..environment import env


USE_SENTRY = env.bool("DS_SKELETEON_GA_1_USE_SENTRY", default=True)
if USE_SENTRY:  # pragma: no cover
    sentry_kwargs = {
        "dsn": env.str("DS_SKELETEON_GA_1_SENTRY_DSN"),
        "environment": env.str("DS_SKELETEON_GA_1_SENTRY_ENVIRONMENT"),
        "integrations": [DjangoIntegration()],
    }
    sentry_sdk.init(**sentry_kwargs)  # pylint: disable=abstract-class-instantiated
