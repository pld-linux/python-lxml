#
%bcond_without	python3
%bcond_without	python2
%define		module	lxml
#
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Pythonowe wiązanie do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	2.2.6
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	http://codespeak.net/lxml/%{module}-%{version}.tgz
# Source0-md5:	b1f700fb22d7ee9b977ee3eceb65b20c
Patch0:		python3.patch
URL:		http://codespeak.net/lxml/
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-Cython
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

%package -n	python3-%{module}
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Pythonowe wiązanie do bibliotek libxml2 i libxslt
Version:	%{version}
Release:	%{release}
Group:		Libraries/Python

%description -n python3-%{module}
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%description -n python3-%{module} -l pl.UTF-8
lxml to pythonowe wiązanie do bibliotek libxml2 i libxslt.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

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

%py3_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc doc/* CHANGES.txt CREDITS.txt TODO.txt
%dir %{py_sitedir}/lxml
%{py_sitedir}/lxml/*.py[co]
%dir %{py_sitedir}/lxml/html
%{py_sitedir}/lxml/html/*.py[co]
%attr(755,root,root) %{py_sitedir}/lxml/etree.so
%attr(755,root,root) %{py_sitedir}/lxml/objectify.so
%{py_sitedir}/lxml-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc doc/* CHANGES.txt CREDITS.txt TODO.txt
%dir %{py3_sitedir}/lxml
%{py3_sitedir}/lxml/*.py[co]
%dir %{py3_sitedir}/lxml/html
%{py3_sitedir}/lxml/html/*.py[co]
%attr(755,root,root) %{py3_sitedir}/lxml/etree.so
%attr(755,root,root) %{py3_sitedir}/lxml/objectify.so
%{py3_sitedir}/lxml-*.egg-info
%endif
