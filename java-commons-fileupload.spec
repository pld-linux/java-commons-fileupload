%define		subver		rc1

Summary:	Jakarta Commons FileUpload
Name:		jakarta-commons-fileupload
Version:	1.0
Release:	0.%{subver}.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/fileupload//commons-fileupload-%{version}-%{subver}-src.tar.gz
# Source0-md5:	3c724e97fdd9951a5912215b15ee86a2
Patch0:		%{name}-build.patch
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	jakarta-servletapi >= 2.3
BuildRequires:	junit >= 3.8.1
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons FileUpload.

%description -l pl
Jakarta Commons FileUpload.

%package doc
Summary:	Jakarta Commons FileUpload documentation
Summary(pl):	Dokumentacja do Jakarta Commons FileUpload
Group:		Development/Languages/Java

%description doc
Jakarta Commons FileUpload documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons FileUpload.

%prep
%setup -q -n commons-fileupload-%{version}-%{subver}
%patch -p1

%build
mkdir -p target/lib
ln -sf %{_javalibdir}/ant.jar target/lib/ant-1.5.jar
ln -sf %{_javalibdir}/optional.jar target/lib/ant-optional-1.5.jar
ln -sf %{_javalibdir}/junit.jar target/lib/junit-3.8.1.jar
ln -sf %{_javalibdir}/servlet.jar target/lib/servletapi-2.3.jar
CLASSPATH="$CLASSPATH:%{_javalibdir}/junit.jar:%{_javalibdir}/ant.jar:%{_javalibdir}/optional.jar:%{_javalibdir}/servlet.jar"
export CLASSPATH
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf commons-fileupload-%{version}-%{subver}.jar $RPM_BUILD_ROOT%{_javalibdir}/commons-fileupload.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
