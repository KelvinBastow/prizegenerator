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
            sh 'cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
        }
        }
        stage('Deploy'){
            steps{
            sh 'bash deploy.sh'
            }
        }
    }
}