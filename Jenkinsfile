pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'your-credentials-id', url: 'https://github.com/sun986654173/First_Jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // 安装项目依赖
                    sh 'pip install selenium'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // 运行测试脚本
                    sh 'python main.py'
                }
            }
        }

        stage('Post Results') {
            steps {
                script {
                    // 这里可以添加发布测试结果或报告的步骤，例如：
                    // 发布测试报告，假设使用的是 JUnit 格式
                    // junit 'path/to/test-results.xml'
                }
            }
        }
    }

    post {
        always {
            script {
                archiveArtifacts artifacts: '**/path/to/artifacts', allowEmptyArchive: true
                junit 'path/to/test-results.xml'
            }
        }
    }
}
