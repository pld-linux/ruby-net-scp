#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname net-scp
Summary:	A pure Ruby implementation of the SCP client protocol
Name:		ruby-%{pkgname}
Version:	1.1.0
Release:	5
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	a7d4ae6a696222a2f4af9fe89bd44886
URL:		http://rubygems.org/gems/net-scp
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-mocha
BuildRequires:	ruby-net-ssh >= 2.6.5
BuildRequires:	ruby-test-unit
%endif
Requires:	ruby-net-ssh >= 2.6.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure Ruby implementation of the SCP client protocol

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
ruby -Itest test/test_all.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGES.txt LICENSE.txt
%{ruby_vendorlibdir}/net/scp.rb
%{ruby_vendorlibdir}/net/scp
%dir %{ruby_vendorlibdir}/uri
%{ruby_vendorlibdir}/uri/open-scp.rb
%{ruby_vendorlibdir}/uri/scp.rb
%{ruby_specdir}/net-scp-%{version}.gemspec

%if 0
%files doc
%defattr(644,root,root,755)
%endif
