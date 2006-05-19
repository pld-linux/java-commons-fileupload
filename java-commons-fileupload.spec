Summary:	Jakarta Commons FileUpload component for Java servlets
Summary(pl):	Komponent Jakarta Commons FileUpload dla serwletów Javy
Name:		jakarta-commons-fileupload
Version:	1.0
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz
# Source0-md5:	c6fa0cc10e18cffa8c479c6cb61914b8
URL:		http://jakarta.apache.org/commons/fileupload/
BuildRequires:	ant(junit) >= 1.5
BuildRequires:	jakarta-servletapi >= 2.3
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
# for tests
export CLASSPATH=%{_javadir}/servlet.jar
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
