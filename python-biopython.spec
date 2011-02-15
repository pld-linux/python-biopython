%define module biopython
Summary:	Python tools for computational molecular biology
Name:		python-%{module}
Version:	1.56
Release:	1
License:	MIT
Group:		Python/Libraries
Source0:	http://biopython.org/DIST/%{module}-%{version}.tar.gz
# Source0-md5:	19e6481e7724b7dadb1c9d0b956c9b77
URL:		http://biopython.org/
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRequires:	python-mx-TextTools
BuildRequires:	python-Numeric
BuildRequires:	python-ReportLab
Requires:	python-mx-TextTools
Requires:	python-Numeric
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
echo y | %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

echo y | %{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/Bio
%{py_sitedir}/BioSQL
%{py_sitedir}/Martel
%{py_sitedir}/*.egg-info
