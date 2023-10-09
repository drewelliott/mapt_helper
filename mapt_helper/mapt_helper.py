#!/usr/bin/env python
# Copyright 2023 Nokia
# Licensed under the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause

from ndk.sdk_common_pb2_grpc import SdkMgrServiceStub, SdkMgrStatus
from ndk.sdk_service_pb2 import AgentRegistrationRequest, NotificationRegisterRequest
import grpc

agent_name = 'mapt_helper'

def establish_grpc_channel() -> object:
    channel = grpc.insecure_channel("localhost:50053")
    return SdkMgrServiceStub(channel)


def register_agent(sdk_mgr_client: object):
    metadata = [("agent_name", agent_name)]

    register_request = AgentRegistrationRequest()
#    register_request.agent_liveliness = keepalive_interval
    response = sdk_mgr_client.AgentRegister(request=register_request, metadata=metadata)

    if response.status == SdkMgrStatus.kSdkMgrSuccess:
        # Agent has been registered successfully
        print("Agent has been registered successfully")
    else:
        # Agent registration failed error string available as response.error_str
        print("ERROR ! Agent failed to register. :: {}".format(response.error_str))


def register_notification_streams(sdk_mgr_client: object) -> int:
    
    metadata = [("agent_name", agent_name)]

    request = NotificationRegisterRequest(op=NotificationRegisterRequest.Create)
    response = sdk_mgr_client.NotificationRegister(request=request, metadata=metadata)

    if response.status == SdkMgrStatus.kSdkMgrSuccess:
        # Agent has been registered successfully
        return response.stream_id
    else:
        # Agent registration failed error string available as response.error_str
        print("ERROR ! Agent failed to register notification stream. :: {}".format(response.error_str))

    
def main():
    sdk_mgr_client = establish_grpc_channel()
    register_agent(sdk_mgr_client)
    stream_id = register_notification_streams(sdk_mgr_client)
    print("the stream id is {}".format(stream_id))


if __name__ == "__main__":
    main()