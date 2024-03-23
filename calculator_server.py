import grpc
from concurrent import futures
import time
import random  # Importation du module random
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)

    def CarInfo(self, request, context):
        while True:

            temp = random.randint(20, 40)  # Température aléatoire entre 20 et 40 degrés Celsius
            speed = random.randint(40, 80)  # Vitesse aléatoire entre 40 et 80 km/h
            rpm = random.randint(2000, 4000)  # RPM aléatoire entre 2000 et 4000 tr/min
            volt = int(random.uniform(1000, 1400)) / 100  # Tension aléatoire entre 10 et 14 volts
            
            response = calculator_pb2.DataResponse(
                temp=int(temp),
                speed=int(speed),
                rpm=int(rpm),
                volt=int(volt)
            )
            yield response

            time.sleep(5)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    try:
        while True:
            time.sleep(86400)  # One day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
