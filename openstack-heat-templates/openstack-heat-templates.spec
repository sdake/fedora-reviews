Name: openstack-heat-templates
Version: 0.0.1
Release: 1%{?dist}
Summary: Heat example templates and DIB elements
Group: System Environment/Base
License: ASL 2.0

# The source for this package was pulled from upstream's git.  Use
# the following commands to generate the tarball:
# git clone https://github.com/openstack/heat-templates
# rm -rf heat-templates/.git
# mv heat-templates openstack-heat-templates-0.0.1
# tar -czvf openstack-heat-templates-0.0.1.tar.gz openstack-heat-templates

Source0: openstack-heat-templates-0.0.1.tar.gz

BuildArch: noarch

%description
Heat example templates and image building elements

%prep
%setup -q

%files
%doc LICENSE README.rst cfn hot jeos openshift-origin tools

%changelog
* Thu Sep 5 2013 Steven Dake <sdake@redhat.com> 0.0.1-1
- Initial heat-templates rpm
