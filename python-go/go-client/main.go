package main

import (
	"context"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "learn/grpc/grpc_out"
)

func main() {
	conn, err := grpc.NewClient("localhost:9009", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("failed to connect: %v", err)
	}
	defer conn.Close()


	client := pb.NewHelloWorldClient(conn)
	response, err := client.Hello(context.Background(), &pb.HelloRequest{Name: "Prem"})
	if err != nil {
		log.Fatalf("failed to response: %v", err)
	}
	log.Printf("Response from python server: %v", response)
}
