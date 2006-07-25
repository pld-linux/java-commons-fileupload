Summary:	Jakarta Commons FileUpload component for Java servlets
Summary(pl):	Komponent Jakarta Commons FileUpload dla serwletów Javy
Name:		jakarta-commons-fileupload
Version:	1.1.1
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz
# Source0-md5:	d003445638bc272512112ace08d63bbb
URL:		http://jakarta.apache.org/commons/fileupload/
BuildRequires:	ant-junit >= 1.5
BuildRequires:	jakarta-servletapi >= 2.3
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8.1
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FileUpload component provides a simple yet flexible means of
adding support for multipart file upload functionality to servlets and
web applications.

%description -l pl
Komponent FileUpload udostêpnia proste, ale elastyczne ¶rodki do
dodawania funkcjonalno¶ci uploadu wieloczê¶ciowych plików do serwletów
i aplikacji WWW.

%package doc
Summary:	Jakarta Commons FileUpload documentation
Summary(pl):	Dokumentacja do Jakarta Commons FileUpload
Group:		Development/Languages/Java

%description doc
Jakarta Commons FileUpload documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons FileUpload.

%prep
%setup -q -n commons-fileupload-%{version}

%build
export JAVA_HOME="%{java_home}"
# for tests
export CLASSPATH="`build-classpath servlet junit`"
ant dist \
	-Dnoget=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf commons-fileupload-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-fileupload.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
