# import os
# import logging
from flask import Flask
from flask_restful import Api

from .controllers import (ListPlaybooks,
                          PlaybookState,
                          StartPlaybook,
                          StartTaggedPlaybook,
                          API,
                          ListEvents,
                          GetEvent,
                          ListGroups,
                          ManageGroups,
                          Hosts,
                          HostMgmt,
                          HostDetails,
                          PrometheusMetrics,
                          Login
                          )

from runner_service import configuration

import logging
logger = logging.getLogger(__name__)


def create_app():

    app = Flask("runner_service")

    # Apply any local configuration to the flask instance
    app.config.from_object(configuration.settings)

    api = Api(app)

    api.add_resource(ListPlaybooks, "/api/v1/playbooks")
    api.add_resource(StartPlaybook, "/api/v1/playbooks/<playbook_name>")
    api.add_resource(StartTaggedPlaybook, "/api/v1/playbooks/<playbook_name>/tags/<tags>")
    api.add_resource(PlaybookState, "/api/v1/playbooks/<play_uuid>")

    api.add_resource(ListEvents, "/api/v1/jobs/<play_uuid>/events")
    api.add_resource(GetEvent, "/api/v1/jobs/<play_uuid>/events/<event_uuid>")

    api.add_resource(ListGroups, "/api/v1/groups")
    api.add_resource(ManageGroups, "/api/v1/groups/<group_name>")

    api.add_resource(Hosts, "/api/v1/hosts")
    api.add_resource(HostDetails, "/api/v1/hosts/<host_name>")
    api.add_resource(HostMgmt, "/api/v1/hosts/<host_name>/groups/<group_name>")

    api.add_resource(API, "/api")
    api.add_resource(PrometheusMetrics, "/metrics")
    api.add_resource(Login, "/api/v1/login")

    # push the app object into the API class, so it can walk the
    # API endpoints.
    API.app = app

    return app
