Name: heat-cfntools
Version: 1.2.0
Release: 1%{?dist}
Summary: Tools required to be installed on OpenStack Heat instances
Group: System Environment/Base
License: ASL 2.0
URL: http://pypi.python.org/pypi/heat-cfntools
Source0: https://pypi.python.org/packages/source/h/heat-cfntools/heat-cfntools-1.2.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools

Requires: python-boto >= 2.4.0
Requires: python-psutil

%description
Tools required to be installed on Heat provisioned cloud instances

%prep
%setup -q -n %{name}-1.2

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc LICENSE README.rst
%{python_sitelib}/heat_cfntools*
%{_bindir}/cfn-create-aws-symlinks
%{_bindir}/cfn-get-metadata
%{_bindir}/cfn-hup
%{_bindir}/cfn-init
%{_bindir}/cfn-push-stats
%{_bindir}/cfn-signal

%changelog
* Mon Mar 11 2013 Steven Dake <sdake@redhat.com> 1.2.0-1
- Tidy up spec file for submission to Fedora

* Thu Dec 24 2012 Steve Baker <sbaker@redhat.com> 1.0-1
- initial fork of heat-jeos
