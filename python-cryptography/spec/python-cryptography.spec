%define _module python-cryptography
%define project cryptography

%{!?svn_revision:%define svn_revision 1}

# COMPATIBILITY FIX: Jenkins job name is neccessary to make build root unique (for CentOS5 and earlier)
%{!?JOB_NAME:%define JOB_NAME standalone}

%global debug_package %{nil}

Name:           python-%{project}
Version:        2.8
Release:        %{svn_revision}%{?dist}
Summary:        cryptography is a package designed to expose cryptographic primitives and recipes to Python developers.
Packager:       Roman Pavlyuk <roman.pavluyk@gmail.com>
Group:          Tools/Other
License:        BSD
URL:            https://github.com/pyca/cryptography
Source0:        %{_module}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)-%{JOB_NAME}
# BuildArch:      x86_64

%if 0%{?rhel}
BuildRequires:  python36-setuptools
BuildRequires:  python3-rpm-macros

Requires:       python36
%endif

%if 0%{?fedora} >= 21
BuildRequires:  python3-setuptools
BuildRequires:  python3-rpm-macros

Requires:       python3

%endif

%description
cryptography is a package designed to expose cryptographic primitives and recipes to Python developers.

%prep
%setup -n %{_module}


%build
pushd ./src
%{py3_build}
popd

%install
pushd ./src 
%{py3_install}
popd

#mkdir -p "$RPM_BUILD_ROOT"

%files
# %{python3_sitelib}/cryptography/*
%{python3_sitearch}/cryptography*

%doc src/*.rst


%changelog
