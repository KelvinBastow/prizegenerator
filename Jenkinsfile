pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        DOCKERHUB = credentials('DOCKERHUB')
    }
    stages{
        stage('Test'){
            steps{
                sh 'bash ./testing.sh'
            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose build'
                sh 'docker-compose up -d'
            }
        }
        stage('Push'){
            steps{
            sh 'docker ps && docker images'
            sh 'docker-compose push'
            }
        }
        stage('Configure Swarm'){
            steps{
            sh 'ansible-playbook -i inventory.yaml playbook-1.yaml'
        }
        }
        stage('Deploy'){
            steps{
            sh 'docker stack deploy --compose-file docker-compose.yaml prizegenerator'
            sh 'docker stack services'
            }
        }
    }
}