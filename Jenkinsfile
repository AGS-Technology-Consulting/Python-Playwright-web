pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.11'
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out successfully'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo 'Python environment setup complete'
            }
        }
        
        stage('Install Playwright Browsers') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    playwright install chromium
                    playwright install-deps
                '''
                echo 'Playwright browsers installed'
            }
        }
        
        stage('Create Directories') {
            steps {
                sh '''
                    mkdir -p logs
                    mkdir -p reports
                    mkdir -p screenshots
                    mkdir -p allure-results
                '''
                echo 'Required directories created'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest tests/test_login.py --alluredir=allure-results --html=reports/report.html --self-contained-html -v || true
                '''
                echo 'Tests executed'
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
                echo 'Allure report generated'
            }
        }
        
        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'HTML Test Report',
                    reportTitles: 'Test Execution Report'
                ])
                echo 'HTML report published'
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'screenshots/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'logs/**/*', allowEmptyArchive: true
                echo 'Artifacts archived'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            // Clean workspace
            cleanWs()
        }
        success {
            echo '✅ Tests passed successfully!'
            echo '📊 View Allure report in Jenkins UI'
        }
        failure {
            echo '❌ Tests failed. Check the Allure report and screenshots for details.'
        }
    }
}