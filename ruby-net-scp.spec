%define	gem_name net-scp
Summary:	A pure Ruby implementation of the SCP client protocol
Name:		ruby-%{gem_name}
Version:	1.0.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	7fda0eda72b66d99816d516c5fcd4de2
URL:		http://net-ssh.rubyforge.org/scp
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
BuildRequires:	ruby-net-ssh
%endif
Requires:	ruby-net-ssh
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
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
ruby -Itest test/test_all.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG.rdoc
%dir %{ruby_vendorlibdir}/net
%{ruby_vendorlibdir}/net/scp.rb
%{ruby_vendorlibdir}/net/scp/
%dir %{ruby_vendorlibdir}/uri
%{ruby_vendorlibdir}/uri/open-scp.rb
%{ruby_vendorlibdir}/uri/scp.rb

%if 0
%files doc
%defattr(644,root,root,755)
%endif
