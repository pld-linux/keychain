Summary:	Key management application for SSH RSA/DSA keys
Summary(pl.UTF-8):	Zarządca kluczy RSA/DSA dla SSH
Name:		keychain
Version:	2.8.0
Release:	3
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.funtoo.org/distfiles/keychain/%{name}-%{version}.tar.bz2
# Source0-md5:	89a3771f39a8a9fd65f11c5fdd4c4b93
Patch0:		https://github.com/funtoo/keychain/commit/6052ce29af20d237f6fe6f044e9f4110e053c763.patch
# Patch0-md5:	ae0185a988ab8610e0f1ca21e6b4dc52
URL:		http://www.funtoo.org/Keychain
BuildRequires:	perl-tools-pod
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
%patch0 -p1

%build
%{__make} keychain.1 keychain

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p keychain $RPM_BUILD_ROOT%{_bindir}/keychain
cp -p keychain.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/keychain
%{_mandir}/man1/keychain.1*
