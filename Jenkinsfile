pipeline {
    agent any
    stages{

        stage('Stage 0: Clean'){
            steps{

                sh "docker rm -f service1"
                sh "docker rm -f service2"
                sh "docker rm -f service3"
                sh "docker rm -f service4"

            }
        }

        stage('Stage 1: Build'){
            steps{
                sh "docker build -t service1 ./Service1"
                sh "docker build -t service2 ./Service2"
                sh "docker build -t service3 ./Service3"
                sh "docker build -t service4 ./Service4"
            }
        }

        stage('Stage 2: Test'){
            steps{
                sh "docker ps && docker images"
            }
        }

        stage('Stage 3: Deploy'){
            steps{
                sh "docker run -d -p 5000:5000 --name ser1 --network mynet service1"
                sh "docker run -d -p 5001:5001 --name ser2 --network mynet service2"
                sh "docker run -d -p 5002:5002 --name ser3 --network mynet service3"
                sh "docker run -d -p 5003:5003 --name ser4 --network mynet service4"
                sh "docker ps"
            }
        }
    }
}