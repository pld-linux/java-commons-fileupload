# TODO
# - make it not to download jar deps to ~/.maven:
#      [get] To: $HOME/.maven/repository/commons-io/jars/commons-io-1.1.jar
#      [get] To: $HOME/.maven/repository/javax.servlet/jars/servlet-api-2.3.jar
#      [get] To: $HOME/.maven/repository/javax.portlet/jars/portlet-api-1.0.jar
#      [get] To: $HOME/.maven/repository/junit/jars/junit-3.8.1.jar

Summary:	Jakarta Commons FileUpload component for Java servlets
Summary(pl.UTF-8):	Komponent Jakarta Commons FileUpload dla serwletów Javy
Name:		jakarta-commons-fileupload
Version:	1.1.1
Release:	3
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz
# Source0-md5:	d003445638bc272512112ace08d63bbb
URL:		http://jakarta.apache.org/commons/fileupload/
BuildRequires:	ant-junit >= 1.5
BuildRequires:	jakarta-commons-io
BuildRequires:	jakarta-servletapi >= 2.3
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8.1
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
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
Summary:	Jakarta Commons FileUpload documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons FileUpload
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-fileupload-doc

%description javadoc
Jakarta Commons FileUpload documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons FileUpload.

%prep
%setup -q -n commons-fileupload-%{version}

%build
required_jars="junit servlet commons-io"
export CLASSPATH=$(/usr/bin/build-classpath $required_jars)
%if 0
cat > build.properties <<EOF
noget=1
final.name=commons-fileupload-%{version}.jar
build.sysclasspath=$CLASSPATH
EOF
%endif

%ant dist \
	-Dfinal.name=commons-fileupload-%{version} \
	-Dnoget=1 \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# install jars
cp -a dist/commons-fileupload-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s commons-fileupload-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-fileupload.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
