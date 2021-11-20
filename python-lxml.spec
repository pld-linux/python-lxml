#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	python2		# Python 2 package
%bcond_without	python3		# Python 3 package
%bcond_without	tests		# unit tests

%define		module	lxml
Summary:	Python 2 binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Wiązanie Pythona 2 do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	4.6.2
Release:	3
License:	BSD
Group:		Libraries/Python
# until 4.6.1
#Source0:	https://lxml.de/files/%{module}-%{version}.tgz
#Source0Download: https://pypi.org/simple/lxml/
Source0:	https://files.pythonhosted.org/packages/source/l/lxml/%{module}-%{version}.tar.gz
# Source0-md5:	2e39c6e17d61f61e5be68fd328ba6a51
URL:		https://lxml.de/
BuildRequires:	libxml2-devel >= 1:2.9.2
BuildRequires:	libxslt-devel >= 1.1.28
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python-Cython >= 0.29.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.29.7
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
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

%build
%if %{with python2}
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
%endif

%if %{with python3}
%py3_build

%if %{with tests}
install -d testdir-3/src/lxml
cd testdir-3/src/lxml
ln -snf ../../../build-3/lib.linux-*/lxml/* ../../../src/lxml/tests .
cd ../..
ln -snf ../doc ../samples ../test.py .
%{__python3} test.py -v
cd ..
%endif
%endif

%if %{with apidocs}
# as of 4.4.2, python3 is not supported in mkhtml.py
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} doc/mkhtml.py doc/html $(pwd) %{version}
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt doc/licenses/{BSD,ZopePublicLicense,elementtree}.txt
%dir %{py_sitedir}/lxml
%{py_sitedir}/lxml/*.py[co]
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
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt doc/licenses/{BSD,ZopePublicLicense,elementtree}.txt
%dir %{py3_sitedir}/lxml
%attr(755,root,root) %{py3_sitedir}/lxml/_elementpath.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/builder.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/etree.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/objectify.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/sax.cpython-*.so
%{py3_sitedir}/lxml/*.py
%{py3_sitedir}/lxml/__pycache__
%{py3_sitedir}/lxml/etree*.h
%{py3_sitedir}/lxml/lxml.etree*.h
%{py3_sitedir}/lxml/includes
%{py3_sitedir}/lxml/isoschematron
%dir %{py3_sitedir}/lxml/html
%{py3_sitedir}/lxml/html/*.py
%{py3_sitedir}/lxml/html/__pycache__
%attr(755,root,root) %{py3_sitedir}/lxml/html/clean.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/lxml/html/diff.cpython-*.so
%{py3_sitedir}/lxml-%{version}-py*.egg-info
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
