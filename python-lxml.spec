#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	python2		# Python 2 package
%bcond_without	python3		# Python 3 package

%define		module	lxml
Summary:	Python 2 binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Wiązanie Pythona 2 do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	3.3.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://lxml.de/files/%{module}-%{version}.tgz
# Source0-md5:	f2675837b4358a5ecab5fd9a783fd0e5
URL:		http://lxml.de/
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	libxslt-devel >= 1.1.26
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-Cython > 0.17
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%description apidocs
lxml API documentation.

%description apidocs -l pl.UT8-8
Dokumentacja API modułu lxml.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build
%endif
%if %{with python3}
%{__python3} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
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
