# GitHub Actions CI/CD Setup Guide

This repository includes comprehensive GitHub Actions workflows for continuous integration and deployment of the Java Spring Boot microservices.

## 🔧 Workflows Overview

### 1. CI/CD Pipeline (`ci-cd.yml`)
**Triggers:** Push to main/develop, Pull Requests
- **Lint & Code Quality:** Checkstyle, SpotBugs validation
- **Build & Test:** Matrix build for all 9 services
- **Security Scan:** OWASP dependency check
- **Integration Tests:** PostgreSQL + Redis services
- **Docker Images:** Build and push to GitHub Container Registry
- **Coverage Reports:** JaCoCo integration with Codecov
- **Performance Tests:** Gatling load testing
- **Deployment:** Staging environment deployment

### 2. Security Scanning (`security.yml`)
**Triggers:** Daily schedule, Push to main, Pull Requests
- **OWASP Dependency Check:** Vulnerability scanning
- **CodeQL Analysis:** Static security analysis
- **Snyk Integration:** Third-party vulnerability detection
- **Docker Security:** Trivy container scanning

### 3. Release Pipeline (`release.yml`)
**Triggers:** Git tags (v*.*.*)
- **Automated Releases:** GitHub release creation
- **Docker Images:** Tagged release images
- **Production Deployment:** Automated production rollout
- **Changelog Generation:** Auto-generated from commits

### 4. Dependency Updates (`dependency-update.yml`)
**Triggers:** Weekly schedule, Manual dispatch
- **Maven Updates:** Latest dependency versions
- **Automated PRs:** Auto-created pull requests
- **Test Validation:** Ensure updates don't break builds

### 5. Pull Request Checks (`pr-checks.yml`)
**Triggers:** Pull Requests
- **PR Validation:** Semantic PR titles, file size checks
- **Code Review:** SonarCloud integration, PMD analysis
- **Automated Comments:** Quality metrics reporting

## 🚀 Setup Instructions

### Required GitHub Secrets

Add these secrets in your repository settings (`Settings` → `Secrets and variables` → `Actions`):

```bash
# Required Secrets
GITHUB_TOKEN          # Auto-provided by GitHub Actions
CODECOV_TOKEN         # Get from codecov.io after connecting repo
SLACK_WEBHOOK         # Slack webhook URL for notifications

# Optional Secrets (for enhanced features)
SNYK_TOKEN           # Snyk.io API token for security scanning
SONAR_TOKEN          # SonarCloud token for code quality
```

### Environment Setup

1. **Enable GitHub Container Registry**
   ```bash
   # The workflows automatically use ghcr.io
   # Ensure your repository has container registry enabled
   ```

2. **Configure Branch Protection**
   - Go to `Settings` → `Branches`
   - Add protection rule for `main` branch:
     - Require status checks: ✅
     - Require pull request reviews: ✅
     - Required status checks:
       - `Code Quality & Linting`
       - `Build & Test (matrix)`
       - `Security Scan`
       - `Integration Tests`

3. **Environment Configuration**
   - Go to `Settings` → `Environments`
   - Create environments:
     - `staging` (auto-deploy from main)
     - `production` (manual approval required)

## 📋 Workflow Features

### Matrix Builds
All 9 microservices are built in parallel:
- `shared-common`
- `eureka-server`
- `api-gateway`
- `config-server`
- `population-health-trends`
- `disease-outbreak-modeling`
- `demographic-forecasting`
- `resource-planning`
- `risk-assessment`

### Quality Gates
- ✅ Code style and formatting (Checkstyle)
- ✅ Bug detection (SpotBugs)
- ✅ Security vulnerabilities (OWASP, Snyk)
- ✅ Unit test coverage (80%+ required)
- ✅ Integration test validation
- ✅ Performance benchmarks
- ✅ Docker security scanning

### Automated Deployments
- **Staging:** Auto-deploy on main branch push
- **Production:** Manual approval for tagged releases
- **Rollback:** Automated rollback on health check failures

## 🔍 Monitoring & Notifications

### Slack Integration
Configure Slack notifications for:
- Build failures
- Security vulnerabilities
- Deployment status
- Release notifications

### Artifact Management
- **Test Reports:** JUnit XML reports
- **Coverage Reports:** JaCoCo HTML/XML
- **Security Reports:** OWASP HTML reports
- **Performance Reports:** Gatling results
- **Docker Images:** GitHub Container Registry

### Status Badges
Add these badges to your README:

```markdown
[![CI/CD Pipeline](https://github.com/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction/actions/workflows/ci-cd.yml)

[![Security Scan](https://github.com/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction/actions/workflows/security.yml/badge.svg)](https://github.com/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction/actions/workflows/security.yml)

[![codecov](https://codecov.io/gh/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction/branch/main/graph/badge.svg)](https://codecov.io/gh/RR-someOne/Prediction-Service---Public-Health-and-Population-Prediction)
```

## 🛠 Customization

### Adding New Services
1. Add service name to the matrix in `ci-cd.yml`
2. Create Dockerfile in `java-backend/{service-name}/`
3. Update Kubernetes manifests

### Custom Quality Rules
Edit the following files to customize:
- `.github/workflows/ci-cd.yml` - Build and test configuration
- `java-backend/checkstyle.xml` - Code style rules
- `java-backend/spotbugs-exclude.xml` - Bug detection exclusions

### Performance Thresholds
Configure in `java-backend/gatling.conf`:
- Response time limits
- Throughput requirements
- Error rate thresholds

## 🚨 Troubleshooting

### Common Issues

1. **Maven Build Failures**
   ```bash
   # Check Java version compatibility
   # Verify Maven wrapper permissions
   chmod +x mvnw
   ```

2. **Docker Build Issues**
   ```bash
   # Ensure Dockerfile exists in service directory
   # Check base image availability
   ```

3. **Test Failures**
   ```bash
   # Review test reports in Actions artifacts
   # Check database connection settings
   ```

### Getting Help
- Check workflow logs in Actions tab
- Review artifact downloads for detailed reports
- Enable debug logging: `ACTIONS_STEP_DEBUG: true`

## 🎯 Best Practices

1. **Keep workflows fast** - Use caching and parallel jobs
2. **Fail fast** - Run quick checks before expensive operations
3. **Security first** - Scan dependencies and containers
4. **Monitor everything** - Use comprehensive reporting
5. **Automate testing** - Include unit, integration, and performance tests

This CI/CD setup ensures high-quality, secure, and reliable deployments of your public health prediction microservices! 🚀