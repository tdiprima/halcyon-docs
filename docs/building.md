# Building

[Halcyon's Github repo ![github](images/github.png){w=50px}](https://github.com/halcyon-project/Halcyon)
## Downloading from GitHub
```
git clone https://github.com/halcyon-project/Halcyon.git
```

## Building Entire Project
```sh
cd Halcyon
mvn clean package
```

## Building Server Jar
```sh
cd Halcyon/Halcyon
mvn clean package
```

## Building installers

Each command must be run on the appropriate platform.  Artifacts are located in dist folder (Halcyon/Halcyon/dist).
```sh
cd Halcyon/Halcyon
mvn clean package jpackage:jpackage@win
mvn clean package jpackage:jpackage@mac
mvn clean package jpackage:jpackage@ubuntu
mvn clean package jpackage:jpackage@rhel
```

## Building Ingest program binary for feature files

This will require a functioning [GraalVM native image environment](https://www.graalvm.org/latest/reference-manual/native-image/)
```sh
cd Halcyon/ingest
mvn -Pingest clean package 
```

## Building Ingest Jar Version for feature files

```sh
cd Halcyon/ingest
mvn -Pingestjar clean package 
```

## SSL
```sh
openssl req -new -newkey rsa:2048 -nodes -keyout beak.key -out beak.csr
openssl pkcs12 -export -in beak.crt -inkey beak.key -name Halcyon -out beak.p12
keytool -importkeystore -deststorepass changeit -destkeystore cacerts -srckeystore beak.p12 -srcstoretype PKCS12
```

