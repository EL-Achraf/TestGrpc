import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Test Add RPC
    num1 = 10
    num2 = 20
    add_request = calculator_pb2.AddRequest(num1=num1, num2=num2)
    add_response = stub.Add(add_request)
    print(f"Add result: {add_response.result}")

    # Test CarInfo RPC
    car_info_request = calculator_pb2.DataRequest()
    car_info_response_stream = stub.CarInfo(car_info_request)
    print("Car Info:")
    for car_info_response in car_info_response_stream:
        print(f"Temperature: {car_info_response.temp}, Speed: {car_info_response.speed}, RPM: {car_info_response.rpm}, Voltage: {car_info_response.volt}")

if __name__ == '__main__':
    run()
