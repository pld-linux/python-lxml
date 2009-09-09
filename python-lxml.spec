#
%define		module	lxml
#
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Summary(pl.UTF-8):	Pythonowe wiązanie do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	2.2.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://codespeak.net/lxml/%{module}-%{version}.tgz
# Source0-md5:	2f2fcb6aae51b5b417a3c0a6b256ec56
URL:		http://codespeak.net/lxml/
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%description -l pl.UTF-8
lxml to pythonowe wiązanie do bibliotek libxml2 i libxslt.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

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
