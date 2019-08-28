#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-archiver
Version  : 1.0.alpha.7
Release  : 5
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.jar
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.jar
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.pom
Source6  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar
Source7  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom
Source8  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.jar
Source9  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.pom
Source10  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.jar
Source11  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.pom
Source12  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.jar
Source13  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.pom
Source14  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.3/plexus-archiver-3.3.pom
Source15  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.jar
Source16  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.pom
Source17  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.jar
Source18  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.pom
Source19  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.jar
Source20  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.pom
Source21  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.jar
Source22  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-archiver-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-archiver package.
Group: Data

%description data
data components for the mvn-plexus-archiver package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.3
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.3/plexus-archiver-3.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-7/plexus-archiver-1.0-alpha-7.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1.1/plexus-archiver-2.1.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.1/plexus-archiver-2.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.2/plexus-archiver-2.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.4.4/plexus-archiver-2.4.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.6.3/plexus-archiver-2.6.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.3/plexus-archiver-3.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.4/plexus-archiver-3.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.5/plexus-archiver-3.5.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.6.0/plexus-archiver-3.6.0.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-archiver/3.7.0/plexus-archiver-3.7.0.pom
