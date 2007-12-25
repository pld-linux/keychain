Summary:	Key management application for SSH RSA/DSA keys
Summary(pl.UTF-8):	Zarządca kluczy RSA/DSA dla SSH
Name:		keychain
Version:	2.6.8
Release:	2
License:	GPL v2
Vendor:		Gentoo Technologies, Inc.
Group:		Applications/Networking
Source0:	http://dev.gentoo.org/~agriffis/keychain/%{name}-%{version}.tar.bz2
# Source0-md5:	2a23b311e438ecebed5639b568738d28
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

%description -l pl.UTF-8
Keychain jest bardzo poręcznym narzędziem do zarządzania kluczami
RSA/DSA dla SSH, zgodnym z OpenSSH i komercyjnym SSH2. Działa jako
nakładka na ssh-agent pozwalając na posiadanie przez użytkownika
dokładnie jednego agenta w systemie zamiast jednego na każdą sesję,
dzięki czemu redukowana jest liczba pytań o hasło do kluczy.

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
