# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           netbeans-javaparser
Version:        6.9
Release:        4
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            http://java.netbeans.org/javaparser/
Group:          Development/Java
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# hg clone http://hg.netbeans.org/main/nb-javac/
# cd nb-javac/
# hg update -r release69_base
# tar -czvf ../nb-javac-6.9.tar.gz .
Source0:        nb-javac-%{version}.tar.gz

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils

Requires:       java >= 0:1.6.0
Requires:       jpackage-utils

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Java parser to analyze Java source files inside of the NetBeans IDE

%prep
%setup -q -c
# remove all binary libs
find . -name "*.jar" -exec %__rm -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
%ant -f make/netbeans/nb-javac/build.xml jar

%install
%__rm -fr %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}
%__install -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%__ln_s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%__install -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl-%{version}.jar
%__ln_s %{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ASSEMBLY_EXCEPTION LICENSE README
%{_javadir}/*

