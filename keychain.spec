Summary:	Key management application for OpenSSH and commercial SSH2-compatible RSA/DSA keys
Summary(pl):	Zarz±dca kluczy ssh
Name:		keychain
Version:	2.0.2
Release:	1
Vendor:		Gentoo Technologies, Inc.
URL:		http://www.gentoo.org/proj/en/keychain.xml
Source0:	http://distro.ibiblio.org/pub/linux/distributions/gentoo/distfiles/%{name}-%{version}.tar.bz2
# Source0-md5:	931bab773fe6cc438b07694a6f22e819
License:	GPL v2
Group:		Applications/Networking
BuildArch:	noarch
Provides:	keychain
Requires:	bash openssh-clients sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keychain is an extremely handy OpenSSH and commercial SSH2-compatible
RSA/DSA key management application. It acts as a front-end to
ssh-agent, allowing you to easily have one long-running ssh-agent
process per system, rather than per login session. This dramatically
reduces the number of times you need to enter your passphrase from
once per new login session to once every time your local machine is
rebooted.

%description -l pl
Keychain jest bardzo porêcznym narzêdziem do zarz±dzania kluczami ssh.
Dzia³a jako nak³adka na ssh-agent pozwalaj±c na posiadanie przez
u¿ytkownika dok³adnie jednego agenta w systemie zamiast jednego na
ka¿d± sesjê, dziêki czemu redukowana jest liczba pytañ pytañ o has³o
do kluczy.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install keychain $RPM_BUILD_ROOT%{_bindir}/keychain

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/keychain
