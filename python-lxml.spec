#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	python2		# Python 2 package
%bcond_without	python3		# Python 3 package

%define		module	lxml
Summary:	Python 2 binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Wiązanie Pythona 2 do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	3.6.0
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://lxml.de/files/%{module}-%{version}.tgz
# Source0-md5:	5957cc384bd6e83934be35c057ec03b6
URL:		http://lxml.de/
BuildRequires:	libxml2-devel >= 1:2.9.2
BuildRequires:	libxslt-devel >= 1.1.28
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.17
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%description -l pl.UTF-8
lxml to pythonowe wiązanie do bibliotek libxml2 i libxslt.

%package -n python3-%{module}
Summary:	Python 3 binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Wiązanie Pythona 3 do bibliotek libxml2 i libxslt
Group:		Libraries/Python

%description -n python3-%{module}
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%description -n python3-%{module} -l pl.UTF-8
lxml to pythonowe wiązanie do bibliotek libxml2 i libxslt.

%package apidocs
Summary:	lxml API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu lxml
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
lxml API documentation.

%description apidocs -l pl.UT8-8
Dokumentacja API modułu lxml.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

# cleanup for packaging
rm -rf docs
cp -a doc docs
# apidocs packaged separately
rm -rf docs/html
# build docs not useful at runtime
rm docs/build.txt
# common licenses
rm docs/licenses/{BSD,GPL}.txt

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc docs/* CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt
%dir %{py_sitedir}/lxml
%{py_sitedir}/lxml/*.py[co]
%{py_sitedir}/lxml/lxml.etree*.h
%{py_sitedir}/lxml/includes
%{py_sitedir}/lxml/isoschematron
%dir %{py_sitedir}/lxml/html
%{py_sitedir}/lxml/html/*.py[co]
%attr(755,root,root) %{py_sitedir}/lxml/etree.so
%attr(755,root,root) %{py_sitedir}/lxml/objectify.so
%{py_sitedir}/lxml-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc docs/* CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt
%dir %{py3_sitedir}/lxml
%attr(755,root,root) %{py3_sitedir}/lxml/etree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/objectify.cpython-*.so
%{py3_sitedir}/lxml/*.py
%{py3_sitedir}/lxml/__pycache__
%{py3_sitedir}/lxml/lxml.etree*.h
%{py3_sitedir}/lxml/includes
%{py3_sitedir}/lxml/isoschematron
%{py3_sitedir}/lxml/html
%{py3_sitedir}/lxml-*.egg-info
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
