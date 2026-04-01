pipeline {
    agent any

    tools {
        // Must match Jenkins → Global Tool Configuration → Allure Commandline
        allure 'ALLURE_HOME'
    }

    environment {
        VENV_DIR        = 'venv'
        ALLURE_RESULTS  = 'Reports'
        AWS_REGION      = 'ap-south-1'
        ALLURE_REPORT   = 'allure-report'
        S3_BUCKET       = 'abc-project-allure-reports-bucket'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/priyankamastek/python-behave-selenium-pipeline.git'
            }
        }

        stage('Create Python Virtual Environment') {
            steps {
                bat '''
                python -m venv %VENV_DIR%
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install selenium
                pip install behave
                pip install allure-behave
                '''
            }
        }

        stage('Run Behave Tests with Allure') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate.bat
                behave -f allure_behave.formatter:AllureFormatter -o %ALLURE_RESULTS% features
                '''
            }
        }

        stage('Generate Allure HTML Report') {
            steps {
                bat '''
                allure generate %ALLURE_RESULTS% -o %ALLURE_REPORT% --clean
                '''
            }
        }

       
 stage('Upload Allure Report to AWS S3 (Day-wise)') {
            environment {
                AWS_ACCESS_KEY_ID     = credentials('aws-jenkins-creds')
                AWS_SECRET_ACCESS_KEY = credentials('aws-jenkins-creds')
            }
            steps {
                bat '''
                set REPORT_DATE=%DATE:~10,4%-%DATE:~4,2%-%DATE:~7,2%
                set AWS_DEFAULT_REGION=%AWS_REGION%

                echo Uploading Allure reports for %REPORT_DATE%

                aws s3 sync %ALLURE_RESULTS% s3://%S3_BUCKET%/%REPORT_DATE%/allure-results/
                aws s3 sync %ALLURE_REPORT% s3://%S3_BUCKET%/%REPORT_DATE%/allure-report/
                '''
            }
        }
    }
    post {

        always {
            // Publish Allure report inside Jenkins
            allure(
                includeProperties: false,
                results: [[path: "${ALLURE_RESULTS}"]]
            )
        }

        success {
            echo '✅ Tests executed successfully. Allure report published and uploaded to S3.'
        }

        failure {
            echo '❌ Build failed. Check Jenkins logs and Allure report.'
        }
    }
}
