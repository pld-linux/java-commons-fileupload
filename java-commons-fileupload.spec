# TODO:
# - tests fails, when build with servletapi built on th builders.
# - everything is ok, when build with servletapi built on my laptop. WTF???
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%include	/usr/lib/rpm/macros.java

%define		srcname commons-fileupload
Summary:	Commons FileUpload component for Java servlets
Summary(pl.UTF-8):	Komponent Commons FileUpload dla serwletów Javy
Name:		java-commons-fileupload
Version:	1.2.1
Release:	2
License:	Apache v2
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz
# Source0-md5:	c2bdb9264aec564e3f4fbbdf4344a844
Patch0:		%{name}-noget.patch
URL:		http://commons.apache.org/fileupload/
BuildRequires:	ant-junit >= 1.5
BuildRequires:	java(portlet) = 1.0
BuildRequires:	java(servlet) >= 2.4
BuildRequires:	java-commons-io
BuildRequires:	java-junit >= 3.8.1
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java(portlet) = 1.0
Requires:	java(servlet) >= 2.4
Requires:	java-commons-io
Requires:	jpackage-utils
Provides:	jakarta-commons-fileupload
Obsoletes:	jakarta-commons-fileupload
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FileUpload component provides a simple yet flexible means of
adding support for multipart file upload functionality to servlets and
web applications.

%description -l pl.UTF-8
Komponent FileUpload udostępnia proste, ale elastyczne środki do
dodawania funkcjonalności uploadu wieloczęściowych plików do serwletów
i aplikacji WWW.

%package javadoc
Summary:	Commons FileUpload documentation
Summary(pl.UTF-8):	Dokumentacja do Commons FileUpload
Group:		Documentation
Requires:	jpackage-utils
Provides:	jakarta-commons-fileupload-javadoc
Obsoletes:	jakarta-commons-fileupload-doc
Obsoletes:	jakarta-commons-fileupload-javadoc

%description javadoc
Commons FileUpload documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons FileUpload.

%prep
%setup -q -n commons-fileupload-%{version}-src
%patch0 -p1

%build
required_jars="junit portlet-api-1.0 servlet-api commons-io"
CLASSPATH=$(build-classpath $required_jars)

%ant jar \
	-Dbuild.sysclasspath=first \
	-Dfinal.name=commons-fileupload-%{version}

%if %{with javadoc}
%ant javadoc \
	-Dfinal.name=commons-fileupload-%{version}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# install jars
cp -a target/commons-fileupload-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s commons-fileupload-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-fileupload.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
