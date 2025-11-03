pipeline{
  agent any

  environment {
      VENV_DIR = 'venv'
  }

  stages{
    stage('Cloning github repo to jenkins'){
      steps{
        script{
          echo 'Cloning github repo to jenkins..........'
          checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/JuanPalms/MLOPS_hotel_reservations.git']])
        }
      }
    }
  stage('Setting up our virtual environment and installing dependencies'){
      steps{
        script{
          echo 'Setting up our virtual environment and installing dependencies..........'
          sh '''
          python -m vevn ${VENV_DIR}
          . ${VEVN_DIR}/bin/activate
          pip install --upgrade pip
          pip install -e .
          '''
        }
      }
    }
  }
}