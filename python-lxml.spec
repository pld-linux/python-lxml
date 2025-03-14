#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	tests		# unit tests

%define		module	lxml
Summary:	Python 2 binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Wiązanie Pythona 2 do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	5.0.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/lxml/
Source0:	https://files.pythonhosted.org/packages/source/l/lxml/%{module}-%{version}.tar.gz
# Source0-md5:	d6ad8a1b8a013f47e6614752a8164431
URL:		https://lxml.de/
BuildRequires:	libxml2-devel >= 1:2.9.2
BuildRequires:	libxslt-devel >= 1.1.28
BuildRequires:	pkgconfig
BuildRequires:	python-Cython >= 0.29.36-2
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
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
BuildArch:	noarch

%description apidocs
lxml API documentation.

%description apidocs -l pl.UT8-8
Dokumentacja API modułu lxml.

%prep
%setup -q -n %{module}-%{version}

# force cython regeneration
%{__rm} src/lxml/{_elementpath.c,builder.c,etree.c,etree.h,etree_api.h,lxml.etree.h,lxml.etree_api.h,objectify.c,sax.c}

%build
%py_build

%if %{with tests}
install -d testdir-2/src/lxml
cd testdir-2/src/lxml
ln -snf ../../../build-2/lib.linux-*/lxml/* ../../../src/lxml/tests .
cd ../..
ln -snf ../doc ../samples ../test.py .
LC_ALL=C.UTF-8 \
%{__python} test.py -v
cd ..
%endif

%if %{with apidocs}
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} doc/mkhtml.py doc/html $(pwd) %{version}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSE.txt LICENSES.txt README.rst TODO.txt doc/licenses/{BSD,elementtree}.txt
%dir %{py_sitedir}/lxml
%{py_sitedir}/lxml/*.pxi
%{py_sitedir}/lxml/*.py[co]
%{py_sitedir}/lxml/etree.pyx
%{py_sitedir}/lxml/objectify.pyx
%{py_sitedir}/lxml/etree*.h
%{py_sitedir}/lxml/lxml.etree*.h
%{py_sitedir}/lxml/includes
%{py_sitedir}/lxml/isoschematron
%attr(755,root,root) %{py_sitedir}/lxml/_elementpath.so
%attr(755,root,root) %{py_sitedir}/lxml/builder.so
%attr(755,root,root) %{py_sitedir}/lxml/etree.so
%attr(755,root,root) %{py_sitedir}/lxml/objectify.so
%attr(755,root,root) %{py_sitedir}/lxml/sax.so
%dir %{py_sitedir}/lxml/html
%{py_sitedir}/lxml/html/*.py[co]
%attr(755,root,root) %{py_sitedir}/lxml/html/clean.so
%attr(755,root,root) %{py_sitedir}/lxml/html/diff.so
%{py_sitedir}/lxml-%{version}-py*.egg-info

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
