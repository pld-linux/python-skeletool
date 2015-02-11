%define		pypi_name	skeletool
Summary:	Framework package for integrated command-line development
Name:		python-%{pypi_name}
Version:	0.2
Release:	1
License:	GPL v3
Group:		Libraries/Python
#Source0:	https://pypi.python.org/packages/2.7/s/skeletool/skeletool-%{version}dev-py2.7.egg
Source0:	https://gitorious.org/skeletool/skeletool/archive/57f281082ce6534ff88135515ca3e26922d15df4.tar.gz
# Source0-md5:	db1e7556c7ede52c58570da26859e661
URL:		https://gitorious.org/skeletool
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skeletool is a Python library that defines a framework to develop
command-line oriented tools with an API. It takes care of the
command-line options parsing and the help feature.

%prep
%setup -qc
mv skeletool-skeletool/* .

mv skeletool/COPYING .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/skeletool
%dir %{py_sitescriptdir}/skeletool
%{py_sitescriptdir}/skeletool/*.py[co]
%{py_sitescriptdir}/skeletool-%{version}dev-py*.egg-info
