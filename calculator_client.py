import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():                      
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        num1 = 10
        num2 = 20
        response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
        print(f"Result of {num1} + {num2} = {response.result}")



run()


