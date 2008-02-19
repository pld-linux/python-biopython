%define module biopython
Summary:	Python tools for computational molecular biology
Name:		python-%{module}
Version:	1.44
Release:	1
License:	MIT
Group:		Python/Libraries
Source0:	http://biopython.org/DIST/%{module}-%{version}.tar.gz
# Source0-md5:	762c7a358af9dc58b712b8b4bb99d0c2
URL:		http://biopython.org/
BuildRequires:	python-devel
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of freely available Python tools for computational molecular
biology.

%prep
%setup -qc

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
