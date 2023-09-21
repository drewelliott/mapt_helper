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
        print(f"ERROR ! Agent failed to register. :: {response.error_str}")


def register_notification_streams(sdk_mgr_client: object) -> int:
    
    metadata = [("agent_name", agent_name)]

    request = NotificationRegisterRequest(op=NotificationRegisterRequest.Create)
    response = sdk_mgr_client.NotificationRegister(request=request, metadata=metadata)

    if response.status == SdkMgrStatus.kSdkMgrSuccess:
        # Agent has been registered successfully
        return response.stream_id
    else:
        # Agent registration failed error string available as response.error_str
        print(f"ERROR ! Agent failed to register notification stream. :: {response.error_str}")

    
def main():
    sdk_mgr_client = establish_grpc_channel()
    register_agent(sdk_mgr_client)
    stream_id = register_notification_streams(sdk_mgr_client)
    print(f"the stream id is {stream_id}")


if __name__ == "__main__":
    main()