# Prediction-Service---Public-Health-and-Population-Prediction
A scalable, high-performance platform for predicting population health trends using epidemiological, demographic, and environmental data.

## Prerequisites

- JDK 17 (Temurin/Adoptium or Oracle/OpenJDK)
- Maven 3.9+

### Install JDK 17 on macOS

You can use any distribution. Two easy options:

1) With Homebrew (Temurin):

```bash
brew install --cask temurin@17
```

Then set JAVA_HOME for your shell (zsh):

```bash
export JAVA_HOME="$(/usr/libexec/java_home -v 17)"
echo 'export JAVA_HOME="$(/usr/libexec/java_home -v 17)"' >> ~/.zprofile
```

2) With SDKMAN!:

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install java 17.0.11-tem
sdk default java 17.0.11-tem
```

Verify:

```bash
java -version
mvn -version
```

Install Maven on macOS (if not present):

```bash
brew install maven
```

## Build (Java backend)

From the `java-backend/` directory:

```bash
mvn clean verify
```

The build enforces Java 17; if you see an error about Java version, ensure `JAVA_HOME` points to a JDK 17 installation.

Note for VS Code users: this repo includes `.vscode/settings.json` pointing to a typical Temurin 17 path on macOS. If your JDK is in a different location, update that path or set `JAVA_HOME` and the Java extension will detect it.

## Python Services

### UNWTO Tourism API
The file `ml-services/population-health-trends/unwto_api/unwto_tourism_api.py` provides an API service for accessing United Nations World Tourism Organization (UNWTO) tourism statistics for NATO countries.

- Location: `ml-services/population-health-trends/unwto_api/unwto_tourism_api.py`
- Usage: Import and use the `UNWTOTourismAPI` class to interact with the UNWTO statistics database.
- Features: Endpoints for tourism levels, country statistics, and authentication via API key.

See the source file for example usage and available endpoints.
