#
%define		module	lxml
#
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Name:		python-%{module}
Version:	0.8
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://codespeak.net/lxml/%{module}-%{version}.tgz
# Source0-md5:	b156da08fea2af7b34774d5f9c4fa206
URL:		http://codespeak.net/lxml/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/ElementTree-%{version}-py%{py_ver}.egg-info

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* CHANGES.txt CREDITS.txt TODO.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/ElementTree*
