# AWS Security CI/CD Lab

Implemented a secure AWS CI/CD pipeline using CodePipeline, CodeBuild, and GitHub integration.
The project emphasizes security best practices such as least-privilege IAM, secrets management, MFA, CloudWatch logging, static analysis, and automated testing to ensure safe and reliable software delivery.

---

## Table of Contents

- [Overview]
- [Real-World Risk]
- [What I Built]
- [Diagram]
- [Objectives]
- [Steps Performed]
  - [1. IAM setup]
  - [2. GitHub integration]
  - [3. CodeBuild project creation]
  - [4. Pipeline setup]
  - [5. Logging to CloudWatch]
  - [6. Security checks]
  - [7. Cleanup]
- [CI/CD Pipeline Stages]
- [Security Features Implemented]
- [Screenshots & Deliverables]
- [Troubleshooting & Common Errors]
- [Lessons Learned]
- [Future Improvements]
- [References]

---

## Overview

A hands-on lab demonstrating secure CI/CD automation in AWS, including CodeBuild, CodePipeline, static analysis, secret management, CloudWatch logging, and secure IAM practices.

---

## Real-World Risk

Without secure CI/CD practices, organizations risk exposing sensitive credentials, deploying untested or vulnerable code, and granting excessive permissions to automated systems. Attackers can exploit misconfigured pipelines to gain unauthorized access, inject malicious code, or pivot through compromised build environments. Failing to mask secrets in logs, neglecting static analysis, or skipping IAM least-privilege can quickly turn automation into an enterprise-wide vulnerability.

---

## What I Built

- Integrated GitHub with AWS CodePipeline and CodeBuild for fully automated builds.
- Configured IAM roles using least-privilege and enabled MFA for administrative access.
- Secured pipeline secrets using AWS Secrets Manager with environment variable injection and log masking.
- Automated test execution and generated coverage reports using pytest.
- Implemented static code analysis using Pylint and AWS CodeGuru Reviewer.
- Centralized build logs in Amazon CloudWatch for troubleshooting and audit trails.
- Encrypted all artifacts at rest in Amazon S3.

---

## Diagram

![Pipeline Diagram](diagram.png)

---

## Objectives

- Automate CI/CD with security best practices.
- Integrate GitHub, CodeBuild, CodePipeline.
- Enforce IAM, MFA, secret management, and logging.
- Apply static code analysis.

---

## Steps Performed

1. IAM User and Role Setup
   - Created an IAM user with programmatic and console access.
   - Enabled MFA for the user to enhance account security.
   - Created and attached custom IAM roles and policies for CodeBuild and CodePipeline.
   - Verified least-privilege permissions and trusted entity relationships.

2. GitHub Integration
   - Created a new GitHub repository for the lab code.
   - Connected AWS CodeBuild/CodePipeline to the GitHub repo using a secure token.
   - Verified repository connection within the AWS console.

3. CodeBuild Project with Secret Management
   - Created a CodeBuild project to automate build and test processes.
   - Stored sensitive values (e.g., API keys) in AWS Secrets Manager.
   - Configured environment variables in CodeBuild to reference secrets securely.
   - Verified secrets were masked in logs (never exposed in plaintext).

4. Pipeline Setup (Build, Test, Static Analysis, Reporting)
   - Built a multi-stage pipeline using AWS CodePipeline with:
   - Source: Pulls latest code from GitHub on every commit.
   - Build: Compiles code, runs tests, and executes static analysis (e.g., pylint/CodeGuru).
   - Report: Generates and publishes test and linting results.
   - Configured automatic retries and notifications for failed stages.
   - Validated end-to-end flow by triggering a full pipeline run.

5. CloudWatch Logging
   - Enabled logging for all pipeline stages in Amazon CloudWatch.
   - Verified log group and log stream creation for build and test steps.
   - Used logs for troubleshooting errors and validating secret masking.

6. Security Checks
   - Secret Masking: Confirmed that sensitive values were automatically redacted in logs.
   - Least-Privilege IAM: Ensured CodeBuild/CodePipeline roles had only necessary permissions.
   - S3 Encryption: Verified S3 artifact bucket encryption with SSE enabled.
   - Static Analysis: Integrated tools (CodeGuru, pylint) to scan for code quality and security issues.
   - Multi-Factor Authentication: Confirmed IAM user MFA setup for AWS console and CLI access.

7. Cleanup
   - Deleted all CodeBuild and CodePipeline projects after the lab.
   - Removed all created IAM roles, policies and test users.
   - Deleted S3 buckets, CloudWatch log groups and Secrets Manager secrets used in the lab.
   - Verified the AWS Billing Dashboard for any remaining active resources or charges.

---

## CI/CD Pipeline Stages

| Stage           | Description                                          |
|-----------------|------------------------------------------------------|
| Source          | Connect to GitHub repo                               |
| Build           | Build/test with CodeBuild, print secret (redacted)   |
| Test            | Pytest reports and test summary                      |
| Static Analysis | Pylint and CodeGuru Reviewer                         |
| Artifact        | Upload build/test reports to S3 (if applicable)      |
| Logging         | All build logs to CloudWatch                         |

---

## Security Features Implemented

- IAM Least Privilege custom service roles.
- MFA Enabled for user.
- Secrets Manager for build environment variables.
- CloudWatch Logs for all build phases.
- Static Analysis with pylint and CodeGuru.
- S3 Bucket Encryption (for artifacts)
- Source Control with GitHub and protected tokens.

---

## Screenshots & Deliverables

*All screenshots are included in the screenshots/ folder.

| Order | File Name                                  | What it Shows                                                   |
| ----- | -------------------------------------------|---------------------------------------------------------------- |
| 1     | cloudwatch-codebuild-log-stream.png        | CloudWatch log stream for CodeBuild                             |
| 2     | cloudwatch-log-groups-list.png             | List of CloudWatch log groups                                   |
| 3     | codebuild_test_report_success.png          | CodeBuild test report: successful run                           |
| 4     | codebuild-build-success.png                | CodeBuild project: successful build                             |
| 5     | codebuild-github-token-connected.png       | GitHub account connected to CodeBuild                           |
| 6     | codebuild-project-details.png              | CodeBuild project details page                                  |
| 7     | codebuild-project-environment.png          | CodeBuild environment settings                                  |
| 8     | codebuild-secret-print-log.png             | CodeBuild log: secret value (redacted) printed in logs          |
| 9     | codebuild-secrets-env-var.png              | Environment variable setup for secrets in CodeBuild             |
| 10    | codebuild-test-report-summary.png          | CodeBuild test report summary                                   |
| 11    | codeguru-scan-results.png                  | CodeGuru static analysis/linting results                        |
| 12    | codepipeline-run-success.png               | CodePipeline run: overall success status                        |
| 13    | codepipeline-source-setup.png              | CodePipeline source (GitHub) setup                              |
| 14    | github-repo-initial-setup.png              | Initial setup of GitHub repository                              |
| 15    | iam-role-codebuild-permissions.png         | IAM permissions for CodeBuild role                              |
| 16    | iam-role-codebuild-trusted-entities.png    | Trusted entities for CodeBuild IAM role                         |
| 17    | iam-role-codepipeline-permissions.png      | IAM permissions for CodePipeline role                           |
| 18    | iam-role-codepipeline-trusted-entities.png | Trusted entities for CodePipeline IAM role                      |
| 19    | iam-user-mfa-enabled.png                   | MFA enabled for IAM user                                        |
| 20    | s3-bucket-created.png                      | S3 bucket created for CodeBuild artifacts                       |
| 21    | s3-bucket-encryption.png                   | S3 bucket encryption settings                                   |
| 22    | secretsmanager-create-secret.png           | Secret creation in AWS Secrets Manager                          |
| 23    | static-analysis-linting.png                | Static analysis/linting results (could also reference CodeGuru) |

## Screenshot Explanations

1. cloudwatch-codebuild-log-stream.png: Displays the CloudWatch log stream for a CodeBuild run, showing real-time build output and aiding in troubleshooting build steps.

2. cloudwatch-log-groups-list.png: Lists all CloudWatch log groups, confirming logging is enabled for all relevant AWS services (e.g., CodeBuild, Lambda, and others).

3. codebuild_test_report_success.png: Shows the summary of a successful test report in CodeBuild, proving tests ran and passed as part of the CI pipeline.

4. codebuild-build-success.png: Captures a successful build status in CodeBuild, confirming the CI pipeline was set up and executed correctly.

5. codebuild-github-token-connected.png: Verifies that CodeBuild is authenticated and connected to a GitHub repository, enabling automated source retrieval for builds.

6. codebuild-project-details.png: Shows the main settings and metadata for the CodeBuild project (name, description, IAM role, etc.).

7. codebuild-project-environment.png: Displays the configured build environment, including compute type, runtime image, and any environment variables.

8. codebuild-secret-print-log.png: Demonstrates secure handling of secrets by showing a redacted secret printed in the build log (validating secret injection and masking).

9. codebuild-secrets-env-var.png: Shows how environment variables were set up in CodeBuild to securely reference values from AWS Secrets Manager.

10. codebuild-test-report-summary.png: Provides an overview of the CodeBuild test report, summarizing all tests run and their outcomes.

11. codeguru-scan-results.png: Documents the results from an Amazon CodeGuru code scan, highlighting static analysis and security/linting feedback.

12. codepipeline-run-success.png: Displays a successful execution of the full CodePipeline workflow, including all stages.

13. codepipeline-source-setup.png: Shows the source stage configuration in CodePipeline, including source provider (e.g., GitHub), branch, and connection status.

14. github-repo-initial-setup.png: Confirms the initial setup and structure of the GitHub repository that is integrated with the AWS pipeline.

15. iam-role-codebuild-permissions.png: Shows the IAM policy/permissions assigned to the CodeBuild service role for secure resource access.

16. iam-role-codebuild-trusted-entities.png: Demonstrates the trusted entities for the CodeBuild role, confirming only CodeBuild can assume this role.

17. iam-role-codepipeline-permissions.png: Details the IAM policy/permissions for the CodePipeline role, showing the allowed actions and resource access.

18. iam-role-codepipeline-trusted-entities.png: Displays the trusted entities for the CodePipeline IAM role, enforcing principle of least privilege.

19. iam-user-mfa-enabled.png: Shows MFA enabled for the AWS IAM user, demonstrating strong authentication practices for admin access.

20. s3-bucket-created.png: Proves an S3 bucket was created for artifact storage, an essential step for CodeBuild/CodePipeline artifact management.

21. s3-bucket-encryption.png: Confirms encryption is enabled on the S3 artifact bucket, meeting compliance and security requirements.

22. secretsmanager-create-secret.png: Demonstrates a secret successfully created in AWS Secrets Manager, which is then used in the build pipeline.

23. static-analysis-linting.png: Captures results from static analysis/linting tools (e.g., CodeGuru or pylint), showing code quality and security checks in the pipeline.

---

## Troubleshooting & Common Errors

- GitHub not connected: Reconnect source credentials under "Account settings > Credentials".
- AccessDenied for Secrets Manager: Attach correct permissions to CodeBuild role.
- YAML_FILE_ERROR: Double-check your `buildspec.yml` syntax.
- pip install errors: Ensure your `requirements.txt` matches your runtime.

---

## Lessons Learned

- Automating secrets handling eliminates hardcoding risks.
- Static analysis catches code issues early in the pipeline.
- Least-privilege IAM roles are critical for build security.
- CloudWatch logs make debugging much easier.

---

## Future Improvements

- Integrate CodePipeline for multi-stage deployments.
- Add Snyk or Bandit for deeper Python security checks.
- Use fine-grained GitHub tokens and OIDC federation.

---

## References

- AWS CodeBuild Documentation
  https://docs.aws.amazon.com/codebuild/

- AWS CI/CD Security Best Practices
  https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-secure-ci-cd-on-aws.html

- pytest
  https://docs.pytest.org/en/7.1.x/

- pylint
  https://pylint.pycqa.org/en/latest/

- AWS CodeGuru Reviewer
  https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html

---

Sebastian Silva C. - July, 2025 - Berlin, Germany

