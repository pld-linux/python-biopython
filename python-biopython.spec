%define module biopython
Summary:	Python tools for computational molecular biology
Name:		python-%{module}
Version:	1.58
Release:	2
License:	MIT
Group:		Python/Libraries
Source0:	http://biopython.org/DIST/%{module}-%{version}.tar.gz
# Source0-md5:	5c48a52a7bbdda032f1e71b91650e4ca
URL:		http://biopython.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRequires:	python-mx-TextTools
BuildRequires:	python-numpy-devel
BuildRequires:	python-ReportLab
Requires:	python-mx-TextTools
Requires:	python-numpy
Requires:	python-ReportLab
Requires:	python-MySQLdb
Requires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of freely available Python tools for computational molecular
biology.

%prep
%setup -q -n %{module}-%{version}

%build
echo y | %py_build

%install
rm -rf $RPM_BUILD_ROOT

echo y | %py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/Bio
%{py_sitedir}/BioSQL
%{py_sitedir}/*.egg-info
