# Installing

## Windows

[Download Windows 10 and 11 installer](https://github.com/halcyon-project/Halcyon/releases/download/halcyon-1.0.0/Halcyon-1.0.0.msi)

Once downloaded, double-click on the installer to start the installation.
:::{figure} images/install1.png
:align: center
:class: shadow-image
:width: 70%
Click next.
:::

:::{figure} images/install2.png
:align: center
:class: shadow-image
:width: 70%
Read and then accept the license agreement and then click next.
:::

:::{figure} images/install3.png
:align: center
:class: shadow-image
:width: 70%
Choose the location where you want the installer to put Halcyon and its associated files and then click next.
:::

:::{figure} images/install4.png
:align: center
:class: shadow-image
:width: 70%
Decide if you would like an icon for Halcyon created and then click next.
:::

:::{figure} images/install5.png
:align: center
:class: shadow-image
:width: 70%
Click Install.
:::

:::{figure} images/install6.png
:align: center
:class: shadow-image
:width: 70%
Click Finish.  Congratulations!  You've installed Halcyon.
:::
You can launch Halcyon by double-clicking on the program icon that is created.
:::{figure} images/install7.png
:align: center
:class: shadow-image
:width: 50%
Very likely, when you start Halcyon by double-clicking the Halcyon program icon, you will get this screen.  It's just Windows letting you know Halcyon needs to access the network.  Click Allow.
:::

:::{figure} images/install8.png
:align: center
:class: shadow-image
:width: 100%
When you launch Halcyon, it will show this windows where it will put, hopefully, informative messages.
:::
When the Halcyon log screen looks like the above, you should be able to open your web browser and navigate to the following address:
http://localhost:8888

You should see the login screen.

## MacOSX

[Download MacOSX DMG file](https://github.com/halcyon-project/Halcyon/releases/download/halcyon-1.0.0/Halcyon-1.0.0.dmg)

The Mac dmg file contains the Halcyon application.  Copy this file to where you want Halcyon to create its associated files.  From a terminal window, switch to the folder yo created and put Halcyon (the file contained within dmg file.

```sh
cd Halcyon (the folder you put Halcyon into)
Halcyon.app/Contents/MacOS/Halcyon
```

At this point, you will see Halcyon start up messages be displayed.  Once it is up and runing, you can open a browser and navigate to http://localhost:8888 to get the login screen.

## Linux
### Ubuntu
[Download Ubuntu / Debian deb package](https://github.com/halcyon-project/Halcyon/releases/download/halcyon-1.0.0/halcyon_1.0.0_amd64.deb)

You can install this debian package on Ubuntu or Debian Linux using the following command

```sh
sudo apt install ./{deb package name}
```

### Redhat
You can install this RPM package with the following command
[Download RedHat rpm package](https://github.com/halcyon-project/Halcyon/releases/download/halcyon-1.0.0/halcyon-1.0.0-1.x86_64.rpm)

```sh
sudo rpm -i ./{rpm package name}
```

Once you have either the DEB or RPM package installed depending on your operating system, create a folder where you want Halcyon's data files to be.  Once you switch into this folder, just type 'Halcyon'

```sh
mkdir halcyon
cd halcyon
Halcyon
```

Halcyon will start to load up and create any files it needs.  You will be able to tailor your installation after the initial startup.

## Java Jar
[Download Java Jar version (required JDK21)](https://github.com/halcyon-project/Halcyon/releases/download/halcyon-1.0.0/Halcyon-1.0.0.jar)

Running the java jar version will require a working JDK21 installation, either [OpenJDK](https://openjdk.org/) or [GraalVM](https://www.graalvm.org/)

Put your jar file in the folder where you want Halcyon to create its data files.  Then switch into that folder and execute the jar.

```sh
mkdir halcyon
mv {downloaded jar file} halcyon
cd halcyon
java --enable-preview -Xmx5G -Xms5G --add-opens=java.base/java.nio=ALL-UNNAMED -jar {Halcyon jar file name}
```

The -Xmx and -Xms parameters control the maximum and starting RAM than the JDK will allocate for this process.  The above reserves 5GB of RAM for Halcyon to run, but keep in mind, you need to have that much RAM or more in order for it to work!

