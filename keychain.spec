Summary:	Key management application for SSH RSA/DSA keys
Summary(pl):	Zarz±dca kluczy RSA/DSA dla SSH
Name:		keychain
Version:	2.5.4.1
Release:	1
License:	GPL v2
Vendor:		Gentoo Technologies, Inc.
Group:		Applications/Networking
Source0:	http://distro.ibiblio.org/pub/linux/distributions/gentoo/distfiles/%{name}-%{version}.tar.bz2
# Source0-md5:	93498f35f8d4cf1abb1941587e68076b
URL:		http://www.gentoo.org/proj/en/keychain.xml
Requires:	openssh-clients
Requires:	sh-utils
BuildArch:	noarch
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
Keychain jest bardzo porêcznym narzêdziem do zarz±dzania kluczami
RSA/DSA dla SSH, zgodnym z OpenSSH i komercyjnym SSH2. Dzia³a jako
nak³adka na ssh-agent pozwalaj±c na posiadanie przez u¿ytkownika
dok³adnie jednego agenta w systemie zamiast jednego na ka¿d± sesjê,
dziêki czemu redukowana jest liczba pytañ o has³o do kluczy.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install keychain	$RPM_BUILD_ROOT%{_bindir}/keychain
install keychain.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/keychain
%{_mandir}/man?/*
