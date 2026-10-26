pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 10, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Branch: ${env.BRANCH_NAME}"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    set -eu
                    python3 --version
                    python3 -m unittest discover -s tests -v
                '''
            }
        }

        stage('Build Validation') {
            steps {
                sh '''
                    set -eu
                    python3 -m py_compile app/app.py
                    echo "Application validation passed."
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline passed.'
        }

        failure {
            echo 'CI pipeline failed. Review the logs.'
        }

        always {
            echo 'CI pipeline finished.'
        }
    }
}
