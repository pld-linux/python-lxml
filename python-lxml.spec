#
%define		module	lxml
#
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Summary(pl):	Pythonowe wi±zanie do bibliotek libxml2 i libxslt
Name:		python-%{module}
Version:	0.8
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://codespeak.net/lxml/%{module}-%{version}.tgz
# Source0-md5:	b156da08fea2af7b34774d5f9c4fa206
Patch0:		%{name}-path.patch
URL:		http://codespeak.net/lxml/
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	python-Pyrex >= 0.9.4.2
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%description -l pl
lxml to pythonowe wi±zanie do bibliotek libxml2 i libxslt.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

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
%attr(755,root,root) %{py_sitedir}/lxml/*.so
%dir %{py_sitedir}/lxml/tests
%{py_sitedir}/lxml/tests/*.py[co]
%{py_sitedir}/lxml/tests/*.xml
