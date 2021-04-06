pipeline {
    agent any
    stages{

        stage('Step 1: Clean'){
            steps{

                sh "docker rm -f service1"
                sh "docker rm -f service2"
                sh "docker rm -f service3"
                sh "docker rm -f service4"

            }
        }

        stage('Step 2: Build'){
            steps{
                sh "docker build -t service1 ./Service1"
                sh "docker build -t service2 ./Service2"
                sh "docker build -t service3 ./Service3"
                sh "docker build -t service4 ./Service4"
            }
        }

        stage('Step 3: Test'){
            steps{
                sh "docker ps && docker images"
            }
        }

        stage('Step 4: Deploy'){
            steps{
                sh "docker run -d -p 5000:5000 --name service1 --network mynet service1"
                sh "docker run -d -p 5001:5001 --name service2 --network mynet service2"
                sh "docker run -d -p 5002:5002 --name service3 --network mynet service3"
                sh "docker run -d -p 5003:5003 --name service4 --network mynet service4"
                sh "docker ps"
            }
        }
    }
}