pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
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
            sh 'cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook-1.yaml'
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